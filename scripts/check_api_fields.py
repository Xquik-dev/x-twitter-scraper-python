# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re
import ast
import datetime
import importlib
import collections.abc
from types import ModuleType
from typing import Any, Union, Mapping, Callable, Iterator, Optional, Sequence, cast, get_args, get_origin
from pathlib import Path
from dataclasses import field, dataclass
from typing_extensions import Literal, Required, Annotated, NotRequired, is_typeddict, get_type_hints

from scripts.api_spec import (
    ROOT,
    METHOD_PATTERN,
    CheckFailure,
    ReviewedList,
    run,
    as_object,
    load_spec,
    request_key,
    spec_source,
    spec_operations,
    unexpected_spec,
    read_request_calls,
)
from tests.resource_requests import RequestCall, keyword
from x_twitter_scraper._types import FileTypes
from x_twitter_scraper._utils import PropertyInfo
from x_twitter_scraper._compat import PYDANTIC_V1, field_outer_type, get_model_fields, field_is_required
from x_twitter_scraper._models import BaseModel

PACKAGE = "x_twitter_scraper"
SIDES = ("request", "response")
KINDS = ("missing", "extra", "enum", "required", "nullable")
ACCEPTED = ReviewedList(
    file="accepted-field-differences.json",
    entry="difference",
    section="API fields",
    pattern=re.compile(f"({METHOD_PATTERN}) /\\S* ({'|'.join(SIDES)}) ({'|'.join(KINDS)}) \\S+"),
    example="Write a method, a path, request or response, a kind and a field, such as "
    "GET /api/v1/x/tweets/{id}/replies request extra cardName.",
    key=str,
)
UNREADABLE_NEXT = (
    "Name the params and response types the SDK defines, or teach scripts/check_api_fields.py the new type."
)
BODY_TYPES = ("application/json", "multipart/form-data", "application/x-www-form-urlencoded")
UNTYPED_RESPONSES = {"NoneType", "object", "BinaryAPIResponse", "AsyncBinaryAPIResponse"}
LEAF_TYPES = (str, int, float, bool, bytes, datetime.datetime, datetime.date)
SEQUENCES = (list, tuple, set, frozenset, collections.abc.Sequence, collections.abc.Iterable)
ContainerKind = Literal["array", "map"]
SUFFIXES: dict[ContainerKind, str] = {"array": "[]", "map": "{}"}


@dataclass(frozen=True)
class Unknown:
    pass


@dataclass(frozen=True)
class FreeForm:
    pass


@dataclass(frozen=True)
class Leaf:
    enum: Optional[frozenset[str]] = None


@dataclass(frozen=True)
class Container:
    kind: ContainerKind
    items: Node


@dataclass(frozen=True)
class Prop:
    node: Node
    required: bool
    nullable: Optional[bool]


@dataclass(frozen=True)
class Obj:
    props: Mapping[str, Prop] = field(default_factory=lambda: {})
    open: bool = False


Node = Union[Unknown, FreeForm, Leaf, Container, Obj]
OPAQUE = (Unknown, FreeForm)


@dataclass(frozen=True)
class Shape:
    query: Obj
    body: Optional[Node]
    response: Optional[Node]
    hidden: frozenset[str] = frozenset()


class UnreadableTypeError(Exception):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def combine_containers(nodes: Sequence[Node], combine: Callable[[Sequence[Node]], Node]) -> Optional[Container]:
    for kind in SUFFIXES:
        items = [node.items for node in nodes if isinstance(node, Container) and node.kind == kind]
        if items:
            return Container(kind, combine(items))
    return None


def merge(nodes: Sequence[Node]) -> Node:
    if nodes and all(node is nodes[0] for node in nodes):
        return nodes[0]
    if any(isinstance(node, FreeForm) for node in nodes):
        return FreeForm()
    objects = [node for node in nodes if isinstance(node, Obj)]
    if objects:
        return merge_objects(objects)
    container = combine_containers(nodes, merge)
    if container is not None:
        return container
    leaves = [node for node in nodes if isinstance(node, Leaf)]
    if leaves:
        enums = [leaf.enum for leaf in leaves]
        return Leaf(None if None in enums else frozenset[str]().union(*(enum for enum in enums if enum is not None)))
    return Unknown()


