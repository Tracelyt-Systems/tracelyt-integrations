# Network Security and Egress Architecture

This document defines the transport security requirements, TLS validation rules, and network boundary policies for **Tracelyt Integrations**.

---

## 1. Transport Encryption (TLS)

1. **Mandatory TLS 1.2 / 1.3**: All telemetry exported across public or unencrypted networks to `tracelyt-ingestion` must use TLS 1.2 or TLS 1.3. Plaintext HTTP/gRPC is rejected.
2. **Strict Certificate Validation**:
   - Collectors must validate server X.509 certificates against standard trusted Certificate Authorities (CAs).
   - **Critical Rule**: Integration guides must **never** recommend disabling TLS certificate verification (`insecure_skip_verify: true`) as a troubleshooting step.

---

## 2. Egress Proxies and Corporate Firewalls

In enterprise environments with strict outbound firewall policies:
- OpenTelemetry Collector supports standard forward proxy configuration via `HTTPS_PROXY` and `NO_PROXY` environment variables.
- Dedicated egress ports:
  - Port `4317` (gRPC over HTTP/2)
  - Port `4318` (HTTP/1.1 or HTTP/2)

---

## 3. Localhost and Intra-Cluster Traffic

- For local sidecar architectures (where the collector runs in the same pod or host as the application on `127.0.0.1`), plaintext communication over loopback is permissible to avoid localhost encryption overhead.
- Telemetry egressing the host boundary to Tracelyt must transition to encrypted TLS.

---

## 4. Related Documentation

- [Credential Handling](credential-handling.md)
- [Integration Threat Model](integration-threat-model.md)
- [Telemetry Flow](../architecture/telemetry-flow.md)
