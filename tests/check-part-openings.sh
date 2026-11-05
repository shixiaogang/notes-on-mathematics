#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
output_dir="$(mktemp -d "${TMPDIR:-/tmp}/part-openings.XXXXXX")"
trap 'rm -rf "$output_dir"' EXIT
export TEXINPUTS="./tex//:${TEXINPUTS:-}"
export TFMFONTS="./fonts/stix2-type1/tfm//:${TFMFONTS:-}"
export ENCFONTS="./fonts/stix2-type1/enc//:${ENCFONTS:-}"
for edition in book volume; do
  prefix=''
  if [[ "$edition" == volume ]]; then prefix='\def\PartTestVolume{1}'; fi
  if ! xelatex -no-pdf -interaction=nonstopmode -halt-on-error \
    -output-directory="$output_dir" -jobname="$edition" \
    "$prefix\input{tests/check-part-openings.tex}" > "$output_dir/$edition.output" 2>&1; then
    cat "$output_dir/$edition.output" >&2
    exit 1
  fi
done
python3 - "$output_dir" <<'PY'
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])
labels = ('first', 'odd', 'even', 'starred', 'optional')
for edition, start in (('book', 3), ('volume', 1)):
    aux = (root / f'{edition}.aux').read_text()
    for name, expected in zip(labels, range(start, start + 10, 2)):
        match = re.search(r'\\newlabel\{part:' + name + r'\}\{\{[^}]*\}\{(\d+)\}', aux)
        assert match, f'{edition}: missing label {name}'
        actual = int(match[1])
        assert actual == expected, f'{edition}: {name}: expected {expected}, got {actual}'
    toc_pages = re.findall(r'\\contentsline \{part\}.*?\}\{(\d+)\}\{', aux)
    assert list(map(int, toc_pages)) == [start, start + 2, start + 4, start + 8], (edition, toc_pages)
    log = (root / f'{edition}.log').read_text()
    physical = list(map(int, re.findall(r'PART-PHYSICAL-PAGE: (\d+)', log)))
    assert physical == list(range(start + 2, start + 12, 2)), (edition, physical)
print('部首页分页回归通过：全集和单卷、奇偶前页、连续部首页、星号及可选目录标题。')
PY