def merge_objects(objects: Sequence[Obj]) -> Obj:
    props: dict[str, Prop] = {}
    for name in dict.fromkeys(name for node in objects for name in node.props):
        have = [node.props[name] for node in objects if name in node.props]
        required = len(have) == len(objects) and all(prop.required for prop in have)
        nullables = [prop.nullable for prop in have]
        nullable = None if None in nullables else any(nullables)
        props[name] = Prop(merge([prop.node for prop in have]), required, nullable)
    return Obj(props, any(node.open for node in objects))


def intersect(nodes: Sequence[Node]) -> Node:
    objects = [node for node in nodes if isinstance(node, Obj)]
    if not objects:
        container = combine_containers(nodes, intersect)
        if container is not None:
            return container
        return next((node for node in nodes if not isinstance(node, OPAQUE)), Unknown())
    props: dict[str, Prop] = {}
    for node in objects:
        for name, prop in node.props.items():
            old = props.get(name)
            if old is None:
                props[name] = prop
            else:
                props[name] = Prop(
                    intersect([old.node, prop.node]),
                    old.required or prop.required,
                    bool(old.nullable and prop.nullable),
                )
    return Obj(props, any(node.open for node in objects))


class Spec:
    def __init__(self, document: Mapping[str, object]) -> None:
        self.document = document

    def resolve(self, reference: str) -> object:
        value: object = self.document
        for token in reference.removeprefix("#/").split("/"):
            value = as_object(value)[token.replace("~1", "/").replace("~0", "~")]
        return value

    def node(self, value: object, stack: tuple[str, ...] = ()) -> tuple[Node, bool]:
        schema = as_object(value)
        reference = schema.get("$ref")
        if isinstance(reference, str):
            if reference in stack:
                return Unknown(), False
            target, nullable = self.node(self.resolve(reference), (*stack, reference))
            types = schema.get("type")
            return target, nullable or (isinstance(types, list) and "null" in cast(list[object], types))
        nullable = schema.get("nullable") is True
        types = schema.get("type")
        if isinstance(types, list):
            nullable = nullable or "null" in cast(list[object], types)
            types = [name for name in cast(list[object], types) if name != "null"]
        elif types == "null":
            return Unknown(), True
        elif types is not None:
            types = [types]
        if "allOf" in schema:
            parts = [as_object(part) for part in cast(list[object], schema["allOf"])]
            nodes = [self.node(part, stack)[0] for part in parts]
            rest = {key: item for key, item in schema.items() if key != "allOf"}
            if "properties" in rest:
                nodes.append(self.node(rest, stack)[0])
            merged = intersect(nodes)
            required = {
                name
                for part in [*parts, rest]
                if "properties" not in part
                for name in cast(list[str], part.get("required", []))
            }
            if isinstance(merged, Obj) and required:
                merged = Obj(
                    {
                        name: Prop(prop.node, prop.required or name in required, prop.nullable)
                        for name, prop in merged.props.items()
                    },
                    merged.open,
                )
            return merged, nullable
        for key in ("oneOf", "anyOf"):
            if key in schema:
                variants: list[Node] = []
                for part in cast(list[object], schema[key]):
                    branch = as_object(part)
                    if branch.get("type") == "null":
                        nullable = True
                        continue
                    branch_node, branch_nullable = self.node(branch, stack)
                    nullable = nullable or branch_nullable
                    variants.append(branch_node)
                if "properties" in schema:
                    base, _ = self.node({k: item for k, item in schema.items() if k != key}, stack)
                    variants = [intersect([base, variant]) for variant in variants]
                return merge(variants), nullable
        if "const" in schema:
            return Leaf(frozenset({str(schema["const"])})), nullable
        if "enum" in schema:
            values = cast(list[object], schema["enum"])
            return Leaf(frozenset(str(item) for item in values if item is not None)), nullable or None in values
        properties = schema.get("properties")
        if isinstance(properties, Mapping):
            required = set(cast(list[str], schema.get("required", [])))
            props: dict[str, Prop] = {}
            for name, item in cast(Mapping[str, object], properties).items():
                prop_node, prop_nullable = self.node(item, stack)
                props[name] = Prop(prop_node, name in required, prop_nullable)
            return Obj(props, schema.get("additionalProperties") not in (None, False)), nullable
        if types is not None and "object" in types:
            values = schema.get("additionalProperties")
            if isinstance(values, Mapping) and values and not schema.get("required"):
                return Container("map", self.node(values, stack)[0]), nullable
            return FreeForm(), nullable
        if types is not None and "array" in types and "items" in schema:
            return Container("array", self.node(schema["items"], stack)[0]), nullable
        return Leaf(), nullable

    def parameter(self, value: object) -> Mapping[str, object]:
        parameter = as_object(value)
        reference = parameter.get("$ref")
        return as_object(self.resolve(reference)) if isinstance(reference, str) else parameter

    def content_node(self, value: object, accept: tuple[str, ...]) -> Optional[Node]:
        container = as_object(value)
        reference = container.get("$ref")
        if isinstance(reference, str):
            container = as_object(self.resolve(reference))
        nodes = [
            self.node(as_object(media)["schema"])[0]
            for media_type, media in as_object(container.get("content", {})).items()
            if media_type.split(";")[0].strip() in accept and "schema" in as_object(media)
        ]
        return merge(nodes) if nodes else None

    def shape(self, item: Mapping[str, object], operation: Mapping[str, object]) -> Shape:
        parameters = [
            self.parameter(value)
            for value in [
                *cast(list[object], item.get("parameters", [])),
                *cast(list[object], operation.get("parameters", [])),
            ]
        ]
        query = {
            cast(str, parameter["name"]): Prop(
                self.node(parameter.get("schema", {}))[0], parameter.get("required") is True, None
            )
            for parameter in parameters
            if parameter.get("in") == "query"
        }
        hidden = frozenset(
            _normalize(cast(str, parameter["name"]))
            for parameter in parameters
            if parameter.get("in") in ("path", "header")
        )
        body = self.content_node(operation["requestBody"], BODY_TYPES) if "requestBody" in operation else None
        responses = [
            node
            for code, response in as_object(operation.get("responses", {})).items()
            if code.startswith("2")
            for node in [self.content_node(response, ("application/json",))]
            if node is not None
        ]
        return Shape(Obj(query), body, merge(responses) if responses else None, hidden)


