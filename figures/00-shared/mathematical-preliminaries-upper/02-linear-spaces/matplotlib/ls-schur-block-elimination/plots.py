"""教学图：Schur 补的 2×2 分块消元过程。

固定 M=[[2,1],[1,2]]，右端 b=(1,3)。分块 A=2, B=C=1, D=2；
用可逆的 A 消去 C，右下角残留 Schur 补 S=D−CA⁻¹B=3/2；
约化系统 (3/2)x2=3−1/2=5/2，得 x2=5/3，回代 x1=(1−x2)/2=−1/3。
全部数学走 mathtext。无随机数，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ...]
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW, RED = "#7188A3", "#829C8B", "#B4A16F", "#A7787D"
INK, MUTED, GRID, STROKE = "#3B4252", "#6B7280", "#D8DCE2", "#4C4D4F"
BLUE_FILL, YELLOW_FILL = "#E5EAF0", "#F1ECDD"
CN_MAIN, CN_AUX, EN = "Source Han Sans SC", "LXGW WenKai", "Fira Math"

matplotlib.rcParams.update({
    "font.family": [EN, CN_MAIN], "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": EN, "mathtext.it": EN,
    "mathtext.bf": EN, "mathtext.sf": EN,
    "axes.unicode_minus": False, "text.color": INK,
    "pdf.fonttype": 3, "svg.fonttype": "path",
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only

M = np.array([[2., 1.], [1., 2.]])
A, B, C, D = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
S = D - C * A**(-1) * B                      # 3/2
X2 = (3 - C * A**(-1) * 1) / S               # 5/3
X1 = (1 - X2) / 2                            # -1/3


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig = plt.figure(figsize=(169 / 25.4, 56 / 25.4))
gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 0.34, 1.75],
                      left=0.02, right=0.985, top=0.90, bottom=0.08, wspace=0.25)
axM = fig.add_subplot(gs[0, 0])
axStep = fig.add_subplot(gs[0, 1])
axEq = fig.add_subplot(gs[0, 2])

# ---- 左：2×2 分块矩阵 ----
cells = [(0, 0, "2", BLUE_FILL), (0, 1, "1", "white"),
         (1, 0, "1", YELLOW_FILL), (1, 1, "2", "white")]
for r, c, txt, fc in cells:
    axM.add_patch(plt.Rectangle((c, 1 - r), 1, 1, facecolor=fc,
                                edgecolor=STROKE, lw=.8))
    axM.text(c + .5, 1 - r + .5, txt, ha="center", va="center", fontsize=11)
# 块名放在格内角落，不与数字重叠（第一行格子 y∈[1,2]，第二行 y∈[0,1]）
axM.text(0.04, 1.94, "$A$", fontsize=7.5, color=BLUE, ha="left", va="top")
axM.text(1.96, 1.94, "$B$", fontsize=7.5, color=INK, ha="right", va="top")
axM.text(0.04, 0.06, "$C$", fontsize=7.5, color=YELLOW, ha="left", va="bottom")
axM.text(1.96, 0.06, "$D$", fontsize=7.5, color=INK, ha="right", va="bottom")
# 消元箭头：从 C 块指向 D 块
arr = FancyArrowPatch((0.62, 0.52), (1.38, 0.48),
                      connectionstyle="arc3,rad=-0.35",
                      arrowstyle="-|>", color=RED, lw=1.1,
                      mutation_scale=11)
axM.add_patch(arr)
axM.set_title("分块矩阵：$A$ 可逆，先消去 $C$", fontsize=8)
axM.set_xlim(-0.2, 2.2); axM.set_ylim(-0.45, 2.35)
axM.set_aspect("equal"); axM.axis("off")

# ---- 中：步骤箭头 ----
axStep.annotate("", xy=(0.95, 0.5), xytext=(0.05, 0.5),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
axStep.text(0.5, 0.68, "用 $A$", ha="center", fontsize=7.5, transform=axStep.transAxes)
axStep.text(0.5, 0.32, "消去 $C$", ha="center", fontsize=7.5, transform=axStep.transAxes)
axStep.axis("off")

# ---- 右：三行推导 ----
axEq.text(0.0, 0.78,
          r"$S=D-CA^{-1}B=2-1\cdot\frac{1}{2}\cdot1=\frac{3}{2}$",
          fontsize=8.5, transform=axEq.transAxes, color=BLUE)
axEq.text(0.0, 0.48,
          r"$\frac{3}{2}\,x_2=3-\frac{1}{2}\cdot1=\frac{5}{2}"
          r"\ \Rightarrow\ x_2=\frac{5}{3}$",
          fontsize=8.5, transform=axEq.transAxes, color=GREEN)
axEq.text(0.0, 0.18,
          r"回代 $x_1=\frac{1-x_2}{2}=-\frac{1}{3}$；"
          r"$\det M=3=2\cdot\frac{3}{2}$",
          fontsize=8, transform=axEq.transAxes, color=INK)
axEq.set_title("Schur 补约化系统", fontsize=8)
axEq.set_xlim(0, 1); axEq.set_ylim(0, 1); axEq.axis("off")

finalize(fig)
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "分块消元怎样把右下角残留写成 Schur 补 S=D−CA⁻¹B？",
    "formula": "M=[[2,1],[1,2]], b=(1,3); A=2,B=C=1,D=2; "
               "S=D-CA^{-1}B=3/2; (3/2)x2=5/2 => x2=5/3; x1=(1-x2)/2=-1/3; "
               "det M=3=det A*det S=2*3/2。",
    "parameters": {
        "M": M.tolist(), "b": [1, 3],
        "blocks": {"A": A, "B": B, "C": C, "D": D},
        "schur_complement_S": S, "x2": X2, "x1": X1,
    },
    "evaluated_data": {
        "det_M": float(np.linalg.det(M)),
        "detA_times_detS": A * S,
        "check_Mx": list(M @ np.array([X1, X2])),
    },
    "processing": "直接求值；无随机采样。",
    "width_mm": 169, "height_mm": 56, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
