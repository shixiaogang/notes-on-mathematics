"""教学图：非正规 Jordan 块的幂范数先放大再衰减。

固定构造：J=[[λ,1],[0,λ]]，λ=0.5，ρ(J)=0.5<1。
J^k=λ^k I + k λ^{k-1} N，N=[[0,1],[0,0]]；k=0..25 精确计算 ‖J^k‖₂。
对照正规情形 ρ^k（对数轴上的直线）。ρ<1 不能排除先放大：k=1 时范数
从 1 升到约 1.46，随后才衰减。本图聚焦 Jordan 块本身的可复算曲线，
不与旧图 ch06-transient-growth 的连乘瞬态叙事重复。
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

LAM = 0.5
J = np.array([[LAM, 1.], [0., LAM]])
KS = np.arange(0, 26)
NORMS = np.array([np.linalg.norm(np.linalg.matrix_power(J, k), 2) for k in KS])
RHO = LAM ** KS
K_PEAK = int(np.argmax(NORMS))
V_PEAK = float(NORMS[K_PEAK])


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(169 / 25.4, 62 / 25.4))
ax.semilogy(KS, NORMS, color=BLUE, lw=1.2, marker="o", ms=3, markevery=1,
            label="$\\|J^k\\|_2$（非正规 Jordan 块）")
ax.semilogy(KS, RHO, color=RED, lw=1.0, ls="--", label="正规对照 $\\rho^k=0.5^k$")
ax.plot(K_PEAK, V_PEAK, "o", ms=6, mfc=YELLOW, mec=INK, mew=.6, zorder=5)
ax.annotate("峰值 $\\|J^{%d}\\|_2=%.3f$" % (K_PEAK, V_PEAK),
            xy=(K_PEAK, V_PEAK), xytext=(5.5, 1.9),
            fontsize=7.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=.6))
ax.text(12, .05, "旁注：$\\rho(J)=0.5<1$，\n但 $\\|J^k\\|$ 先升到峰值再衰减——\n$\\rho<1$ 不能排除先放大",
        fontsize=7.5, color=RED)
ax.set_xlabel("幂次 $k$", fontsize=8)
ax.set_ylabel("矩阵范数（对数轴）", fontsize=8)
ax.set_title("非正规矩阵的幂：谱半径小于 1 仍有瞬态放大", fontsize=8)
ax.set(xticks=range(0, 26, 2), ylim=(1e-5, 4))
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
    "reader_question": "ρ(J)=0.5<1，为什么 ‖J^k‖ 不单调下降？",
    "formula": "J=[[0.5,1],[0,0.5]]=λI+N；J^k=λ^k I + k λ^{k-1} N。ρ(J)=0.5。"
               "‖J^k‖₂ 精确计算于 k=0..25；峰值在 k=%d，值 %.4f；ρ^k 为正规对照。" % (K_PEAK, V_PEAK),
    "parameters": {"lambda": LAM, "grid": "k=0..25",
                    "J": [[0.5, 1], [0, 0.5]]},
    "evaluated_data": {
        "norms_Jk": [round(float(v), 6) for v in NORMS],
        "rho_k": [round(float(v), 6) for v in RHO],
        "peak": {"k": K_PEAK, "value": round(V_PEAK, 6)},
    },
    "processing": "np.linalg.matrix_power + svd 范数，精确求值；无随机采样。",
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
