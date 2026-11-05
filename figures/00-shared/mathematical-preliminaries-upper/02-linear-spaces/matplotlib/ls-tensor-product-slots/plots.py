"""教学图：两个向量的张量积 u⊗v 排成 2×3 数组。

固定构造：u=(1,2)^T ∈ R^2，v=(3,-1,2)^T ∈ R^3，
(u⊗v)_{i,j}=u_i v_j = [[3,-1,2],[6,-2,4]]。
图中标出第2行 = u_2 v^T、第3列 = v_3 u。
u 的前两个分量与 v 的前两个分量取自正文示例 x=(1,2)^T、y=(3,-1)^T。
无随机数，不调用 LaTeX。
从任意目录运行：python plots.py [--only ls-tensor-product-slots]
"""
from pathlib import Path
import argparse
import json
import sys

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in HERE.parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

from plot_style import (BLUE, BLUE_FILL, GREEN, GREEN_FILL, STROKE,  # noqa: E402
                        configure, prepare_figure, style_record)

configure()

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
parser.parse_args()

U = [1, 2]
V = [3, -1, 2]
T = [[ui * vj for vj in V] for ui in U]  # [[3,-1,2],[6,-2,4]]
ROW, COL = 1, 2  # 0-based：标出第2行与第3列

WIDTH_MM, HEIGHT_MM = 112, 32
C = 1.0  # 单元格高度（数据坐标）
CW = 1.2  # 结果网格的单元格宽度


def num(x):
    return f"${x}$" if x >= 0 else f"${{-{abs(x)}}}$"


fig = plt.figure(figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4))
ax = fig.add_axes([0, 0, 1, 1])
# 数据单位 1 = 7 mm，横纵比例一致
UNIT_MM = 7.0
ax.set_xlim(0, WIDTH_MM / UNIT_MM)
ax.set_ylim(0, HEIGHT_MM / UNIT_MM)
ax.axis("off")

y_top, y_bot = 1.95, 0.95          # 第1行、第2行单元格底边
y_mid = y_bot + C                  # 两行分界
y_title = y_top + C + .55          # 各部分名称的基线

# ---- 左：u（竖排两格，蓝）----
xu = 1.3
for i, ui in enumerate(U):
    y = y_top - i * C
    ax.add_patch(Rectangle((xu, y), C, C, facecolor=BLUE_FILL, edgecolor=BLUE, lw=.8))
    ax.text(xu + C / 2, y + C / 2, num(ui), ha="center", va="center", fontsize=8)
    ax.text(xu - .15, y + C / 2, f"$u_{i + 1}$", ha="right", va="center",
            fontsize=7.5, color=BLUE)
ax.text(xu + C / 2, y_title, r"$\mathbfit{u}\in\mathbb{R}^2$",
        ha="center", va="bottom", fontsize=8)

ax.text(xu + C + .5, y_mid, r"$\otimes$", ha="center", va="center", fontsize=10, color=STROKE)

# ---- 中：v（横排三格，绿），垂直居中于两行分界 ----
xv = xu + C + 1.0
yv = y_mid - C / 2
for j, vj in enumerate(V):
    x = xv + j * C
    ax.add_patch(Rectangle((x, yv), C, C, facecolor=GREEN_FILL, edgecolor=GREEN, lw=.8))
    ax.text(x + C / 2, yv + C / 2, num(vj), ha="center", va="center", fontsize=8)
    ax.text(x + C / 2, yv - .12, f"$v_{j + 1}$", ha="center", va="top",
            fontsize=7.5, color=GREEN)
ax.text(xv + 1.5 * C, y_title, r"$\mathbfit{v}\in\mathbb{R}^3$",
        ha="center", va="bottom", fontsize=8)

ax.text(xv + 3 * C + .5, y_mid, r"$=$", ha="center", va="center", fontsize=10, color=STROKE)

