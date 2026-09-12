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

Run every gate before requesting review.

```sh
bun run check:all /absolute/path/to/parent-coverage.json HEAD
bun run build
```

Measure parent coverage using `bash scripts/coverage --baseline` at the parent revision.
The full check verifies that report against Git's source hashes.
SDK commits preserve full-source coverage; LOC changes remain advisory.

Install CodeQL CLI 2.27.0 from its official GitHub release.
Verify the archive against the release's SHA-256 checksum before extraction.
Set `XQUIK_CODEQL_BIN` to its executable path.
The default path is `~/.cache/xquik-codeql/2.27.0/codeql/codeql`.
Install the pinned queries once:

```sh
"$XQUIK_CODEQL_BIN" pack download codeql/python-queries@1.8.10
```

Full checks also run a 180-second AddressSanitizer fuzz campaign.
Use Linux x86_64 with uv 0.12.13 and a working systemd user service.
From another platform, set `XQUIK_FUZZ_HOST` to your authorized Linux SSH runner.
The command transfers SDK source and lockfiles into an isolated temporary directory.
The fuzz process cannot access the network or modify files outside its evidence directory.
Logs, generated inputs, and failure artifacts remain at the printed evidence path.
SDK validation has no time limit; all required checks must still pass.

Each full check creates a fresh database and runs security-extended queries.
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

Publish an immutable `v*` release after its commit reaches `main`.

Try the publishing workflow at the release tag when Actions is available.
If Actions fails, use the maintained local publisher without repeated retries.
Local checks remain mandatory for either route.

```sh
bun run release:prepare /absolute/path/to/parent-coverage.json HEAD^
bun run release:publish /absolute/path/to/parent-coverage.json HEAD^
bun run release:verify
```

Start from a clean, committed checkout with verified parent coverage.
Run `bash scripts/coverage-parent HEAD^` to generate the parent report.
It retains raw coverage, test output, and a detached parent checkout.
Both revisions use the candidate's locked dependencies and Python versions.
Historical skipped tests remain baseline gaps, never release passes.
Publishing requires the matching `v*` tag and membership in remote `main`.
Preparation retains reproducible distributions under `dist/releases/<commit>`.
The publisher checks metadata and reruns validation before uploading.
Set `XQUIK_PYPI_KEYCHAIN_SERVICE` to an approved macOS Keychain item name.
Alternatively, supply `UV_PUBLISH_TOKEN` through your authorized secret manager.
Never place publishing tokens in commands, logs, or runtime environment files.
Commands emit JSON completion status and preserve diagnostic errors.
Retry the same publish command after partial uploads.
uv accepts existing identical files and rejects conflicting artifacts.
Verification compares registry hashes, checks yanked status, and installs from PyPI.

Verify registry metadata and install the published version before declaring release completion.

[contribution-policy]: https://github.com/Xquik-dev/.github/blob/main/CONTRIBUTING.md
[review-policy]: https://github.com/Xquik-dev/.github/blob/main/REVIEWING.md

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