def _normalize(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())


def spec_shapes(document: Mapping[str, object]) -> dict[str, tuple[str, Shape]]:
    spec = Spec(document)
    return {
        operation.key: (operation.label, spec.shape(operation.item, operation.spec))
        for operation in spec_operations(document)
    }


class Converter:
    def __init__(self) -> None:
        self.types: dict[type, Obj] = {}
        self.unions: dict[object, Node] = {}

    def node(self, annotation: object, stack: tuple[type, ...] = ()) -> tuple[Node, bool]:
        while get_origin(annotation) in (Annotated, Required, NotRequired):
            annotation = get_args(annotation)[0]
        if annotation is None or annotation is type(None):
            return Unknown(), True
        if annotation == FileTypes:
            return Leaf(), False
        origin = get_origin(annotation)
        arguments = get_args(annotation)
        if origin is Union:
            members = [member for member in arguments if member is not type(None)]
            if annotation not in self.unions:
                self.unions[annotation] = merge([self.node(member, stack)[0] for member in members])
            return self.unions[annotation], len(members) < len(arguments)
        if origin is Literal:
            return Leaf(frozenset(str(item) for item in arguments if item is not None)), None in arguments
        if origin in SEQUENCES:
            return Container("array", self.node(arguments[0], stack)[0]), False
        if origin is dict:
            values = self.node(arguments[1], stack)[0]
            return (FreeForm() if isinstance(values, Unknown) else Container("map", values)), False
        if origin is not None:
            return FreeForm(), False
        if any(annotation is leaf for leaf in LEAF_TYPES):
            return Leaf(), False
        if annotation is object or annotation is Any:
            return Unknown(), False
        if not isinstance(annotation, type):
            raise UnreadableTypeError(f"uses the type {annotation!r}, which the check cannot read")
        if annotation in stack:
            return Unknown(), False
        if annotation not in self.types:
            self.types[annotation] = self._fields(annotation, (*stack, annotation))
        return self.types[annotation], False

    def _fields(self, kind: type, stack: tuple[type, ...]) -> Obj:
        if is_typeddict(kind):
            return self._typeddict(kind, stack)
        if issubclass(kind, BaseModel):
            return self._model(kind, stack)
        raise UnreadableTypeError(f"uses the type {kind.__qualname__}, which the check cannot read")

    def _model(self, model: type[BaseModel], stack: tuple[type, ...]) -> Obj:
        props: dict[str, Prop] = {}
        for name, info in get_model_fields(model).items():
            node, nullable = self.node(field_outer_type(info), stack)
            nullable = nullable or (PYDANTIC_V1 and bool(getattr(info, "allow_none", False)))
            required = field_is_required(info)
            props[info.alias or name] = Prop(node, required, _known_nullable(required, nullable))
        return Obj(props)

    def _typeddict(self, typeddict: type, stack: tuple[type, ...]) -> Obj:
        total = bool(getattr(typeddict, "__total__", True))
        props: dict[str, Prop] = {}
        for name, annotation in get_type_hints(typeddict, include_extras=True).items():
            origin: object = get_origin(annotation)
            node, nullable = self.node(annotation, stack)
            required = origin is Required or (origin is not NotRequired and total)
            props[wire_name(name, annotation)] = Prop(node, required, nullable)
        return Obj(props)


