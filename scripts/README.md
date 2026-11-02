# Developer and Maintenance Scripts (`scripts/`)

This directory is designated for future repository maintenance scripts, upstream version tracking utilities, and local developer helpers.

---

## 1. Scripting Guidelines

1. **Portability**: All maintenance scripts must run across Linux, macOS, and Windows environments without platform-specific dependencies.
2. **Standard Library First**: Prefer Python 3 standard library scripts or POSIX shell utilities.
3. **No Redundant Wrappers**: Do not create shell scripts that merely wrap a single command or perform trivial tasks.
4. **Safety & Zero Side Effects**: Scripts must never mutate local git history, publish artifacts, or communicate with unverified external endpoints without explicit operator confirmation.

---

## 2. Active Tooling Notice

Active validation tooling for documentation links and secret integrity is maintained in [`tools/validate_docs.py`](../tools/validate_docs.py).
