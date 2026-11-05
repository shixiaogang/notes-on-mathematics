"""教学图：伴随的作用转移 —— <Ax,y>=<x,Aᵀy> 的两条路径。

固定示意：左空间 V、右空间 W 两个方框；$x\\in V$ 经 $A$ 到 $W$ 得 $Ax$，
$y\\in W$ 经 $A^T$ 回到 $V$ 得 $A^Ty$，两条路径给出同一个内积。无随机数。
从任意目录运行：python3 plots.py [--only ls-adjoint-action-transfer]
"""
from pathlib import Path
import argparse
import json

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
INK, MUTED = "#3B4252", "#6B7280"
BLUE_FILL, GREEN_FILL = "#E5EAF0", "#E8EEE9"
CN_MAIN, CN_AUX, EN = "Source Han Sans SC", "LXGW WenKai", "Fira Math"

matplotlib.rcParams.update({
    "font.family": [EN, CN_MAIN], "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": EN, "mathtext.it": EN,
    "mathtext.bf": EN, "mathtext.sf": EN,
    "axes.unicode_minus": False, "text.color": INK,
    "figure.facecolor": "white", "savefig.facecolor": "white",
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


fig, ax = plt.subplots(figsize=(112 / 25.4, 78 / 25.4))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

# 两个空间方框
ax.add_patch(FancyBboxPatch((.04, .20), .30, .60, boxstyle="round,pad=.012",
                            facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
ax.add_patch(FancyBboxPatch((.66, .20), .30, .60, boxstyle="round,pad=.012",
                            facecolor=GREEN_FILL, edgecolor=GREEN, lw=1.1))
ax.text(.19, .75, "$V$", fontsize=10, color=BLUE, ha="center")
ax.text(.81, .75, "$W$", fontsize=10, color=GREEN, ha="center")

# 点：x 在 V（上），y 在 W（下）；Ax 在 W（上），Aᵀy 在 V（下）
x_pt, ax_pt = (.19, .58), (.81, .58)
y_pt, aty_pt = (.81, .34), (.19, .34)
for p, c in [(x_pt, BLUE), (ax_pt, BLUE), (y_pt, GREEN), (aty_pt, GREEN)]:
    ax.plot(*p, "o", ms=6, color=c, mec=INK, mew=.5)
ax.text(x_pt[0] - .02, x_pt[1] + .045, "$x$", fontsize=8)
ax.text(ax_pt[0] - .02, ax_pt[1] + .045, "$Ax$", fontsize=8)
ax.text(y_pt[0] + .015, y_pt[1] - .02, "$y$", fontsize=8)
ax.text(aty_pt[0] + .02, aty_pt[1] - .05, "$A^Ty$", fontsize=8)

# 两条转移路径
ax.annotate("", xy=ax_pt, xytext=x_pt,
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.2,
                            connectionstyle="arc3,rad=-0.15"))
ax.annotate("", xy=aty_pt, xytext=y_pt,
            arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.2,
                            connectionstyle="arc3,rad=-0.15"))
ax.text(.50, .74, "$A$：先作用 $x$", fontsize=7.5, color=BLUE, ha="center")
ax.text(.50, .22, "$A^T$：先作用 $y$", fontsize=7.5, color=GREEN, ha="center")

# 恒等等式
ax.text(.50, .12, "$\\langle Ax,\\, y\\rangle_W = \\langle x,\\, A^Ty\\rangle_V$",
        fontsize=9, color=INK, ha="center")
ax.text(.50, .03, "伴随把内积中的作用从一侧整体搬到另一侧",
        fontsize=7.5, color=MUTED, ha="center")

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "伴随矩阵 Aᵀ 到底把“谁作用到谁”的关系搬到了哪里？",
    "formula": "<Ax,y>_W = <x,A^T y>_V for all x in V, y in W; "
               "two paths: apply A to x then inner-product with y, or apply A^T to y then inner-product with x.",
    "parameters": {"spaces": ["V", "W"], "map": "A: V->W, A^T: W->V"},
    "evaluated_data": {"identity": "<Ax,y>_W = <x,A^T y>_V"},
    "processing": "示意构图；无随机采样、无数值计算。",
    "width_mm": 112, "height_mm": 78, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
