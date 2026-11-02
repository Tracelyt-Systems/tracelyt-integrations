# Integration Documentation Standards

This document establishes the authoring standards, content requirements, and quality checks for integration guides in **Tracelyt Integrations**.

---

## 1. Documentation Principles

1. **Mandatory Template**: Every integration guide must follow the [Standard Integration Guide Template](../templates/integration-guide-template.md).
2. **Upstream Attribution**: Always cite official upstream documentation and package repositories (e.g., PyPI, Maven Central, npm).
3. **Explicit Labeling**: Clearly label all technical statements:
   - `[Verified]`: Confirmed via reproducible test run.
   - `[Upstream Requirement]`: Mandatory constraint imposed by the upstream technology.
   - `[Tracelyt Requirement]`: Specific header or token configuration needed by Tracelyt.
   - `[Planned]`: Future capability not yet verified.
   - `[Known Limitation]`: Explicit edge cases, uninstrumented routes, or missing metrics.

---

## 2. Configuration Code Blocks

- Configuration snippets (YAML, JSON, XML) must be syntactically valid and tested.
- Secrets must always use placeholder syntax (`${TRACELYT_PROJECT_TOKEN}`). Never commit real credentials.

---

## 3. Related Documentation

- [Integration Guide Template](../templates/integration-guide-template.md)
- [Integration Lifecycle](integration-lifecycle.md)
- [Configuration Conventions](configuration-conventions.md)
