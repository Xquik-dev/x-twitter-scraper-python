# Security Policy

## Supported Versions

Security fixes target the latest published release.

Upgrade before reporting behavior from an older release.

## Report A Vulnerability

Use [GitHub private vulnerability reporting][private-report].

Email [support@xquik.com](mailto:support@xquik.com) when GitHub is unavailable.

Do not open a public issue.

Include affected versions, impact, reproduction steps, and suggested mitigations.

Remove credentials, personal data, and private service details.

We aim to acknowledge reports within 3 business days.

We aim to provide a status update within 7 business days.

We coordinate disclosure after confirming and fixing the issue.

## Security Boundaries

This SDK builds requests and parses documented API responses.

Applications control credentials, base URLs, transports, retries, and middleware.

Only send credentials to trusted HTTPS endpoints.

Treat response data and webhook payloads as untrusted input.

The hosted Xquik service has a separate operational boundary.

This repository excludes private infrastructure and service implementation details.

## Threat Model

Relevant threats include:

- Credential leakage through logs, URLs, middleware, or debug output.
- Request redirection through untrusted base URLs.
- Malformed responses causing unsafe parsing or resource exhaustion.
- Dependency, generator, workflow, and release supply-chain compromise.
- Unsafe asynchronous access or transport behavior.

Security controls include redaction tests, CodeQL, and fuzzing.

CI also verifies dependencies, licenses, coverage, and reproducible archives.

## Response Process

Maintainers triage reports privately.

Confirmed fixes use private coordination when an embargo is needed.

Maintainers add regression tests and run every required gate.

Releases document user impact without exposing exploit details prematurely.

Maintainers publish an advisory when coordinated disclosure permits.

[private-report]: https://github.com/Xquik-dev/x-twitter-scraper-python/security/advisories/new

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
