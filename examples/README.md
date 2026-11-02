# Example Applications Policy (`examples/`)

This directory is designated for future reproducible example applications demonstrating how to instrument and connect external workloads to Tracelyt.

> **Policy Notice**: In accordance with the Stage 1 engineering prompt, **no mock or fake sample applications are created during this setup task**. This document establishes the strict quality, security, and verification requirements that any future example application must satisfy.

---

## 1. What Qualifies as an Example Application

An approved example application must:
1. **Be Self-Contained and Minimal**: Contain only the minimal code necessary to demonstrate telemetry instrumentation (tracing, metrics, or logs).
2. **Use Official OpenTelemetry Standards**: Use official OpenTelemetry SDKs and standard OTLP exporters.
3. **Be Fully Reproducible**: Must run cleanly on a developer's workstation without requiring private proprietary infrastructure or paid third-party licenses.

---

## 2. Mandatory Documentation Requirements for Examples

Every future example must include its own `README.md` covering:
- **Prerequisites**: Exact runtime versions (e.g., Python 3.12, JDK 21, Node.js 20).
- **Setup & Launch**: Step-by-step instructions to install dependencies and run the application.
- **Verification Commands**: `curl` commands or HTTP requests to generate synthetic traffic and trigger spans.
- **Expected Telemetry Behavior**: Clear description of the traces, spans, and metric counters emitted.
- **Cleanup Commands**: Explicit steps to stop processes and tear down any local containers (`docker compose down -v`).

---

## 3. Security Restrictions

- **Zero Credentials**: Examples must never embed real API tokens, license keys, or passwords.
- **Environment Variables**: All endpoints and authentication tokens must be injected via environment variables (e.g., `OTEL_EXPORTER_OTLP_ENDPOINT`, `TRACELYT_PROJECT_TOKEN`).
- **No Unexpected External Costs**: Examples must not spin up paid cloud resources by default.
