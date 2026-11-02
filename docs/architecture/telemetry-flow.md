# Telemetry Flow and Ingestion Pipeline

This document describes the end-to-end telemetry flow from monitored customer applications and infrastructure into Tracelyt's backend services.

---

## 1. End-to-End Telemetry Sequence

```mermaid
sequenceDiagram
    autonumber
    participant App as Monitored Workload (e.g., Spring / FastAPI)
    participant SDK as OpenTelemetry SDK / Agent
    participant Collector as Local Collector Sidecar / Gateway
    participant Ingestion as tracelyt-ingestion
    participant Pipeline as tracelyt-telemetry-pipeline
    participant Storage as Telemetry Storage (ClickHouse)

    App->>SDK: Application Event / Request Handled
    SDK->>SDK: Generate Span & Metric Records (Inject Context)
    SDK->>Collector: Export OTLP/gRPC (localhost:4317)
    Note over Collector: Memory Limiter & Batch Processing
    Collector->>Ingestion: Authenticated OTLP/gRPC (TLS + Project Token)
    Ingestion->>Ingestion: Validate Token & Admission Control
    Ingestion->>Pipeline: Enqueue Validated Batch
    Pipeline->>Pipeline: Enrich, Deduplicate, & Route
    Pipeline->>Storage: Commit to Telemetry Storage Tables
```

---

## 2. Ingestion Network Contract

To ensure predictable firewall and routing configuration:
- **Protocol**: OTLP over gRPC (HTTP/2) or OTLP over HTTP (HTTP/1.1 or HTTP/2).
- **Authentication**: Bearer token or custom header (`X-Tracelyt-Project-Token`) validated by `tracelyt-ingestion` against `tracelyt-control-plane`.
- **Encryption**: TLS 1.2 or TLS 1.3 is mandatory for external egress to public Tracelyt endpoints.

---

## 3. Related Documentation

- [OpenTelemetry Strategy](opentelemetry-strategy.md)
- [Collector Architecture](collector-architecture.md)
- [System Boundaries](system-boundaries.md)
