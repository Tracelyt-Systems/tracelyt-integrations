# Integration Architecture Documentation

This directory documents the integration architecture, ecosystem boundaries, and data flow models for **Tracelyt Integrations**.

> **Implementation Notice**: In accordance with Stage 1 (Foundation & Setup), all specifications in this directory represent **planned integration architecture**. No production instrumentation packages, receivers, or exporters are implemented during this setup phase.

---

## Architecture Index

1. [Integration Overview](integration-overview.md) — Subsystem role, mission, and ecosystem relationship.
2. [System Boundaries](system-boundaries.md) — Strict responsibility matrix with Tracelyt platform services.
3. [Integration Categories](integration-categories.md) — Languages, Frameworks, Infrastructure, Databases, Messaging, and Cloud.
4. [OpenTelemetry Strategy](opentelemetry-strategy.md) — Deep dive into OTLP, semantic conventions, and SDK vs Collector instrumentation.
5. [Collector Architecture](collector-architecture.md) — OpenTelemetry Collector pipelines: receivers, processors, exporters, and connectors.
6. [Telemetry Flow](telemetry-flow.md) — End-to-end data flow from monitored application to Tracelyt ingestion.
7. [Compatibility Architecture](compatibility-architecture.md) — Multi-dimensional compatibility matrix and verification model.

---

## Key Architectural Principles

- **OpenTelemetry-First**: Prefer established OpenTelemetry standards over proprietary instrumentation agents.
- **Evidence-Based Compatibility**: Do not claim an integration works without documented, reproducible validation.
- **Decoupled Governance**: Cross-service schemas belong in `tracelyt-specs`; deployment infrastructure belongs in `tracelyt-deploy`.
- **Zero Proprietary SDK Lock-In**: Applications export standard OTLP over HTTP or gRPC.
