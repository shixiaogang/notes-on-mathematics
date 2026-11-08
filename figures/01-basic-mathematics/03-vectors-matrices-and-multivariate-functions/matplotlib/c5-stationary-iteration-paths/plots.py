"""第12章 12.3（本部分第5章）：定常迭代在贯穿例上的轨迹与误差。

贯穿例 A=[[4,1],[1,3]]，b=(1,2)，x0=0，精确解 x*=(1/11,7/11)。全部迭代用有理数精确计算：
  左图：两条方程直线 4x1+x2=1（实线）、x1+3x2=2（虚线）；
        Jacobi 前 4 轮的迭代点 (0,0),(1/4,2/3),(1/12,7/12),(5/48,23/36),...；
        Gauss--Seidel 前 3 轮的逐坐标折线 (0,0)->(1/4,0)->(1/4,7/12)->(5/48,7/12)->...
  右图：Richardson(alpha=1/4)、Jacobi、SOR(omega=6/5)、Gauss--Seidel 在 k=0..10 的
        误差 ||x_k-x*||_2，纵轴取对数。谱半径分别约 0.405、0.289、0.2、1/12。
无随机数据。运行：python3 plots.py（从任意目录），输出 figure.pdf / figure.png / figure.svg / data.json。
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").exists())
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
from plot_style import BLUE, GREEN, YELLOW, PURPLE, INK, MUTED, STROKE, configure, prepare_figure, note, style_record
configure()

A = [[F(4), F(1)], [F(1), F(3)]]
b = [F(1), F(2)]
XS = [F(1, 11), F(7, 11)]


def residual(x):
    return [b[i] - A[i][0] * x[0] - A[i][1] * x[1] for i in range(2)]


def err(x):
    return math.hypot(float(x[0] - XS[0]), float(x[1] - XS[1]))


def richardson(x, alpha=F(1, 4)):
    r = residual(x)
    return [x[0] + alpha * r[0], x[1] + alpha * r[1]]


def jacobi(x):
    r = residual(x)
    return [x[0] + r[0] / A[0][0], x[1] + r[1] / A[1][1]]


def sor_sweep(x, omega, trace=None):
    x = list(x)
    for i in range(2):
        r = b[i] - A[i][0] * x[0] - A[i][1] * x[1]
        x[i] += omega * r / A[i][i]
        if trace is not None:
            trace.append(list(x))
    return x


def run(step, K):
    x = [F(0), F(0)]
    out = [x]
    for _ in range(K):
        x = step(x)
        out.append(x)
    return out


K = 10
METHODS = [  # key, label, color, marker
    ("richardson", "Richardson，$\\alpha=1/4$", YELLOW, "^"),
    ("jacobi", "Jacobi", BLUE, "o"),
    ("sor", "SOR，$\\omega=6/5$", PURPLE, "D"),
    ("gs", "Gauss\u2013Seidel", GREEN, "s"),
]
STEPS = {"richardson": richardson, "jacobi": jacobi,
         "gs": lambda x: sor_sweep(x, F(1)), "sor": lambda x: sor_sweep(x, F(6, 5))}
iters = {k: run(STEPS[k], K) for k, *_ in METHODS}
errors = {k: [err(x) for x in v] for k, v in iters.items()}
jac_path = iters["jacobi"][:5]
gs_trace = [[F(0), F(0)]]
x = gs_trace[0]
for _ in range(3):
    x = sor_sweep(x, F(1), gs_trace)

fig, (a, c) = plt.subplots(1, 2, figsize=(108 / 25.4, 54 / 25.4), layout="constrained",
                           gridspec_kw={"width_ratios": [1, 1.15]})
xx = [-0.03, 0.33]
a.plot([0.06, 0.265], [1 - 4 * 0.06, 1 - 4 * 0.265], color=MUTED, lw=.6)
a.plot(xx, [(2 - v) / 3 for v in xx], color=MUTED, lw=.6, ls="--")
a.plot([float(p[0]) for p in jac_path], [float(p[1]) for p in jac_path], color=BLUE, lw=1.1,
       marker="o", ms=3.2, mfc="white", mew=.9, label="Jacobi")
a.plot([float(p[0]) for p in gs_trace], [float(p[1]) for p in gs_trace], color=GREEN, lw=1.1,
       marker="s", ms=2.6, label="Gauss\u2013Seidel")
a.plot([1 / 11], [7 / 11], marker="x", ms=4, mew=.8, color=INK, ls="none")
note(a.text(1 / 11 - 0.006, 7 / 11 + 0.02, "$\\mathbf{x}_\\star$", ha="right", va="bottom", color=INK))
note(a.text(0.008, -0.012, "$\\mathbf{x}_0$", ha="left", va="top", color=INK))
note(a.text(0.262, 0.01, "方程1", ha="left", va="bottom", color=MUTED))
note(a.text(-0.025, 0.69, "方程2", ha="left", va="bottom", color=MUTED))
a.set(xlim=(-0.03, 0.33), ylim=(-0.07, 0.76), xticks=[0, 0.1, 0.2, 0.3], yticks=[0, 0.2, 0.4, 0.6],
      xlabel="$x_1$", ylabel="$x_2$", title="(a) 迭代路径")

for key, label, col, mk in METHODS:
    c.semilogy(range(K + 1), errors[key], color=col, lw=1.1, marker=mk, ms=2.6,
               mfc="white" if key == "jacobi" else col, mew=.9, label=label)
c.set(xlim=(0, K), ylim=(1e-11, 2), xticks=range(0, K + 1, 2), yticks=[1, 1e-3, 1e-6, 1e-9],
      xlabel="迭代轮数 $k$", ylabel="$\\Vert\\mathbf{x}_k-\\mathbf{x}_\\star\\Vert_2$", title="(b) 误差")
c.grid(False, which="both")
c.legend(loc="lower left", fontsize=7.5, handlelength=1.6, handletextpad=.4, borderaxespad=.2)

prepare_figure(fig)
for ext in ("pdf", "png", "svg"):
    fig.savefig(HERE / f"figure.{ext}", dpi=300)
plt.close(fig)

(HERE / "data.json").write_text(json.dumps({
    "kind": "exact rational iteration of the chapter running example; no random data",
    "A": [[4, 1], [1, 3]], "b": [1, 2], "x0": [0, 0], "x_star": ["1/11", "7/11"],
    "jacobi_path": [[str(v) for v in p] for p in jac_path],
    "gauss_seidel_trace": [[str(v) for v in p] for p in gs_trace],
    "first_iterates": {k: [str(v) for v in iters[k][1]] for k in iters},
    "errors_2norm": {k: [float(f"{e:.6e}") for e in v] for k, v in errors.items()},
    "size_mm": [108, 54], "style": style_record(),
}, ensure_ascii=False, indent=2) + "\n")
print({k: f"{v[1]:.4f} -> {v[-1]:.3e}" for k, v in errors.items()})
