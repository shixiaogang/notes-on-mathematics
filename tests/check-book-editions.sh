#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - <<'PY'
from pathlib import Path
from scripts.book_catalog import ROOT, volumes, tex_inputs, references
catalog = volumes()
assert [v["number"] for v in catalog] == list(range(1, 5))
assert len({v["pdf"] for v in catalog}) == 4
assert not Path("tex/main.tex").exists(), "全集入口应退役"
expected = [7, 24, 13, 31]
for volume, count in zip(catalog, expected):
    entry = (ROOT / volume["entry"]).read_text()
    assert "\\BookVolumeSlug" in entry and "\\input{tex/book}" in entry
    assert volume["title"] in entry
    sources = tex_inputs(ROOT, volume["content"])
    text = "\n".join(sources.values())
    assert text.count("\\chapter{") == count, (volume["slug"], count)
    assert "\\bookpart" in text
    assert text.count("\\section{本章小结}") == count
references()
print("出版结构通过：卷一至卷四、75章、卷内编号、部分入口及标签唯一性。")
PY
output_dir="$(mktemp -d "${TMPDIR:-/tmp}/book-index.XXXXXX")"
trap 'rm -rf "$output_dir"' EXIT
export TEXINPUTS="./tex//:${TEXINPUTS:-}"
for fixture in check-index-pipeline check-index-pipeline-volume check-term-pdfstring; do
  xelatex -interaction=nonstopmode -halt-on-error \
    -output-directory="$output_dir" "tests/$fixture.tex" > "$output_dir/$fixture.output" 2>&1 \
    || { cat "$output_dir/$fixture.output"; exit 1; }
  if [[ "$fixture" != check-term-pdfstring ]]; then
    texindy -L general -C utf8 -M tex/styles/book-index.xdy \
      -o "$output_dir/$fixture.ind" "$output_dir/$fixture.idx" \
      > "$output_dir/$fixture.index-output" 2>&1 \
      || { cat "$output_dir/$fixture.index-output"; exit 1; }
    xelatex -interaction=nonstopmode -halt-on-error \
      -output-directory="$output_dir" "tests/$fixture.tex" > "$output_dir/$fixture.output" 2>&1 \
      || { cat "$output_dir/$fixture.output"; exit 1; }
  fi
done
python3 - "$output_dir" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])
full = (root / "check-index-pipeline.idx").read_text()
local = (root / "check-index-pipeline-volume.idx").read_text()
for term in ["向量@向量，vector", "SVD@SVD，singular value decomposition",
             "正定性-matrix-positive-definite@正定性，positive definiteness", "R-hat diagnostic"]:
    assert term in full, term
assert "前页哨兵词" not in full
assert "R-hat diagnostic" not in local
assert "Gaussian process，Gaussian process" not in full
for path in root.glob("*.log"):
    text = path.read_text()
    assert "Token not allowed in a PDF string" not in text
    assert "Missing character:" not in text
print("最小索引流水线与 PDF 字符串检查通过。")
PY
