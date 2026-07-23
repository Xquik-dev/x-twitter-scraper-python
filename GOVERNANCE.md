# Governance

## Scope

This repository publishes the Xquik Python SDK.

The public OpenAPI specification defines its external contract.

## Roles

Contributors propose changes, tests, documentation, and reviews.

Maintainers hold repository administration and release permissions.

GitHub organization access remains the authority for maintainer permissions.

## Decisions

Use public issues for non-sensitive design discussions.

Use pull requests for reviewed repository changes.

Preserve generated API contracts unless the public specification changes.

Prefer consensus for user-visible and governance decisions.

Document unresolved tradeoffs in the pull request.

## Reviews

Every nontrivial change requires review before release.

Maintainer-authored changes require another human reviewer.

Security-sensitive changes require an explicit security review.

Reviewers follow the shared [review policy][review-policy].

## Releases

Release automation prepares version and changelog updates.

Maintainers verify tests, security gates, and release metadata.

Release tags must reference the reviewed default-branch commit.

Python wheel and source archives must remain reproducible.

## Maintainer Changes

Sustained contributors may request maintainer consideration.

Existing maintainers evaluate judgment, reliability, and security practices.

Remove inactive access when continuity and security permit.

Document material governance changes through reviewed pull requests.

## Continuity

At least 2 maintainers should hold required release access.

Current public evidence does not yet prove that threshold.

Track this limitation in [OPENSSF.md](OPENSSF.md).

[review-policy]: https://github.com/Xquik-dev/.github/blob/main/REVIEWING.md

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
