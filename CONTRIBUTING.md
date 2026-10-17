# Contributing

Read [GOVERNANCE.md](GOVERNANCE.md) before proposing major changes.

Follow the shared [Xquik contribution policy][contribution-policy].

## Set Up

Install uv 0.13.1 or newer, then run these commands.

```sh
./scripts/bootstrap
```

Validation uses Python 3.10.22 and 3.14.8 with locked dependencies.
Install both runtimes before measuring parent coverage.

```sh
uv python install 3.10.22 3.14.8
```

Without `uv`, install `requirements-dev.lock` inside an isolated environment.

Never commit credentials or runtime environment files.

## Generated Code

Most SDK files come from the public OpenAPI contract.

Preserve generated method names and response contracts.

Avoid generated-file changes when a generator fix exists.

Place stable examples outside generated directories.

## Verify Changes

Run focused tests while editing.

Run every check before requesting review.

```sh
bin/check-local
```

It runs these checks in order and stops at the first failure.

1. Locked dependency install for Python 3.10.22 and 3.14.8.
2. API coverage against the API spec, as [API coverage](#api-coverage) describes.
3. API fields against the API spec, as [API fields](#api-fields) describes.
4. Ruff, Pyright, Mypy, and a package import.
5. REUSE licensing lint.
6. Reproducible wheel and source archive builds.
7. Package metadata with twine.
8. Tests on Python 3.10.22 and 3.14.8 with Pydantic 1 and 2.
9. Coverage of the parent revision, then coverage of your change against it.
10. A `pip-audit` scan of the locked dependencies, judged by the audit policy below.
11. CodeQL security-extended queries. CodeQL is mandatory.

A failure prints 1 line naming the check and the next step.
With a clean tree and a pushed commit, it posts the result as the `xquik-local-checks` commit status.
Pass `--no-status` to skip that status.
Coverage compares against `HEAD^` by default.
For a branch with several commits, pass its base, as in `bin/check-local origin/main`.
SDK commits preserve full-source coverage. LOC changes remain advisory.
The check scripts remove their temporary directories on any exit, including failure or interruption.

The extended gate adds formatting, fuzzing, comply licensing, and a LOC report.

```sh
bun run check:all /absolute/path/to/parent-coverage.json HEAD
```

Measure parent coverage using `bash scripts/coverage --baseline` at the parent revision.
The baseline stays in the Git common directory as `xquik-coverage-baseline.json`, or at `COVERAGE_BASELINE` when set.
The extended gate verifies that report against Git's source hashes.

Install CodeQL CLI 2.27.2 or newer before running `bin/check-local`.

```sh
brew install --cask codeql
```

Set `XQUIK_CODEQL_BIN` to use another CodeQL executable.
The analysis downloads the pinned `codeql/python-queries@1.8.12` pack when it is missing.

The dependency audit checks every pin in `uv.lock`.
That includes pins for other platforms and both Pydantic groups.
It fails on any finding in a shipped runtime dependency.
It also fails on any development finding that has a fix.
An unfixable development finding passes only while `audit-exceptions.json` lists it.
Each entry names the advisory `id`, the `package` path, a `reason`, and a `recheck` date.
The reason is `build-time only` or `peer dependency provided by the host`.
The recheck date is at most 30 days out, and the finding blocks again on that date.

The extended gate and `bash scripts/fuzz` run a 180-second AddressSanitizer fuzz campaign.
Use Linux x86_64 with uv 0.13.1 or newer and a working systemd user service.
From another platform, set `XQUIK_FUZZ_HOST` to your authorized Linux SSH runner.
The command transfers SDK source and lockfiles into an isolated temporary directory.
The fuzz process cannot access the network or modify files outside its evidence directory.
Logs and failure inputs print before the temporary directory is removed.
SDK validation has no time limit. All required checks must still pass.

Each CodeQL run creates a fresh database and runs security-extended queries.
Findings, failed extraction, and incomplete analysis block release.
The report prints before the temporary directory is removed.

Add regression tests for every corrected defect.

`TEST_API_BASE_URL` accepts literal loopback addresses only.

This guard prevents tests from mutating remote services.

## API coverage

The first check after the dependency install fails when the SDK lags the API.
It reads each operation of the API spec as its method and full path, such as `GET /api/v1/x/trends/history`.
It reads the SDK's operations from the request calls in `src/x_twitter_scraper/resources`.
Each SDK path gets the path of the client's default base URL in front, so `/x/trends` becomes `/api/v1/x/trends`.
Path parameter names do not matter, so `{id}` matches `{tweetId}`.

A failure prints 1 line per problem, then the next step.

- An operation is in the API but not in the SDK. Add it to the SDK, or list it in `excluded-operations.json` with a reason.
- `excluded-operations.json` lists an operation the API no longer has, or one the SDK already implements. Remove it from the file.
- A resource file is not valid Python, or a request call in it has a path or `cast_to` the check cannot read. Fix that line. Write each request path as a string or a `path_template` call, and pass `cast_to`.

Operations the SDK has and the API spec lacks pass.

`excluded-operations.json` holds a list of groups.
Each group has a non-empty `reason` and at least 1 operation.
An operation appears at most once in the file.

```json
[
  {
    "reason": "Needs a dashboard sign-in cookie, which API keys and bearer tokens cannot use.",
    "operations": ["GET /api/v1/api-keys", "POST /api/v1/api-keys"]
  }
]
```

The check reads the spec from https://xquik.com/openapi.json.
Set `XQUIK_OPENAPI_SPEC` to a local file path or another URL to check against another copy.
The spec must be JSON.
The public copy leaves out `GET /api/v1/credits/topup/redirect`, which the SDK keeps as `credits.redirect_topup_checkout`.

```sh
XQUIK_OPENAPI_SPEC=/path/to/openapi.json uv run --locked python -m scripts.check_api_coverage
```

## API fields

The check after API coverage fails when the SDK's fields differ from the API spec.
For each operation the SDK implements, it compares the query parameters and JSON or multipart body fields of the request, and the JSON body of each 2xx response, at every depth.
It reads the spec's fields through `$ref`, `allOf`, `oneOf` and `anyOf`, and the SDK's fields from the params and response types each request call names.
Path and header parameters, free-form objects and fields under an object that allows extra properties stay out.
A field missing on 1 side counts once, at its top position.

Each difference prints as 1 line with the method, the full path, `request` or `response`, a kind and the field's JSON path.

```text
GET /api/v1/monitors response enum monitors[].pausedReason
```

- `missing` means the spec has the field and the SDK does not. Add it to the SDK.
- `extra` means the SDK has a field the spec does not list. Keep it when callers may use it, and accept it.
- `enum` means both sides list values and the values differ. Add the missing values, and accept values the SDK keeps.
- `required` and `nullable` mean the flags differ where the SDK encodes them. Fix them only when the change keeps old calls and old responses working.

Fixes stay additive. Never remove or rename a public field or parameter to satisfy the check. Accept it instead.

`accepted-field-differences.json` holds the reviewed differences the SDK keeps on purpose, in groups with a non-empty `reason`.
A difference appears at most once.
An accepted difference the check no longer finds fails as stale, so remove it from the file.

```json
[
  {
    "reason": "Search filters the current spec no longer lists on these routes. The SDK keeps them, so code written for earlier versions keeps working.",
    "differences": ["GET /api/v1/x/tweets/{id}/replies request extra cardName"]
  }
]
```

The check reads the spec the same way as API coverage, including `XQUIK_OPENAPI_SPEC`.

```sh
XQUIK_OPENAPI_SPEC=/path/to/openapi.json uv run --locked --all-extras python -m scripts.check_api_fields
```

## Build From Source

Build both public distributions.

```sh
uv build
```

Install the wheel inside a clean environment for integration testing.

## Submit changes

Use clear Conventional Commit subjects and sign commits with `git commit --signoff`.
Follow the shared [review policy][review-policy].

## Report Security Issues

Never disclose suspected vulnerabilities in public issues.

Follow [SECURITY.md](SECURITY.md) for private reporting.

## Releases

Maintainers publish releases from a local Mac. GitHub Actions does not run for this repository.

First merge a release commit into `main`.
That commit sets the version in `pyproject.toml` and `src/x_twitter_scraper/_version.py`.
It also adds a matching `CHANGELOG.md` section.
Then check out `main` with a clean tree and run this command.

```sh
bin/release-local
```

The script prints 1 line before each step.

1. It refuses a dirty tree, another branch, or a commit that differs from `origin/main`.
2. It reads the version from `pyproject.toml` and refuses when tag `v<version>` exists on GitHub.
3. It runs `bin/check-local`.
4. It runs the dependency audit again and refuses when the audit policy blocks.
5. It builds reproducible distributions under `dist/releases/<commit>` and checks their metadata.
6. It skips the upload when PyPI already has the version, and says so.
7. Otherwise, it uploads with `uv publish`.
8. It compares the PyPI files with the local build and installs the release from PyPI.
9. It pushes the annotated `v<version>` tag and creates the GitHub release from the changelog section.

Preview a release with `bin/release-local --dry-run`.
It runs every step except the upload, the tag, and the GitHub release.
It never reads the Keychain, so it needs no `PYPI_KEYCHAIN_SERVICE`.
It also accepts a detached checkout of `origin/main`, so a preview can run in a separate worktree.

The PyPI token lives in the macOS Keychain.
Set `PYPI_KEYCHAIN_SERVICE` to the name of the Keychain item that holds it.
Keep that name out of this repository.
When the variable is unset or the item is missing, the script stops and says what to do.
The script reads the token only while `uv publish` runs.
It never prints the token or the item's name, and it writes neither to a file.
Run `bun run release:verify` to recheck a published release.

[contribution-policy]: https://github.com/Xquik-dev/.github/blob/main/CONTRIBUTING.md
[review-policy]: https://github.com/Xquik-dev/.github/blob/main/REVIEWING.md

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
