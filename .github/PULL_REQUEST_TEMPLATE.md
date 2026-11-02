## Description

Briefly describe the purpose of this pull request, the integration technology addressed, and context.

Fixes #(issue)

---

## Type of Change

- [ ] New integration guide or documentation
- [ ] Integration status promotion / lifecycle update
- [ ] Architecture or standards update
- [ ] CI/CD or repository tooling improvement
- [ ] Bug fix / broken link repair

---

## Architectural & Boundary Checklist

- [ ] Respects [System Boundaries](../docs/architecture/system-boundaries.md) (no ingestion or pipeline logic).
- [ ] Uses [Standard Integration Guide Template](../docs/templates/integration-guide-template.md) for new guides.
- [ ] Aligned with [OpenTelemetry Strategy](../docs/architecture/opentelemetry-strategy.md).
- [ ] Compatibility claims are verified against official upstream references.
- [ ] No real secrets, passwords, or credentials are committed.

---

## Quality Checklist

- [ ] Documentation links verified via `python tools/validate_docs.py` (or `make docs-check`).
- [ ] Formatting adheres to `.editorconfig` rules.
