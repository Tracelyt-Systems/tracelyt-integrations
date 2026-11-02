# Developer Tooling (`tools/`)

This directory contains utility scripts and validation tooling for contributors and maintainers of **Tracelyt Integrations**.

---

## 1. Tooling Policy

1. **Hermetic & Portable**: Developer tools should rely strictly on standard library Python modules to ensure portability across Linux, macOS, and Windows.
2. **Deterministic Output**: Tools must return exit code 0 on success and non-zero on failure to integrate cleanly into CI workflows.
3. **No Unsanctioned Modifications**: Utility scripts must not modify source files or git history without explicit user interaction.

---

## 2. Active Tools

### `validate_docs.py`
A comprehensive documentation and secret integrity scanner that:
- Verifies that all relative Markdown link destinations resolve to actual existing files.
- Scans all files for accidental commit of private API keys, tokens, or credentials.
- Can be invoked directly via:
  ```bash
  python tools/validate_docs.py
  # or
  make docs-check
  ```
