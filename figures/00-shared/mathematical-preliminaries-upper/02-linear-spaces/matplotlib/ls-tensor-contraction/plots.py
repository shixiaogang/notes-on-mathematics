"""教学图：张量缩约（contraction）——沿两个槽位配对求和。

固定构造：2×2×2 张量 T，两个切片
T[:,:,0]=[[1,2],[3,4]]，T[:,:,1]=[[5,6],[7,8]]；
沿 (i,j) 对角槽缩约：C_k=Σ_i T[i,i,k]，得 C_0=1+4=5，C_1=5+8=13。
无随机数，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ls-tensor-contraction]
"""
from pathlib import Path
import argparse
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, YELLOW, RED = "#7188A3", "#B4A16F", "#A7787D"
INK, MUTED = "#3B4252", "#6B7280"
BLUE_FILL, YELLOW_FILL = "#E5EAF0", "#F1ECDD"
CN_MAIN, CN_AUX, EN = "Source Han Sans SC", "LXGW WenKai", "Fira Math"

matplotlib.rcParams.update({
    "font.family": [EN, CN_MAIN], "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": EN, "mathtext.it": EN,
    "mathtext.bf": EN, "mathtext.sf": EN,
    "axes.unicode_minus": False, "text.color": INK,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 3, "svg.fonttype": "path",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only

SLICES = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]  # T[:,:,k]
C = [SLICES[k][0][0] + SLICES[k][1][1] for k in range(2)]  # [5, 13]


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 84 / 25.4))
ax.set_xlim(-.5, 7.5); ax.set_ylim(-.6, 4.6); ax.axis("off")

for k in range(2):
    x0 = k * 3.6
    ax.text(x0 + 1, 3.9, f"$k={k}$ 切片", fontsize=8, ha="center", color=INK)
    for i in range(2):
        for j in range(2):
            diag = (i == j)
            ax.add_patch(Rectangle((x0 + j, 2 - i), 1, 1,
                                  facecolor=YELLOW_FILL if diag else BLUE_FILL,
                                  edgecolor=RED if diag else BLUE,
                                  lw=1.2 if diag else .8))
            ax.text(x0 + j + .5, 2 - i + .5, str(SLICES[k][i][j]),
                    fontsize=8, ha="center", va="center",
                    color=RED if diag else INK)
    # 求和箭头：沿网格边框走线，不穿过任何数字格。
    # 上对角格 (0,0)：先沿 y=2 边框向右，再沿 x=x0+1 边框向下；
    # 下对角格 (1,1)：从其下边缘 y=1 垂直向下。
    ax.annotate("", xy=(x0 + 1.0, .45), xytext=(x0 + .5, 2.0),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=.8,
                                connectionstyle="angle,angleA=0,angleB=-90,rad=0"))
    ax.annotate("", xy=(x0 + 1.3, .45), xytext=(x0 + 1.5, 1.0),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=.8))
    ax.text(x0 + 1, .05, f"$C_{k}=T[0,0,{k}]+T[1,1,{k}]={C[k]}$",
            fontsize=7.5, ha="center", color=RED)

ax.text(3.5, 4.4, "缩约：沿槽位 $(i,j)$ 把 $T[i,i,k]$ 配对求和，消去两个槽位",
        fontsize=8, ha="center", color=INK)
ax.text(3.5, -.45, "黄色格为被缩约的对角槽位；其余槽位保留为 $k$，结果是向量 $C=(5,13)$",
        fontsize=7.5, ha="center", color=MUTED)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "缩约到底消去了哪些槽位，又是怎样把它们“配对相加”的？",
    "formula": "T[:,:,0]=[[1,2],[3,4]], T[:,:,1]=[[5,6],[7,8]]; "
               "contract slots (i,j): C_k = sum_i T[i,i,k]; C_0=1+4=5, C_1=5+8=13.",
    "parameters": {"tensor_shape": [2, 2, 2], "contracted_axes": [0, 1], "kept_axis": 2},
    "evaluated_data": {"C": C},
    "processing": "逐分量求和；无随机采样。",
    "width_mm": 112, "height_mm": 84, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
