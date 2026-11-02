# Configuration Conventions and Environment Standards

This document establishes the configuration conventions, environment variable naming standards, and secure defaults for **Tracelyt Integrations**.

---

## 1. Environment Variable Standards

Integrations adhere to standard OpenTelemetry environment variables supplemented by Tracelyt project context:

| Variable Name | Required? | Example Value | Description |
| :--- | :--- | :--- | :--- |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | Yes | `https://ingest.tracelyt.io:4317` | Target OTLP gRPC or HTTP endpoint. |
| `OTEL_SERVICE_NAME` | Yes | `order-service` | Logical service name identifying the workload. |
| `OTEL_EXPORTER_OTLP_HEADERS` | Conditional | `x-tracelyt-token=${TRACELYT_TOKEN}` | Authentication headers required by ingestion. |
| `OTEL_RESOURCE_ATTRIBUTES` | Optional | `deployment.environment=production` | Key-value resource metadata. |
| `OTEL_TRACES_SAMPLER` | Optional | `parentbased_always_on` | Sampling strategy. |

---

## 2. Collector YAML Formatting Rules

- **Indentation**: Exactly 2 spaces. No tab characters.
- **Key Naming**: lower_snake_case for OpenTelemetry Collector configuration properties.
- **Zero Secrets**: Credentials must use environment variable expansion syntax: `${env:TRACELYT_TOKEN}`.

---

## 3. Related Documentation

- [OpenTelemetry Strategy](../architecture/opentelemetry-strategy.md)
- [Collector Architecture](../architecture/collector-architecture.md)
- [Credential Handling](../security/credential-handling.md)
