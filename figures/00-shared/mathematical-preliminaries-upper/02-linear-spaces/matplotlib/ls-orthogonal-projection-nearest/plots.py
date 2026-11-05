"""教学图：子空间上的最近点是正交投影。

解析式固定构造：U 为过原点、方向 d=(2,1) 的直线；点 y=(1,3)。
投影 P_U y = (y·d)/(d·d) d = (2,1)；误差 e = y - P_U y = (-1,2)，与 d 正交。
另取直线上非正交候选 Q=2d=(4,2)，比较距离。无随机数，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ls-orthogonal-projection-nearest]
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

D = np.array([2., 1.])                      # U 的方向
Y = np.array([1., 3.])                      # 给定点
P = (Y @ D) / (D @ D) * D                   # 正交投影 = (2,1)
E = Y - P                                   # 误差 = (-1,2)
Q = 2. * D                                  # 非正交候选 = (4,2)


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

# 子空间 U：过原点、方向 d=(2,1) 的直线
t = np.array([-1.25, 2.75])
ax.plot(t * D[0], t * D[1], color=BLUE, lw=1.4, zorder=2)
ax.text(5.05, 2.62, "$U$（子空间）", fontsize=8, color=BLUE)

# 投影点 P_U y 与误差向量
ax.plot(*P, "o", ms=5, mfc=GREEN, mec=INK, mew=.5, zorder=5)
arrow(ax, P, Y, GREEN, lw=1.2)
ax.text(0.05, 1.95, "$y-P_Uy$（误差，垂直于 $U$）", fontsize=7.5, color=GREEN)

# 直角标记
u = D / np.linalg.norm(D)
e = E / np.linalg.norm(E)
s = 0.30
corner1 = P + s * u
corner2 = P + s * u + s * e
corner3 = P + s * e
ax.plot([corner1[0], corner2[0], corner3[0]],
        [corner1[1], corner2[1], corner3[1]], color=GREEN, lw=.6)

# 给定点 y 与投影点标注
ax.plot(*Y, "o", ms=5, mfc=BLUE, mec=INK, mew=.5, zorder=5)
ax.text(0.72, 3.12, "$y$", fontsize=8, color=BLUE)
ax.text(2.12, 0.72, "$P_Uy$", fontsize=8, color=GREEN)

# 非正交候选 Q 及其更长距离
ax.plot(*Q, "o", ms=5, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
ax.plot([Y[0], Q[0]], [Y[1], Q[1]], color=YELLOW, lw=.9, ls="--", zorder=3)
ax.text(3.05, 2.85, "非正交候选 $Q=(4,2)$", fontsize=7.5, color=YELLOW)

ax.text(-2.05, 3.62, "正交投影是 $U$ 上离 $y$ 最近的点", fontsize=8)
ax.text(-2.05, -1.42,
        "$\\|y-P_Uy\\|=\\sqrt{5}\\approx2.24$ 最短；$\\|y-Q\\|=\\sqrt{10}\\approx3.16$",
        fontsize=7.5, color=MUTED)
ax.set_title("子空间最近点：误差垂直于子空间", fontsize=8)
ax.set(xlim=(-2.2, 5.9), ylim=(-1.7, 4.0), xticks=range(-2, 6, 2), yticks=range(-1, 4))
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
    "reader_question": "子空间上离给定点最近的点为什么一定是正交投影？",
    "formula": "U={t(2,1):t in R}; P_U y=(y·d)/(d·d)d; y=(1,3), d=(2,1); "
               "P_U y=(2,1); error=(-1,2), 且 error·d=0。",
    "parameters": {
        "subspace_direction": list(D),
        "point_y": list(Y),
        "projection_P": list(P),
        "error_vector": list(E),
        "non_orthogonal_candidate_Q": list(Q),
    },
    "evaluated_data": {
        "y_dot_d": float(Y @ D), "d_dot_d": float(D @ D),
        "projection_norm": float(np.linalg.norm(E)),
        "projection_norm_sqrt5": "sqrt(5)=2.236",
        "distance_to_Q": float(np.linalg.norm(Y - Q)),
        "distance_to_Q_sqrt10": "sqrt(10)=3.162",
        "error_orthogonal_check": float(E @ D),
    },
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
