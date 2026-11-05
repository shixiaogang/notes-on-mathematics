"""教学图：原范数单位球与对偶范数单位球的支撑关系。

固定构造：原范数取 ℓ1（菱形），其对偶为 ℓ∞（方盒）。
取菱形边上 x=(0.5,0.5)，支撑超平面 {z: z·x=1} 即 z1+z2=2，
恰好切到 ℓ∞ 方盒的顶点 (1,1)。无随机数，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ls-dual-norm-unit-ball]
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Polygon, Rectangle
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW, RED = "#7188A3", "#829C8B", "#B4A16F", "#A7787D"
INK, MUTED, GRID, STROKE = "#3B4252", "#6B7280", "#D8DCE2", "#4C4D4F"
BLUE_FILL, GREEN_FILL = "#E5EAF0", "#E8EEE9"
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

X = np.array([0.5, 0.5])  # 菱形边上的点；支撑线 z·x=1 ⇔ z1+z2=2


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 88 / 25.4))

# ℓ∞ 方盒（对偶单位球），虚线
ax.add_patch(Rectangle((-1, -1), 2, 2, facecolor=GREEN_FILL, edgecolor=GREEN,
                      lw=1.1, ls="--"))
# ℓ1 菱形（原单位球），实线
ax.add_patch(Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True,
                     facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))

# 支撑超平面 z1+z2=2：从 (0.7,1.3) 到 (1.3,0.7)
ax.plot([0.65, 1.35], [1.35, 0.65], color=RED, lw=1.1)
ax.plot(*X, "o", ms=5, mfc=BLUE, mec=INK, mew=.5, zorder=5)
ax.plot(1, 1, "o", ms=5, mfc=GREEN, mec=INK, mew=.5, zorder=5)
ax.plot([X[0], 1], [X[1], 1], color=MUTED, lw=.5, ls=":")

ax.text(-.15, .74, "$x=(0.5,0.5)$", fontsize=7.5, color=BLUE)
ax.text(1.06, .82, "切点 $(1,1)$", fontsize=7.5, color=GREEN)
ax.text(.82, 1.42, "支撑超平面 $\\{{z: z\\cdot x=1\\}}$", fontsize=7.5, color=RED)
ax.text(-1.55, -.25, "$\\ell_1$ 单位球 $B$", fontsize=7.5, color=BLUE)
ax.text(-1.55, 1.12, "$\\ell_\\infty$ 单位球 $B^*$", fontsize=7.5, color=GREEN)
ax.text(-1.55, -1.42, "$B^*=\\{z:\\sup_{x\\in B} z\\cdot x\\leq 1\\}$：对偶球",
        fontsize=7.5, color=INK)

ax.set_title("原范数单位球与对偶范数单位球互为支撑（$\\ell_1$ ↔ $\\ell_\\infty$）",
             fontsize=8)
ax.set(xlim=(-1.7, 1.7), ylim=(-1.6, 1.7))
ax.set(xticks=[-1, 0, 1], yticks=[-1, 0, 1])
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
    "reader_question": "对偶范数的单位球为什么恰好是原范数单位球各支撑半平面的交集？",
    "formula": "B_ell1={|z1|+|z2|<=1}; B*=B_ell_inf={|z1|<=1,|z2|<=1}; "
               "at x=(0.5,0.5), support line z·x=1 <=> z1+z2=2, touches B* at (1,1).",
    "parameters": {"x_on_ell1_ball": list(X)},
    "evaluated_data": {
        "x": list(X),
        "tangent_point_on_dual_ball": [1.0, 1.0],
        "support_line": "z1 + z2 = 2",
    },
    "processing": "解析式直接核对；无随机采样。",
    "width_mm": 112, "height_mm": 88, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
