"""教学图：线性映射的核、像与秩零度定理 dim ker T + dim im T = dim 定义域。

(a) T:R^2 -> R^2，T(x,y)=(x,0)：ker T 是 y 轴（一维直线，红色），
    im T 是 x 轴（一维直线，蓝色），dim ker=1，dim im=1，1+1=2。
(b) T:R^3 -> R^2，T(x,y,z)=(x,y)：ker T 是 z 轴（一维直线，红色），
    im T 是 xy 平面（二维，浅蓝），dim ker=1，dim im=2，1+2=3。
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
parser.add_argument("--only", default=NAME, choices=[NAME])
selection = parser.parse_args().only


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


fig = plt.figure(figsize=(169 / 25.4, 72 / 25.4))
a = fig.add_subplot(1, 2, 1)
b = fig.add_subplot(1, 2, 2, projection="3d")

# ---- (a) T(x,y)=(x,0)：核=y 轴，像=x 轴 ----
a.axline((0, 0), slope=0, color=BLUE, lw=1.6, zorder=2)
a.axline((0, 0), slope=np.inf, color=RED, lw=1.6, zorder=2)
v = np.array([2., 1.])
Tv = np.array([2., 0.])
arrow(a, (0, 0), v, INK, lw=1.2)
a.plot(*Tv, "o", ms=5, mfc=BLUE, mec=INK, mew=.5, zorder=5)
a.plot([v[0], Tv[0]], [v[1], Tv[1]], color=MUTED, ls="--", lw=.6)
a.text(2.25, 1.02, "$v=(2,1)$", fontsize=8, color=INK)
a.text(2.05, -0.42, "$T(v)=(2,0)$", fontsize=8, color=BLUE)
a.text(3.30, 0.16, "$\\operatorname{im}T=x$ 轴", fontsize=8, color=BLUE, ha="right")
a.text(0.12, -1.62, "$\\ker T=y$ 轴", fontsize=8, color=RED)
a.text(-2.9, 1.75, "$\\dim\\ker T=1$，$\\dim\\operatorname{im}T=1$，$1+1=2$", fontsize=8)
a.set_title("(a) $T:\\mathbb{R}^2\\to\\mathbb{R}^2$，$T(x,y)=(x,0)$", fontsize=8)
a.set(xlim=(-3.2, 3.4), ylim=(-1.9, 2.1), xticks=[-2, 0, 2], yticks=[-1, 1])
a.set_aspect("equal")
a.grid(True)

# ---- (b) T(x,y,z)=(x,y)：核=z 轴，像=xy 平面 ----
xx, yy = np.meshgrid([-2, 2], [-2, 2])
b.plot_surface(xx, yy, np.zeros_like(xx), color=BLUE_FILL, edgecolor=BLUE,
                               lw=.5, alpha=.9, zorder=1)
b.plot([0, 0], [0, 0], [-1.6, 2.4], color=RED, lw=1.6, zorder=5)
p = np.array([1., 1., 1.])
b.plot(*p, "o", ms=4, color=INK, zorder=6)
b.plot([p[0], p[0]], [p[1], p[1]], [p[2], 0], color=MUTED, ls="--", lw=.6, zorder=4)
b.text(1.40, 1.35, 1.45, "$p=(1,1,1)$", fontsize=8, color=INK)
b.text(0, 0, 2.5, "$\\ker T=z$ 轴", fontsize=8, color=RED)
b.text(1.4, -1.6, -0.55, "$\\operatorname{im}T=xy$ 平面", fontsize=8, color=BLUE)
b.text(-2.0, -2.0, 2.3, "$\\dim\\ker=1$，$\\dim\\operatorname{im}=2$，$1+2=3$", fontsize=8)
b.set_title("(b) $T:\\mathbb{R}^3\\to\\mathbb{R}^2$，$T(x,y,z)=(x,y)$", fontsize=8)
b.set(xlim=(-2.2, 2.2), ylim=(-2.2, 2.2), zlim=(-1.2, 2.8),
      xticks=[-2, 0, 2], yticks=[-2, 0, 2], zticks=[0, 1, 2])
b.view_init(elev=18, azim=-62)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "被映到 0 的向量（核）与实际用到的输出方向（像），维度为什么相加等于定义域维数？",
    "formula": "(a) T(x,y)=(x,0): ker T={(0,y)}, dim=1; im T={(x,0)}, dim=1. (b) T(x,y,z)=(x,y): ker T={(0,0,z)}, dim=1; im T=R^2, dim=2. Rank-nullity: dim ker + dim im = dim domain.",
    "parameters": {
        "panel_a": {"map": "T(x,y)=(x,0)", "sample": {"v": [2, 1], "T(v)": [2, 0]},
                    "kernel": "y 轴", "image": "x 轴"},
        "panel_b": {"map": "T(x,y,z)=(x,y)", "sample": {"p": [1, 1, 1], "T(p)": [1, 1, 0]},
                    "kernel": "z 轴", "image": "xy 平面 (z=0)"},
        "rank_nullity": {"a": "1+1=2", "b": "1+2=3"},
    },
    "evaluated_data": {"a_sample_v": list(v), "a_sample_Tv": list(Tv), "b_sample_p": list(p)},
    "processing": "直接求值；无平滑、无随机采样。",
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
