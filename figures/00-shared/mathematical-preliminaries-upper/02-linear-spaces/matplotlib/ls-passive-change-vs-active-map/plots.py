"""教学图：被动换基（向量不动、坐标系转动）与主动变换（坐标系不动、向量被搬走）的对照。

固定构造：同一个初始向量 x=(3,3)。左 panel：旧标准基下读数 (3,3)，
换用斜基 b1=(2,1), b2=(-1,1) 后 x=2 b1+b2，读数变为 (2,1)，x 的箭头在平面上没动。
右 panel：坐标系保持标准基，x 被 A=[[1,1],[0,1]] 映到 Ax=(6,3)，箭头换了位置。
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

B1 = np.array([2., 1.])
B2 = np.array([-1., 1.])
X = np.array([3., 3.])
AX = np.array([6., 3.])  # A = [[1,1],[0,1]]

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

# ---- 左：被动换基。x 不动，旧坐标读数 (3,3)，新读数 (2,1) ----
for t in (-1, 0, 1, 2):
    p0, p1 = t * B1 - 2.6 * B2, t * B1 + 2.6 * B2
    a.plot([p0[0], p1[0]], [p0[1], p1[1]], color=GRID, lw=.4, zorder=1)
for t in (-1, 0, 1):
    p0, p1 = t * B2 - 1.8 * B1, t * B2 + 1.8 * B1
    a.plot([p0[0], p1[0]], [p0[1], p1[1]], color=GRID, lw=.4, zorder=1)
arrow(a, (0, 0), B1, BLUE, lw=1.0)
arrow(a, (0, 0), B2, GREEN, lw=1.0)
arrow(a, (0, 0), X, INK, lw=1.4)
a.plot([X[0], X[0]], [0, X[1]], color=MUTED, ls=":", lw=.6)
a.plot([0, X[0]], [X[1], X[1]], color=MUTED, ls=":", lw=.6)
a.plot([2 * B1[0], X[0]], [2 * B1[1], X[1]], color=MUTED, ls="--", lw=.6)
a.plot([B2[0], X[0]], [B2[1], X[1]], color=MUTED, ls="--", lw=.6)
a.text(B1[0] + .08, B1[1] - .22, "$b_1$", fontsize=8, color=BLUE)
a.text(B2[0] - .42, B2[1] + .04, "$b_2$", fontsize=8, color=GREEN)
a.text(X[0] + .10, X[1] + .06, "$x$", fontsize=8, color=INK)
a.text(3.15, 1.55, "旧读数 $(3,3)$", fontsize=8, color=MUTED)
a.text(-2.7, 3.62, "新读数 $(2,1)$：$x=2\\,b_1+b_2$", fontsize=8)
a.text(-2.7, -0.85, "向量没动，只是坐标轴换了", fontsize=8)
a.set_title("(a) 被动换基：向量不动，坐标数字变了", fontsize=8)
a.set(xlim=(-2.9, 5.6), ylim=(-1.1, 4.2), xticks=[-2, 0, 2, 4], yticks=[-1, 0, 1, 2, 3])
a.set_aspect("equal")
a.grid(True)

# ---- 右：主动变换。坐标系不动，x 被 A 搬到 Ax ----
arrow(b, (0, 0), X, BLUE, lw=1.3)
arrow(b, (0, 0), AX, GREEN, lw=1.3)
b.plot([X[0], X[0]], [0, X[1]], color=MUTED, ls=":", lw=.6)
b.plot([0, X[0]], [X[1], X[1]], color=MUTED, ls=":", lw=.6)
b.plot([AX[0], AX[0]], [0, AX[1]], color=MUTED, ls=":", lw=.6)
b.plot([0, AX[0]], [AX[1], AX[1]], color=MUTED, ls=":", lw=.6)
b.annotate("", xy=tuple(AX), xytext=tuple(X),
           arrowprops=dict(arrowstyle="->", color=YELLOW, lw=1.1,
                           connectionstyle="arc3,rad=-0.25"))
b.text(1.9, 3.45, "$x=(3,3)$", fontsize=8, color=BLUE)
b.text(AX[0] + .10, AX[1] + .05, "$Ax=(6,3)$", fontsize=8, color=GREEN)
b.text(-.2, -0.85, "坐标系没动，切变 $A x=(6,3)$（$A$：向右错一位）", fontsize=8)
b.set_title("(b) 主动变换：坐标系不动，向量换了位置", fontsize=8)
b.set(xlim=(-1.1, 7.4), ylim=(-1.1, 4.2), xticks=[0, 2, 4, 6], yticks=[0, 1, 2, 3])
b.set_aspect("equal")
b.grid(True)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "坐标数字改变，到底是向量变了，还是看它的坐标系变了？",
    "formula": "x=(3,3). Passive: old coords (3,3); b1=(2,1), b2=(-1,1), x=2*b1+b2=(4,2)+(-1,1)=(3,3), new coords (2,1). Active: A=[[1,1],[0,1]], A*x=(6,3).",
    "parameters": {
        "initial_vector": [3, 3],
        "new_basis": {"b1": [2, 1], "b2": [-1, 1]},
        "old_coordinates": [3, 3], "new_coordinates": [2, 1],
        "active_map": {"matrix": [[1, 1], [0, 1]], "image": [6, 3]},
        "same_initial_vector_in_both_panels": True,
    },
    "evaluated_data": {"x": list(X), "two_b1": list(2 * B1), "Ax": list(AX)},
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
