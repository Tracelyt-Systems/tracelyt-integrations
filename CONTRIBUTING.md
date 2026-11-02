# Contributing to Tracelyt Integrations

Thank you for your interest in contributing to **Tracelyt Integrations**! We welcome contributions that expand and refine our integration ecosystem with clear architecture, verified compatibility, and reproducible validation.

---

## 1. Ground Rules

- **Integration Standards**: All proposed integration guides must follow the [Standard Integration Guide Template](docs/templates/integration-guide-template.md) and adhere to the [Integration Lifecycle](docs/standards/integration-lifecycle.md).
- **No Unverified Claims**: Do not mark an integration as `Validated` or `Supported` without documented, reproducible validation evidence.
- **Service Boundaries**: Respect Tracelyt platform boundaries. Integrations document how external workloads connect to Tracelyt; they do not implement ingestion, querying, or alerting logic. Review [System Boundaries](docs/architecture/system-boundaries.md).
- **Security-First**: Never commit real credentials, API tokens, or private endpoints. Follow [Credential Handling](docs/security/credential-handling.md).
- **Code of Conduct**: All participants must follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 2. Proposing a New Integration

1. Check open issues and discussions to verify the integration has not already been proposed.
2. Submit an issue using the [Integration Request Template](.github/ISSUE_TEMPLATE/integration_request.yml).
3. Review our [Contribution Workflow](docs/development/contribution-workflow.md) and [Testing Guidelines](docs/development/testing-guidelines.md).
4. Run validation checks locally before submitting your Pull Request:
   ```bash
   python tools/validate_docs.py
   ```

---

## 3. Reporting Issues

- For bug reports or broken integration links, submit a [Bug Report](.github/ISSUE_TEMPLATE/bug_report.yml).
- For security vulnerabilities, do not open a public issue. Follow [SECURITY.md](SECURITY.md).
