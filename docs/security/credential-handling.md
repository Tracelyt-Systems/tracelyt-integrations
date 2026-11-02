# Credential Handling and Secret Management

This document establishes the security guidelines for managing authentication credentials, API tokens, and database passwords across **Tracelyt Integrations**.

---

## 1. Principles of Credential Safety

1. **Zero Plaintext Secrets**: No API keys, project tokens, or database passwords may ever be hardcoded into integration guides, collector manifests, or repository files.
2. **Environment Variable Expansion**: Collectors must resolve credentials at runtime via environment variables:
   ```yaml
   exporters:
     otlp:
       endpoint: https://ingest.tracelyt.io:4317
       headers:
         x-tracelyt-token: ${env:TRACELYT_PROJECT_TOKEN}
   ```
3. **Secret Store Integration**: In production Kubernetes deployments, environment variables should be populated from Kubernetes `Secret` objects or external secret operators (HashiCorp Vault, AWS Secrets Manager).
4. **Log Sanitization**: Collector logging exporters must be set to `verbosity: basic` in production to prevent printing raw span attributes containing credentials to stdout.

---

## 2. Credential Rotation Strategy

- Project ingestion tokens can be regenerated in `tracelyt-control-plane`.
- The collector supports zero-downtime rolling configuration reloads when tokens are updated in Kubernetes secrets.

---

## 3. Related Documentation

- [Integration Threat Model](integration-threat-model.md)
- [Configuration Conventions](../standards/configuration-conventions.md)
- [Network Security](network-security.md)
