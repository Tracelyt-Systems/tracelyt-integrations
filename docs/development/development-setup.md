# Local Development Setup Guide

This guide walks you through setting up your local workstation to contribute documentation, templates, and integration assets to **Tracelyt Integrations**.

---

## 1. Prerequisites

- **Python**: Version 3.10 or higher (for running documentation and link validation tooling).
- **Git**: Version 2.40+.
- **Make** (Optional): For running Makefile automation targets.
- **Docker / Docker Compose** (Optional): For future integration test verification against local workloads.

Verify your local Python version:
```bash
python --version
```

---

## 2. Cloning the Repository

```bash
git clone https://github.com/Tracelyt-Systems/tracelyt-integrations.git
cd tracelyt-integrations
```

---

## 3. Running Validation Checks

Before submitting changes, run the validation tool to ensure all relative links resolve cleanly and no credentials are leaked:

```bash
python tools/validate_docs.py
# or using Make
make validate
```

---

## 4. Editor Configuration

Ensure your editor respects [`.editorconfig`](../../.editorconfig):
- 2 spaces indentation for YAML and Markdown.
- Unix line endings (`LF`).
- UTF-8 encoding without byte-order marks.

---

## 5. Related Documentation

- [Contribution Workflow](contribution-workflow.md)
- [Testing Guidelines](testing-guidelines.md)
- [Review Checklist](review-checklist.md)

