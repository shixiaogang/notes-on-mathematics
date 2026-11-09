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

# n=200，c 对数等距于 [0.01,100]，再把目标整体乘 1000（曲率整体偏大）。r=10，有/无 gamma 缩放。
base, gbase, H, rng = rotated_logcosh(200, .01, 100, 3); x0 = rng.standard_normal(200)
S = 1000.
fun = lambda x: S*base(x); grad = lambda x: S*gbase(x)
fig, ax = figure(width_mm=86, height_mm=52)
a = run_lbfgs(fun, grad, x0, 10, T=1500, gtol=1e-5, scale=True)
b = run_lbfgs(fun, grad, x0, 10, T=1500, gtol=1e-5, scale=False)
for r, c, lw, ls in ((b, YELLOW, 1.5, (0, (4, 2))), (a, GREEN, 1.4, '-')):
    ax.semilogy(r['evals'], r['gnorm'], color=c, lw=lw, ls=ls)
ax.set_xlim(0, 1500)
ax.text(a['evals'][-1]*.5, 3e2, '有缩放', color=INK)
ax.text(900, 8e2, '无缩放', color=INK)
ax.set_xlabel('函数值与梯度计算次数', labelpad=1); ax.set_ylabel('梯度大小', labelpad=1); ax.set_ylim(1e-5, 1e6); ax.set_yticks([1e-4, 1, 1e4]); ax.minorticks_off()
save(fig, HERE, 'figure', {'scaled_evals': int(a['evals'][-1]), 'scaled_iters': len(a['gnorm'])-1, 'unscaled_evals': int(b['evals'][-1]), 'unscaled_iters': len(b['gnorm'])-1, 'unscaled_final': float(b['gnorm'][-1])})
