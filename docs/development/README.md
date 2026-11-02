# Developer Hub and Integration Guidelines

Welcome to the developer documentation for contributing to **Tracelyt Integrations**.

---

## Developer Guides Index

- [Development Setup](development-setup.md) — Prerequisites, environment initialization, and validation tool usage.
- [Contribution Workflow](contribution-workflow.md) — PR lifecycle, branch management, and integration proposal steps.
- [Testing Guidelines](testing-guidelines.md) — 5-tier validation strategy for integration assets and configurations.
- [Review Checklist](review-checklist.md) — Maintainer review criteria for integration pull requests.

---

## Quick Validation Commands

```bash
# Validate markdown link integrity and scan for secrets
python tools/validate_docs.py

# Using Makefile (if available)
make validate
```

