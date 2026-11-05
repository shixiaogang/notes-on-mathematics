"""教学图：Givens 旋转与 Householder 反射把向量映到坐标轴上。

解析式固定构造：x=(a,b)=(2,1)，r=||x||=sqrt(5)。
左：Givens 旋转 G=[[c,s],[-s,c]]，c=a/r，s=b/r，把 x 映到 (r,0)（第二分量旋到 0）。
右：Householder 反射 H=I-2vvᵀ/vᵀv，v=x-(r,0)，把 x 映到 (r,0)，反射轴为 v 的垂线。
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
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": STROKE, "ytick.color": STROKE,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "grid.color": GRID, "grid.linewidth": .4,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 3, "svg.fonttype": "path",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only

X = np.array([2., 1.])
R = np.linalg.norm(X)                       # sqrt(5)
C, S = X[0] / R, X[1] / R                   # Givens 余弦/正弦
GIV = np.array([[C, S], [-S, C]])
TARGET = GIV @ X                            # (r, 0)
V = X - np.array([R, 0.])                   # Householder 法向量
H = np.eye(2) - 2 * np.outer(V, V) / (V @ V)
REFLECTED = H @ X
PHI = np.degrees(np.arctan2(X[1], X[0]))    # x 的方位角，约 26.565°


def arrow(ax, p, q, color, lw=1.1, ls="-"):
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, ls=ls,
                                shrinkA=0, shrinkB=0))


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, (a, b) = plt.subplots(1, 2, figsize=(169 / 25.4, 66 / 25.4))

for ax in (a, b):
    ax.axhline(0, color=STROKE, lw=.75, zorder=1)
    ax.axvline(0, color=STROKE, lw=.75, zorder=1)

# ---- 左 panel：Givens 旋转 ----
th = np.linspace(0, np.radians(PHI), 60)
a.plot(R * np.cos(th), R * np.sin(th), color=MUTED, lw=.6, ls=":")
arrow(a, (0, 0), X, BLUE)
arrow(a, (0, 0), TARGET, GREEN)
a.plot(*X, "o", ms=4, mfc=BLUE, mec=INK, mew=.4, zorder=5)
a.text(2.08, 1.02, "$(a,b)=(2,1)$", fontsize=8, color=BLUE)
a.text(1.55, -0.30, "$(r,0)=(\\sqrt{5},0)$", fontsize=8, color=GREEN)
a.annotate("旋转角 $\\theta\\approx26.6°$", xy=(R * np.cos(np.radians(PHI / 2)),
          R * np.sin(np.radians(PHI / 2))), xytext=(0.55, 1.55),
          fontsize=7.5, color=MUTED,
          arrowprops=dict(arrowstyle="->", color=MUTED, lw=.6))
a.set_title("(a) Givens 旋转：把第二分量旋到 0", fontsize=8)
a.set(xlim=(-0.6, 3.3), ylim=(-0.9, 2.1), xticks=range(0, 4), yticks=range(0, 2))
a.set_aspect("equal")
a.grid(True)

# ---- 右 panel：Householder 反射 ----
alpha = np.radians(PHI / 2)                 # 反射轴方位角
d = np.array([np.cos(alpha), np.sin(alpha)])
b.plot([-1.6 * d[0], 2.9 * d[0]], [-1.6 * d[1], 2.9 * d[1]],
       color=MUTED, lw=.7, ls="--")
arrow(b, (0, 0), X, BLUE)
arrow(b, (0, 0), REFLECTED, GREEN)
b.plot(*X, "o", ms=4, mfc=BLUE, mec=INK, mew=.4, zorder=5)
b.text(2.08, 1.02, "$(a,b)=(2,1)$", fontsize=8, color=BLUE)
b.text(1.55, -0.30, "$Hx=(r,0)$", fontsize=8, color=GREEN)
b.text(1.55, 0.62, "反射轴（虚线）", fontsize=7.5, color=MUTED, rotation=PHI / 2)
b.set_title("(b) Householder 反射：映到 $(\\pm r,0)$", fontsize=8)
b.set(xlim=(-0.6, 3.3), ylim=(-0.9, 2.1), xticks=range(0, 4), yticks=range(0, 2))
b.set_aspect("equal")
b.grid(True)

finalize(fig)
fig.tight_layout()
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "Givens 旋转与 Householder 反射怎样把一个向量打到坐标轴上？",
    "formula": "x=(2,1), r=||x||=sqrt(5); Givens c=2/r, s=1/r, Gx=(r,0); "
               "Householder v=x-(r,0), H=I-2vvᵀ/vᵀv, Hx=(r,0)。",
    "parameters": {
        "vector_x": list(X), "r": R, "givens_c": C, "givens_s": S,
        "givens_matrix": GIV.tolist(), "target": list(TARGET),
        "householder_v": list(V), "householder_matrix": H.tolist(),
        "reflected": list(REFLECTED), "angle_deg": PHI,
    },
    "evaluated_data": {
        "norm_x": float(np.linalg.norm(X)),
        "givens_check": list(TARGET),
        "householder_check": list(REFLECTED),
        "reflection_axis_slope": float(np.tan(alpha)),
    },
    "processing": "直接求值；无平滑、无随机采样。",
    "width_mm": 169, "height_mm": 66, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
