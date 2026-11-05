"""教学图：正交 Procrustes——两组点之间的最优正交映射。

解析式固定构造：三组点取 X={(1.2,0),(0,1),(-1,0.3)}。
最优旋转 R 为 45° 旋转矩阵（det=+1），把 X 映到 Y=R X；
反射备选（det=−1）给出镜像位置（黄色虚线），距离更大，不是最优。
无随机数，不调用 LaTeX。从任意目录运行：python3 plots.py [--only ...]
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Polygon
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW, RED = "#7188A3", "#829C8B", "#B4A16F", "#A7787D"
INK, MUTED, GRID, STROKE = "#3B4252", "#6B7280", "#D8DCE2", "#4C4D4F"
BLUE_FILL, RED_FILL, GREEN_FILL, YELLOW_FILL = "#E5EAF0", "#F0E5E6", "#E8EEE9", "#F1ECDD"
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

X = np.array([[1.2, 0.], [0., 1.0], [-1.0, 0.3]])
C45 = np.cos(np.pi / 4)
ROT = np.array([[C45, -C45], [C45, C45]])     # 45° 旋转，det=+1
Y = X @ ROT.T
REFL = np.diag([1., -1.])                     # 反射备选，det=−1
Y_REF = X @ REFL


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

# 反射备选（黄虚线三角形）
ax.add_patch(Polygon(Y_REF[list(range(3)) + [0]], closed=True,
                     facecolor="none", edgecolor=YELLOW, lw=.9, ls="--"))
for p in Y_REF:
    ax.plot(*p, "s", ms=4, mfc="white", mec=YELLOW, mew=.8, zorder=4)

# 原三角形 X（蓝）与旋转后 Y（绿）
ax.add_patch(Polygon(X[list(range(3)) + [0]], closed=True,
                     facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.0))
ax.add_patch(Polygon(Y[list(range(3)) + [0]], closed=True,
                     facecolor=GREEN_FILL, edgecolor=GREEN, lw=1.0))
for p in X:
    ax.plot(*p, "o", ms=4, mfc=BLUE, mec=INK, mew=.4, zorder=5)
for p in Y:
    ax.plot(*p, "o", ms=4, mfc=GREEN, mec=INK, mew=.4, zorder=5)
for xi, yi in zip(X, Y):
    arrow(ax, xi, yi, MUTED, lw=.6, ls=":")

ax.text(1.30, -0.18, "原集 $\\{x_i\\}$", fontsize=8, color=BLUE)
ax.text(0.95, 1.05, "旋转后 $\\{y_i\\}=R\\{x_i\\}$", fontsize=8, color=GREEN)
ax.text(-1.95, -1.15, "反射备选（det=−1）：距离更大，不是最优", fontsize=7.5, color=YELLOW)
ax.text(-1.95, 1.55, "$R$ 为 45° 旋转矩阵，$\\det R=+1$", fontsize=8)
ax.set_title("正交 Procrustes：最优旋转贴合两组点", fontsize=8)
ax.set(xlim=(-2.2, 2.2), ylim=(-1.6, 1.9), xticks=range(-2, 3), yticks=range(-1, 2))
ax.set_aspect("equal")
ax.grid(True)

finalize(fig)
fig.tight_layout()
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "正交 Procrustes 为什么在旋转（det=+1）而不是反射（det=−1）处最优？",
    "formula": "X={(1.2,0),(0,1),(-1,0.3)}; R=(√2/2)[[1,-1],[1,1]]（45°），det R=+1; "
               "反射备选 diag(1,-1)，det=−1，到目标点距离更大。",
    "parameters": {
        "points_X": X.tolist(),
        "rotation_R": ROT.tolist(), "det_R": float(np.linalg.det(ROT)),
        "reflection_alt": REFL.tolist(), "det_reflection": float(np.linalg.det(REFL)),
    },
    "evaluated_data": {
        "points_Y": Y.tolist(),
        "points_reflected": Y_REF.tolist(),
    },
    "processing": "固定解析点集与旋转矩阵；无随机采样。",
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
