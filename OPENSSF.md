# OpenSSF Best Practices Evidence

This register tracks the Gold assessment for this repository.

The official entry is [bestpractices.dev project 13738][badge].

The assessment is dated 2026-07-23.

## Eligibility

This public Python SDK is active and released.

It is eligible for the OpenSSF Best Practices badge.

No OpenSSF-defined ineligibility applies.

## Verified Technical Controls

| Area | Evidence |
| --- | --- |
| License | Apache-2.0 and REUSE 3.3 metadata |
| Contribution process | DCO sign-off, and `bin/check-local` before every merge |
| Governance | Public roles, decisions, releases, and continuity policy |
| Security reporting | Private reporting, response targets, boundaries, and threat model |
| Tests | Python 3.10 and 3.14 with Pydantic 1 and 2 |
| Statement coverage | `./scripts/coverage` enforces 90% |
| Branch coverage | `./scripts/coverage` enforces 80% |
| Static analysis | Ruff, Pyright, Mypy, and CodeQL security-extended queries |
| Dependency review | Pinned `pip-audit` with reviewed exceptions in `bin/check-local` and `bin/release-local` |
| Licensing gate | Pinned REUSE lint in `bin/check-local` checks every repository file |
| Reproducibility | 2 wheels and source archives must have identical bytes |
| Local checks | `bin/check-local` runs every gate before review and release |
| Two-factor authentication | The Xquik-dev organization requires 2FA |

The current matrix covers 12,010 of 12,654 statements, or 94.91%.

It covers 1,149 of 1,418 branches, or 81.03%.

The matrix runs 3,029 Pydantic 2 tests.

It runs 3,016 Pydantic 1 tests.

## Outstanding Gold Blockers

Human and organizational evidence remains incomplete.

Do not claim Gold while any mandatory criterion remains unmet.

| Gold Requirement | Current Evidence | Required Action |
| --- | --- | --- |
| Access continuity | Public evidence does not prove 2 release-capable maintainers | Grant and verify another maintainer's access |
| Bus factor | Git history shows one significant contributor | Add another significant contributor |
| Unassociated contributors | Fewer than 2 qualifying contributors are independent | Accept qualifying external contributions |
| Independent review | History does not prove 50% qualifying review coverage | Require and record independent reviews |
| Human security review | No completed review exists within 5 years | Commission and publish a scoped review |

Gold eligibility still requires review by a different human.

## Maintenance

Run the evidence commands before releases.

```sh
bin/check-local
```

It runs lint, tests, coverage, the dependency audit, REUSE lint, and reproducibility checks.

Reassess the register before every major release.

Update bestpractices.dev only with public evidence.

[badge]: https://www.bestpractices.dev/projects/13738

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
