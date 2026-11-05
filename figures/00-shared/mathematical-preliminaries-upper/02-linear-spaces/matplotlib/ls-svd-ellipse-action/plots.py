"""教学图：最小二乘的行图像与列图像（残差水平椭圆）。

解析式固定构造：A=[[2,1],[0.5,1.5]]，b=(3,2)，恰有解 x̂=(1,1)（因 A 可逆）。
左 panel（x 空间，行图像）：两条直线 2x1+x2=3 与 0.5x1+1.5x2=2 交于 x̂；
  残差 f(x)=||Ax-b||² 的水平集是以 x̂ 为中心的同心椭圆。
右 panel（y 空间，列图像）：列 a1=(2,0.5)、a2=(1,1.5) 张成平行四边形，
  b=a1+a2 恰在列空间内，残差 r=b-Ax̂=0。
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

A = np.array([[2., 1.], [0.5, 1.5]])
B = np.array([3., 2.])
XHAT = np.linalg.solve(A, B)                # (1,1)
Q = A.T @ A
LAM, EIG = np.linalg.eigh(Q)                # 残差水平椭圆的半轴


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

# ---- 左 panel：行图像，残差水平椭圆 ----
xs = np.linspace(-0.6, 2.7, 50)
a.plot(xs, 3 - 2 * xs, color=BLUE, lw=1.2, label="$2x_1+x_2=3$")
a.plot(xs, (2 - 0.5 * xs) / 1.5, color=GREEN, lw=1.2, label="$0.5x_1+1.5x_2=2$")
th = np.linspace(0, 2 * np.pi, 120)
circle = np.array([np.cos(th), np.sin(th)])
for c in (0.5, 1.5, 3.0):
    ell = XHAT[:, None] + EIG @ (np.diag(np.sqrt(c / LAM)) @ circle)
    a.plot(ell[0], ell[1], color=MUTED, lw=.6, ls=":")
a.plot(*XHAT, "o", ms=5, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
a.text(1.18, 0.62, "$\\hat x=(1,1)$", fontsize=8, color=YELLOW)
a.text(-0.55, 2.42, "同心虚线：$\\|Ax-b\\|^2=c$", fontsize=7.5, color=MUTED)
a.legend(loc="lower left", fontsize=7.5, frameon=False)
a.set_title("(a) x 空间：行图像，残差二次型的水平椭圆", fontsize=8)
a.set(xlim=(-0.9, 3.1), ylim=(-0.9, 3.0), xticks=range(0, 4), yticks=range(0, 3))
a.set_aspect("equal")
a.grid(True)

# ---- 右 panel：列图像，b 落在列空间内 ----
A1, A2 = A[:, 0], A[:, 1]
b.add_patch(Polygon([(0, 0), A1, A1 + A2, A2], closed=True,
                    facecolor=BLUE_FILL, edgecolor=BLUE, lw=.6, zorder=1))
arrow(b, (0, 0), A1, BLUE)
arrow(b, (0, 0), A2, GREEN)
arrow(b, A1, B, GREEN, lw=.8, ls="--")
arrow(b, A2, B, BLUE, lw=.8, ls="--")
b.plot(*B, "o", ms=5, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
b.text(1.55, 0.35, "$a_1=(2,0.5)$", fontsize=7.5, color=BLUE)
b.text(0.15, 1.28, "$a_2=(1,1.5)$", fontsize=7.5, color=GREEN)
b.text(2.62, 2.12, "$b=(3,2)=a_1+a_2$", fontsize=8, color=YELLOW)
b.text(-0.45, -0.55, "$r=b-A\\hat x=0$：$b$ 落在列空间 $\\mathrm{Col}(A)$ 内",
       fontsize=7.5, color=MUTED)
b.set_title("(b) y 空间：列图像，残差为零", fontsize=8)
b.set(xlim=(-0.7, 3.9), ylim=(-0.9, 2.8), xticks=range(0, 4), yticks=range(0, 3))
b.set_aspect("equal")
b.grid(True)

finalize(fig)
fig.tight_layout()
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "最小二乘的解 x̂ 在 x 空间与 y 空间分别对应什么几何位置？",
    "formula": "A=[[2,1],[0.5,1.5]], b=(3,2); x̂=A^{-1}b=(1,1); "
               "f(x)=(x-x̂)ᵀAᵀA(x-x̂) 是以 x̂ 为中心的同心椭圆；"
               "列图像 b=1·a1+1·a2，残差 r=0。",
    "parameters": {
        "A": A.tolist(), "b": list(B), "xhat": list(XHAT),
        "row_lines": ["2x1+x2=3", "0.5x1+1.5x2=2"],
        "columns": {"a1": list(A1), "a2": list(A2)},
        "ellipse_levels_c": [0.5, 1.5, 3.0],
    },
    "evaluated_data": {
        "AtA": Q.tolist(),
        "eigenvalues_of_AtA": list(LAM),
        "AtA_check": list(A.T @ A @ XHAT),
        "residual_at_xhat": list(B - A @ XHAT),
    },
    "processing": "eigh 为固定解析矩阵的精确对角化；无随机采样。",
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
