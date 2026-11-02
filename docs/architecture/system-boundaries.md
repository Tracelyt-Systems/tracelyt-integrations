# Service Boundaries and Platform Responsibilities

This document defines the strict architectural boundaries between `tracelyt-integrations` and other repositories within the Tracelyt open-source observability platform.

---

## Service Responsibility Matrix

| Platform Service | Service Owns | Integrations Repository Does NOT Own |
| :--- | :--- | :--- |
| **`tracelyt-control-plane`** | Organizations, projects, users, authentication, authorization, project API tokens, quotas, and management APIs. | Integrations do not issue project tokens, manage user accounts, or store organization memberships. |
| **`tracelyt-ingestion`** | Receiving telemetry over OTLP (gRPC/HTTP), admission control, payload validation, and rate limiting. | Integrations do not implement server-side telemetry receivers or ingestion endpoints. |
| **`tracelyt-specs`** | Authoritative source of truth for cross-service API contracts, event envelopes, and schema governance. | Integrations do not independently invent custom Tracelyt wire protocols or conflicting message schemas. |
| **`tracelyt-telemetry-pipeline`**| Batching, enrichment, filtering, aggregation, and routing of telemetry streams. | Integrations do not replace or replicate backend stream processing pipelines. |
| **`tracelyt-query-engine`** | Querying telemetry storage, computing metric aggregations, filtering logs, and trace flame-graph retrieval. | Integrations do not query telemetry storage clusters directly. |
| **`tracelyt-alerting`** | Alert rule definitions, condition evaluations, incident lifecycles, and notification intents. | Integrations do not evaluate alert conditions or manage incident state. |
| **`tracelyt-notifications`** | Delivering alert and incident messages via email, Slack, Teams, Discord, and webhooks. | Integrations do not deliver end-user notification messages. |
| **`tracelyt-ai-investigator`** | AI-assisted incident triage, telemetry evidence correlation, RAG, and root-cause analysis. | Integrations do not execute AI reasoning, prompt templates, or incident investigation agents. |
| **`tracelyt-deploy`** | Helm charts, Kubernetes operators, Docker Compose, Terraform modules, and platform deployment orchestration. | Integrations do not maintain platform-wide deployment infrastructure. |

---

## Architectural Interaction Rules

1. **Standards-Based Ingress**: Integrations document how workloads export telemetry using official OpenTelemetry standards (OTLP/gRPC and OTLP/HTTP) to `tracelyt-ingestion`.
2. **Configuration Assets**: Any future OpenTelemetry Collector configuration snippets provided in this repository must point to standard OTLP endpoints documented by `tracelyt-ingestion`.
3. **No Proprietary Overrides**: Integrations must never mandate proprietary, vendor-locked agent binaries when standard OpenTelemetry SDKs or collectors are available.

---

## Related Documentation

- [Integration Overview](integration-overview.md)
- [OpenTelemetry Strategy](opentelemetry-strategy.md)
- [Integration Lifecycle](../standards/integration-lifecycle.md)
