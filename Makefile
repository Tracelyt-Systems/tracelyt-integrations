.PHONY: help validate docs-check clean

help:
	@echo "Tracelyt Integrations Repository Commands:"
	@echo "  make validate    - Validate markdown link integrity and scan for secrets"
	@echo "  make docs-check  - Alias for make validate"
	@echo "  make clean       - Remove cached files and temporary directories"

validate: docs-check

docs-check:
	python tools/validate_docs.py

clean:
	python -c "import shutil, pathlib; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
