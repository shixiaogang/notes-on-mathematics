"""教学图：两个向量的线性组合张成多大范围。

解析式固定构造：u=(2,1)，v=(1,2)；左 panel 画平行四边形格点 c1 u+c2 v，
右 panel 对比只用 u 的组合只能停留在一条直线上。无随机采样，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ls-linear-combination-span]
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
BLUE_FILL, RED_FILL = "#E5EAF0", "#F0E5E6"
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

U = np.array([2., 1.])
V = np.array([1., 2.])


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

# ---- 左 panel：两个方向的组合取遍整个平面 ----
for c1 in (-1, 0, 1):
    for c2 in (-1, 0, 1):
        p = c1 * U + c2 * V
        a.plot(*p, "o", ms=2.5, color=MUTED, zorder=3)
a.add_patch(Polygon([(0, 0), U, U + V, V], closed=True,
                   facecolor=BLUE_FILL, edgecolor=BLUE, lw=.6, zorder=1))
arrow(a, (0, 0), U, BLUE)
arrow(a, (0, 0), V, GREEN)
a.plot(*(U + V), "o", ms=5, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
a.text(U[0] + .12, U[1] - .05, "$u$", fontsize=8, color=BLUE)
a.text(V[0] - .32, V[1] + .10, "$v$", fontsize=8, color=GREEN)
a.text((U + V)[0] + .12, (U + V)[1] + .05, "$u+v$", fontsize=8, color=YELLOW)
a.text(-3.4, 3.45, "$c_1u+c_2v$：$c_1,c_2$ 任意，点取遍整个平面", fontsize=8)
a.set_title("(a) 两个不共线方向：组合张成整个平面", fontsize=8)
a.set(xlim=(-3.7, 4.1), ylim=(-3.3, 4.0), xticks=range(-3, 5), yticks=range(-3, 4))
a.set_aspect("equal")
a.grid(True)

# ---- 右 panel：只用 u 的组合只能停在一条直线上 ----
t = np.array([-2.3, 2.6])
b.plot(t * U[0], t * U[1], color=RED, lw=1.4, zorder=2)
for c in (-1, 1, 2):
    p = c * U
    b.plot(*p, "o", ms=4, mfc=RED, mec=INK, mew=.4, zorder=4)
arrow(b, (0, 0), U, BLUE)
b.plot(*V, "o", ms=5, mfc=GREEN, mec=INK, mew=.5, zorder=5)
b.annotate("$v$ 不在 $cu$ 这条直线上", xy=tuple(V), xytext=(-4.9, 1.9),
           fontsize=8, color=GREEN,
           arrowprops=dict(arrowstyle="->", color=GREEN, lw=.6))
b.text(-5.3, -2.75, "只用 $u$：所有 $c u$ 都在过原点的同一条直线上", fontsize=8)
b.set_title("(b) 只有一个方向：组合只覆盖一条直线", fontsize=8)
b.set(xlim=(-5.6, 5.6), ylim=(-3.0, 3.2), xticks=range(-4, 6, 2), yticks=range(-2, 4))
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
    "reader_question": "两个向量的线性组合到底能到达平面上多大的范围？",
    "formula": "u=(2,1), v=(1,2); span{u,v}={c1 u + c2 v : c1,c2 in R}=R^2; span{u}={c u : c in R}，是过原点的一条直线。",
    "parameters": {
        "basis_vectors": {"u": [2, 1], "v": [1, 2]},
        "lattice_grid": "c1,c2 in {-1,0,1} 的 9 个格点",
        "highlighted_combination": "u+v=(3,3)",
        "right_panel_line": "t*u, t in [-2.6, 2.6]；标点 -u=(-2,-1), u=(2,1), 2u=(4,2)",
        "off_line_point": "v=(1,2) 不在 span{u} 上（直线方程 y=x/2，v 的 y=2 != 0.5）",
    },
    "evaluated_data": {
        "lattice_points": [(c1 * U[0] + c2 * V[0], c1 * U[1] + c2 * V[1])
                           for c1 in (-1, 0, 1) for c2 in (-1, 0, 1)],
        "u": list(U), "v": list(V), "u_plus_v": list(U + V),
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
