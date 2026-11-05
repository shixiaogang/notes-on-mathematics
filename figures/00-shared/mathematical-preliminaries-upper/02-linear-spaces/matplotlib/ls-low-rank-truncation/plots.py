"""教学图：低秩截断（SVD 秩一近似）的几何与误差。

解析式固定构造：A=[[2,0.5],[0.5,1]]（对称正定），σ1≈2.207，σ2≈0.793。
左 panel：单位圆（灰）经 A 变成椭圆（蓝）；秩一近似 A1=σ1 v1 v1ᵀ 把单位圆
  压扁成沿 v1、长 σ1 的一条线段（黄），误差即椭圆与线段之差。
右 panel：奇异值条形图——保留 σ1、舍弃 σ2。
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

A = np.array([[2., 0.5], [0.5, 1.]])
LAM, V = np.linalg.eigh(A)
S1, S2 = LAM[1], LAM[0]
V1 = V[:, 1]


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, (a, b) = plt.subplots(1, 2, figsize=(169 / 25.4, 66 / 25.4))

# ---- 左 panel：椭圆 vs 秩一线段 ----
th = np.linspace(0, 2 * np.pi, 200)
circle = np.array([np.cos(th), np.sin(th)])
ell = V @ np.diag(LAM) @ circle
a.plot(np.cos(th), np.sin(th), color=MUTED, lw=.9)
a.fill(ell[0], ell[1], color=BLUE_FILL, zorder=1)
a.plot(ell[0], ell[1], color=BLUE, lw=1.2, zorder=3)
a.plot([-S1 * V1[0], S1 * V1[0]], [-S1 * V1[1], S1 * V1[1]],
       color=YELLOW, lw=3.0, solid_capstyle="round", zorder=4)
a.text(-2.05, 1.25, "$A$ 的椭圆像", fontsize=8, color=BLUE)
a.text(0.35, 1.05, "秩一近似：压扁成主轴线段", fontsize=7.5, color=YELLOW)
a.set_title("(a) 单位圆 → 椭圆 vs 秩一线段", fontsize=8)
a.set(xlim=(-2.6, 2.6), ylim=(-1.7, 1.7), xticks=range(-2, 3), yticks=range(-1, 2))
a.set_aspect("equal")
a.grid(True)

# ---- 右 panel：奇异值条形 ----
bars = b.bar(["$\\sigma_1\\approx2.21$", "$\\sigma_2\\approx0.79$"],
             [S1, S2], width=.5, color=[BLUE, GRID], edgecolor=INK, linewidth=.5)
b.annotate("保留", xy=(0, S1), xytext=(0, S1 + .25),
           fontsize=8, color=BLUE, ha="center")
b.annotate("舍弃", xy=(1, S2), xytext=(1, S2 + .35),
           fontsize=8, color=MUTED, ha="center",
           arrowprops=dict(arrowstyle="->", color=MUTED, lw=.6))
b.set_ylabel("奇异值大小")
b.set_ylim(0, 2.9)
b.set_title("(b) 奇异值谱：截断小奇异值", fontsize=8)
b.grid(True, axis="y")
b.grid(False, axis="x")

finalize(fig)
fig.tight_layout()
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "截断小奇异值在几何上把椭圆变成了什么？误差在哪里？",
    "formula": "A=[[2,0.5],[0.5,1]]; σ1=λ1=(3+√2)/2≈2.207, σ2=λ2=(3-√2)/2≈0.793; "
               "rank-1 A1=σ1 v1 v1ᵀ，A1·单位圆=线段 [-σ1v1, σ1v1]；"
               "||A-A1||_2=σ2≈0.793。",
    "parameters": {
        "A": A.tolist(),
        "sigma_values": list(LAM[::-1]),
        "truncation": "保留 σ1，舍弃 σ2",
    },
    "evaluated_data": {
        "sigma1": float(S1), "sigma2": float(S2),
        "operator_norm_error": float(S2),
    },
    "processing": "eigh 为固定解析矩阵的精确对角化；无随机采样。",
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
