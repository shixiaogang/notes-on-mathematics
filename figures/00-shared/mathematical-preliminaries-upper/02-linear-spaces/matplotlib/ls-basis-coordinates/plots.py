"""教学图：同一个几何向量，在标准基与斜基下坐标读数不同。

固定构造：x=(1,2)。左 panel 用标准基 e1=(1,0), e2=(0,1)，读数 (1,2)；
右 panel 用斜基 b1=(2,1), b2=(-1,1)，解 x=x1 b1+x2 b2 得 (x1,x2)=(1,1)。
无随机采样，不调用 LaTeX。从任意目录运行。
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW, RED = "#7188A3", "#829C8B", "#B4A16F", "#A7787D"
INK, MUTED, GRID, STROKE = "#3B4252", "#6B7280", "#D8DCE2", "#4C4D4F"
BLUE_FILL = "#E5EAF0"
CN_MAIN, CN_AUX, EN = "Source Han Sans SC", "LXGW WenKai", "Fira Math"

matplotlib.rcParams.update({
    "font.family": [EN, CN_MAIN], "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": EN, "mathtext.it": EN,
    "mathtext.bf": EN, "mathtext.sf": EN,
    "axes.unicode_minus": False, "text.color": INK, "axes.labelcolor": INK,
    "axes.edgecolor": STROKE, "axes.linewidth": .75,
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": STROKE, "ytick.color": STROKE,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "grid.color": GRID, "grid.linewidth": .4,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 3, "svg.fonttype": "path",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME])
selection = parser.parse_args().only

E1 = np.array([1., 0.])
E2 = np.array([0., 1.])
B1 = np.array([2., 1.])
B2 = np.array([-1., 1.])
X = np.array([1., 2.])


def arrow(ax, p, q, color, lw=1.1, ls="-"):
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, ls=ls,
                                shrinkA=0, shrinkB=0))


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, (a, b) = plt.subplots(1, 2, figsize=(169 / 25.4, 66 / 25.4))

# ---- 左：标准基 ----
arrow(a, (0, 0), E1, MUTED, lw=.9)
arrow(a, (0, 0), E2, MUTED, lw=.9)
arrow(a, (0, 0), X, BLUE, lw=1.4)
a.plot([X[0], X[0]], [0, X[1]], color=MUTED, ls="--", lw=.6)
a.plot([0, X[0]], [X[1], X[1]], color=MUTED, ls="--", lw=.6)
a.text(E1[0] + .08, E1[1] - .16, "$e_1$", fontsize=8, color=MUTED)
a.text(E2[0] - .10, E2[1] + .10, "$e_2$", fontsize=8, color=MUTED)
a.text(X[0] + .08, X[1] + .05, "$x$", fontsize=8, color=BLUE)
a.text(.06, -0.42, "$x = 1\\,e_1 + 2\\,e_2$，读数 $(1,2)$", fontsize=8)
a.set_title("(a) 标准基 $e_1,e_2$：坐标 $(1,2)$", fontsize=8)
a.set(xlim=(-.4, 1.9), ylim=(-.7, 2.7), xticks=[0, 1], yticks=[1, 2])
a.set_aspect("equal")
a.grid(True)

# ---- 右：斜基 ----
for t in (-1, 0, 1):  # 平行于 b2 的斜线
    p0, p1 = t * B1 - 3.2 * B2, t * B1 + 3.2 * B2
    b.plot([p0[0], p1[0]], [p0[1], p1[1]], color=GRID, lw=.4, zorder=1)
for t in (-1, 0, 1):  # 平行于 b1 的横线
    p0, p1 = t * B2 - 2.2 * B1, t * B2 + 2.2 * B1
    b.plot([p0[0], p1[0]], [p0[1], p1[1]], color=GRID, lw=.4, zorder=1)
arrow(b, (0, 0), B1, BLUE, lw=1.1)
arrow(b, (0, 0), B2, GREEN, lw=1.1)
arrow(b, (0, 0), X, INK, lw=1.4)
b.plot([B1[0], X[0]], [B1[1], X[1]], color=MUTED, ls="--", lw=.6)
b.plot([B2[0], X[0]], [B2[1], X[1]], color=MUTED, ls="--", lw=.6)
b.text(B1[0] + .10, B1[1] - .20, "$b_1$", fontsize=8, color=BLUE)
b.text(B2[0] - .34, B2[1] + .06, "$b_2$", fontsize=8, color=GREEN)
b.text(X[0] + .10, X[1] + .04, "$x$", fontsize=8, color=INK)
b.text(-2.55, -0.78, "$x = 1\\,b_1 + 1\\,b_2$，读数 $(1,1)$", fontsize=8)
b.set_title("(b) 斜基 $b_1,b_2$：坐标 $(1,1)$", fontsize=8)
b.set(xlim=(-2.9, 3.3), ylim=(-.9, 2.8), xticks=[-2, 0, 2], yticks=[-1, 1, 2])
b.set_aspect("equal")

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "同一个向量的坐标，为什么依赖于所选的基？",
    "formula": "x=(1,2). Standard: x=1 e1+2 e2, coords (1,2). Oblique basis b1=(2,1), b2=(-1,1): solve x=x1 b1+x2 b2 -> 2x1-x2=1, x1+x2=2 -> x1=1, x2=1.",
    "parameters": {
        "geometric_vector": [1, 2],
        "standard_basis": {"e1": [1, 0], "e2": [0, 1]},
        "oblique_basis": {"b1": [2, 1], "b2": [-1, 1]},
        "coordinates": {"standard": [1, 2], "oblique": [1, 1]},
        "reading_dashes": "左 panel：从 x=(1,2) 向两坐标轴作垂线；右 panel：从 b1=(2,1) 作 b2 的平行线、从 b2=(-1,1) 作 b1 的平行线，二者交于 x。",
    },
    "evaluated_data": {
        "b1_plus_b2": list(B1 + B2),
        "check_oblique": "b1+b2=(1,2)=x",
    },
    "processing": "直接求值；无平滑、无随机采样。",
    "width_mm": 169, "height_mm": 66, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
