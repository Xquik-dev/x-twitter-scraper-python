# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import re
import ast
import sys
import json
import datetime
import importlib
import collections.abc
from types import ModuleType
from typing import Any, Union, Mapping, Iterator, Optional, Sequence, cast, get_args, get_origin
from pathlib import Path
from dataclasses import field, dataclass
from urllib.parse import urlsplit
from typing_extensions import Literal, Required, Annotated, NotRequired, is_typeddict, get_type_hints

from tests.resource_requests import UnreadableRequestError, request_calls
from x_twitter_scraper._types import FileTypes
from x_twitter_scraper._utils import PropertyInfo
from x_twitter_scraper._compat import PYDANTIC_V1, field_outer_type, get_model_fields, field_is_required
from x_twitter_scraper._models import BaseModel
from scripts.check_api_coverage import (
    ROOT,
    DEFAULT_SPEC,
    HTTP_METHODS,
    SPEC_FAILURE,
    CheckFailure,
    as_object,
    load_spec,
    server_path,
    operation_key,
)
from x_twitter_scraper._constants import DEFAULT_BASE_URL

ACCEPTED = "accepted-field-differences.json"
PACKAGE = "x_twitter_scraper"
SIDES = ("request", "response")
KINDS = ("missing", "extra", "enum", "required", "nullable")
DIFFERENCE = re.compile(
    f"({'|'.join(method.upper() for method in HTTP_METHODS)}) /\\S* ({'|'.join(SIDES)}) ({'|'.join(KINDS)}) \\S+"
)
BODY_TYPES = ("application/json", "multipart/form-data", "application/x-www-form-urlencoded")
UNTYPED_RESPONSES = {"NoneType", "object", "BinaryAPIResponse", "AsyncBinaryAPIResponse"}
LEAF_TYPES = (str, int, float, bool, bytes, datetime.datetime, datetime.date)
SEQUENCES = (list, tuple, set, frozenset, collections.abc.Sequence, collections.abc.Iterable)


@dataclass(frozen=True)
class Opaque:
    free: bool = False


@dataclass(frozen=True)
class Leaf:
    enum: Optional[frozenset[str]] = None


@dataclass(frozen=True)
class Array:
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


Node = Union[Opaque, Leaf, Array, Obj]


@dataclass(frozen=True)
class Shape:
    query: Obj
    body: Optional[Node]
    response: Optional[Node]
    hidden: frozenset[str] = frozenset()


MERGED: dict[tuple[int, ...], tuple[Sequence[Node], Node]] = {}


def merge(nodes: Sequence[Node]) -> Node:
    key = tuple(id(node) for node in nodes)
    if key not in MERGED:
        MERGED[key] = (nodes, _merge(nodes))
    return MERGED[key][1]


def _merge(nodes: Sequence[Node]) -> Node:
    if any(isinstance(node, Opaque) and node.free for node in nodes):
        return Opaque(free=True)
    nodes = [node for node in nodes if not isinstance(node, Opaque)]
    objects = [node for node in nodes if isinstance(node, Obj)]
    if objects:
        props: dict[str, Prop] = {}
        for name in dict.fromkeys(name for node in objects for name in node.props):
            have = [node.props[name] for node in objects if name in node.props]
            required = len(have) == len(objects) and all(prop.required for prop in have)
            nullables = [prop.nullable for prop in have]
            nullable = None if None in nullables else any(nullables)
            props[name] = Prop(merge([prop.node for prop in have]), required, nullable)
        return Obj(props, any(node.open for node in objects))
    arrays = [node for node in nodes if isinstance(node, Array)]
    if arrays:
        return Array(merge([node.items for node in arrays]))
    leaves = [node for node in nodes if isinstance(node, Leaf)]
    if leaves:
        enums = [leaf.enum for leaf in leaves]
        return Leaf(None if None in enums else frozenset[str]().union(*(enum for enum in enums if enum is not None)))
    return Opaque()