def _known_nullable(required: bool, nullable: bool) -> Optional[bool]:
    if required or not nullable:
        return nullable
    return None


def wire_name(name: str, annotation: object) -> str:
    while get_origin(annotation) in (Required, NotRequired):
        annotation = get_args(annotation)[0]
    aliases = [meta.alias for meta in getattr(annotation, "__metadata__", ()) if isinstance(meta, PropertyInfo)]
    return next((alias for alias in aliases if alias), name)


def _resolve(module: ModuleType, expression: ast.expr) -> object:
    owner: object
    if isinstance(expression, ast.Name):
        owner, name = module, expression.id
    elif isinstance(expression, ast.Attribute):
        owner, name = _resolve(module, expression.value), expression.attr
    else:
        raise UnreadableTypeError(f"names {ast.unparse(expression)}, which the check cannot read")
    if not hasattr(owner, name):
        raise UnreadableTypeError(f"names {ast.unparse(expression)}, which the check cannot find")
    return getattr(owner, name)


def _sent_fields(converter: Converter, module: ModuleType, expression: Optional[ast.expr]) -> Optional[Node]:
    if isinstance(expression, ast.Await):
        expression = expression.value
    match expression:
        case None:
            return None
        case ast.Dict(keys=entries):
            return Obj(
                {str(key.value): Prop(Unknown(), False, None) for key in entries if isinstance(key, ast.Constant)}
            )
        case ast.Call(func=ast.Name(id="maybe_transform" | "async_maybe_transform"), args=[sent, named]):
            params = _resolve(module, named)
            node = converter.node(params)[0]
            if (
                isinstance(node, Obj)
                and isinstance(sent, ast.Dict)
                and isinstance(params, type)
                and is_typeddict(params)
            ):
                names = {key.value for key in sent.keys if isinstance(key, ast.Constant)}
                hints = get_type_hints(params, include_extras=True)
                wires = {wire_name(name, annotation) for name, annotation in hints.items() if name in names}
                node = Obj({wire: prop for wire, prop in node.props.items() if wire in wires})
            return node
        case _:
            raise UnreadableTypeError(
                f"builds request fields with {ast.unparse(expression)}, which the check cannot read"
            )


def _response(converter: Converter, module: ModuleType, cast_to: ast.expr) -> Optional[Node]:
    match cast_to:
        case ast.Call(func=ast.Name(id="cast"), args=[_, target]):
            return _response(converter, module, target)
        case ast.Call():
            raise UnreadableTypeError(f"names {ast.unparse(cast_to)}, which the check cannot read")
        case _ if ast.unparse(cast_to) in UNTYPED_RESPONSES:
            return None
        case _:
            return converter.node(_resolve(module, cast_to))[0]


def _call_shape(converter: Converter, module: ModuleType, request: RequestCall) -> Shape:
    options = keyword(request.call, "options")
    query = _sent_fields(converter, module, keyword(options, "query")) if isinstance(options, ast.Call) else None
    body = _sent_fields(converter, module, keyword(request.call, "body"))
    return Shape(query if isinstance(query, Obj) else Obj(), body, _response(converter, module, request.cast_to))


def _merge_optional(first: Optional[Node], second: Optional[Node]) -> Optional[Node]:
    if first is None or second is None:
        return first or second
    return merge([first, second])


def sdk_shapes(root: Path, package: str) -> dict[str, Shape]:
    converter = Converter()
    resources = root / "src" / package / "resources"
    shapes: dict[str, Shape] = {}
    for request in read_request_calls(root, resources):
        relative = request.source.relative_to(resources.parent).with_suffix("")
        module = importlib.import_module(".".join((package, *relative.parts)))
        try:
            shape = _call_shape(converter, module, request)
        except UnreadableTypeError as error:
            raise CheckFailure(
                f"{request.source.relative_to(root)}:{request.call.lineno} {error.reason}.", UNREADABLE_NEXT
            ) from error
        key = request_key(request)
        previous = shapes.get(key)
        shapes[key] = (
            shape
            if previous is None
            else Shape(
                merge_objects([previous.query, shape.query]),
                _merge_optional(previous.body, shape.body),
                _merge_optional(previous.response, shape.response),
            )
        )
    return shapes


