# Telemetry Data Privacy and PII Minimization

This document outlines the privacy guidelines, Personally Identifiable Information (PII) filtering rules, and data minimization standards for **Tracelyt Integrations**.

> **CORE PRINCIPLE**: Do not assume telemetry data is safe to transmit simply because it is collected via OpenTelemetry. Application traces and error logs frequently contain sensitive user data that must be scrubbed before export.

---

## 1. High-Risk Telemetry Attributes

Application instrumentation commonly captures sensitive attributes that must be scrubbed or obfuscated:
- **Authentication Secrets**: `authorization` headers, `cookie` headers, JWTs, API tokens, passwords in HTTP query strings or request bodies.
- **Direct PII**: Email addresses, telephone numbers, postal addresses, government identification numbers (SSNs).
- **Financial & Payment Data**: Credit card numbers (PANs), CVVs, bank account identifiers.
- **Sensitive Database Queries**: Raw SQL queries containing unmasked user input in `WHERE` clauses.

---

## 2. Pre-Export Scrubbing via Collector Processors

The OpenTelemetry Collector provides processors to scrub sensitive attributes at the edge before telemetry exits the customer network:

```yaml
processors:
  # 1. Strip sensitive HTTP headers and attributes
  attributes/privacy:
    actions:
      - key: http.request.header.authorization
        action: delete
      - key: http.request.header.cookie
        action: delete
      - key: enduser.id
        action: hash

  # 2. Redact sensitive SQL query strings using transform processor
  transform/redact_queries:
    error_mode: ignore
    trace_statements:
      - context: span
        statements:
          - replace_pattern(attributes["db.statement"], "password='[^']*'", "password='[REDACTED]'")
          - replace_pattern(attributes["db.statement"], "token='[^']*'", "token='[REDACTED]'")
```

---

## 3. Data Minimization Principles

1. **Collect Only What Is Needed**: Disable verbose auto-instrumentation modules that capture full HTTP request/response bodies unless explicitly required for diagnostic triage.
2. **Span Sampling**: Use head-based or tail-based sampling in production to limit data volume and reduce privacy exposure.
3. **Tenant & Project Scoping**: All exported telemetry must include the `tracelyt.project.id` resource attribute to ensure strict data partitioning at ingestion.

---

## 4. Related Documentation

- [Integration Threat Model](integration-threat-model.md)
- [Credential Handling](credential-handling.md)
- [Collector Architecture](../architecture/collector-architecture.md)

