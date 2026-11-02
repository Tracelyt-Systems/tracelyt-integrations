# ADR-0001: Adopt OpenTelemetry as the Primary Interoperability Standard

- **Status**: Accepted
- **Date**: 2026-10-30
- **Authors**: Tracelyt Maintainers
- **Deciders**: Maintainer Team

---

## 1. Context and Problem Statement

An observability platform requires mechanisms to collect traces, metrics, and logs across diverse programming languages, application frameworks, cloud providers, and infrastructure platforms.

Historically, observability vendors built proprietary agents, custom bytecode manipulation tools, and proprietary wire protocols. We must evaluate whether Tracelyt should develop custom agents and protocols or standardize on the CNCF [OpenTelemetry](https://opentelemetry.io/) project.

---

## 2. Decision Drivers

- **Vendor Neutrality & Open Standards**: Customers reject proprietary agent lock-in; open standards foster trust.
- **Ecosystem Breadth**: OpenTelemetry maintains production-ready SDKs across 11+ languages, auto-instrumentation agents, and hundreds of community collector components.
- **Engineering Focus**: Standardizing on OpenTelemetry allows the Tracelyt engineering team to concentrate platform innovation on stream processing, query engines, and AI investigation rather than rebuilding basic byte-code agents.
- **Interoperability**: Standard OTLP protocols allow customers to switch or fan-out telemetry seamlessly without modifying application source code.

---

## 3. Considered Options

1. **Adopt OpenTelemetry as the Core Standard**: Build Tracelyt integrations natively around OpenTelemetry SDKs, Semantic Conventions, and the OpenTelemetry Collector.
2. **Develop Proprietary Tracelyt Agents**: Build custom Java, Python, and Go agents with a custom wire protocol. High maintenance burden and slow feature parity.
3. **Hybrid Model (Proprietary Agent + OTLP Bridge)**: Build custom agents that can export OTLP. Unnecessary complexity and code duplication.

---

## 4. Decision Outcome

Chosen option: **Option 1: Adopt OpenTelemetry as the Core Standard**.

### Positive Consequences
- Immediate compatibility with any application already instrumented with OpenTelemetry.
- Zero proprietary agent installation required on customer workloads.
- Shared semantic conventions across all Tracelyt services (`tracelyt-ingestion`, `tracelyt-query-engine`, `tracelyt-ai-investigator`).
- Long-term stability under CNCF governance.

### Negative Consequences / Trade-offs
- Upstream breaking changes or alpha component deprecations in OpenTelemetry must be tracked and managed.
- Tracelyt depends on upstream collector distributions for specialized infrastructure receivers.

---

## 5. Security & Privacy Implications

- OpenTelemetry Collector enables local scrubbing of PII and credentials before data leaves the customer perimeter.
- Avoids the security risks of installing untrusted proprietary binary kernel modules or root daemons.

---

## 6. Revisit Conditions

This decision will be re-evaluated if:
- OpenTelemetry introduces licensing changes that restrict open-source adoption.
- Specific mission-critical telemetry signals cannot be represented within OpenTelemetry Semantic Conventions.

