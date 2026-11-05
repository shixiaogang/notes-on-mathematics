#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
output_dir="$(mktemp -d "${TMPDIR:-/tmp}/paragraph-statements.XXXXXX")"
trap 'rm -rf "$output_dir"' EXIT
export TEXINPUTS="./tex//:${TEXINPUTS:-}"
export TFMFONTS="./fonts/stix2-type1/tfm//:${TFMFONTS:-}"
export ENCFONTS="./fonts/stix2-type1/enc//:${ENCFONTS:-}"
if ! xelatex -no-pdf -interaction=nonstopmode -halt-on-error \
  -output-directory="$output_dir" tests/check-paragraph-statements.tex \
  > "$output_dir/compile.output" 2>&1; then
  cat "$output_dir/compile.output" >&2
  exit 1
fi
python3 - "$output_dir/check-paragraph-statements.positions" <<'PY'
from pathlib import Path
import sys

positions = {}
for line in Path(sys.argv[1]).read_text().splitlines():
    name, x, y, page = line.split()
    positions.setdefault(name, []).append((int(x), int(y), int(page)))
reference = positions['body'][0][0]
assert all(abs(x - reference) <= 6554 for x, _, _ in positions['body'])
for name in ('plain', 'example', 'theorem', 'definition', 'lemma', 'proof',
             'mathproblem', 'algorithm', 'codeblock'):
    assert len(positions.get(name, [])) == 1, (name, positions.get(name))
    actual = positions[name][0][0]
    assert abs(actual - reference) <= 6554, (
        name, f'heading x={actual / 65536:.3f}pt, '
              f'body x={reference / 65536:.3f}pt')
assert positions['plain'][0][1:] == positions['plain-text'][0][1:], (
    'ordinary paragraph heading must remain on the same line as its text')
assert positions['boundary-heading'][0][2] == positions['boundary-box'][0][2], (
    'paragraph heading must stay on the same page as the following box opening')
print('段标题对齐回归通过：普通正文及八种环境对齐；普通标题保持同行，页底标题与后框开头保持同页。')
PY
