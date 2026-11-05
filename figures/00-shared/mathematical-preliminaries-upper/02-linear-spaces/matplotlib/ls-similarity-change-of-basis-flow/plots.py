"""教学图：相似换基的闭环——旧基坐标经 P^{-1} 换入新基、作用 B、再经 P 回换。

固定构造：交换图（commutative diagram）。
上边：旧基下作用 y = A x。
左边：输入换基 x' = P^{-1} x（向下箭头）。
下边：新基下作用 y' = B x'，其中 B = P^{-1} A P。
右边：输出回换 y = P y'（向上箭头）。
沿上边与沿下边-两边的路径给出同一个 y，闭环合拢即 B = P^{-1} A P。
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
from matplotlib.patches import FancyBboxPatch
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
    "xtick.color": STROKE, "ytick.color": STROKE,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "grid.color": GRID, "grid.linewidth": .4,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 3, "svg.fonttype": "path",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME])
selection = parser.parse_args().only


def arrow(ax, p, q, color=INK, lw=1.2):
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                shrinkA=0, shrinkB=0))


def box(ax, x, y, w, h, title, math_line, face, edge):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                               boxstyle="round,pad=0.6,rounding_size=1.2",
                               linewidth=1.0, edgecolor=edge, facecolor=face,
                               alpha=0.35, zorder=2))
    ax.text(x + w / 2, y + h - 3.4, title, ha="center", va="center",
            fontsize=8, color=edge, zorder=3)
    ax.text(x + w / 2, y + 3.6, math_line, ha="center", va="center",
            fontsize=8.5, color=INK, zorder=3)


fig, ax = plt.subplots(figsize=(169 / 25.4, 78 / 25.4))

# 四个节点：上排旧基，下排新基
TL, TR = (8, 26), (64, 26)
BL, BR = (8, 4), (64, 4)
BW, BH = 28, 13

box(ax, *TL, BW, BH, "旧基输入坐标", r"$\mathbf{x}$", BLUE, BLUE)
box(ax, *TR, BW, BH, "旧基输出坐标", r"$\mathbf{y}=\mathbf{A}\mathbf{x}$", BLUE, BLUE)
box(ax, *BL, BW, BH, "新基输入坐标", r"$\mathbf{x}'=\mathbf{P}^{-1}\mathbf{x}$", GREEN, GREEN)
box(ax, *BR, BW, BH, "新基输出坐标", r"$\mathbf{y}'=\mathbf{B}\mathbf{x}'$", GREEN, GREEN)

# 上边：旧基作用 A；下边：新基作用 B=P^{-1}AP
arrow(ax, (TL[0] + BW, TL[1] + BH / 2), (TR[0], TR[1] + BH / 2))
ax.text((TL[0] + BW + TR[0]) / 2, TL[1] + BH / 2 + 2.4,
        r"$\mathbf{A}$", ha="center", fontsize=9, color=INK)

arrow(ax, (BL[0] + BW, BL[1] + BH / 2), (BR[0], BR[1] + BH / 2))
ax.text((BL[0] + BW + BR[0]) / 2, BL[1] + BH / 2 - 3.2,
        r"$\mathbf{B}=\mathbf{P}^{-1}\mathbf{A}\mathbf{P}$",
        ha="center", fontsize=8.5, color=INK)

# 左边：输入换基 P^{-1}（向下）；右边：输出回换 P（向上）
arrow(ax, (TL[0] + BW / 2, TL[1]), (BL[0] + BW / 2, BL[1] + BH))
ax.text(TL[0] + BW / 2 - 3.2, (TL[1] + BL[1] + BH) / 2,
        r"$\mathbf{P}^{-1}$", ha="center", va="center",
        fontsize=9, rotation=90, color=MUTED)

arrow(ax, (BR[0] + BW / 2, BR[1] + BH), (TR[0] + BW / 2, TR[1]))
ax.text(TR[0] + BW / 2 + 3.2, (TR[1] + BR[1] + BH) / 2,
        r"$\mathbf{P}$", ha="center", va="center",
        fontsize=9, rotation=90, color=MUTED)

ax.text(50, 44.5, "同一自映射：旧基（蓝）与新基（绿）的两套记录，闭环合拢",
        ha="center", fontsize=8.5, color=INK)

ax.set(xlim=(0, 100), ylim=(0, 48))
ax.set_aspect("equal")
ax.axis("off")


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "相似 B=P^{-1}AP 怎样从换基推导出来，闭环为什么合拢？",
    "formula": "Top: y=Ax. Left (input change): x'=P^{-1}x. Bottom (new-basis action): y'=B x'=P^{-1} A P x'. Right (output back): y=P y'. Both paths give y; closure gives B=P^{-1}AP.",
    "parameters": {
        "old_basis_row": ["input x", "output y=Ax"],
        "new_basis_row": ["input x'=P^{-1}x", "output y'=B x'"],
        "arrows": {"top": "A", "bottom": "B=P^{-1}AP",
                   "left": "P^{-1}", "right": "P"},
    },
    "evaluated_data": {},
    "processing": "交换图示意；无数值采样、无平滑。",
    "width_mm": 169, "height_mm": 78, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
