"""Render only the two standalone TikZ teaching figures, never the book.

Requires XeLaTeX, pdftoppm and pypdf; all auxiliary output stays in a temporary
directory. Editable fragments are the files included by the chapter source.
"""
from pathlib import Path
import sys
import json
import os
import shutil
import subprocess
import tempfile
from pypdf import PdfReader

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
NAMES = ("geometry-cycle-filled-simplex", "graph-running-intersection")
tex_env = os.environ.copy()
for variable, directory in (("T1FONTS", "type1"), ("TFMFONTS", "tfm"),
                            ("ENCFONTS", "enc")):
    tex_env[variable] = str(ROOT / "fonts/stix2-type1" / directory) + "//:" + tex_env.get(variable, "")
records = []
for name in NAMES:
    source = asset_path(OUT, f"{name}.tex")
    with tempfile.TemporaryDirectory(prefix="concept-tikz-") as tmp:
        work = Path(tmp)
        driver = work / "figure.tex"
        driver.write_text(r"""\documentclass[10pt,border=0pt]{standalone}
\usepackage{fontspec,xeCJK,tikz,amsmath}
\usepackage[notext]{stix2}
\newcommand{\bmmax}{0}
\newcommand{\hmmax}{0}
\usepackage{bm}
\setmainfont{SourceSans3-Regular.otf}[Path={FONTDIR/}]
\setsansfont{SourceSans3-Regular.otf}[Path={FONTDIR/}]
\setCJKmainfont{LXGWWenKai-Regular.ttf}[Path={FONTDIR/}]
\setCJKsansfont{LXGWWenKai-Regular.ttf}[Path={FONTDIR/}]
\newcommand{\figurefont}{\sffamily}
% Minimal volume-two palette needed by these two editable fragments.
\definecolor{FigureInk}{HTML}{222222}
\definecolor{FigureStroke}{HTML}{4C4D4F}
\definecolor{FigureBlue}{HTML}{7998AD}
\definecolor{FigureYellowFill}{HTML}{FFF1CF}
\begin{document}
\input{SOURCE}
\end{document}
""".replace("FONTDIR", (ROOT / "fonts").as_posix()).replace(
            "SOURCE", source.as_posix()), encoding="utf-8")
        result = subprocess.run(["xelatex", "-interaction=nonstopmode",
            "-halt-on-error", "-no-shell-escape", "-no-pdf", "figure.tex"], cwd=work,
            env=tex_env,
            capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stdout[-4000:])
        pdf = asset_path(OUT, f"{name}.pdf")
        conversion = subprocess.run(["xdvipdfmx", "-f",
            str(ROOT / "fonts/stix2-type1/map/stix2.map"), "-E",
            "-o", "figure.pdf", "figure.xdv"], cwd=work, env=tex_env,
            capture_output=True, text=True)
        if conversion.returncode:
            raise RuntimeError(conversion.stderr[-4000:])
        shutil.copyfile(work / "figure.pdf", pdf)
        subprocess.run(["pdftoppm", "-png", "-singlefile", "-r", "360",
            str(pdf), str(asset_path(OUT, name))], check=True, capture_output=True)
        page = PdfReader(pdf).pages[0]
        records.append({"name": name, "width_mm": float(page.mediabox.width)*25.4/72,
            "height_mm": float(page.mediabox.height)*25.4/72,
            "teaching_construction": True, "font": "LXGW WenKai / Source Sans 3 / STIX2",
            "source": source.name, "tool": "TikZ / XeLaTeX",
            "log_missing_glyph": "Missing character" in result.stdout})
(asset_path(OUT, "tikz-sources.json")).write_text(json.dumps({"created": "2026-10-06",
    "figures": records,
    "facts": {
        "geometry-cycle-filled-simplex": {"vertices": [1,2,3],
            "edges": [[1,2],[1,3],[2,3]], "left_faces": [],
            "right_faces": [[1,2,3]], "left_betti": [1,1], "right_betti": [1,0]},
        "graph-running-intersection": {"original_edges": [[1,2],[2,3],[3,4]],
            "valid_bag_order": [[1,2],[2,3],[3,4]],
            "invalid_bag_order": [[1,2],[3,4],[2,3]],
            "failure": "Bags containing vertex 2 are separated by a bag that does not contain 2."}
    }}, ensure_ascii=False, indent=2), encoding="utf-8")