# ---- 右：u⊗v（2×3 网格），左侧标 u_i、上方标 v_j ----
xg = xv + 3 * C + 1.35
gw = 3 * CW
for i in range(2):
    y = y_top - i * C
    ax.text(xg - .15, y + C / 2, f"$u_{i + 1}$", ha="right", va="center",
            fontsize=7.5, color=BLUE)
    for j in range(3):
        x = xg + j * CW
        ax.add_patch(Rectangle((x, y), CW, C, facecolor="white", edgecolor=STROKE, lw=.6))
        ax.text(x + CW / 2, y + C / 2, num(T[i][j]), ha="center", va="center", fontsize=8)
for j in range(3):
    ax.text(xg + j * CW + CW / 2, y_top + C + .1, f"$v_{j + 1}$", ha="center", va="bottom",
            fontsize=7.5, color=GREEN)
ax.text(xg + gw / 2, y_title, r"$\mathbfit{u}\otimes\mathbfit{v}$，元素 $u_i v_j$",
        ha="center", va="bottom", fontsize=8)

# 第2行：蓝色实线框，右侧注 u_2 v^T
pad = .07
ax.add_patch(FancyBboxPatch((xg + pad, y_bot + pad), gw - 2 * pad, C - 2 * pad,
                            boxstyle="round,pad=0,rounding_size=0.12",
                            facecolor="none", edgecolor=BLUE, lw=1.1))
ax.text(xg + gw + .25, y_bot + C / 2, r"第2行：$u_2\,\mathbfit{v}^{\top}$",
        ha="left", va="center", fontsize=8, color=BLUE)

# 第3列：绿色虚线框，右侧注 v_3 u
xc = xg + COL * CW
ax.add_patch(FancyBboxPatch((xc + 2 * pad, y_bot + 2 * pad), CW - 4 * pad, 2 * C - 4 * pad,
                            boxstyle="round,pad=0,rounding_size=0.12",
                            facecolor="none", edgecolor=GREEN, lw=1.1, ls=(0, (3, 1.6))))
ax.text(xc + CW / 2, y_bot - .12, r"第3列：$v_3\,\mathbfit{u}$",
        ha="center", va="top", fontsize=8, color=GREEN)

prepare_figure(fig)
for ext, kw in (("pdf", {}), ("svg", {}), ("png", {"dpi": 300})):
    fig.savefig(HERE / f"{NAME}.{ext}", **kw)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "两个向量的全部两两乘积怎样排成一个二阶数组？它的行与列分别是哪个因子的倍数？",
    "formula": "(u⊗v)_{i,j}=u_i v_j with u=(1,2)^T, v=(3,-1,2)^T; "
               "row 2 = u_2 v^T = 2·(3,-1,2); column 3 = v_3 u = 2·(1,2)^T.",
    "consistency": "u 的分量与正文示例 ex:ls-tensor-product-two-vectors 的 x=(1,2)^T 相同，"
                   "v 的前两个分量与 y=(3,-1)^T 相同；图注 fig:ls-tensor-product-slots 给出同一组数。",
    "parameters": {"u": U, "v": V},
    "evaluated_data": {"tensor_product": T, "highlighted_row": ROW + 1, "highlighted_column": COL + 1},
    "processing": "逐分量相乘；无随机采样。",
    "layout": {"width_mm": WIDTH_MM, "height_mm": HEIGHT_MM, "text_reference_width_mm": 112,
               "scale": 1.0, "label_pt": {"main": 8, "index": 7.5},
               "colors": {"u_and_row": BLUE, "v_and_column": GREEN}},
    "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
    "revision": "2026-10-31 重绘：原图为 2×2 基槽位网格与另一组 2×2 外积，与图注不符；"
                "改为 u∈R²、v∈R³ 与 2×3 张量积，标出行、列的倍数关系，数学标注改用 Fira Math 数学字体。",
}
(HERE / "sources.json").write_text(
    json.dumps({"style": style_record(), "figures": {NAME: record}},
               ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
