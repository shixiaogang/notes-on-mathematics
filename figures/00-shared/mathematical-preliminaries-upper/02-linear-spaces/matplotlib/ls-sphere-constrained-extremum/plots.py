"""教学图：单位圆约束下 xᵀAx 的极值在特征方向上。

解析式固定构造：A=[[2,0.5],[0.5,1]]（对称正定）。特征值 λ1≈2.207、λ2≈0.793。
单位圆上 xᵀAx 的最大值在 v1 方向取到 λ1，最小值在 v2 方向取到 λ2；
椭圆 xᵀAx=λ1 在 ±v1 处与单位圆相切，xᵀAx=λ2 在 ±v2 处相切。
另画子空间约束（过原点直线 y=0.5x）上的两个极值点。
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

A = np.array([[2., 0.5], [0.5, 1.]])
LAM, V = np.linalg.eigh(A)
LAM1, LAM2 = LAM[1], LAM[0]                 # 大、小特征值
V1, V2 = V[:, 1], V[:, 0]


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


fig, ax = plt.subplots(figsize=(112 / 25.4, 84 / 25.4))

# 单位圆
th = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.cos(th), np.sin(th), color=MUTED, lw=.9, zorder=2)

# 椭圆 xᵀAx = λ1 与 xᵀAx = λ2
circle = np.array([np.cos(th), np.sin(th)])
ell1 = V @ np.diag(np.sqrt(LAM1 / LAM)) @ circle
ell2 = V @ np.diag(np.sqrt(LAM2 / LAM)) @ circle
ax.plot(ell1[0], ell1[1], color=BLUE, lw=1.1, zorder=3)
ax.plot(ell2[0], ell2[1], color=GREEN, lw=1.1, zorder=3)

# 特征方向
arrow(ax, (0, 0), V1, BLUE, lw=1.2)
arrow(ax, (0, 0), V2, GREEN, lw=1.2)
ax.text(V1[0] * 1.30 - .05, V1[1] * 1.30 - .18,
        "$v_1$（最大方向）", fontsize=7.5, color=BLUE)
ax.text(V2[0] * 1.18 + .08, V2[1] * 1.18 - .22,
        "$v_2$（最小方向）", fontsize=7.5, color=GREEN)

# 子空间约束：过原点直线 y=-0.6x（与特征方向不重合）
d = np.array([1., -0.6]); d = d / np.linalg.norm(d)
ax.plot([-1.3 * d[0], 1.3 * d[0]], [-1.3 * d[1], 1.3 * d[1]],
        color=YELLOW, lw=1.0, ls="--", zorder=2)
for sgn in (1, -1):
    p = sgn * d
    ax.plot(*p, "o", ms=4, mfc=YELLOW, mec=INK, mew=.4, zorder=5)
ax.text(-1.95, 0.95, "约束直线上的\n两个极值点", fontsize=7.5, color=YELLOW)

ax.text(-1.95, 1.55, "$\\max x^\\top A x=\\lambda_1\\approx2.21$", fontsize=8, color=BLUE)
ax.text(-1.95, -1.68, "$\\min x^\\top A x=\\lambda_2\\approx0.79$", fontsize=8, color=GREEN)
ax.set_title("单位圆约束下的极值落在特征方向", fontsize=8)
ax.set(xlim=(-2.1, 2.1), ylim=(-1.85, 1.85), xticks=range(-2, 3), yticks=range(-1, 2))
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
    "reader_question": "为什么单位圆上二次型 xᵀAx 的最大、最小都在特征方向？",
    "formula": "A=[[2,0.5],[0.5,1]]; λ1=(3+√2)/2≈2.207, λ2=(3-√2)/2≈0.793; "
               "max_{||x||=1} xᵀAx=λ1 在 v1；min=λ2 在 v2；"
               "椭圆 xᵀAx=λ1 与单位圆在 ±v1 相切。",
    "parameters": {
        "A": A.tolist(),
        "eigenvalues": list(LAM), "eigenvectors_columns_V": V.tolist(),
        "subspace_constraint": "直线 y=-0.6x，单位方向 (1,-0.6)/√1.36",
    },
    "evaluated_data": {
        "v1_norm": float(np.linalg.norm(V1)), "v2_norm": float(np.linalg.norm(V2)),
        "v1_dot_v2": float(V1 @ V2),
        "max_value_on_circle": float(LAM1), "min_value_on_circle": float(LAM2),
    },
    "processing": "eigh 为固定解析矩阵的精确对角化；无随机采样。",
    "width_mm": 112, "height_mm": 84, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
