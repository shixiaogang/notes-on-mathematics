"""教学图：Sylvester 方程 AX+XB=C 可解的特征值分离条件。

解析式固定构造：A=diag(1,2)，B=diag(-3,-4)。
复平面上只用两个实集合的距离示意：
  A 的特征值集合 {1,2}（蓝），−B 的特征值集合 {3,4}（绿）；
  sep(A,−B)=min|λ_i(A)−μ_j(−B)|=|2−3|=1>0，此时 Sylvester 方程对任意 C 可解。
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

EIG_A = [1., 2.]
EIG_MINUS_B = [3., 4.]
SEP = min(abs(a - b) for a in EIG_A for b in EIG_MINUS_B)   # = 1


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 74 / 25.4))

# 实轴（兼作刻度）
ax.axhline(0, color=STROKE, lw=.75)
for x in range(0, 6):
    ax.plot([x, x], [-.05, .05], color=STROKE, lw=.6)
    ax.text(x, -.24, str(x), fontsize=7.5, color=MUTED, ha="center")
for x in EIG_A:
    ax.plot(x, 0, "o", ms=7, mfc=BLUE, mec=INK, mew=.5, zorder=5)
    ax.text(x, .16, f"$\\lambda={int(x)}$", fontsize=7.5, color=BLUE, ha="center")
for x in EIG_MINUS_B:
    ax.plot(x, 0, "o", ms=7, mfc=GREEN, mec=INK, mew=.5, zorder=5)
    ax.text(x, .16, f"$\\mu={int(x)}$", fontsize=7.5, color=GREEN, ha="center")

# 间距括号
ax.annotate("", xy=(3, -.32), xytext=(2, -.32),
            arrowprops=dict(arrowstyle="<->", color=RED, lw=.9))
ax.text(2.5, -.62, "$\\mathrm{sep}(A,-B)=1>0$", fontsize=8, color=RED, ha="center")

ax.text(1.5, .78, "$A$ 的特征值集合", fontsize=8, color=BLUE, ha="center")
ax.text(3.5, .78, "$-B$ 的特征值集合", fontsize=8, color=GREEN, ha="center")
ax.text(-.55, -1.05,
        "例：$A=\\mathrm{diag}(1,2)$，$B=\\mathrm{diag}(-3,-4)$；两集合不相交即可解",
        fontsize=7.5, color=MUTED)
ax.set_title("Sylvester 方程：两个特征值集合分离即可解", fontsize=8)
ax.set(xlim=(-.9, 5.3), ylim=(-1.35, 1.2))
ax.set(yticks=[], xticks=[])
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=False, bottom=False)

finalize(fig)
fig.tight_layout()
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "Sylvester 方程 AX+XB=C 什么时候对任意 C 都有唯一解？",
    "formula": "A=diag(1,2), B=diag(-3,-4); eig(A)={1,2}; eig(-B)={3,4}; "
               "sep(A,-B)=min|λ_i(A)-μ_j(-B)|=|2-3|=1>0；"
               "条件：σ(A)∩σ(-B)=∅，即 λ_i(A)+μ_j(B)≠0 对所有 i,j。",
    "parameters": {
        "A_diag": [1, 2], "B_diag": [-3, -4],
        "eig_A": EIG_A, "eig_minus_B": EIG_MINUS_B,
    },
    "evaluated_data": {
        "separation": SEP,
        "all_pair_distances": [abs(a - b) for a in EIG_A for b in EIG_MINUS_B],
    },
    "processing": "直接求值；无随机采样。",
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
