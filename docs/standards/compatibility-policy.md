# Compatibility and Support Policy

This document defines the compatibility requirements, verification criteria, and deprecation timelines for integrations maintained within **Tracelyt Integrations**.

---

## 1. Supported Version Policies

1. **Active Runtimes Only**: Integrations prioritize runtimes actively supported by upstream maintainers (e.g., Python 3.10+, Node.js 18/20 LTS, Java 17/21 LTS). End-of-life (EOL) runtimes are not officially supported.
2. **Upstream OpenTelemetry Versioning**: Integrations target stable OpenTelemetry core releases. Alpha or experimental upstream plugins are tagged with `Experimental` status.
3. **Multi-Version Verification**: Guides must record the exact version range tested, rather than asserting open-ended compatibility (`"Tested on Spring Boot 3.2.0–3.3.2"` instead of `"Supports Spring Boot 3+"`).

---

## 2. Deprecation and Sunset Policy

When an upstream library or integration pattern is superseded:
1. **Deprecation Notice**: The guide header is updated to `Deprecated` status with a link to the replacement integration.
2. **Transition Window**: Deprecated integrations remain in the repository for a minimum of **90 calendar days**.
3. **Removal**: After 90 days, assets are archived and removed from the active branch in a minor or major release.

---

## 3. Related Documentation

- [Compatibility Architecture](../architecture/compatibility-architecture.md)
- [Versioning Policy](versioning-policy.md)
- [Integration Lifecycle](integration-lifecycle.md)
