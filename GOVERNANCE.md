# Project Governance

This document describes the governance model, roles, decision-making processes, and integration evaluation criteria for `tracelyt-integrations`.

---

## 1. Governance Principles

- **Openness & Consensus**: Integration evaluations, architecture decisions, and lifecycle promotions are conducted transparently on GitHub.
- **Evidence-Based Support**: Integrations are promoted through lifecycle stages (`Proposed` -> `Planned` -> `In Development` -> `Experimental` -> `Validated` -> `Supported`) strictly based on documented verification data.
- **Standards-First**: OpenTelemetry semantic conventions and OTLP protocols are prioritized over proprietary configurations.

---

## 2. Roles and Responsibilities

### Contributors
Anyone who submits integration documentation, configuration validation fixes, or architectural proposals.

### Maintainers
Active stewards of the repository responsible for:
- Reviewing and approving integration proposals.
- Validating compatibility reports and upstream dependencies.
- Managing lifecycle state transitions in the integration catalog.
- Upholding security, credential sanitization, and documentation hygiene.

Current maintainers are listed in [MAINTAINERS.md](MAINTAINERS.md).

---

## 3. Decision-Making Process

1. **Architecture Decision Records (ADRs)**: Fundamental architectural shifts (e.g., standardizing on OpenTelemetry, defining collector packaging requirements) require an ADR following [docs/decisions/adr-template.md](docs/decisions/adr-template.md).
2. **Integration Acceptance**: Adding a new official integration guide requires review by at least one maintainer and verification of upstream software references.
