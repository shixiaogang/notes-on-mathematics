"""教学图：诱导范数 ‖A‖₂=max_{‖x‖=1}‖Ax‖ 的几何意义。

固定构造：A=[[2,1],[0,1]]。AᵀA=[[4,2],[2,2]]，特征值 3±√5，
σmax=√(3+√5)≈2.288，对应方向 (1,0.618)；左 panel 画单位圆与最优方向 x*，
右 panel 画 A 映射出的椭圆与最长半轴 Ax*。无随机数，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ls-induced-norm-action]
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle
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

A = np.array([[2., 1.], [0., 1.]])
# 数值核对：AᵀA 的最大特征值方向 (1, 0.618)
V_STAR = np.array([1., (np.sqrt(5) - 1) / 2]) / np.sqrt(1 + ((np.sqrt(5) - 1) / 2) ** 2)
AV_STAR = A @ V_STAR
SIG_MAX = np.linalg.norm(AV_STAR)


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


fig, (a, b) = plt.subplots(1, 2, figsize=(169 / 25.4, 72 / 25.4))

# 左：定义域单位圆
a.add_patch(Circle((0, 0), 1, facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
arrow(a, (0, 0), V_STAR, RED)
a.plot(*V_STAR, "o", ms=4, mfc=RED, mec=INK, mew=.4, zorder=5)
a.text(V_STAR[0] + .06, V_STAR[1] + .04, "$x^*$", fontsize=8, color=RED)
a.text(-1.55, 1.25, "$\\|x\\|_2=1$", fontsize=7.5, color=BLUE)
a.set_title("(a) 定义域：单位圆 $\\{x:\\|x\\|_2=1\\}$", fontsize=8)
a.set(xlim=(-1.7, 1.7), ylim=(-1.4, 1.5), xticks=[-1, 0, 1], yticks=[-1, 0, 1])
a.set_aspect("equal")
a.grid(True)

# 右：A 映射后的椭圆
th = np.linspace(0, 2 * np.pi, 240)
ell = A @ np.vstack([np.cos(th), np.sin(th)])
b.fill(ell[0], ell[1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1)
arrow(b, (0, 0), AV_STAR, RED)
b.plot(*AV_STAR, "o", ms=4, mfc=RED, mec=INK, mew=.4, zorder=5)
b.text(AV_STAR[0] + .08, AV_STAR[1] + .05, "$Ax^*$", fontsize=8, color=RED)
b.text(1.35, 1.05, "$\\|Ax^*\\|_2=\\sigma_{max}\\approx2.29$",
       fontsize=7.5, color=RED)
b.text(-3.4, 1.05, "$A\\{x:\\|x\\|_2=1\\}$", fontsize=7.5, color=BLUE)
b.set_title("(b) 值域：单位圆被 $A$ 拉成椭圆，最长半轴即 $\\|A\\|_2$", fontsize=8)
b.set(xlim=(-3.6, 3.1), ylim=(-1.5, 1.5), xticks=[-3, -2, -1, 0, 1, 2, 3],
      yticks=[-1, 0, 1])
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
    "reader_question": "诱导范数 ‖A‖₂ 为什么等于 A 把单位圆撑出的椭圆的最长半轴？",
    "formula": "A=[[2,1],[0,1]]; A^T A=[[4,2],[2,2]]; eigenvalues 3±sqrt(5); "
               "sigma_max=sqrt(3+sqrt(5))≈2.288; maximizing direction v*∝(1,0.618).",
    "parameters": {
        "A": A.tolist(),
        "v_star_direction": [1.0, (np.sqrt(5) - 1) / 2],
    },
    "evaluated_data": {
        "v_star_unit": list(V_STAR),
        "A_v_star": list(AV_STAR),
        "sigma_max": float(SIG_MAX),
        "sigma_min": float(np.sqrt(3 - np.sqrt(5))),
    },
    "processing": "解析式与 numpy.linalg.norm 核对；无随机采样。",
    "width_mm": 169, "height_mm": 72, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
