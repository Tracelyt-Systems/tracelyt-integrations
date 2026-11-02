# Integration Catalog (`integrations/`)

This directory is designated for future integration-specific guides, component definitions, and approved configuration snippets for connecting third-party technologies with Tracelyt.

> **Implementation Notice**: In accordance with Stage 1 (Foundation & Setup), **no production integration code or configuration packages are implemented during this setup task**. This document establishes the folder structure, naming conventions, and acceptance criteria for future integrations.

---

## 1. Future Directory Organization

When approved integrations are implemented, they will be organized into categorized subdirectories:

```text
integrations/
├── languages/                   # Language-specific SDK configurations (java, python, nodejs, go, dotnet)
├── frameworks/                  # Framework guides (spring-boot, fastapi, express, aspnetcore)
├── infrastructure/              # Infrastructure and host monitors (docker, kubernetes, linux)
├── databases/                   # Database monitoring configs (mysql, mongodb, redis)
├── messaging/                   # Message broker tracing configs (kafka, rabbitmq)
└── cloud/                       # Cloud provider telemetry connectors (aws, azure, gcp)
```

---

## 2. Integration Acceptance Criteria

Before an integration guide or configuration asset can be committed to this catalog:
1. **Lifecycle Status**: Must be officially accepted and track its stage per the [Integration Lifecycle](../docs/standards/integration-lifecycle.md).
2. **Template Compliance**: Must strictly follow the [Standard Integration Guide Template](../docs/templates/integration-guide-template.md).
3. **Upstream Grounding**: Must reference official OpenTelemetry or vendor instrumentation documentation.
4. **Security Review**: Must adhere to [Credential Handling](../docs/security/credential-handling.md) and [Telemetry Data Privacy](../docs/security/telemetry-data-privacy.md).
5. **No Fake Claims**: An integration cannot be marked `Validated` or `Supported` without documented, reproducible test evidence.
