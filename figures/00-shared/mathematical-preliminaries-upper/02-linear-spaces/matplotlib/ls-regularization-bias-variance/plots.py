"""教学图：正则化在残差与参数范数之间的权衡（L 曲线）。

解析式固定构造：A=diag(2,1)，b=(4,1)，岭回归解 x(λ)=(8/(4+λ), 1/(1+λ))。
左 panel：L 曲线——横轴 ‖x(λ)‖、纵轴 ‖Ax−b‖(λ)，参数 λ 沿曲线流动。
右 panel：两条曲线随 λ 变化——残差上升、参数范数下降。
固定 λ 网格，无随机数，不调用 LaTeX。从任意目录运行：python3 plots.py [--only ...]
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

LAM = np.linspace(0.02, 8.0, 41)
X1 = 8.0 / (4.0 + LAM)
X2 = 1.0 / (1.0 + LAM)
XNORM = np.sqrt(X1**2 + X2**2)
RES = np.sqrt((2 * X1 - 4)**2 + (X2 - 1)**2)


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, (a, b) = plt.subplots(1, 2, figsize=(169 / 25.4, 66 / 25.4))

# ---- 左 panel：L 曲线 ----
a.plot(XNORM, RES, color=BLUE, lw=1.2)
for i, lam in ((0, 0.02), (20, LAM[20]), (40, 8.0)):
    a.plot(XNORM[i], RES[i], "o", ms=4, mfc=YELLOW, mec=INK, mew=.4, zorder=5)
a.annotate("λ 小：参数范数大\n过拟合，方差大", xy=(2.18, 0.04),
           xytext=(1.30, 0.30), fontsize=7.5,
           arrowprops=dict(arrowstyle="->", color=BLUE, lw=.6))
a.annotate("λ 大：残差大\n偏差大", xy=(0.12, 4.02),
           xytext=(1.25, 3.45), fontsize=7.5,
           arrowprops=dict(arrowstyle="->", color=RED, lw=.6))
a.set_xlabel("$\\|x(\\lambda)\\|$（参数范数）")
a.set_ylabel("$\\|Ax-b\\|$（残差）")
a.set_title("(a) L 曲线：两端各有一类误差", fontsize=8)
a.set(xlim=(0, 2.6), ylim=(0, 4.6))
a.grid(True)

# ---- 右 panel：随 λ 的两条曲线 ----
b.plot(LAM, RES, color=RED, lw=1.2, label="$\\|Ax-b\\|$ 残差：随 λ 增大")
b.plot(LAM, XNORM, color=GREEN, lw=1.2, label="$\\|x(\\lambda)\\|$ 参数范数：随 λ 减小")
b.axvline(1.0, color=MUTED, lw=.5, ls=":")
b.text(1.05, 3.6, "折衷区", fontsize=7.5, color=MUTED)
b.set_xlabel("正则参数 λ")
b.set_title("(b) 同一组数据，两种曲线此消彼长", fontsize=8)
b.legend(loc="center right", fontsize=7.5, frameon=False)
b.set(xlim=(0, 8), ylim=(0, 4.6))
b.grid(True)

finalize(fig)
fig.tight_layout()
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "正则参数 λ 调大调小分别引入什么误差？L 曲线为什么弯？",
    "formula": "A=diag(2,1), b=(4,1); ridge x(λ)=(8/(4+λ), 1/(1+λ)); "
               "||x||^2=(8/(4+λ))^2+(1/(1+λ))^2; "
               "||Ax-b||^2=(16/(4+λ)-4)^2+(1/(1+λ)-1)^2。",
    "parameters": {
        "A_diag": [2, 1], "b": [4, 1],
        "lambda_grid": "linspace(0.02, 8, 41)",
        "ridge_solution": "x1=8/(4+λ), x2=1/(1+λ)",
    },
    "evaluated_data": {
        "lambda_0": {"x": [8 / 4, 1 / 1], "xnorm": float(np.sqrt(5)), "residual": 0.0},
        "lambda_8": {"x": [8 / 12, 1 / 9],
                     "xnorm": float(np.sqrt((8 / 12)**2 + (1 / 9)**2)),
                     "residual": float(np.sqrt((16 / 12 - 4)**2 + (1 / 9 - 1)**2))},
    },
    "processing": "固定 λ 网格直接求值；无随机采样。",
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
