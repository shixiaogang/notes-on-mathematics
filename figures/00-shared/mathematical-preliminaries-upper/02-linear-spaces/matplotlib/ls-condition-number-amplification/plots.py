"""教学图：条件数如何放大误差——良态与病态 2x2 系统对照。

固定构造：良态 A1=[[1,.2],[.2,1]]（σmax=1.2, σmin=0.8, κ=1.5）；
病态 A2=[[1,.85],[.85,1]]（σmax=1.85, σmin=0.15, κ≈12.3）。
左/右 panel 各画单位圆 z 与其像 A z（椭圆），轴长即奇异值；
误差放大 Δx=A^{-1}Δb：圆盘半径 ε 的最长半轴为 ε/σmin。
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
BLUE_FILL, RED_FILL = "#E5EAF0", "#F0E5E6"
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

A_GOOD = np.array([[1., .2], [.2, 1.]])
A_BAD = np.array([[1., .85], [.85, 1.]])
EPS = 0.1


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


def svd_info(A):
    s = np.linalg.svd(A, compute_uv=False)
    return s[0], s[-1], s[0] / s[-1]


def ellipse(A, t):
    z = np.stack([np.cos(t), np.sin(t)], axis=0)
    return A @ z


fig, (a, b) = plt.subplots(1, 2, figsize=(169 / 25.4, 64 / 25.4))
t = np.linspace(0, 2 * np.pi, 400)

# ---- 左：良态 ----
smax1, smin1, k1 = svd_info(A_GOOD)
a.plot(np.cos(t), np.sin(t), color=MUTED, lw=.6, ls="--", label="单位圆 $\\|z\\|=1$")
w1 = ellipse(A_GOOD, t)
a.fill(w1[0], w1[1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1, zorder=3)
a.annotate("", xy=(smax1 / np.sqrt(2), smax1 / np.sqrt(2)), xytext=(0, 0),
           arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=.9))
a.text(1.02, 1.06, "$\\sigma_{max}=%.2f$" % smax1, fontsize=7.5, color=BLUE)
a.annotate("", xy=(smin1 / np.sqrt(2), -smin1 / np.sqrt(2)), xytext=(0, 0),
           arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=.7))
a.text(.62, -.62, "$\\sigma_{min}=%.2f$" % smin1, fontsize=7.5, color=MUTED)
a.set_title("(a) 良态：$\\kappa(A)=\\sigma_{max}/\\sigma_{min}=%.1f$" % k1, fontsize=8)
a.text(-1.55, -1.72, "误差圆盘 $\\varepsilon=0.1$ 的最长半轴\n$\\varepsilon/\\sigma_{min}=%.2f$，放大温和" % (EPS / smin1),
       fontsize=7.5, color=BLUE)
a.set(xlim=(-1.9, 2.0), ylim=(-1.9, 1.9), xticks=range(-1, 2), yticks=range(-1, 2))
a.set_aspect("equal"); a.grid(True); a.legend(loc="upper right", fontsize=7.5, frameon=False)

# ---- 右：病态 ----
smax2, smin2, k2 = svd_info(A_BAD)
b.plot(np.cos(t), np.sin(t), color=MUTED, lw=.6, ls="--")
w2 = ellipse(A_BAD, t)
b.fill(w2[0], w2[1], facecolor=RED_FILL, edgecolor=RED, lw=1.1, zorder=3)
b.plot(EPS * w2[0], EPS * w2[1], color=RED, lw=1.4, zorder=4)
b.annotate("", xy=(smax2 / np.sqrt(2), smax2 / np.sqrt(2)), xytext=(0, 0),
           arrowprops=dict(arrowstyle="-|>", color=RED, lw=.9))
b.text(.78, 1.42, "$\\sigma_{max}=%.2f$" % smax2, fontsize=7.5, color=RED)
b.annotate("", xy=(smin2 / np.sqrt(2), -smin2 / np.sqrt(2)), xytext=(0, 0),
           arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=.7))
b.text(.16, -.30, "$\\sigma_{min}=%.2f$" % smin2, fontsize=7.5, color=MUTED)
b.set_title("(b) 病态：$\\kappa(A)=%.1f$，椭圆被拉成细条" % k2, fontsize=8)
b.text(-1.9, -1.72, "误差圆盘 $\\varepsilon=0.1$ 被拉成细长椭圆\n最长半轴 $\\varepsilon/\\sigma_{min}=%.2f$，放大 %.0f 倍"
       % (EPS / smin2, (EPS / smin2) / EPS),
       fontsize=7.5, color=RED)
b.set(xlim=(-2.2, 2.2), ylim=(-1.9, 1.9), xticks=range(-2, 3), yticks=range(-1, 2))
b.set_aspect("equal"); b.grid(True)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "解 Ax=b 时，b 上很小的误差为什么会在 x 上被放大成大误差？",
    "formula": "Δx=A^{-1}Δb；单位圆的像为椭圆，半轴长即奇异值 σmax,σmin；"
               "误差放大因子 κ(A)=σmax/σmin，最长半轴 ε/σmin。",
    "parameters": {
        "A_good": [[1, .2], [.2, 1]],
        "A_bad": [[1, .85], [.85, 1]],
        "eps": EPS,
        "grid": "单位圆 z=(cos t, sin t), t∈[0,2π] 取 400 点",
    },
    "evaluated_data": {
        "svd_good": {"sigma_max": round(float(smax1), 4), "sigma_min": round(float(smin1), 4),
                     "kappa": round(float(k1), 4)},
        "svd_bad": {"sigma_max": round(float(smax2), 4), "sigma_min": round(float(smin2), 4),
                    "kappa": round(float(k2), 4)},
        "error_axis_good": EPS / smin1,
        "error_axis_bad": EPS / smin2,
    },
    "processing": "np.linalg.svd 精确求值；无平滑、无随机采样。",
    "width_mm": 169, "height_mm": 64, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
