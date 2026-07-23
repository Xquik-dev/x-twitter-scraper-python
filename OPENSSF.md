# OpenSSF Best Practices Evidence

This register tracks the Gold assessment for this repository.

The official entry is [bestpractices.dev project 13738][badge].

Assessment date: 2026-07-23.

## Eligibility

This public Python SDK is active and released.

It is eligible for the OpenSSF Best Practices badge.

No OpenSSF-defined ineligibility applies.

## Verified Technical Controls

| Area | Evidence |
| --- | --- |
| License | Apache-2.0 and REUSE 3.3 metadata |
| Contribution process | DCO sign-off and independent review rules |
| Governance | Public roles, decisions, releases, and continuity policy |
| Security reporting | Private reporting, response targets, boundaries, and threat model |
| Tests | Python 3.10 and 3.14 with Pydantic 1 and 2 |
| Statement coverage | `./scripts/coverage` enforces 90% |
| Branch coverage | `./scripts/coverage` enforces 80% |
| Static analysis | Ruff, Pyright, Mypy, and CodeQL security-extended queries |
| Dependency review | Dependabot and pinned `pip-audit` |
| Licensing gate | Pinned REUSE action checks every repository file |
| Reproducibility | 2 wheels and source archives must have identical bytes |
| CI | Pull requests and pushes run pinned, least-privilege workflows |
| Two-factor authentication | The Xquik-dev organization requires 2FA |

The current matrix covers 10,305 of 10,941 statements, or 94.19%.

It covers 1,139 of 1,408 branches, or 80.89%.

The matrix runs 2,989 Pydantic 2 tests.

It runs 2,976 Pydantic 1 tests.

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

This remediation pull request needs a different human reviewer.

## Maintenance

Run these evidence commands before releases:

```sh
./scripts/lint
./scripts/test
./scripts/coverage
./scripts/audit
uvx --from reuse==6.2.0 reuse lint
./scripts/check-reproducible
```

Reassess the register before every major release.

Update bestpractices.dev only with public evidence.

[badge]: https://www.bestpractices.dev/projects/13738

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
