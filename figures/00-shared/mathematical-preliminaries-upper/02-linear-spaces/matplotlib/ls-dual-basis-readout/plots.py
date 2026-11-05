"""教学图：对偶基怎样把线性泛函对各基向量的读数分离。

固定构造：基 b1=(2,1)，b2=(-1,1)。对偶基满足 b^i · b_j = δ^i_j，解得
b^1=(1/3,1/3)，b^2=(-1/3,2/3)。取 a=(1,0)，泛函 ℓ(x)=x·a：
ℓ(b1)=2，ℓ(b2)=-1；等值线 a·x=c 是竖直线 x=c（c=-1,0,2）。
对偶分解 a = ℓ(b1) b^1 + ℓ(b2) b^2 = 2 b^1 - b^2 = (1,0)，验证成立。
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
B1D = np.array([1 / 3, 1 / 3])   # b^1
B2D = np.array([-1 / 3, 2 / 3])  # b^2
A = np.array([1., 0.])


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


fig, ax = plt.subplots(figsize=(112 / 25.4, 80 / 25.4))

# 等值线 ℓ(x)=a·x=c：a=(1,0) 时即竖直线 x=c
for c, lab, col in [(-1, "$\\ell=-1$", MUTED), (0, "$\\ell=0$", MUTED),
                    (2, "$\\ell=2$", MUTED)]:
    ax.axline((c, 0), slope=np.inf, color=col, ls="--", lw=.6, zorder=1)
    ax.text(c, 2.45, lab, fontsize=7.5, ha="center", color=col)

arrow(ax, (0, 0), B1, BLUE, lw=1.2)
arrow(ax, (0, 0), B2, GREEN, lw=1.2)
arrow(ax, (0, 0), B1D, RED, lw=1.0, ls="--")
arrow(ax, (0, 0), B2D, RED, lw=1.0, ls="--")
arrow(ax, (0, 0), A, YELLOW, lw=1.3)

ax.text(B1[0] + .10, B1[1] + .02, "$b_1$", fontsize=8, color=BLUE)
ax.text(B2[0] - .38, B2[1] + .08, "$b_2$", fontsize=8, color=GREEN)
ax.text(B1D[0] + .10, B1D[1] - .16, "$b^1$", fontsize=8, color=RED)
ax.text(B2D[0] - .30, B2D[1] + .04, "$b^2$", fontsize=8, color=RED)
ax.text(A[0] + .08, A[1] - .20, "$a$", fontsize=8, color=YELLOW)
ax.text(-2.15, -0.62, "等值线 $\\ell(x)=x\\cdot a$；$\\ell(b_1)=2$，$\\ell(b_2)=-1$", fontsize=8)
ax.text(-2.15, -0.95, "$a=\\ell(b_1)\\,b^1+\\ell(b_2)\\,b^2=2\\,b^1-b^2$", fontsize=8)
ax.set_title("对偶基：把对 $b_1,b_2$ 的读数分别装进 $b^1,b^2$", fontsize=8)
ax.set(xlim=(-2.4, 2.9), ylim=(-1.25, 2.75), xticks=[-2, -1, 0, 1, 2], yticks=[-1, 0, 1, 2])
ax.set_aspect("equal")
ax.grid(True)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

check = 2 * B1D - B2D
record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "对偶基向量为什么能把线性泛函对各基向量的读数分离开？",
    "formula": "b1=(2,1), b2=(-1,1). Dual: b1^T·b^1=1, b2^T·b^1=0 -> b^1=(1/3,1/3); b1^T·b^2=0, b2^T·b^2=1 -> b^2=(-1/3,2/3). a=(1,0): ell(x)=x·a; ell(b1)=2, ell(b2)=-1. a=2 b^1 - b^2 = (1,0). Level lines x·a=c are vertical lines x=-1,0,2.",
    "parameters": {
        "basis": {"b1": [2, 1], "b2": [-1, 1]},
        "dual_basis": {"b^1": [round(B1D[0], 4), round(B1D[1], 4)], "b^2": [round(B2D[0], 4), round(B2D[1], 4)]},
        "covector": {"a": [1, 0], "ell(b1)": 2, "ell(b2)": -1},
        "decomposition_verify": "2 b^1 - b^2 = (%.4f, %.4f)" % tuple(check),
        "level_lines": "x=-1, x=0, x=2（竖直线）",
    },
    "evaluated_data": {"b1": list(B1), "b2": list(B2), "b1_dual": list(B1D),
                       "b2_dual": list(B2D), "check": list(check)},
    "processing": "直接求值；无平滑、无随机采样。",
    "width_mm": 112, "height_mm": 80, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
