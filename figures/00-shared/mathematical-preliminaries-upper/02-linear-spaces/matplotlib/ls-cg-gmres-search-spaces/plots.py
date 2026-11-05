"""教学图：CG 与 GMRES 的搜索空间对照。

左：二次目标 f(x)=x^T D x，D=diag(4,1)，x0=(1.3,-1)。CG 沿 D-共轭方向
精确线搜索两步到达极小点（原点），与梯度下降的锯齿对比。
右：残差等高线（同心圆）；Krylov 仿射空间 x0+K_1 是一条直线，残差在其
上的最小点即原点到该直线的垂足；二维情形 K_2=R²，两步内残差可取到 0。
全部固定构造、精确线搜索；无随机采样，不调用 LaTeX。
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

D = np.diag([4., 1.])
X0 = np.array([1.3, -1.0])

# CG：精确线搜索两步
xs = [X0.copy()]
x = X0.copy()
r = -D @ x
d = r.copy()
for _ in range(2):
    alpha = (r @ r) / (d @ D @ d)
    x = x + alpha * d
    xs.append(x.copy())
    r_new = r - alpha * D @ d
    beta = (r_new @ r_new) / (r @ r)
    d = r_new + beta * d
    r = r_new
X1, X2 = xs[1], xs[2]

# GMRES panel 构造：残差圆 + 仿射直线 K1
X0G = np.array([1.2, 0.9])
DHAT = np.array([0.301, 0.954]); DHAT = DHAT / np.linalg.norm(DHAT)
XSTAR = X0G - (X0G @ DHAT) * DHAT


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, (a, b) = plt.subplots(1, 2, figsize=(169 / 25.4, 66 / 25.4))
t = np.linspace(0, 2 * np.pi, 300)

# ---- 左：CG ----
for c in (0.5, 1.0, 2.0, 4.0):
    a.plot(np.sqrt(c / 4) * np.cos(t), np.sqrt(c) * np.sin(t),
           color=BLUE, lw=.5, alpha=.55)
for p, q in zip(xs[:-1], xs[1:]):
    a.annotate("", xy=q, xytext=p,
               arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.1))
a.plot(*X0, "o", ms=4, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
a.plot(*X1, "o", ms=4, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
a.plot(0, 0, "o", ms=5, mfc=GREEN, mec=INK, mew=.5, zorder=5)
a.text(X0[0] + .05, X0[1] - .06, "$x_0$", fontsize=8, color=YELLOW)
a.text(X1[0] - .28, X1[1] - .10, "$x_1$", fontsize=8, color=YELLOW)
a.text(.06, .08, "$x_*$", fontsize=8, color=GREEN)
a.text(-1.55, -1.35, "CG：方向 $D$-共轭，\n精确线搜索两步到达极小点", fontsize=7.5, color=RED)
a.set_title("(a) CG：二次目标等高线与共轭折线", fontsize=8)
a.set(xlim=(-1.7, 1.8), ylim=(-1.5, 1.5), xticks=range(-1, 2), yticks=range(-1, 2))
a.set_aspect("equal"); a.grid(True)

# ---- 右：GMRES ----
for r in (0.5, 1.0, 1.5, 2.0):
    b.plot(r * np.cos(t), r * np.sin(t), color=BLUE, lw=.5, alpha=.55)
ts = np.linspace(-1.6, 2.6, 10)
line = X0G[None, :] + ts[:, None] * DHAT[None, :]
b.plot(line[:, 0], line[:, 1], color=GREEN, lw=1.1, zorder=3)
b.plot([0, XSTAR[0]], [0, XSTAR[1]], color=MUTED, lw=.6, ls=":", zorder=2)
b.annotate("", xy=XSTAR, xytext=X0G,
           arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.1))
b.plot(*X0G, "o", ms=4, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
b.plot(*XSTAR, "o", ms=5, mfc=GREEN, mec=INK, mew=.5, zorder=5)
b.plot(0, 0, "o", ms=4, mfc=INK, mec=INK, mew=.5, zorder=5)
b.text(-0.62, 0.16, "解 $x$（残差为零）", fontsize=7.5, color=INK)
b.text(X0G[0] + .05, X0G[1] + .02, "$x_0$", fontsize=8, color=YELLOW)
b.text(1.08, -0.62, "$x_1$：残差最小点", fontsize=7.5, color=GREEN)
b.text(-1.95, 1.35, "同心圆：残差范数 $\\|r\\|$\n绿线：$K_1=x_0+\\operatorname{span}\\{r_0\\}$",
       fontsize=7.5, color=GREEN,
       bbox=dict(facecolor="white", edgecolor="none", alpha=.9, pad=1.6))
b.text(-1.75, -1.85, "$x_1$ 是原点到直线的垂足；\n二维下 $K_2=R^2$，两步内残差可取 0",
       fontsize=7.5, color=INK)
b.set_title("(b) GMRES：在 Krylov 仿射空间中最小化残差", fontsize=8)
b.set(xlim=(-2.0, 2.2), ylim=(-2.0, 2.0), xticks=range(-2, 3), yticks=range(-2, 3))
b.set_aspect("equal"); b.grid(True)

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "CG 与 GMRES 各自在什么样的搜索空间里找解？为什么步数有上界？",
    "formula": "CG：f=x^T D x, D=diag(4,1)；x0=(1.3,-1)，D-共轭方向精确线搜索两步到原点。"
               "GMRES：残差 ‖b-Ax‖ 在仿射空间 x0+K_k(A,r0) 上最小化；K1 为直线，最小点=原点垂足；"
               "二维时 K2=R²。",
    "parameters": {
        "D": [4., 1.], "x0": [1.3, -1.0],
        "cg_steps": 2,
        "gmres_x0": [1.2, 0.9], "k1_direction": list(DHAT),
    },
    "evaluated_data": {
        "cg_x1": [round(float(v), 6) for v in X1],
        "cg_x2": [round(float(v), 6) for v in X2],
        "gmres_xstar": [round(float(v), 6) for v in XSTAR],
        "residual_at_xstar": round(float(np.linalg.norm(XSTAR)), 6),
    },
    "processing": "CG 递推与投影均按公式精确求值；无随机采样。",
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
