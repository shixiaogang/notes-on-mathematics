"""教学图：SVD 构造三步——Gram 矩阵 → 正交对角化 → 奇异值与奇异向量。

固定 A=[[2,0.5],[0.5,1]]（对称正定）。AᵀA=[[4.25,1.5],[1.5,1.25]]，
特征值 λ1≈4.87, λ2≈0.63；奇异值 σ_i=√λ_i≈2.21, 0.79；
右奇异向量 v_i 即特征向量，左奇异向量 u_i=Av_i/σ_i。
每栏配一个小几何示意，栏间箭头表示步骤；全部数学走 mathtext。
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
BLUE_FILL, GREEN_FILL = "#E5EAF0", "#E8EEE9"
CN_MAIN, CN_AUX, EN = "Source Han Sans SC", "LXGW WenKai", "Fira Math"

matplotlib.rcParams.update({
    "font.family": [EN, CN_MAIN], "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": EN, "mathtext.it": EN,
    "mathtext.bf": EN, "mathtext.sf": EN,
    "axes.unicode_minus": False, "text.color": INK,
    "pdf.fonttype": 3, "svg.fonttype": "path",
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only

A = np.array([[2., 0.5], [0.5, 1.]])
ATA = A.T @ A
LAM, V = np.linalg.eigh(ATA)
order = np.argsort(LAM)[::-1]
LAM, V = LAM[order], V[:, order]
SIG = np.sqrt(LAM)
U = A @ V / SIG


def arrow(ax, p, q, color, lw=1.1, ls="-"):
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, ls=ls,
                                shrinkA=0, shrinkB=0))


def small_matrix(ax, x0, y0, cell, vals, color):
    """画 2×2 小矩阵格子：x0,y0 为左上角，vals 为两行字符串。"""
    for i in range(2):
        for j in range(2):
            ax.add_patch(plt.Rectangle((x0 + j * cell, y0 - i * cell), cell, cell,
                                       facecolor="white", edgecolor=STROKE, lw=.5))
            ax.text(x0 + j * cell + cell / 2, y0 - i * cell - cell / 2, vals[i][j],
                    ha="center", va="center", fontsize=6.5, color=color)
    for s in (-0.06, 2 * cell + 0.06):
        ax.plot([x0 + s, x0 + s], [y0 + 0.05, y0 - 2 * cell - 0.05],
                color=STROKE, lw=.8)


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, (a, b, c) = plt.subplots(1, 3, figsize=(169 / 25.4, 66 / 25.4))
th = np.linspace(0, 2 * np.pi, 120)
circle = np.array([np.cos(th), np.sin(th)])

# ---- 第一步：Gram 矩阵的二次型椭圆 ----
ell = V @ np.diag(np.sqrt(2.0 / LAM)) @ circle
a.plot(ell[0], ell[1], color=BLUE, lw=1.1)
a.plot(0, 0, "o", ms=3, mfc=MUTED, mec=MUTED)
a.text(-2.6, 2.05, "椭圆：$x^\\top A^\\top A x=2$", fontsize=7.5, color=BLUE)
# 两个小矩阵左右并排置于椭圆下方，列距足够、数字不碰括号线
for lbl, rows, col, xc in [
        ("$A$", [("$2$", "$0.5$"), ("$0.5$", "$1$")], INK, -1.6),
        ("$A^\\top A$", [("$4.25$", "$1.5$"), ("$1.5$", "$1.25$")], BLUE, 1.6)]:
    dx, ytop, ybot = .62, -2.75, -3.30
    x1, x2 = xc - dx, xc + dx
    a.text(xc, ytop + .55, lbl, fontsize=7.5, ha="center", va="center", color=col)
    a.text(x1, ytop, rows[0][0], fontsize=7.5, ha="center", va="center", color=col)
    a.text(x2, ytop, rows[0][1], fontsize=7.5, ha="center", va="center", color=col)
    a.text(x1, ybot, rows[1][0], fontsize=7.5, ha="center", va="center", color=col)
    a.text(x2, ybot, rows[1][1], fontsize=7.5, ha="center", va="center", color=col)
    for bx in (x1 - .62, x2 + .62):
        a.plot([bx, bx], [ybot - .22, ytop + .22], color=STROKE, lw=.8)
a.set_title("")
a.set(xlim=(-2.9, 2.9), ylim=(-3.8, 2.5)); a.set_aspect("equal"); a.axis("off")

# ---- 第二步：正交对角化，特征方向 ----
a1, a2 = np.cos(th), np.sin(th)
b.plot(a1, a2, color=MUTED, lw=.8)
arrow(b, (0, 0), V[:, 0], BLUE, lw=1.2)
arrow(b, (0, 0), V[:, 1], GREEN, lw=1.2)
b.text(V[0, 0] * 1.32, V[1, 0] * 1.32, "$v_1$", fontsize=8, color=BLUE)
b.text(V[0, 1] * 1.18, V[1, 1] * 1.18, "$v_2$", fontsize=8, color=GREEN)
b.text(-1.45, -1.35, r"$\lambda_1\approx4.87,\ \lambda_2\approx0.63$",
       fontsize=7.5, color=GREEN)
b.text(0, -1.75, r"$A^\top A=V\,\mathrm{diag}(\lambda_1,\lambda_2)V^\top$",
       ha="center", fontsize=8, transform=b.transData)
b.set_title("")
b.set(xlim=(-1.5, 1.5), ylim=(-2.05, 1.5)); b.set_aspect("equal"); b.axis("off")

# ---- 第三步：单位圆 → 椭圆，左右奇异向量 ----
ellA = A @ circle
c.plot(a1, a2, color=MUTED, lw=.8)
c.plot(ellA[0], ellA[1], color=BLUE, lw=1.1)
arrow(c, (0, 0), SIG[0] * V[:, 0], BLUE, lw=1.2)
arrow(c, (0, 0), SIG[1] * V[:, 1], GREEN, lw=1.2)
c.text(SIG[0] * V[0, 0] - .10, SIG[0] * V[1, 0] - .55,
       "$u_1=Av_1/\\sigma_1$", fontsize=7.5, color=BLUE)
c.annotate("$u_2=Av_2/\\sigma_2$",
           xy=(SIG[1] * V[0, 1], SIG[1] * V[1, 1]),
           xytext=(0.95, 1.62), fontsize=7.5, color=GREEN,
           arrowprops=dict(arrowstyle="->", color=GREEN, lw=.6))
c.text(-1.55, -2.05, r"$\sigma_i=\sqrt{\lambda_i}\approx2.21,\ 0.79$",
       fontsize=7.5, color=YELLOW)
c.text(0, -2.5, r"$A=U\,\mathrm{diag}(\sigma_i)V^\top$",
       ha="center", fontsize=8, transform=c.transData)
c.set_title("")
c.set(xlim=(-2.5, 2.5), ylim=(-2.9, 2.4)); c.set_aspect("equal"); c.axis("off")

# 栏间步骤箭头 + 统一基线标题
fig.subplots_adjust(left=0.03, right=0.985, top=0.84, bottom=0.10, wspace=0.9)
for x in (0.365, 0.685):
    fig.text(x, 0.45, "→", fontsize=13, color=MUTED, ha="center", va="center")
for x, t in ((0.129, "第一步：形成 Gram 矩阵"),
             (0.498, "第二步：正交对角化，得特征方向"),
             (0.886, "第三步：单位圆 → 椭圆")):
    fig.text(x, 0.93, t, fontsize=8, ha="center", va="center")

finalize(fig)
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "SVD 的三个量（Gram 矩阵、特征方向、奇异值）是怎样一步步算出来的？",
    "formula": "A=[[2,0.5],[0.5,1]]; AᵀA=[[4.25,1.5],[1.5,1.25]]; "
               "AᵀA=V diag(λ1,λ2) Vᵀ; λ1≈4.87, λ2≈0.63; "
               "σ_i=√λ_i; u_i=Av_i/σ_i; A=U diag(σ_i) Vᵀ。",
    "parameters": {
        "A": A.tolist(), "AtA": ATA.tolist(),
        "lambda": list(LAM), "sigma": list(SIG),
        "V_columns": V.tolist(), "U_columns": U.tolist(),
    },
    "evaluated_data": {
        "sigma1": float(SIG[0]), "sigma2": float(SIG[1]),
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
