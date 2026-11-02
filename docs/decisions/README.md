# Architecture Decision Records (ADRs)

This directory documents key architectural decisions made for **Tracelyt Integrations**. We use the Architecture Decision Record (ADR) process to capture the context, rationale, trade-offs, and consequences of significant technical choices.

---

## ADR Process

1. **Format**: Follow the template defined in [adr-template.md](adr-template.md).
2. **Numbering**: Use four-digit sequential numbering (`0001-...md`).
3. **Status Workflow**:
   - `Proposed` — Under active review by maintainers.
   - `Accepted` — Approved and adopted as official architecture.
   - `Rejected` — Evaluated and declined.
   - `Superseded` — Replaced by a subsequent ADR.
   - `Deprecated` — No longer applicable.

---

## Decision Log

| ID | Title | Status | Date | Primary Driver |
| :--- | :--- | :--- | :--- | :--- |
| [ADR-0001](0001-adopt-opentelemetry-standard.md) | Adopt OpenTelemetry as the Primary Interoperability Standard | **Accepted** | 2026-10-30 | Vendor neutrality, broad language support, and open semantic conventions. |

---

## Related Documentation

- [Integration Overview](../architecture/integration-overview.md)
- [OpenTelemetry Strategy](../architecture/opentelemetry-strategy.md)
- [Governance Model](../../GOVERNANCE.md)

