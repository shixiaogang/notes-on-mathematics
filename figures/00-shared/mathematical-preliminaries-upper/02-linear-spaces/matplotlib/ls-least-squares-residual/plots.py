"""教学图：最小二乘残差垂直于列空间（三维透视示意）。

解析式固定构造：A=[[1,0],[0,1],[1,1]]，列 a1=(1,0,1)、a2=(0,1,1)，
列空间 Col(A) 是过原点的平面。b=(2,3,2)，最小二乘解 x̂=(1,2)，
投影 Ax̂=a1+2a2=(1,2,3)，残差 r=b-Ax̂=(1,1,-1)，与 a1、a2 均正交。
无随机数，不调用 LaTeX。从任意目录运行：python3 plots.py [--only ...]
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
BLUE_FILL, RED_FILL, GREEN_FILL, YELLOW_FILL = "#E5EAF0", "#F0E5E6", "#E8EEE9", "#F1ECDD"
CN_MAIN, CN_AUX, EN = "Source Han Sans SC", "LXGW WenKai", "Fira Math"

matplotlib.rcParams.update({
    "font.family": [EN, CN_MAIN], "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": EN, "mathtext.it": EN,
    "mathtext.bf": EN, "mathtext.sf": EN,
    "axes.unicode_minus": False, "text.color": INK, "axes.labelcolor": INK,
    "axes.edgecolor": STROKE, "axes.linewidth": .75,
    "xtick.color": STROKE, "ytick.color": STROKE,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 3, "svg.fonttype": "path",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only

A1 = np.array([1., 0., 1.])
A2 = np.array([0., 1., 1.])
B = np.array([2., 3., 2.])
XHAT = np.array([1., 2.])
AXHAT = XHAT[0] * A1 + XHAT[1] * A2         # (1,2,3)
R = B - AXHAT                               # (1,1,-1)


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig = plt.figure(figsize=(112 / 25.4, 82 / 25.4))
ax = fig.add_subplot(111, projection="3d")

# 列空间平面：s*a1 + t*a2
s = np.linspace(-0.6, 1.6, 2)
tt = np.linspace(-0.6, 1.6, 2)
S, T = np.meshgrid(s, tt)
Xp = S * A1[0] + T * A2[0]
Yp = S * A1[1] + T * A2[1]
Zp = S * A1[2] + T * A2[2]
ax.plot_surface(Xp, Yp, Zp, color=BLUE_FILL, edgecolor=BLUE, lw=.6,
                alpha=.9, zorder=1)

ax.quiver(0, 0, 0, *A1, color=BLUE, lw=1.1, arrow_length_ratio=.12)
ax.quiver(0, 0, 0, *A2, color=GREEN, lw=1.1, arrow_length_ratio=.12)
ax.scatter(*B, color=BLUE, s=22, edgecolor=INK, linewidth=.5, zorder=5)
ax.scatter(*AXHAT, color=GREEN, s=22, edgecolor=INK, linewidth=.5, zorder=5)
ax.plot([B[0], AXHAT[0]], [B[1], AXHAT[1]], [B[2], AXHAT[2]],
        color=RED, lw=1.1, ls="--", zorder=4)
ax.quiver(*AXHAT, *R, color=RED, lw=1.2, arrow_length_ratio=.15)

ax.text(A1[0] + .12, A1[1], A1[2] + .15, "$a_1$", fontsize=8, color=BLUE)
ax.text(A2[0], A2[1] + .12, A2[2] + .15, "$a_2$", fontsize=8, color=GREEN)
ax.text(B[0] + .12, B[1] + .05, B[2] + .1, "$b$", fontsize=8, color=BLUE)
ax.text(AXHAT[0] - .55, AXHAT[1] - .05, AXHAT[2] + .12, "$A\\hat x$", fontsize=8, color=GREEN)
ax.text(1.55, 1.9, 3.6, "$r=b-A\\hat x$", fontsize=8, color=RED)
ax.text(-0.55, -0.55, 2.6, "$r\\perp\\mathrm{Col}(A)$", fontsize=7.5, color=RED)

ax.set_title("最小二乘：残差垂直于列空间平面", fontsize=8)
ax.set(xlim=(-.6, 2.6), ylim=(-.6, 3.4), zlim=(-.6, 4.2))
ax.set(xticks=[0, 1, 2], yticks=[0, 1, 2, 3], zticks=[0, 1, 2, 3, 4])
ax.view_init(elev=18, azim=-62)
ax.grid(True)

finalize(fig)
fig.tight_layout()
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "最小二乘解处的残差为什么垂直于整个列空间？",
    "formula": "A=[a1,a2], a1=(1,0,1), a2=(0,1,1); b=(2,3,2); x̂=(1,2); "
               "Ax̂=a1+2a2=(1,2,3); r=b-Ax̂=(1,1,-1); r·a1=0, r·a2=0。",
    "parameters": {
        "columns": {"a1": list(A1), "a2": list(A2)},
        "b": list(B), "xhat": list(XHAT),
        "projection_Axhat": list(AXHAT), "residual_r": list(R),
    },
    "evaluated_data": {
        "r_dot_a1": float(R @ A1), "r_dot_a2": float(R @ A2),
        "residual_norm": float(np.linalg.norm(R)),
    },
    "processing": "直接求值；三维视角 elev=18°, azim=-62°；无随机采样。",
    "width_mm": 112, "height_mm": 82, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
