from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
sys.path.insert(0, str(ROOT/"figures/05-optimization/02-smooth-optimization/matplotlib/qn-common"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
from qnlib import *
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = "#4C4D4F"

# 10维旋转 log cosh 目标（c 对数等距于 [0.1,100]，强凸），强 Wolfe 线搜索 c1=1e-4，c2=0.9，比较 W0=I 与 W0=1e-3 I。
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
res = {}
for ax, scale, xm in zip(axs, (1., 1e-3), (32, 300)):
    fun, grad, H, rng = rotated_logcosh(10, .1, 100, 1); x0 = rng.standard_normal(10)
    for kind, c, lw, lab in (('dfp', YELLOW, 1.5, 'DFP'), ('bfgs', GREEN, 1.4, 'BFGS')):
        r = run_quasi_newton(fun, grad, x0, scale*np.eye(10), kind, T=xm, gtol=1e-9)
        g = r['gnorm']; ax.semilogy(np.arange(len(g)), g, color=c, lw=lw, label=lab)
        res[f'{kind}-{scale}'] = dict(iters=int(len(g)-1), final=float(g[-1]))
    ax.set_xlim(0, xm); ax.set_ylim(1e-9, 1e3); ax.set_yticks([1e-8, 1e-4, 1]); ax.set_xlabel('$t$', labelpad=1); ax.minorticks_off()
axs[0].set_ylabel('梯度大小', labelpad=1)
axs[0].legend(loc='upper right', handlelength=1.6, borderaxespad=0)
panel(fig, .09, .97, .985, .25, .22); tags(fig, list(axs))
save(fig, HERE, 'figure', {'problem': 'rotated logcosh n=10 c in [0.1,100] seed 1', 'results': res})