def intersect(nodes: Sequence[Node]) -> Node:
    objects = [node for node in nodes if isinstance(node, Obj)]
    arrays = [node for node in nodes if isinstance(node, Array)]
    if not objects and arrays:
        return Array(intersect([node.items for node in arrays]))
    if not objects:
        return next((node for node in nodes if not isinstance(node, Opaque)), Opaque())
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
                return Opaque(), False
            target, nullable = self.node(self.resolve(reference), (*stack, reference))
            types = schema.get("type")
            return target, nullable or (isinstance(types, list) and "null" in cast(list[object], types))
        nullable = schema.get("nullable") is True
        types = schema.get("type")
        if isinstance(types, list):
            nullable = nullable or "null" in cast(list[object], types)
            types = [name for name in cast(list[object], types) if name != "null"]
        elif types == "null":
            return Opaque(), True
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
            return Opaque(free=True), nullable
        if types is not None and "array" in types and "items" in schema:
            return Array(self.node(schema["items"], stack)[0]), nullable
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
    shapes: dict[str, tuple[str, Shape]] = {}
    for path, value in as_object(document.get("paths")).items():
        item = as_object(value)
        for method in HTTP_METHODS:
            if method in item:
                operation = as_object(item[method])
                absolute = server_path(operation.get("servers"), item.get("servers"), document.get("servers")) + path
                shapes[operation_key(method.upper(), absolute)] = (
                    f"{method.upper()} {absolute}",
                    spec.shape(item, operation),
                )
    return shapes


class Converter:
    def __init__(self) -> None:
        self.memo: dict[type, Node] = {}

    def node(self, annotation: object, stack: tuple[type, ...] = ()) -> tuple[Node, bool]:
        while get_origin(annotation) in (Annotated, Required, NotRequired):
            annotation = get_args(annotation)[0]
        if annotation is None or annotation is type(None):
            return Opaque(), True
        if annotation == FileTypes:
            return Leaf(), False
        origin = get_origin(annotation)
        arguments = get_args(annotation)
        if origin is Union:
            members = [member for member in arguments if member is not type(None)]
            return merge([self.node(member, stack)[0] for member in members]), len(members) < len(arguments)
        if origin is Literal:
            return Leaf(frozenset(str(item) for item in arguments if item is not None)), None in arguments
        if origin in SEQUENCES:
            return Array(self.node(arguments[0], stack)[0]), False
        if origin is not None:
            return Opaque(free=True), False
        if any(annotation is leaf for leaf in LEAF_TYPES):
            return Leaf(), False
        if annotation is object or annotation is Any:
            return Opaque(), False
        kind = cast(type, annotation)
        is_model = isinstance(annotation, type) and issubclass(kind, BaseModel)
        if not is_model and not (isinstance(annotation, type) and is_typeddict(kind)):
            raise TypeError(f"The check cannot read the type {annotation!r}")
        if kind in stack:
            return Opaque(), False
        if kind not in self.memo:
            self.memo[kind] = (self.model if is_model else self.typeddict)(kind, (*stack, kind))
        return self.memo[kind], False

    def model(self, model: type, stack: tuple[type, ...]) -> Node:
        props: dict[str, Prop] = {}
        for name, info in get_model_fields(cast(type[BaseModel], model)).items():
            annotation = field_outer_type(info)
            node, nullable = self.node(annotation, stack)
            nullable = nullable or (PYDANTIC_V1 and bool(getattr(info, "allow_none", False)))
            required = field_is_required(info)
            props[info.alias or name] = Prop(node, required, nullable if required else (None if nullable else False))
        return Obj(props)

    def typeddict(self, typeddict: type, stack: tuple[type, ...]) -> Node:
        total = bool(getattr(typeddict, "__total__", True))
        props: dict[str, Prop] = {}
        for name, annotation in get_type_hints(typeddict, include_extras=True).items():
            origin: object = get_origin(annotation)
            required = True if origin is Required else False if origin is NotRequired else total
            node, nullable = self.node(annotation, stack)
            props[wire_name(name, annotation)] = Prop(node, required, nullable)
        return Obj(props)


def wire_name(name: str, annotation: object) -> str:
    while get_origin(annotation) in (Required, NotRequired):
        annotation = get_args(annotation)[0]
    aliases = [meta.alias for meta in getattr(annotation, "__metadata__", ()) if isinstance(meta, PropertyInfo)]
    return next((alias for alias in aliases if alias), name)


