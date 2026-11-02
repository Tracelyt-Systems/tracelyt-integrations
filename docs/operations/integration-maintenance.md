# Integration Maintenance and Support SLA

This document defines the ongoing maintenance commitments, vulnerability triage timelines, and support guarantees for integrations in **Tracelyt Integrations**.

---

## 1. Support Level Commitments

Integrations marked with **`Supported`** status receive active maintenance:
- **Upstream Synchronization**: Compatibility matrices are reviewed and verified within 30 business days of upstream GA releases.
- **Vulnerability Remediation**: Critical security advisories in upstream collector distributions or referenced dependencies are triaged within 5 business days.
- **Bug Fixes**: Configuration bugs or broken example pipelines reported by the community are reviewed on a best-effort basis.

---

## 2. Deprecation and EOL Schedules

- Integrations targeting upstream software reaching end-of-life (EOL) are transitioned to `Deprecated` status.
- Deprecated integrations receive zero new feature enhancements and are removed from the active branch after a minimum of **90 calendar days**.

---

## 3. Related Documentation

- [Integration Lifecycle](../standards/integration-lifecycle.md)
- [Compatibility Policy](../standards/compatibility-policy.md)
- [Maintainers List](../../MAINTAINERS.md)

