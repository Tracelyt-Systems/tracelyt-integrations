# Integration Guide: [Technology Name]

> **Template Notice**: This is the standardized 17-section template for all integration guides in `tracelyt-integrations`. Remove this notice when instantiating a new guide.

---

## 1. Integration Name
- **Technology**: e.g., Spring Boot / FastAPI / MySQL
- **Integration Identifier**: `lang-java-springboot`

## 2. Integration Category
- Category: Languages | Frameworks | Infrastructure | Databases | Messaging | Cloud

## 3. Current Status
- **Lifecycle Status**: Proposed | Planned | In Development | Experimental | Validated | Supported | Deprecated | Removed

## 4. Maintainer or Upstream Owner
- **Tracelyt Maintainer**: @github-handle
- **Upstream Organization**: e.g., OpenTelemetry Project / Vendor Name

## 5. Official Upstream References
- Official Documentation: `https://...`
- Upstream GitHub Repository: `https://...`

## 6. Supported Software Versions
- **Target Technology Versions**: e.g., 3.2.0 – 3.3.4
- **Runtime Versions**: e.g., JDK 17, JDK 21 LTS
- **OpenTelemetry Component Versions**: e.g., `opentelemetry-javaagent` v2.5.0

## 7. Supported Telemetry Signals
- [ ] Traces
- [ ] Metrics
- [ ] Logs

## 8. Prerequisites
- [Upstream Requirement] Required runtime or compiler.
- [Tracelyt Requirement] Valid project token generated from `tracelyt-control-plane`.

## 9. Required Permissions
- Required network egress, operating system capabilities, or database user privileges.

## 10. Configuration Overview
Outline configuration files and environment variables. Provide tested snippets using placeholder secrets (`${TRACELYT_TOKEN}`).

## 11. Data Flow
Describe the path from application instrumentation to `tracelyt-ingestion`.

## 12. Security Considerations
- TLS configuration and verification.
- Secret handling and credential sanitization.
- Sensitive attribute filtering.

## 13. Compatibility Limitations
- Explicitly list unsupported versions, reactive limitations, or edge-case transports.

## 14. Validation Procedure
Step-by-step instructions to reproduce and verify telemetry generation in a local test environment.

## 15. Troubleshooting
Common failure modes, missing spans, broken trace contexts, or port conflicts.

## 16. Known Issues
Unresolved upstream bugs or open tickets affecting this integration.

## 17. Version History
- YYYY-MM-DD: Initial proposed guide.
