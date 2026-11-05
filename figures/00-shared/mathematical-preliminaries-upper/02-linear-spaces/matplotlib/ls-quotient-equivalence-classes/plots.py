"""教学图：商空间 V/N 是所有平行于子空间 N 的等价类 x+N 的集合。

固定构造：V=R^2，N 是过原点的 x 轴直线。等价类为水平线 y=const：
0+N 即 N 本身（y=0），p+N 是过 p 的整条平行线。同一平行线上任意两点之差属于 N。
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


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 80 / 25.4))

X = np.array([-3.4, 3.6])
# N = 0+N：过原点的水平线（商空间的零点类）
ax.plot(X, [0, 0], color=BLUE, lw=1.6, zorder=2)
# 等价类 p+N：三条平行于 N 的水平线
ax.plot(X, [1, 1], color=GREEN, lw=1.1, zorder=2)
ax.plot(X, [2, 2], color=YELLOW, lw=1.1, zorder=2)
ax.plot(X, [-1, -1], color=RED, lw=1.1, ls="--", zorder=2)

# 每个类取代表点，并在 y=1 上再放一个点，说明同一类里的点彼此等价
ax.plot(0, 0, "o", ms=4, mfc=BLUE, mec=INK, mew=.5, zorder=5)
ax.plot(.3, 1, "o", ms=4.5, mfc=GREEN, mec=INK, mew=.5, zorder=5)
ax.plot(2.1, 1, "o", ms=4.5, mfc="white", mec=GREEN, mew=.9, zorder=5)
ax.plot(-.6, 2, "o", ms=4.5, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
ax.plot(1.4, -1, "o", ms=4.5, mfc=RED, mec=INK, mew=.5, zorder=5)

ax.annotate("", xy=(2.1, 1), xytext=(.3, 1),
            arrowprops=dict(arrowstyle="<->", color=GREEN, lw=.6))
ax.text(1.05, .78, "两点差属于 $N$", fontsize=7.5, color=GREEN, ha="center")

ax.text(2.35, .10, "$0+N=N$", fontsize=8, color=BLUE)
ax.text(2.35, 1.10, "$p_1+N$", fontsize=8, color=GREEN)
ax.text(2.35, 2.10, "$p_2+N$", fontsize=8, color=YELLOW)
ax.text(2.35, -0.90, "$p_3+N$", fontsize=8, color=RED)
ax.text(-3.3, -1.75, "商空间 $V/N=\\{x+N:x\\in V\\}$：把整条平行线当成一个点", fontsize=8)
ax.set_title("同一平行线上的点彼此等价", fontsize=8)
ax.set(xlim=(-3.6, 4.1), ylim=(-2.0, 2.7), xticks=[-3, -2, -1, 0, 1, 2, 3],
       yticks=[-1, 0, 1, 2])
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
    "reader_question": "商空间 V/N 到底是由哪些对象组成的？",
    "formula": "V=R^2; N=span(e1)={(x,0)}. Equivalence classes: p+N={(x,p_y)}. 0+N=N. Same line y=c: two points p,q on it satisfy p-q in N.",
    "parameters": {
        "subspace": "N = x 轴（过原点的直线）",
        "classes": {"0+N": "y=0（蓝色实线）", "p1+N": "y=1（绿色）",
                    "p2+N": "y=2（黄色）", "p3+N": "y=-1（红色虚线）"},
        "representatives": {"origin": [0, 0], "p1": [.3, 1], "p1'": [2.1, 1], "p2": [-.6, 2], "p3": [1.4, -1]},
        "equivalence_demo": "(.3,1) 与 (2.1,1) 之差 (1.8,0) 属于 N，故同一类",
    },
    "evaluated_data": {"class_lines_y": [0, 1, 2, -1], "representatives": [[0, 0], [.3, 1], [2.1, 1], [-.6, 2], [1.4, -1]]},
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
