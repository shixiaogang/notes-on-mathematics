"""第12章 12.7：岭回归与截断SVD的滤波因子和方向增益。

全部曲线按解析式绘制，无随机数据：
  岭回归滤波因子 f(σ)=σ²/(σ²+λ)，方向增益 σ/(σ²+λ)，峰值 1/(2√λ) 在 σ=√λ；
  截断SVD（阈值 τ）滤波因子为 1[σ>τ]，增益为 1/σ（σ>τ）或 0；
  最小二乘（伪逆）增益 1/σ。
参数取正文示例：λ=1e-4、1e-2，τ=0.1；示例矩阵两列 (1,1,1)、(1,1.01,0.99)
的奇异值 σ1≈2.449、σ2≈0.0100 用竖虚线标出。
运行：python3 plots.py（从任意目录），输出 figure.pdf / figure.png / figure.svg。
"""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").exists())
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
from plot_style import BLUE, GREEN, YELLOW, RED, MUTED, STROKE, configure, prepare_figure, note
configure()

LAMS = [(1e-4, BLUE, "-"), (1e-2, GREEN, "-")]
TAU = 0.1
A = np.array([[1, 1], [1, 1.01], [1, 0.99]])
SIG = np.linalg.svd(A, compute_uv=False)          # ≈ (2.449, 0.0100)
s = np.logspace(-3, 1, 801)

fig, (a, b) = plt.subplots(1, 2, figsize=(112 / 25.4, 60 / 25.4), layout="constrained")

for lam, col, ls in LAMS:
    a.plot(s, s**2 / (s**2 + lam), color=col, ls=ls, label=f"岭回归 $\\lambda=10^{{{int(np.log10(lam))}}}$")
a.plot([s[0], TAU, TAU, s[-1]], [0, 0, 1, 1], color=RED, ls="--", lw=1.1, label=f"截断 $\\tau={TAU:g}$")
a.set(xscale="log", xlim=(s[0], s[-1]), ylim=(-0.04, 1.08), yticks=[0, 0.5, 1],
      xlabel="奇异值 $\\sigma$", ylabel="滤波因子 $f$", title="(a) 滤波因子")

b.plot(s, 1 / s, color=MUTED, lw=.8, label="最小二乘 $1/\\sigma$")
for lam, col, ls in LAMS:
    b.plot(s, s / (s**2 + lam), color=col, ls=ls)
    b.plot([np.sqrt(lam)], [1 / (2 * np.sqrt(lam))], marker="o", ms=2.6, color=col, ls="none")
st = s[s > TAU]
b.plot(st, 1 / st, color=RED, ls="--", lw=1.1)
b.plot([TAU, TAU], [1e-1, 1 / TAU], color=RED, ls="--", lw=1.1)
b.set(xscale="log", yscale="log", xlim=(s[0], s[-1]), ylim=(1e-1, 1.2e3),
      xlabel="奇异值 $\\sigma$", ylabel="方向增益", title="(b) 方向增益")

for ax in (a, b):
    for v in SIG:
        ax.axvline(v, color=STROKE, lw=.6, ls=":")
    ax.grid(True, which="major")
a.text(SIG[1] * 1.15, 0.92, "$\\sigma_2$", fontsize=7.5, color=STROKE)
a.text(SIG[0] * 1.15, 0.5, "$\\sigma_1$", fontsize=7.5, color=STROKE)
h, l = a.get_legend_handles_labels()
h2, l2 = b.get_legend_handles_labels()
fig.legend(h2 + h, l2 + l, loc="outside lower center", ncol=4, fontsize=7.5,
           handlelength=1.6, columnspacing=1.0, handletextpad=0.4)

prepare_figure(fig)
for ext in ("pdf", "png", "svg"):
    fig.savefig(HERE / f"figure.{ext}", dpi=300)
plt.close(fig)
print("sigma", SIG)
