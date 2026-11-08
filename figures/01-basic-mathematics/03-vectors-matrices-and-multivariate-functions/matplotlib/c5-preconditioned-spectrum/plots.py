"""第12章图（12.4.11 预条件）：对角缩放前后的特征值分布。

正文算例：d=10，A=STS，S=diag(1,...,10)，T 为三对角矩阵（对角元 1，次对角元 0.4）。
对角缩放 M=diag(A)=S^2，取 C=S，则 C^{-1}AC^{-T}=T，M^{-1}A 与 T 相似，
其特征值为解析式 1+0.8cos(j*pi/11)，j=1..10；A 的特征值由 numpy.linalg.eigvalsh 计算。
无随机数，不调用 LaTeX。从任意目录运行：python3 plots.py
"""
from pathlib import Path
import json
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))

import matplotlib.pyplot as plt  # noqa: E402

from plot_style import BLUE, GREEN, STROKE, configure, note, prepare_figure, style_record  # noqa: E402

configure()

D, T_OFF = 10, 0.4
S = np.diag(np.arange(1.0, D + 1))
T = np.eye(D) + T_OFF * (np.eye(D, k=1) + np.eye(D, k=-1))
A = S @ T @ S
eig_a = np.linalg.eigvalsh(A)
eig_t = np.sort(1 + 2 * T_OFF * np.cos(np.arange(1, D + 1) * np.pi / (D + 1)))
M_inv = np.diag(1 / np.diag(A))
eig_ma = np.sort(np.linalg.eigvals(M_inv @ A).real)
assert np.allclose(eig_ma, eig_t) and np.allclose(np.linalg.eigvalsh(T), eig_t)
kappa_a, kappa_t = eig_a[-1] / eig_a[0], eig_t[-1] / eig_t[0]
factor = lambda k: (np.sqrt(k) - 1) / (np.sqrt(k) + 1)

WIDTH_MM, HEIGHT_MM = 100, 34
fig, ax = plt.subplots(figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4), layout="constrained")
for y, vals, color in [(1, eig_a, BLUE), (0, eig_t, GREEN)]:
    ax.scatter(vals, np.full_like(vals, y), s=16, color=color, edgecolor=STROKE, linewidth=.4, zorder=3)
for y, lo, hi, color, kap, ha, x in [(1, eig_a[0], eig_a[-1], BLUE, kappa_a, "center", np.sqrt(eig_a[0] * eig_a[-1])),
                                     (0, eig_t[0], eig_t[-1], GREEN, kappa_t, "left", 2.3)]:
    yb = y + .33
    ax.plot([lo, hi], [yb, yb], color=color, lw=.6)
    for xe in (lo, hi):
        ax.plot([xe, xe], [yb - .09, yb + .09], color=color, lw=.6)
    note(ax.text(x, yb + (.06 if ha == "center" else 0), rf"$\lambda_{{\max}}/\lambda_{{\min}}\approx{kap:.1f}$" if kap > 100
                 else rf"$\lambda_{{\max}}/\lambda_{{\min}}\approx{kap:.2f}$",
                 color=color, ha=ha, va="bottom" if ha == "center" else "center"))
ax.set_xscale("log")
ax.set_xlim(.1, 300)
ax.set_ylim(-.6, 1.75)
ax.set_yticks([0, 1], [r"$\mathbf{M}^{-1}\mathbf{A}$", r"$\mathbf{A}$"])
ax.tick_params(axis="y", length=0)
ax.spines["left"].set_visible(False)
ax.set_xticks([.1, 1, 10, 100], ["0.1", "1", "10", "100"])
ax.set_xlabel(r"特征值 $\lambda$（对数刻度）")
ax.grid(False, which="both")
prepare_figure(fig)
for ext in ("pdf", "png"):
    fig.savefig(HERE / f"figure.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical and exactly computed eigenvalues of the worked example in the text",
    "matrix": "A=STS, S=diag(1..10), T=tridiag(0.4,1,0.4); M=diag(A)=S^2",
    "eig_A": [round(float(x), 4) for x in eig_a],
    "eig_MinvA": [round(float(x), 4) for x in eig_t],
    "kappa_A": round(float(kappa_a), 2),
    "kappa_MinvA": round(float(kappa_t), 2),
    "cg_factor_A": round(float(factor(kappa_a)), 3),
    "cg_factor_MinvA": round(float(factor(kappa_t)), 3),
    "width_mm": WIDTH_MM, "height_mm": HEIGHT_MM, "png_dpi": 300,
    "outputs": ["figure.pdf", "figure.png"],
}
(HERE / "sources.json").write_text(json.dumps({"style": style_record(), "figure": record},
                                              ensure_ascii=False, indent=2) + "\n")
print(json.dumps(record, ensure_ascii=False))
