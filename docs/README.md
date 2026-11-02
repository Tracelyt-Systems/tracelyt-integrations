# Tracelyt Integrations Documentation

Welcome to the documentation for **Tracelyt Integrations** (`tracelyt-integrations`), the integration guidance, compatibility catalog, and collector configuration repository of the Tracelyt open-source observability platform.

---

## Documentation Navigation

### 1. Integration Architecture
- [Architecture Overview](architecture/README.md) — Architectural overview, core capabilities, and principles.
- [Integration Overview](architecture/integration-overview.md) — Mission, role within Tracelyt, and primary integration touchpoints.
- [System Boundaries](architecture/system-boundaries.md) — Responsibility matrix across Tracelyt platform repositories.
- [Integration Categories](architecture/integration-categories.md) — Classification: Languages, Frameworks, Infrastructure, Databases, Messaging, and Cloud.
- [OpenTelemetry Strategy](architecture/opentelemetry-strategy.md) — Standards alignment, semantic conventions, OTLP, and signals.
- [Collector Architecture](architecture/collector-architecture.md) — OpenTelemetry Collector pipelines: receivers, processors, exporters, and connectors.
- [Telemetry Flow](architecture/telemetry-flow.md) — End-to-end data flow from monitored application to Tracelyt ingestion.
- [Compatibility Architecture](architecture/compatibility-architecture.md) — Multi-dimensional compatibility matrix and verification model.

### 2. Integration Standards & Governance
- [Standards Overview](standards/README.md) — Standards and engineering policies index.
- [Integration Lifecycle](standards/integration-lifecycle.md) — 8-stage lifecycle from Proposed to Supported or Deprecated.
- [Integration Documentation Standard](standards/integration-documentation.md) — Guidelines for writing accurate, verified integration guides.
- [Compatibility Policy](standards/compatibility-policy.md) — Upstream version verification and support timelines.
- [Versioning Policy](standards/versioning-policy.md) — Semantic versioning (SemVer 2.0) for integration assets.
- [Upstream Dependency Policy](standards/upstream-dependency-policy.md) — Dependency trust, licensing, and upstream tracking.
- [Configuration Conventions](standards/configuration-conventions.md) — Environment variables, YAML naming, and secure defaults.

### 3. Guide Templates
- [Templates Overview](templates/README.md) — Overview of reusable contributor templates.
- [Standard Integration Guide Template](templates/integration-guide-template.md) — 17-section mandatory template for all integration guides.

### 4. Security & Privacy
- [Security Architecture Overview](security/README.md) — Security posture, threat boundaries, and objectives.
- [Integration Threat Model](security/integration-threat-model.md) — STRIDE-aligned threat model for external integrations.
- [Credential Handling](security/credential-handling.md) — Secret management, environment variables, and zero-leak logging.
- [Network Security](security/network-security.md) — TLS requirements, endpoint validation, and egress proxies.
- [Permissions and Access](security/permissions-and-access.md) — Least-privilege monitoring permissions and read-only defaults.
- [Telemetry Data Privacy](security/telemetry-data-privacy.md) — PII masking, attribute scrubbing, and data minimization.

### 5. Developer Experience & Testing
- [Developer Hub Overview](development/README.md) — Overview of developer resources and contribution paths.
- [Development Setup](development/development-setup.md) — Workstation prerequisites and validation tool usage.
- [Contribution Workflow](development/contribution-workflow.md) — PR lifecycle, branch management, and review standards.
- [Testing Guidelines](development/testing-guidelines.md) — 5-tier validation strategy for integration assets.
- [Review Checklist](development/review-checklist.md) — Maintainer review criteria for integration PRs.

### 6. Operations & Maintenance
- [Operations Overview](operations/README.md) — Operational principles and integration maintenance guidelines.
- [Troubleshooting Guide](operations/troubleshooting.md) — Diagnosing missing telemetry, connection timeouts, and collector crashes.
- [Compatibility Verification](operations/compatibility-verification.md) — Procedures for verifying upstream releases.
- [Integration Maintenance](operations/integration-maintenance.md) — Ongoing maintenance commitments and deprecation schedules.

### 7. Architecture Decision Records (ADRs)
- [ADR Index](decisions/README.md) — Decision log and ADR lifecycle state machine.
- [ADR Template](decisions/adr-template.md) — Standardized format for technical proposals.
- [ADR-0001: Adopt OpenTelemetry as Interoperability Standard](decisions/0001-adopt-opentelemetry-standard.md) — Core interoperability decision.

### 8. Roadmap
- [Milestone Roadmap](roadmap/README.md) — 6-phase evolutionary engineering roadmap.
