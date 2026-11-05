"""教学图：两个过原点子空间的主夹角与投影残差。

固定构造：U = span{(1,0)}（x 轴），V = span{v}，v=(cos40°, sin40°)。
主夹角 θ 是两子空间间最小夹角，cosθ=|⟨u,v⟩|/(‖u‖‖v‖)；
v 在 U 上的正交投影 p，残差长度 ‖v‖sinθ 即“投影不掉”的部分。
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
from matplotlib.patches import Arc
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW, RED = "#7188A3", "#829C8B", "#B4A16F", "#A7787D"
INK, MUTED, GRID, STROKE = "#3B4252", "#6B7280", "#D8DCE2", "#4C4D4F"
BLUE_FILL, GREEN_FILL = "#E5EAF0", "#E8EEE9"
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

THETA = np.deg2rad(40.)
U_HAT = np.array([1., 0.])
V = np.array([np.cos(THETA), np.sin(THETA)])
P = np.array([V[0], 0.])  # v 在 U 上的正交投影


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 62 / 25.4))

# 子空间直线
ax.plot([-0.35, 1.45], [0, 0], color=BLUE, lw=1.4, zorder=2)
ax.plot([-0.3 * V[0], 1.35 * V[0]], [-0.3 * V[1], 1.35 * V[1]], color=GREEN, lw=1.4, zorder=2)

# v 与其投影
ax.annotate("", xy=V, xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.1))
ax.plot(*P, "o", ms=4, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
ax.plot([P[0], V[0]], [P[1], V[1]], color=MUTED, lw=.7, ls="--", zorder=3)
# 直角标记
ax.plot([P[0], P[0] + .06], [P[1], P[1] + .06], color=MUTED, lw=.6)
ax.plot([P[0], P[0] + .06], [P[1] + .06, P[1] + .06], color=MUTED, lw=.6)

# 夹角弧
ax.add_patch(Arc((0, 0), .9, .9, angle=0, theta1=0, theta2=40, color=RED, lw=1.1))
ax.text(.62, .13, "$\\theta=40°$", fontsize=8, color=RED)

ax.text(1.30, .04, "$U$", fontsize=8, color=BLUE)
ax.text(1.30 * V[0] + .04, 1.30 * V[1] + .02, "$V$", fontsize=8, color=GREEN)
ax.text(V[0] - .22, V[1] + .10, "$v$", fontsize=8, color=GREEN)
ax.text(P[0] - .12, P[1] - .09, "$p=(v\\cdot\\hat u)\\hat u$", fontsize=7.5, color=YELLOW)
ax.text(V[0] + .03, (V[1]) / 2, "$\\|v\\|\\sin\\theta$", fontsize=7.5, color=MUTED)
ax.text(-.32, .95,
        "$\\cos\\theta=\\frac{|\\langle u,v\\rangle|}{\\|u\\|\\|v\\|}$\n$\\theta$ 越小，两子空间越接近重合",
        fontsize=7.5)
ax.set_title("两直线子空间的主夹角与正交投影残差", fontsize=8)
ax.set(xlim=(-.45, 1.55), ylim=(-.2, 1.1), xticks=range(0, 2), yticks=range(0, 2))
ax.set_aspect("equal"); ax.grid(True)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "两个过原点的子空间“有多近”？投影后还剩多少？",
    "formula": "U=span{(1,0)}; V=span{v}, v=(cos40°,sin40°); "
               "cosθ=|<u,v>|/(‖u‖‖v‖)=cos40°; p=投影_U v=(v·û)û; 残差 ‖v−p‖=‖v‖sinθ。",
    "parameters": {
        "u_hat": [1., 0.], "v": [round(float(V[0]), 6), round(float(V[1]), 6)],
        "theta_deg": 40,
    },
    "evaluated_data": {
        "projection_p": [round(float(P[0]), 6), 0.],
        "cos_theta": round(float(np.cos(THETA)), 6),
        "sin_theta": round(float(np.sin(THETA)), 6),
        "residual_norm": round(float(np.sin(THETA)), 6),
    },
    "processing": "直接三角恒等式求值；无随机采样。",
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
