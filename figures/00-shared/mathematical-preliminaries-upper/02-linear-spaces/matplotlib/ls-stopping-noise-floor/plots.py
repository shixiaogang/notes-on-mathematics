"""教学图：迭代误差的三段——几何下降、噪声地板、过犹不及。

固定构造：含噪递推 e_{k+1}=q e_k + δ，q=0.7，δ=0.05，e0=1，k=0..30。
精确递推：前期按 q^k 几何下降，稳态收敛到地板 δ/(1−q)=0.1667；
继续迭代误差不再下降。水平虚线为停止阈值 0.20——早停错过收敛段，
晚停撞上地板。无随机采样（扰动为固定常数），不调用 LaTeX。
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

Q, DELTA, E0 = 0.7, 0.05, 1.0
KS = np.arange(0, 31)
E = np.empty(len(KS)); E[0] = E0
for k in range(1, len(KS)):
    E[k] = Q * E[k - 1] + DELTA
FLOOR = DELTA / (1 - Q)
THRESH = 0.20


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(169 / 25.4, 62 / 25.4))
ax.semilogy(KS, E, color=BLUE, lw=1.2, marker="o", ms=3, markevery=1,
            label="误差 $\\|e_k\\|$")
ax.axhline(FLOOR, color=RED, lw=.9, ls="--")
ax.plot([24.5, 24.5], [FLOOR, 0.132], color=RED, lw=.5)
ax.text(22.3, 0.118, "噪声地板 $\\delta/(1-q)=%.3f$" % FLOOR, fontsize=7.5, color=RED)
ax.axhline(THRESH, color=GREEN, lw=.8, ls=":")
ax.text(23.5, THRESH * 1.18, "停止阈值 0.20", fontsize=7.5, color=GREEN)
ax.annotate("", xy=(5.2, 0.42), xytext=(1.5, 0.42),
            arrowprops=dict(arrowstyle="-|>", color=INK, lw=.7))
ax.text(3.8, 0.78, "几何下降段", fontsize=7.5, color=INK)
ax.text(12.5, 0.112, "继续迭代：误差触底不再下降", fontsize=7.5, color=RED)
ax.set_xlabel("迭代步数 $k$", fontsize=8)
ax.set_ylabel("误差范数（对数轴）", fontsize=8)
ax.set_title("为什么要设停止准则：迭代误差的三段行为", fontsize=8)
ax.set(xticks=range(0, 31, 3), ylim=(0.1, 2))
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
    "reader_question": "迭代到什么时候该停？继续迭代为什么不再变准？",
    "formula": "e_{k+1}=0.7 e_k+0.05, e0=1；稳态地板 δ/(1−q)=0.05/0.3=0.1667。"
               "阈值 0.20 与曲线交点约在 k=9；之后误差被地板锁定。",
    "parameters": {"q": Q, "delta": DELTA, "e0": E0, "grid": "k=0..30",
                   "threshold": THRESH},
    "evaluated_data": {
        "errors": [round(float(v), 6) for v in E],
        "floor": round(FLOOR, 6),
        "crossing_k_approx": 9,
    },
    "processing": "固定常数递推精确求值；无随机采样。",
    "width_mm": 169, "height_mm": 62, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
