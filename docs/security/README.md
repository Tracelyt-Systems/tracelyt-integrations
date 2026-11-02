# Security Architecture for Integrations

This directory defines the security posture, threat model, credential guidelines, and privacy policies for **Tracelyt Integrations**.

---

## Security Documentation Index

- [Integration Threat Model](integration-threat-model.md) — STRIDE-aligned threat model for external integrations and collector pipelines.
- [Credential Handling](credential-handling.md) — API keys, environment variables, secret managers, and zero-leak logging.
- [Network Security](network-security.md) — Mandatory TLS, certificate validation, egress boundaries, and proxies.
- [Permissions and Access](permissions-and-access.md) — Least-privilege monitoring permissions and read-only host access.
- [Telemetry Data Privacy](telemetry-data-privacy.md) — PII minimization, sensitive attribute scrubbing, and tenant isolation.

---

## Reporting a Security Issue

Please follow our private vulnerability reporting guidelines in [SECURITY.md](../../SECURITY.md). Do not submit security vulnerabilities via public GitHub issues.