def _resolve(module: ModuleType, expression: ast.expr) -> object:
    if isinstance(expression, ast.Name):
        return getattr(module, expression.id)
    if isinstance(expression, ast.Attribute):
        return getattr(_resolve(module, expression.value), expression.attr)
    raise ValueError(ast.unparse(expression))


def _keyword(call: ast.Call, name: str) -> Optional[ast.expr]:
    return next((keyword.value for keyword in call.keywords if keyword.arg == name), None)


def _sent_fields(converter: Converter, module: ModuleType, expression: Optional[ast.expr]) -> Optional[Node]:
    if isinstance(expression, ast.Await):
        expression = expression.value
    if expression is None:
        return None
    if isinstance(expression, ast.Dict):
        return Obj(
            {str(key.value): Prop(Opaque(), False, None) for key in expression.keys if isinstance(key, ast.Constant)}
        )
    if (
        not isinstance(expression, ast.Call)
        or not isinstance(expression.func, ast.Name)
        or expression.func.id not in ("maybe_transform", "async_maybe_transform")
    ):
        raise ValueError(f"The check cannot read the request fields {ast.unparse(expression)}")
    params = _resolve(module, expression.args[1])
    node = converter.node(params)[0]
    sent = expression.args[0]
    if isinstance(node, Obj) and isinstance(sent, ast.Dict) and is_typeddict(params):
        keys = {key.value for key in sent.keys if isinstance(key, ast.Constant)}
        hints = get_type_hints(cast(type, params), include_extras=True)
        wires = {wire_name(name, annotation) for name, annotation in hints.items() if name in keys}
        node = Obj({wire: prop for wire, prop in node.props.items() if wire in wires})
    return node


def sdk_shapes(root: Path, package: str, base_url: str) -> dict[str, Shape]:
    converter = Converter()
    base_path = urlsplit(base_url).path.rstrip("/")
    resources = root / "src" / package / "resources"
    shapes: dict[str, Shape] = {}
    try:
        calls = list(request_calls(resources))
    except UnreadableRequestError as error:
        raise CheckFailure(
            f"{error.source.relative_to(root)}:{error.line} {error.reason}.",
            "Fix that line. Write each request path as a string or a path_template call, and pass cast_to.",
        ) from error
    for call in calls:
        relative = call.source.relative_to(resources.parent).with_suffix("")
        module = importlib.import_module(".".join((package, *relative.parts)))
        key = operation_key(call.method, base_path + call.template)
        try:
            shape = _call_shape(converter, module, call.call, call.cast_to)
        except (AttributeError, TypeError, ValueError, IndexError) as error:
            raise CheckFailure(
                f"{call.source.relative_to(root)}:{call.call.lineno} has request or response types the check cannot read.",
                "Name the params and response types the SDK defines, or teach scripts/check_api_fields.py the new type.",
            ) from error
        previous = shapes.get(key)
        if previous is not None:
            shape = Shape(
                cast(Obj, merge([previous.query, shape.query])),
                _merge_optional(previous.body, shape.body),
                _merge_optional(previous.response, shape.response),
            )
        shapes[key] = shape
    return shapes


def _call_shape(converter: Converter, module: ModuleType, call: ast.Call, cast_to: ast.expr) -> Shape:
    options = _keyword(call, "options")
    query = _sent_fields(converter, module, _keyword(options, "query")) if isinstance(options, ast.Call) else None
    body = _sent_fields(converter, module, _keyword(call, "body"))
    if isinstance(cast_to, ast.Call):
        cast_to = cast_to.args[1]
    response = None if ast.unparse(cast_to) in UNTYPED_RESPONSES else converter.node(_resolve(module, cast_to))[0]
    return Shape(query if isinstance(query, Obj) else Obj(), body, response)


def _merge_optional(first: Optional[Node], second: Optional[Node]) -> Optional[Node]:
    if first is None or second is None:
        return first or second
    return merge([first, second])


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
    elif isinstance(spec, Array) and isinstance(sdk, Array):
        compare(spec.items, sdk.items, f"{path}[]", out)
    elif isinstance(spec, Leaf) and isinstance(sdk, Leaf):
        if None not in (spec.enum, sdk.enum) and spec.enum != sdk.enum:
            out.append(("enum", path))
    elif not isinstance(spec, Opaque) and not isinstance(sdk, Opaque):
        out.append(("missing", path or "(body)"))


