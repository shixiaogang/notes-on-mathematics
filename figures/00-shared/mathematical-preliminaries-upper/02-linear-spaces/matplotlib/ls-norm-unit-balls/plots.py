"""教学图：同一方向在不同范数下的单位球（单位向量依赖范数）。

固定构造：沿射线 (t,t) 方向观察四种范数的单位球交点。
ℓ1 菱形交点 t=0.5；ℓ2 单位圆交点 t=1/√2≈0.707；ℓ∞ 方盒交点 t=1；
加权椭圆（M-范数）x²/4+y²/0.64=1 交点 t≈0.743。无随机数。
从任意目录运行：python3 plots.py [--only ls-norm-unit-balls]
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Polygon, Circle, Rectangle, Ellipse
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
    "xtick.labelsize": 7, "ytick.labelsize": 7,
    "grid.color": GRID, "grid.linewidth": .4,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 3, "svg.fonttype": "path",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, axes = plt.subplots(1, 4, figsize=(169 / 25.4, 60 / 25.4))
RAY = np.array([1., 1.]) / np.sqrt(2)  # 公共射线方向

panels = [
    ("(a) $\\ell_1$ 范数：菱形", "diamond", 0.5, "(0.50, 0.50)"),
    ("(b) $\\ell_2$ 范数：单位圆", "circle", 1 / np.sqrt(2), "(0.71, 0.71)"),
    ("(c) $\\ell_\\infty$ 范数：方盒", "square", 1.0, "(1.00, 1.00)"),
    ("(d) 加权 $M$-范数：椭圆", "ellipse", 1 / np.sqrt(0.25 + 1 / 0.64), "(0.74, 0.74)"),
]

for ax, (title, kind, t_hit, label) in zip(axes, panels):
    if kind == "diamond":
        ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True,
                             facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
    elif kind == "circle":
        ax.add_patch(Circle((0, 0), 1, facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
    elif kind == "square":
        ax.add_patch(Rectangle((-1, -1), 2, 2, facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
    else:
        ax.add_patch(Ellipse((0, 0), width=4, height=1.6,
                             facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
    # 公共射线
    ax.plot([0, 1.5 * RAY[0]], [0, 1.5 * RAY[1]], color=MUTED, lw=.6, ls="--")
    p = t_hit * RAY
    ax.plot(*p, "o", ms=5, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
    ax.annotate(label, xy=tuple(p), xytext=(p[0] + .12, p[1] - .28),
                fontsize=7, color=INK)
    ax.set_title(title, fontsize=8)
    ax.set(xlim=(-1.7, 1.7), ylim=(-1.7, 1.7),
           xticks=[-1, 0, 1], yticks=[-1, 0, 1])
    ax.set_aspect("equal")
    ax.grid(True)

fig.suptitle("同一条射线 (1,1) 方向上，“单位向量”的位置随范数改变",
             fontsize=8, y=0.98)
finalize(fig)
fig.tight_layout(rect=(0, 0, 1, .88))
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "“x 是单位向量”这句话为什么必须先说明用的是哪一种范数？",
    "formula": "沿方向 (1,1) 取射线 t*(1,1)/sqrt(2)；四种范数的单位球交点分别为："
               "ell1: t=0.5; ell2: t=1/sqrt(2); ell_inf: t=1; M-ellipse x^2/4+y^2/0.64=1: t≈0.743.",
    "parameters": {
        "ray_direction": list(RAY),
        "ellipse_equation": "x^2/4 + y^2/0.64 = 1",
    },
    "evaluated_data": {
        "ell1_hit": [0.5, 0.5],
        "ell2_hit": [1 / np.sqrt(2), 1 / np.sqrt(2)],
        "ell_inf_hit": [1.0, 1.0],
        "M_ellipse_hit": [1 / np.sqrt(0.25 + 1 / 0.64)] * 2,
    },
    "processing": "解析式直接求交点；无随机采样。",
    "width_mm": 169, "height_mm": 60, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
