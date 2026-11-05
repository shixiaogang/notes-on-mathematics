"""教学图：二维行列式的有向体积。

固定构造：单位正方形经 A=[[1.5,0.5],[0.3,1.2]] 映射为平行四边形，
det A=1.65>0（取向不变）；交换两列得 A⁻=[[0.5,1.5],[1.2,0.3]]，
det A⁻=-1.65（取向翻转）。两个 panel 面积都是 |det|=1.65。
无随机数，不调用 LaTeX。从任意目录运行：python3 plots.py [--only ls-determinant-oriented-volume]
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

A_POS = np.array([[1.5, 0.5], [0.3, 1.2]])   # det = 1.65
A_NEG = np.array([[0.5, 1.5], [1.2, 0.3]])  # det = -1.65


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


def draw_panel(ax, A, title, det_text, orient_text, orient_xy, flip):
    e1, e2 = A[:, 0], A[:, 1]
    ax.add_patch(Rectangle((0, 0), 1, 1, facecolor="none", edgecolor=MUTED,
                          lw=.6, ls=":"))
    ax.add_patch(Polygon([(0, 0), e1, e1 + e2, e2], closed=True,
                        facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1))
    arrow(ax, (0, 0), e1, BLUE)
    arrow(ax, (0, 0), e2, GREEN)
    ax.text(e1[0] + .05, e1[1] - .05, "$a_1$", fontsize=8, color=BLUE)
    ax.text(e2[0] - .28, e2[1] + .10, "$a_2$", fontsize=8, color=GREEN)
    # 有向角弧：正 panel 从 a1 方向扫到 a2 方向（逆时针），负 panel 反向
    u1, u2 = e1 / np.linalg.norm(e1) * .55, e2 / np.linalg.norm(e2) * .55
    ax.annotate("", xy=tuple(u2 if not flip else u1),
                xytext=tuple(u1 if not flip else u2),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=.9,
                                connectionstyle="arc3,rad=0.25" if not flip
                                else "arc3,rad=-0.25"))
    ax.text(orient_xy[0], orient_xy[1], orient_text, fontsize=7.5, color=RED)
    ax.text(.15, 1.55, det_text, fontsize=7.5, color=INK)
    ax.set_title(title, fontsize=8)
    ax.set(xlim=(-.35, 2.6), ylim=(-.3, 1.85), xticks=[0, 1, 2], yticks=[0, 1])
    ax.set_aspect("equal")
    ax.grid(True)


fig, (a, b) = plt.subplots(1, 2, figsize=(169 / 25.4, 70 / 25.4))

draw_panel(a, A_POS,
           "(a) det A = 1.65 > 0：保取向",
           "平行四边形面积 = det A = 1.65",
           "$a_1\\to a_2$ 为逆时针",
           (.75, .62), False)
draw_panel(b, A_NEG,
           "(b) det A = −1.65 < 0：翻转取向",
           "面积大小 = |det A| = 1.65",
           "$a_1\\to a_2$ 翻为顺时针",
           (1.0, .62), True)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "行列式的正负号在图上到底标记了面积的什么信息？",
    "formula": "A+=[[1.5,0.5],[0.3,1.2]], det=1.65; A-=[[0.5,1.5],[1.2,0.3]], det=-1.65; "
               "both map unit square to parallelogram of area 1.65, opposite orientation.",
    "parameters": {
        "unit_square": "[0,1]x[0,1]",
        "A_positive": A_POS.tolist(),
        "A_negative": A_NEG.tolist(),
    },
    "evaluated_data": {
        "det_positive": float(np.linalg.det(A_POS)),
        "det_negative": float(np.linalg.det(A_NEG)),
        "columns_positive": {"a1": list(A_POS[:, 0]), "a2": list(A_POS[:, 1])},
        "columns_negative": {"a1": list(A_NEG[:, 0]), "a2": list(A_NEG[:, 1])},
    },
    "processing": "解析式与 numpy.linalg.det 核对；无随机采样。",
    "width_mm": 169, "height_mm": 70, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
