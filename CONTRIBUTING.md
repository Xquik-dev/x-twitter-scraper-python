# Contributing

Read [GOVERNANCE.md](GOVERNANCE.md) before proposing major changes.

Follow the shared [Xquik contribution policy][contribution-policy].

## Set Up

Install uv 0.12.13 from its official release, then run:

```sh
./scripts/bootstrap
```

Validation uses Python 3.10.21 and 3.14.7 with locked dependencies.
Install both runtimes before measuring parent coverage:

```sh
uv python install 3.10.21 3.14.7
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

It runs these checks in order and stops at the first failure:

1. Locked dependency install for Python 3.10.21 and 3.14.7.
2. Ruff, Pyright, Mypy, and a package import.
3. REUSE licensing lint.
4. Reproducible wheel and source archive builds.
5. Package metadata with twine.
6. Tests on Python 3.10.21 and 3.14.7 with Pydantic 1 and 2.
7. Coverage of the parent revision, then coverage of your change against it.
8. A `pip-audit` scan of the locked dependencies, judged by the audit policy below.
9. CodeQL security-extended queries. CodeQL is mandatory.

A failure prints 1 line naming the check and the next step.
With a clean tree and a pushed commit, it posts the result as the `xquik-local-checks` commit status.
Pass `--no-status` to skip that status.
Coverage compares against `HEAD^` by default.
For a branch with several commits, pass its base: `bin/check-local origin/main`.
SDK commits preserve full-source coverage; LOC changes remain advisory.

The extended gate adds formatting, fuzzing, comply licensing, and a LOC report:

```sh
bun run check:all /absolute/path/to/parent-coverage.json HEAD
```

Measure parent coverage using `bash scripts/coverage --baseline` at the parent revision.
The extended gate verifies that report against Git's source hashes.

Install CodeQL CLI 2.27.0 or newer before running `bin/check-local`:

```sh
brew install --cask codeql
```

Set `XQUIK_CODEQL_BIN` to use another CodeQL executable.
The analysis downloads the pinned `codeql/python-queries@1.8.10` pack when it is missing.

The dependency audit checks every pin in `uv.lock`.
That includes pins for other platforms and both Pydantic groups.
It fails on any finding in a shipped runtime dependency.
It also fails on any development finding that has a fix.
An unfixable development finding passes only while `audit-exceptions.json` lists it.
Each entry names the advisory `id`, the `package` path, a `reason`, and a `recheck` date.
The reason is `build-time only` or `peer dependency provided by the host`.
The recheck date is at most 30 days out, and the finding blocks again on that date.

The extended gate and `bash scripts/fuzz` run a 180-second AddressSanitizer fuzz campaign.
Use Linux x86_64 with uv 0.12.13 and a working systemd user service.
From another platform, set `XQUIK_FUZZ_HOST` to your authorized Linux SSH runner.
The command transfers SDK source and lockfiles into an isolated temporary directory.
The fuzz process cannot access the network or modify files outside its evidence directory.
Logs, generated inputs, and failure artifacts remain at the printed evidence path.
SDK validation has no time limit; all required checks must still pass.

Each CodeQL run creates a fresh database and runs security-extended queries.
Findings, failed extraction, and incomplete analysis block release.
Reports remain in the printed evidence directory.

Add regression tests for every corrected defect.

`TEST_API_BASE_URL` accepts literal loopback addresses only.

This guard prevents tests from mutating remote services.

## Build From Source

Build both public distributions:

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
Then check out `main` with a clean tree and run:

```sh
bin/release-local
```

The script prints 1 line before each step:

1. It refuses a dirty tree, another branch, or a commit that differs from `origin/main`.
2. It reads the version from `pyproject.toml` and refuses when tag `v<version>` exists on GitHub.
3. It runs `bin/check-local`.
4. It runs the dependency audit again and refuses when the audit policy blocks.
5. It builds reproducible distributions under `dist/releases/<commit>` and checks their metadata.
6. It skips the upload when PyPI already has the version, and says so.
7. Otherwise, it uploads with `uv publish`.
8. It compares the PyPI files with the local build and installs the release from PyPI.
9. It pushes the annotated `v<version>` tag and creates the GitHub release from the changelog section.

The PyPI token lives in the macOS Keychain under service `xquik-pypi-token`.
When that item is missing, the script stops and says to add it.
The script reads the token only while `uv publish` runs.
It never prints the token or writes it to a file.
Run `bun run release:verify` to recheck a published release.

[contribution-policy]: https://github.com/Xquik-dev/.github/blob/main/CONTRIBUTING.md
[review-policy]: https://github.com/Xquik-dev/.github/blob/main/REVIEWING.md

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
