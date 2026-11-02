# Maintainer Review Checklist for Integrations

This document provides maintainers with a standardized review rubric for evaluating integration guide pull requests in **Tracelyt Integrations**.

---

## 1. Architectural Fit & Scope
- [ ] Does the proposed integration respect [System Boundaries](../architecture/system-boundaries.md)?
- [ ] Is it placed in the correct category per [Integration Categories](../architecture/integration-categories.md)?
- [ ] Does it follow [OpenTelemetry Strategy](../architecture/opentelemetry-strategy.md) rather than proposing proprietary agents?

---

## 2. Documentation Structure & Standards
- [ ] Are all 17 sections of the [Standard Integration Guide Template](../templates/integration-guide-template.md) present?
- [ ] Are official upstream documentation links and repository URLs provided?
- [ ] Is the lifecycle status set accurately per [Integration Lifecycle](../standards/integration-lifecycle.md)? (Must start as `In Development` or `Experimental`).
- [ ] Are all code snippets syntactically valid YAML/JSON?

---

## 3. Security & Privacy Review
- [ ] Are all credentials represented as environment variable expansions (`${env:TOKEN}`)? Zero hardcoded secrets allowed.
- [ ] Does the guide mandate TLS for external network egress?
- [ ] Does it enforce least-privilege permissions (e.g., read-only database accounts)?
- [ ] Are sensitive attributes (authorization headers, cookies) scrubbed?

---

## 4. Verification & Validation
- [ ] Is there an actionable, reproducible validation procedure documented?
- [ ] Have the claimed software versions been verified against upstream release notes?
- [ ] Does `python tools/validate_docs.py` pass with zero errors?

