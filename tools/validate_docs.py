#!/usr/bin/env python3
"""
Documentation and Secret Integrity Validator for Tracelyt Integrations.
Verifies relative markdown links and scans for accidental secret leaks.
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Regex to capture markdown links: [text](target)
LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

# Patterns indicating potential secrets or tokens
SECRET_PATTERNS = [
    (re.compile(r'(?i)(?:api_key|apikey|secret_key|private_key)\s*[:=]\s*["\']([a-zA-Z0-9_\-]{20,})["\']'), "API Key / Secret Token"),
    (re.compile(r'AKIA[0-9A-Z]{16}'), "AWS Access Key ID"),
    (re.compile(r'-----BEGIN (?:RSA )?PRIVATE KEY-----'), "Private Key Header"),
    (re.compile(r'ghp_[a-zA-Z0-9]{36}'), "GitHub Personal Access Token"),
    (re.compile(r'xox[baprs]-[0-9a-zA-Z]{10,48}'), "Slack API Token"),
]

IGNORED_DIRS = {'.git', '.venv', 'venv', '__pycache__', '.pytest_cache', '.ruff_cache', 'build', 'dist', 'node_modules'}


def check_markdown_links() -> list[str]:
    errors = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for file in files:
            if not file.endswith('.md'):
                continue
            filepath = Path(root) / file
            rel_doc_path = filepath.relative_to(REPO_ROOT)
            try:
                content = filepath.read_text(encoding='utf-8')
            except Exception as e:
                errors.append(f"Cannot read {rel_doc_path}: {e}")
                continue

            for match in LINK_PATTERN.finditer(content):
                target = match.group(2).strip()

                # Ignore external links, mailto, and in-page anchor links
                if (target.startswith(('http://', 'https://', 'mailto:', '#', 'ftp://'))
                        or target.startswith('file://')):
                    continue

                # Strip anchor fragment
                target_path_str = target.split('#')[0]
                if not target_path_str:
                    continue

                resolved_path = (filepath.parent / target_path_str).resolve()
                if not resolved_path.exists():
                    errors.append(
                        f"Broken relative link in {rel_doc_path}: '{target}' -> '{resolved_path}' does not exist"
                    )
    return errors


def check_secrets() -> list[str]:
    errors = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for file in files:
            filepath = Path(root) / file
            # Skip binary files, lockfiles, and git assets
            if file.endswith(('.png', '.ico', '.jpg', '.jpeg', '.pdf', '.jar')):
                continue
            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                continue

            for pattern, desc in SECRET_PATTERNS:
                if pattern.search(content):
                    rel_path = filepath.relative_to(REPO_ROOT)
                    errors.append(f"Potential secret detected ({desc}) in {rel_path}")
    return errors


def main() -> int:
    print("=== Starting Tracelyt Integrations Documentation & Secret Verification ===")
    print("\n1. Checking Markdown relative link integrity...")
    link_errors = check_markdown_links()
    for err in link_errors:
        print(f"  [ERROR] {err}")

    print("\n2. Scanning for credentials and sensitive patterns...")
    secret_errors = check_secrets()
    for err in secret_errors:
        print(f"  [ERROR] {err}")

    total_errors = len(link_errors) + len(secret_errors)
    if total_errors > 0:
        print(f"\n[FAIL] Validation failed with {total_errors} error(s).")
        return 1

    print("\n[SUCCESS] All documentation integrity and secret checks passed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
