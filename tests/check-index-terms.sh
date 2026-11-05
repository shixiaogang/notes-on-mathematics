#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"

python3 -m unittest -v tests/test_audit_index_terms.py
python3 scripts/audit_index_terms.py check
