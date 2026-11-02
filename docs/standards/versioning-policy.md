# Versioning Policy for Integration Assets

This document defines the versioning conventions and semantic guarantees for integration manifests, collector configurations, and documentation assets.

---

## 1. Semantic Versioning (SemVer 2.0)

All released integration artifacts follow [Semantic Versioning 2.0.0](https://semver.org/):

$$\text{MAJOR}.\text{MINOR}.\text{PATCH}$$

- **MAJOR**: Breaking changes to integration configurations, removal of previously supported runtimes, or structural shifts requiring user configuration rewrites.
- **MINOR**: Additions of newly validated integrations, non-breaking configuration options, or extended framework coverage.
- **PATCH**: Bug fixes, documentation corrections, broken link repairs, and security remediations.

---

## 2. Breaking Changes Governance

A change is classified as breaking if:
- It removes an existing configuration property or alters its default value.
- It changes the required network port or transport protocol.
- It requires an upstream library upgrade that drops backward compatibility.

Breaking changes must be preceded by a deprecation notice in a minor release.

---

## 3. Related Documentation

- [Compatibility Policy](compatibility-policy.md)
- [Integration Lifecycle](integration-lifecycle.md)
