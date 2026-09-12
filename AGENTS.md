# Xquik Python SDK

Use `package.json` for commands and `pyproject.toml` and `uv.lock` for dependencies.
Pass the verified parent coverage JSON path to `bun run check:all`.
Preserve unrelated changes, public contracts, useful tests, and diagnostics.
Never read, print, stage, or back up runtime environment files or credentials.

## Delivery

- SDK commits are exempt from LOC reduction and per-commit coverage gains.
  Preserve coverage, assertions, guards, diagnostics, and useful behavior.
  Report native Git statistics and full-source coverage against verified parent measurements.
  Never combine cross-language percentages.
- Run `bun run check:all` before commits, pushes, merges, and releases.
  SDK checks, builds, publishing, and deployments have no time limit.
  Record elapsed time; timing alone never blocks SDK delivery.
  Include tests, coverage, LOC, types, lint, formatting, security, contracts, docs, and p99 gap reporting.
  Never waive checks or count failed, skipped, unavailable, or incomplete checks as passing.
- Run `bun run build` separately. SDK builds have no time limit.
- P99 measurement coverage, performance, cost, and discovery scores are advisory targets.
  Report missing measurements and insufficient samples as gaps, never passing evidence.
- Keep local release tooling working. Try Actions for SDK publishing when available.
  Use the local publisher when Actions fails; do not wait on unavailable runners.
  Align versions, changelogs, tags, artifacts, registries, compatibility, and documentation.
  Required documentation precedes deployment. Verify publication and installation before declaring a package released.

## Code review rules

- Apply unslop and thermo-nuclear-code-quality-review before validation and delivery.
- Resolve correctness, security, billing, deployment-safety, contract, and blocking review findings.
- Use latest stable pinned dependencies and tooling suited to the Python ecosystem.
  Preserve enforcement, strict typing, reproducible installs, and useful behavior.
- Preserve complete failing output and seeds. Stop hangs after 60 seconds; let bounded fuzz campaigns finish.
- Reuse validation only while its code, dependencies, configuration, environment, and risks remain unchanged.
