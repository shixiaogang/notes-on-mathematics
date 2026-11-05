"""教学图：Gram 矩阵 G_{ij}=<b_i,b_j> 的几何含义。

固定构造：斜基 b1=(2,0)，b2=(1,1.5)。
G11=<b1,b1>=4，G22=<b2,b2>=3.25，G12=<b1,b2>=2；
G12 即 b2 投影到 b1 方向后与 b1 作内积的结果。无随机数，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ls-gram-matrix-coefficients]
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
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only

B1 = np.array([2., 0.])
B2 = np.array([1., 1.5])
# b2 在 b1 方向上的投影足：(b1·b2)/(b1·b1) * b1 = 2/4 * (2,0) = (1,0)
FOOT = (B1 @ B2) / (B1 @ B1) * B1


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


fig, ax = plt.subplots(figsize=(112 / 25.4, 74 / 25.4))

# 投影辅助线：b2 尖端 -> 投影足；投影段 0 -> foot
ax.plot([B2[0], FOOT[0]], [B2[1], FOOT[1]], color=MUTED, lw=.6, ls="--", zorder=1)
arrow(ax, (0, 0), FOOT, GREEN, lw=.9, ls=":")
ax.plot(*FOOT, "o", ms=3, color=MUTED, zorder=3)

# 基向量
arrow(ax, (0, 0), B1, BLUE)
arrow(ax, (0, 0), B2, GREEN)

ax.text(B1[0] + .06, B1[1] + .08, "$b_1$", fontsize=8, color=BLUE)
ax.text(B2[0] + .06, B2[1] - .02, "$b_2$", fontsize=8, color=GREEN)
ax.text(.95, -.30, "$G_{11}=\\langle b_1,b_1\\rangle=\\|b_1\\|^2=4$",
        fontsize=7.5, color=BLUE, ha="center")
ax.text(.12, 1.62, "$G_{22}=\\langle b_2,b_2\\rangle=\\|b_2\\|^2=3.25$",
        fontsize=7.5, color=GREEN)
ax.text(.52, .22, "$G_{12}=\\langle b_1,b_2\\rangle=2$",
        fontsize=7.5, color=YELLOW)
ax.annotate("投影足 (1,0)", xy=tuple(FOOT), xytext=(1.35, .55),
            fontsize=7.5, color=MUTED,
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=.5))

ax.set_title("斜基下 Gram 矩阵的三个元素：长度项与交叉投影项", fontsize=8)
ax.set(xlim=(-.35, 2.9), ylim=(-.55, 2.1))
ax.set_xticks(range(0, 3)); ax.set_yticks(range(0, 2))
ax.set_aspect("equal")
ax.grid(True)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "斜基下 Gram 矩阵的对角线和非对角元素分别在图上对应什么几何量？",
    "formula": "b1=(2,0), b2=(1,1.5); G_ij=<b_i,b_j>; G11=4, G22=3.25, G12=G21=2.",
    "parameters": {
        "b1": list(B1), "b2": list(B2),
        "projection_foot_of_b2_on_b1": list(FOOT),
    },
    "evaluated_data": {
        "G11": float(B1 @ B1), "G22": float(B2 @ B2), "G12": float(B1 @ B2),
    },
    "processing": "直接求值；无平滑、无随机采样。",
    "width_mm": 112, "height_mm": 74, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
