"""教学图：对称矩阵微扰后椭圆（特征值/特征向量）的变化。

固定构造：A 特征值 2 与 0.5，主轴方向 20°；E=[[0.1,0.15],[0.15,-0.05]]。
椭圆 {x: x^T M x ≤ 1} 的半轴长 1/√λ；A 与 A+E 的椭圆叠加：轴长微变
（Weyl：|Δλ_i|≤‖E‖₂），轴方向微旋（转动幅度被谱隙 γ=λ1−λ2 牵制，
γ 大则方向稳）。
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
parser.add_argument("--only", default=NAME, choices=[NAME])
selection = parser.parse_args().only

TH = np.deg2rad(20.)
V1 = np.array([np.cos(TH), np.sin(TH)])
V2 = np.array([-np.sin(TH), np.cos(TH)])
A = 2. * np.outer(V1, V1) + 0.5 * np.outer(V2, V2)
E = np.array([[0.1, 0.15], [0.15, -0.05]])
AP = A + E
L1, L2 = 2.0, 0.5
GAMMA = L1 - L2
ENORM = float(np.linalg.norm(E, 2))
W1, VV1 = np.linalg.eigh(AP)  # 升序


def ellipse_pts(M, t):
    lam, Vv = np.linalg.eigh(M)
    pts = (1. / np.sqrt(lam[0])) * np.outer(Vv[:, 0], np.cos(t)) \
        + (1. / np.sqrt(lam[1])) * np.outer(Vv[:, 1], np.sin(t))
    return pts


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 62 / 25.4))
t = np.linspace(0, 2 * np.pi, 300)
p0 = ellipse_pts(A, t)
p1 = ellipse_pts(AP, t)
ax.fill(p0[0], p0[1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1, zorder=2)
ax.plot(p1[0], p1[1], color=RED, lw=1.1, ls="--", zorder=3)
# 轴箭头
ax.annotate("", xy=(1 / np.sqrt(LAM) if False else 0.707 * V1[0], 0.707 * V1[1]),
            xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=.9))
ax.annotate("", xy=(1.414 * V2[0], 1.414 * V2[1]), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=.9))
ax.text(-2.05, -1.75,
        "实线 $A$，虚线 $A+E$\n$|\\Delta\\lambda|\\leq\\|E\\|_2=%.3f$\n谱隙 $\\gamma=\\lambda_1-\\lambda_2=%.1f$：\n隙越大，轴方向越不易被微扰转动"
        % (ENORM, GAMMA), fontsize=7.5)
ax.set_title("对称矩阵微扰：椭圆轴微旋、半轴微变", fontsize=8)
ax.set(xlim=(-2.1, 1.9), ylim=(-1.9, 2.0), xticks=range(-2, 2), yticks=range(-1, 3))
ax.set_aspect("equal"); ax.grid(True)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "对称矩阵加一个小扰动，特征值和特征向量会变多少？",
    "formula": "椭圆{x: x^T M x≤1}半轴长 1/√λ。A 的 λ=2,0.5；E=[[.1,.15],[.15,-.05]]。"
               "Weyl: |Δλ_i|≤‖E‖₂=%.4f；谱隙 γ=1.5 越大，特征向量方向越稳。" % ENORM,
    "parameters": {"eigenvalues_A": [2.0, 0.5], "axis_angle_deg": 20,
                   "E": [[0.1, 0.15], [0.15, -0.05]]},
    "evaluated_data": {
        "norm_E": round(ENORM, 6),
        "eigenvalues_A": [round(float(v), 6) for v in sorted(W1, reverse=True)] if False
        else [2.0, 0.5],
        "eigenvalues_ApE": [round(float(v), 6) for v in sorted(W1, reverse=True)],
        "gamma": GAMMA,
    },
    "processing": "np.linalg.eigh 精确求值；无随机采样。",
    "width_mm": 112, "height_mm": 62, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