def _join(path: str, name: str) -> str:
    return f"{path}.{name}" if path else name


def compare(spec: Node, sdk: Node, path: str, out: list[tuple[str, str]]) -> None:
    if isinstance(spec, Obj) and isinstance(sdk, Obj):
        for name, spec_prop in spec.props.items():
            here = _join(path, name)
            sdk_prop = sdk.props.get(name)
            if sdk_prop is None:
                out.append(("missing", here))
                continue
            if spec_prop.required != sdk_prop.required:
                out.append(("required", here))
            if None not in (spec_prop.nullable, sdk_prop.nullable) and spec_prop.nullable != sdk_prop.nullable:
                out.append(("nullable", here))
            compare(spec_prop.node, sdk_prop.node, here, out)
        if not spec.open:
            out.extend(("extra", _join(path, name)) for name in sdk.props if name not in spec.props)
    elif isinstance(spec, Container) and isinstance(sdk, Container) and spec.kind == sdk.kind:
        compare(spec.items, sdk.items, f"{path}{SUFFIXES[spec.kind]}", out)
    elif isinstance(spec, Leaf) and isinstance(sdk, Leaf):
        if None not in (spec.enum, sdk.enum) and spec.enum != sdk.enum:
            out.append(("enum", path))
    elif not isinstance(spec, OPAQUE) and not isinstance(sdk, OPAQUE):
        out.append(("missing", path or "(body)"))


def _visible(node: Obj, hidden: frozenset[str], spec_names: set[str]) -> Obj:
    return Obj(
        {name: prop for name, prop in node.props.items() if name in spec_names or _normalize(name) not in hidden},
        node.open,
    )


def differences(spec: Shape, sdk: Shape) -> Iterator[tuple[str, str, str]]:
    spec_names = set(spec.query.props) | (set(spec.body.props) if isinstance(spec.body, Obj) else set[str]())
    request: list[tuple[str, str]] = []
    compare(spec.query, _visible(sdk.query, spec.hidden, spec_names), "", request)
    body = _visible(sdk.body, spec.hidden, spec_names) if isinstance(sdk.body, Obj) else sdk.body
    if spec.body is not None and body is not None:
        compare(spec.body, body, "", request)
    elif isinstance(spec.body, Obj):
        request.extend(("missing", name) for name in spec.body.props)
    elif isinstance(body, Obj):
        request.extend(("extra", name) for name in body.props)
    response: list[tuple[str, str]] = []
    if spec.response is not None:
        compare(spec.response, sdk.response or Leaf(), "", response)
    yield from (("request", kind, path) for kind, path in request)
    yield from (("response", kind, path) for kind, path in response)


def check(source: str, root: Path, package: str = PACKAGE) -> str:
    document = load_spec(source)
    try:
        spec = spec_shapes(document)
    except (KeyError, TypeError, ValueError) as error:
        raise unexpected_spec(source) from error
    accepted = ACCEPTED.read(root)
    sdk = sdk_shapes(root, package)
    compared = sorted(spec.keys() & sdk.keys())
    found = {
        f"{spec[key][0]} {side} {kind} {path}"
        for key in compared
        for side, kind, path in differences(spec[key][1], sdk[key])
    }
    unaccepted = sorted(found - accepted.keys())
    stale = [
        f"{ACCEPTED.file} lists {difference}, which the check no longer finds. Remove it."
        for difference in accepted
        if difference not in found
    ]
    if unaccepted:
        raise CheckFailure(
            *unaccepted,
            *stale,
            f"Fix each field above in the SDK, or list it in {ACCEPTED.file} with a reason.",
        )
    if stale:
        raise CheckFailure(*stale, f"Remove each difference above from {ACCEPTED.file}.")
    return (
        f"The SDK's fields match the API for {len(compared)} operations, "
        f"and {ACCEPTED.file} lists {len(accepted)} accepted differences."
    )


def main(root: Path = ROOT, package: str = PACKAGE) -> int:
    return run(lambda: check(spec_source(), root, package))


if __name__ == "__main__":
    raise SystemExit(main())
