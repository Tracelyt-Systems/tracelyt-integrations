# Upstream Dependency and Licensing Policy

This document defines the licensing, provenance, and verification standards for external libraries and upstream OpenTelemetry components referenced in **Tracelyt Integrations**.

---

## 1. Licensing and Provenance

- **Permissive Licenses Only**: All external packages, libraries, and collector components referenced in official guides must use OSI-approved permissive licenses compatible with Apache 2.0 (e.g., Apache 2.0, MIT, BSD-2/3-Clause).
- **Prohibited Licenses**: Components under copyleft licenses (GPL, AGPL) are prohibited from being packaged or distributed as core Tracelyt assets.
- **No Unattributed Source Copying**: Upstream source code must never be copied verbatim into this repository. Instead, integrations must consume dependencies via official package registries (Maven Central, PyPI, npm, Docker Hub).

---

## 2. Upstream Release Tracking

- Maintainers actively monitor release feeds for:
  - `opentelemetry-collector` and `opentelemetry-collector-contrib`.
  - Core language SDKs (`opentelemetry-java`, `opentelemetry-python`, etc.).
- Critical upstream security advisories trigger immediate triage and documentation updates.

---

## 3. Related Documentation

- [Compatibility Policy](compatibility-policy.md)
- [Versioning Policy](versioning-policy.md)