def _visible(node: Optional[Node], hidden: frozenset[str], spec_names: set[str]) -> Optional[Node]:
    if not isinstance(node, Obj):
        return node
    return Obj(
        {name: prop for name, prop in node.props.items() if name in spec_names or _normalize(name) not in hidden},
        node.open,
    )


def differences(spec: Shape, sdk: Shape) -> Iterator[tuple[str, str, str]]:
    spec_names: set[str] = set(spec.query.props) | (set(spec.body.props) if isinstance(spec.body, Obj) else set[str]())
    request: list[tuple[str, str]] = []
    compare(spec.query, cast(Obj, _visible(sdk.query, spec.hidden, spec_names)), "", request)
    body = _visible(sdk.body, spec.hidden, spec_names)
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


def _invalid(problem: str) -> CheckFailure:
    return CheckFailure(
        f"{ACCEPTED} is not valid. {problem}",
        f"Fix {ACCEPTED} in the format CONTRIBUTING.md shows under API fields.",
    )


def read_accepted(root: Path) -> list[str]:
    try:
        groups: object = json.loads((root / ACCEPTED).read_bytes())
    except OSError as error:
        raise _invalid("The file cannot be read.") from error
    except json.JSONDecodeError as error:
        raise _invalid(f"Line {error.lineno} column {error.colno} breaks the JSON syntax.") from error
    except ValueError as error:
        raise _invalid("Its bytes are not valid text.") from error
    if not isinstance(groups, list):
        raise _invalid("It must be a list of groups, each with a reason and differences.")
    accepted: list[str] = []
    for number, group in enumerate(cast(list[object], groups), 1):
        fields: Mapping[str, object] = cast(Mapping[str, object], group) if isinstance(group, Mapping) else {}
        if set(fields) != {"reason", "differences"}:
            raise _invalid(f"Group {number} must hold a reason and differences, and nothing else.")
        reason, listed = fields["reason"], fields["differences"]
        if not isinstance(reason, str) or not reason.strip():
            raise _invalid(f"Group {number} needs a non-empty reason.")
        if not isinstance(listed, list) or not listed:
            raise _invalid(f"Group {number} needs at least 1 difference.")
        for difference in cast(list[object], listed):
            if not isinstance(difference, str) or not DIFFERENCE.fullmatch(difference):
                raise _invalid(
                    f"Group {number} lists {json.dumps(difference)}. "
                    "Write a method, a path, request or response, a kind and a field, such as "
                    "GET /api/v1/x/tweets/{id}/replies request extra cardName."
                )
            if difference in accepted:
                raise _invalid(f"{difference} appears more than once.")
            accepted.append(difference)
    return accepted


def check(spec_source: str, root: Path, package: str = PACKAGE) -> str:
    document = load_spec(spec_source)
    try:
        spec = spec_shapes(document)
    except (KeyError, TypeError, ValueError) as error:
        raise CheckFailure(SPEC_FAILURE.format(source=spec_source)) from error
    accepted = read_accepted(root)
    sdk = sdk_shapes(root, package, DEFAULT_BASE_URL)
    compared = sorted(spec.keys() & sdk.keys())
    found = sorted(
        {
            f"{spec[key][0]} {side} {kind} {path}"
            for key in compared
            for side, kind, path in differences(spec[key][1], sdk[key])
        }
    )
    unaccepted = [difference for difference in found if difference not in accepted]
    stale = [
        f"{ACCEPTED} lists {difference}, which the check no longer finds. Remove it."
        for difference in accepted
        if difference not in found
    ]
    if unaccepted:
        raise CheckFailure(
            *unaccepted,
            *stale,
            f"Fix each field above in the SDK, or list it in {ACCEPTED} with a reason.",
        )
    if stale:
        raise CheckFailure(*stale, f"Remove each difference above from {ACCEPTED}.")
    return (
        f"The SDK's fields match the API for {len(compared)} operations, "
        f"and {ACCEPTED} lists {len(accepted)} accepted differences."
    )


def main(root: Path = ROOT, package: str = PACKAGE) -> int:
    try:
        print(check(os.environ.get("XQUIK_OPENAPI_SPEC") or DEFAULT_SPEC, root, package))
    except CheckFailure as failure:
        print("\n".join(failure.lines), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
