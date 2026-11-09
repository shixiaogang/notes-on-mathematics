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

# n=200 旋转 log cosh 目标（c 对数等距于 [1e-3,1e3]），强 Wolfe，c2=0.9。
fun, grad, H, rng = rotated_logcosh(200, 1e-3, 1e3, 3); x0 = rng.standard_normal(200)
fig, (ax, bx) = figure(width_mm=112, height_mm=56, ncols=2)
out = {}
for r, c, ls, lw in ((1, PURPLE, (0, (1.2, 1.4)), 1.3), (3, YELLOW, (0, (4, 2)), 1.4), (10, BLUE, '-', 1.2), (30, GREEN, '-', 1.4)):
    res = run_lbfgs(fun, grad, x0, r, T=3000, gtol=1e-6)
    g = res['gnorm']; ax.semilogy(np.arange(len(g)), g, color=c, lw=lw, ls=ls, label=f'$r={r}$')
    out[r] = int(len(g)-1)
ax.set_xlim(0, max(out.values())*1.05); ax.set_ylim(1e-6, 1e4); ax.set_yticks([1e-5, 1e-2, 10]); ax.minorticks_off(); ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('梯度大小', labelpad=1)
ax.legend(loc='upper right', handlelength=1.8, borderaxespad=0, labelspacing=.25)
rs = [1, 2, 3, 5, 10, 20, 30, 50, 100]; its = []; costs = []
for r in rs:
    res = run_lbfgs(fun, grad, x0, r, T=6000, gtol=1e-6)
    its.append(len(res['gnorm'])-1); costs.append((len(res['gnorm'])-1)*4*r*200/1e6)
bx.loglog(rs, its, '-o', color=GREEN, lw=1.4, ms=3, mew=0)
bx.loglog(rs, costs, '-o', color=PURPLE, lw=1.4, ms=3, mew=0)
bx.text(1.3, its[0]*1.25, '迭代数', color=INK); bx.text(4, costs[1]*.09+.0, '方向计算', color=INK)
bx.set_xlabel('$r$', labelpad=1); bx.set_xticks([1, 10, 100]); bx.set_ylim(.03, 8000); bx.set_yticks([.1, 10, 1000]); bx.minorticks_off()
panel(fig, .09, .985, .985, .25, .25); tags(fig, [ax, bx])
save(fig, HERE, 'figure', {'problem': 'rotated logcosh n=200 c in [1e-3,1e3] seed 3', 'iters_tol1e-6': dict(zip(map(str, rs), its)), 'cost_1e6': costs, 'iters_lines': out})
