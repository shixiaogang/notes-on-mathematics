"""教学图：固定迭代误差衰减由谱半径决定。

固定构造：e_{k+1}=T e_k，e0=(1,0,0)，‖e0‖=1；
三个标量迭代矩阵 T=ρ I（正规），ρ=0.5（快）、0.9（慢）、1.1（发散），
k=0..20 精确 ‖e_k‖=ρ^k。半对数坐标下分别为下降、慢降、上升直线。
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

KS = np.arange(0, 21)
CASES = [(0.5, "ρ(T)=0.5：快收敛", BLUE, "o"),
         (0.9, "ρ(T)=0.9：慢收敛", GREEN, "s"),
         (1.1, "ρ(T)=1.1>1：发散", RED, "^")]


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(169 / 25.4, 60 / 25.4))
for rho, label, color, mk in CASES:
    ax.semilogy(KS, rho ** KS, color=color, lw=1.1, marker=mk, ms=3,
                markevery=2, label=label)
ax.axhline(1, color=MUTED, lw=.5, ls=":")
ax.text(.6, 2.6, "$\\|e_0\\|=1$", fontsize=7.5, color=MUTED)
ax.set_xlabel("迭代步数 $k$", fontsize=8)
ax.set_ylabel("误差范数 $\\|e_k\\|$（对数轴）", fontsize=8)
ax.set_title("固定迭代 $e_{k+1}=Te_k$：谱半径决定收敛与否与快慢", fontsize=8)
ax.set(xticks=range(0, 21, 2), ylim=(3e-5, 12))
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
    "reader_question": "为什么说迭代收敛当且仅当谱半径 ρ(T)<1？",
    "formula": "e_k=T^k e0；正规 T=ρI 时 ‖e_k‖=ρ^k（e0 单位向量）。ρ<1 单调衰减，ρ>1 指数增长。",
    "parameters": {"grid": "k=0..20", "e0_norm": 1.0,
                   "cases": [{"rho": r, "label": l} for r, l, _, _ in CASES]},
    "evaluated_data": {
        "norm_0.5": [round(float(v), 6) for v in 0.5 ** KS],
        "norm_0.9": [round(float(v), 6) for v in 0.9 ** KS],
        "norm_1.1": [round(float(v), 6) for v in 1.1 ** KS],
    },
    "processing": "ρ^k 直接求值；无随机采样。",
    "width_mm": 169, "height_mm": 60, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
