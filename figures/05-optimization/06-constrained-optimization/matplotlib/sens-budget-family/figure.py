from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Budget quadratic at tau=0.5, 2, 4: feasible triangle, contours of 0.5*||x-(2,1)||^2, minimizer, active edges.
fig, axs = figure(width_mm=112, height_mm=44, ncols=3)
data = {}
for ax, tau, act, sub in zip(axs, [.5, 2, 4], [(1, 3), (1,), ()], ['(a)', '(b)', '(c)']):
    triangle(ax, tau, act)
    circles(ax)
    x, lam = budget(tau); data[str(tau)] = [list(x), list(lam)]
    ax.plot([2], [1], marker='x', color=BLUE, ms=4.2, mew=1.1, ls='none', zorder=6)
    opt_point(ax, x)
    ax.set_aspect('equal')
    clean(ax, (-.35, 4.4), (-.35, 4.4), sub=sub)
    ax.set_xticks([0, 2, 4]); ax.set_yticks([0, 2, 4])
    ax.text(.12, 3.95, rf'$\tau={tau}$', fontsize=8)
    ax.spines['left'].set_position(('data', -.35))
axs[0].set_ylabel('$x_2$', labelpad=1)
for ax in axs: ax.set_xlabel(ax.get_xlabel().replace('(', '$x_1$\n(', 1), labelpad=1)
save(fig, Path(__file__).resolve().parent, 'figure', {'objective': '0.5*||x-(2,1)||^2', 'solutions': data})
