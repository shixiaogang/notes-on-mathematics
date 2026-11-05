"""教学图：Kronecker 积 A⊗B 的块结构。

固定构造：A=[[1,2],[3,4]]，B=[[1,1],[0,1]]，
A⊗B 为 4×4：[[1,1,2,2],[0,1,0,2],[3,3,4,4],[0,3,0,4]]，
每个 2×2 小块为 a_{ij} B。无随机数，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ls-kronecker-block-structure]
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, INK, MUTED, STROKE = "#7188A3", "#3B4252", "#6B7280", "#4C4D4F"
BLUE_FILL = "#E5EAF0"
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

A = np.array([[1., 2.], [3., 4.]])
B = np.array([[1., 1.], [0., 1.]])
K = np.kron(A, B)


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 88 / 25.4))
cmap = LinearSegmentedColormap.from_list("block", ["#FFFFFF", BLUE_FILL, BLUE])
vmax = 4.0

for i in range(4):
    for j in range(4):
        v = K[i, j]
        ax.add_patch(Rectangle((j, 3 - i), 1, 1, facecolor=cmap(v / vmax),
                               edgecolor=STROKE, lw=.5))
        ax.text(j + .5, 3 - i + .5, f"{v:g}", fontsize=8,
                ha="center", va="center",
                color="white" if v >= 3 else INK)

# 块边界粗线
ax.plot([2, 2], [0, 4], color=INK, lw=1.4)
ax.plot([0, 4], [2, 2], color=INK, lw=1.4)

# 块标签（置于各块左上角，避开格内数字中心）
block_labels = [("$a_{11}B$", .08, 3.92), ("$a_{12}B$", 2.08, 3.92),
                ("$a_{21}B$", .08, 1.92), ("$a_{22}B$", 2.08, 1.92)]
for lab, cx, cy in block_labels:
    ax.text(cx, cy, lab, fontsize=6.5, ha="left", va="top", color=INK,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.0, alpha=.9))

ax.text(2, 4.35, "$A\\otimes B$，$A$=(1,2; 3,4)，$B$=(1,1; 0,1)",
        fontsize=8, ha="center", color=INK)
ax.text(2, -.35, "块 $(i,j)$ 整体等于标量 $a_{ij}$ 乘矩阵 $B$；色深编码数值大小",
        fontsize=7.5, ha="center", color=MUTED)
ax.set_xlim(-.2, 4.2); ax.set_ylim(-.6, 4.7); ax.axis("off")
ax.set_aspect("equal")

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "A⊗B 的每个块为什么正好是 a_{ij} 乘上整个 B？",
    "formula": "A=[[1,2],[3,4]], B=[[1,1],[0,1]]; "
               "A⊗B = [[1·B, 2·B],[3·B, 4·B]] = [[1,1,2,2],[0,1,0,2],[3,3,4,4],[0,3,0,4]].",
    "parameters": {"A": A.tolist(), "B": B.tolist()},
    "evaluated_data": {"kron_product": K.tolist()},
    "processing": "numpy.kron 直接求值；无随机采样。",
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
