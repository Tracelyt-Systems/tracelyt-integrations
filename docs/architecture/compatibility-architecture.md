# Compatibility Architecture and Verification Model

This document outlines the multi-dimensional compatibility model and verification guidelines for **Tracelyt Integrations**.

---

## 1. Multi-Dimensional Compatibility Dimensions

An observability integration depends on multiple interoperability layers:

1. **Target Runtime**: Python 3.10–3.12, JDK 17/21 LTS, Node.js 18/20 LTS, .NET 8.0+.
2. **Framework Version**: Spring Boot 3.2.x/3.3.x, FastAPI 0.110+, Express 4.x/5.x.
3. **OpenTelemetry SDK Version**: Language-specific SDK releases (e.g., `opentelemetry-java` 1.35+).
4. **Collector Distribution**: `otelcol` or `otelcol-contrib` release version (e.g., v0.100.0+).
5. **Tracelyt Ingestion Contract**: Ingestion protocol compatibility defined in `tracelyt-specs`.

---

## 2. Compatibility Matrix Format (Template)

Integration guides record compatibility using the following verified schema:

| Target Technology | Technology Version | OpenTelemetry SDK / Component | Verified Collector Version | Verification Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Spring Boot** | 3.3.x | `opentelemetry-javaagent` v2.5.0 | `otelcol-contrib` v0.104.0 | Planned (Unverified) | `Planned` |
| **FastAPI** | 0.111.x | `opentelemetry-instrumentation-fastapi` v0.46b0 | `otelcol-contrib` v0.104.0 | Planned (Unverified) | `Planned` |
| **Express.js** | 4.19.x | `@opentelemetry/instrumentation-express` v0.40.0 | `otelcol-contrib` v0.104.0 | Planned (Unverified) | `Planned` |

> **Rule**: Until a matrix entry is tested against real workloads in a reproducible environment, the status must remain `Planned` or `Experimental`.

---

## 3. Related Documentation

- [Compatibility Policy](../standards/compatibility-policy.md)
- [Integration Lifecycle](../standards/integration-lifecycle.md)
- [Testing Guidelines](../development/testing-guidelines.md)
