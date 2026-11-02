# Validation Framework and Asset Guidelines (`validation/`)

This directory is designated for future automated validation suites, collector syntax linters, and compatibility verification assets.

> **Validation Policy**: In accordance with the Stage 1 engineering prompt, **no fake tests or simulated success scripts are created during this setup task**. This document establishes the validation standards for future integration verification.

---

## 1. Planned Validation Categories

When integration assets and collector configurations are added to the repository, they will be verified across five validation layers:

| Layer | Validation Purpose | Verification Tooling |
| :--- | :--- | :--- |
| **1. Configuration Syntax** | Verify YAML/JSON syntax and schema conformance of OpenTelemetry Collector manifests. | `yamllint`, OpenTelemetry Collector `validate` subcommand. |
| **2. Component Availability** | Verify that referenced receivers, processors, and exporters exist in the targeted Collector distribution (Core vs Contrib). | Automated manifest parser comparing against component registries. |
| **3. Instrumentation Initialization** | Verify that language SDKs and auto-instrumentation agents attach successfully without crashing the host application. | Dockerized container startup assertions. |
| **4. Telemetry Signal Verification** | Verify that emitted spans, metrics, and logs conform to OpenTelemetry Semantic Conventions. | Local mock OTLP receivers inspecting payload attributes. |
| **5. Regression Testing** | Verify that new upstream framework or SDK releases do not break existing Tracelyt integration patterns. | Scheduled matrix workflows in CI. |

---

## 2. No Synthetic Pass Rule

- A test or validation script must never return exit code 0 unless it has genuinely verified real application or collector telemetry behavior.
- Incomplete or experimental integrations must be labeled as `Experimental` or `In Development`, rather than fabricating passing test runs.
