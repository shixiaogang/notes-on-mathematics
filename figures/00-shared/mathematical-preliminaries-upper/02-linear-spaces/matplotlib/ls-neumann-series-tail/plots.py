"""教学图：Neumann 级数的尾界与真实残差。

固定构造：T=[[0.7,0.6],[0,0.1]]，q=‖T‖₂<1，
(I−T)^{-1}=Σ_{k≥0}T^k。部分和 S_n=Σ_{k=0}^n T^k 的真实残差
R_n=(I−T)^{-1}−S_n=T^{n+1}(I−T)^{-1} 精确计算；
几何尾界 ‖R_n‖≤q^{n+1}/(1−q) 对照。n=0..15 半对数。
无随机采样，不调用 LaTeX。从任意目录运行：python3 plots.py [--only ...]
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

T = np.array([[0.7, 0.6], [0., 0.1]])
Q = float(np.linalg.norm(T, 2))
INV = np.linalg.inv(np.eye(2) - T)
NS = np.arange(0, 16)
REAL = np.array([np.linalg.norm(INV - sum(np.linalg.matrix_power(T, k) for k in range(n + 1)), 2)
                 for n in NS])
BOUND = Q ** (NS + 1) / (1 - Q)


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 58 / 25.4))
ax.semilogy(NS, BOUND, color=RED, lw=1.0, ls="--", marker="s", ms=3,
            label="尾界 $q^{n+1}/(1-q)$，$q=\\|T\\|_2=%.2f$" % Q)
ax.semilogy(NS, REAL, color=BLUE, lw=1.2, marker="o", ms=3,
            label="真实残差 $\\|(I-T)^{-1}-S_n\\|_2$")
ax.set_xlabel("部分和步数 $n$", fontsize=8)
ax.set_ylabel("尾（对数轴）", fontsize=8)
ax.set_title("Neumann 级数：尾界随 $q^{n+1}$ 几何衰减", fontsize=8)
ax.set(xticks=range(0, 16, 2), ylim=(1e-3, 20))
ax.grid(True, which="both")
ax.legend(loc="lower left", fontsize=7.5, frameon=False)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "Neumann 级数截断后，误差有多大？尾界是紧的吗？",
    "formula": "(I-T)^{-1}=Σ_{k≥0}T^k；R_n=(I-T)^{-1}-S_n=T^{n+1}(I-T)^{-1}；"
               "‖R_n‖≤q^{n+1}/(1-q)，q=‖T‖₂=%.4f。" % Q,
    "parameters": {"T": [[0.7, 0.6], [0, 0.1]], "grid": "n=0..15"},
    "evaluated_data": {
        "q": round(Q, 6),
        "real_residual": [round(float(v), 6) for v in REAL],
        "bound": [round(float(v), 6) for v in BOUND],
    },
    "processing": "级数部分和与逆矩阵精确相减求范数；无随机采样。",
    "width_mm": 112, "height_mm": 58, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
