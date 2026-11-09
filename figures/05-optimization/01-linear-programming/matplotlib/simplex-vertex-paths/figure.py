from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import simplex
SA=[[1,2,1,0,0],[2,1,0,1,0],[0,1,0,0,1]]; b_=[8,10,3]; c_=[-4,-5,0,0,0]
def route(rule):
    st, tr, x = simplex(SA, b_, c_, [3,4,5], rule)
    return [(float(r['x'][0]), float(r['x'][1])) for r in tr]
xlim, ylim = (-.5, 6.4), (-.5, 4.6)
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
A, b = with_sign(RES_A, RES_B); V = polygon(A, b)
for ax, rule, col, lab in zip(axs, ['dantzig','bland'], [GREEN, YELLOW], ['(a)','(b)']):
    draw_region(ax, V)
    contours(ax, PROFIT, [15, 26], xlim, ylim)
    r = route(rule); path(ax, r, color=col, lw=1.6)
    opt_point(ax, r[-1])
    setup(ax, xlim, ylim, range(0,7), range(0,5), label=lab)
    offs = {0:(.12,.13)}
    for k, p in enumerate(r[:-1]):
        ax.text(p[0]+.14, p[1]+.16, f'$t={k}$', fontsize=7.5, color=INK, zorder=9)
    ax.text(r[-1][0]+.16, r[-1][1]+.1, f'$t={len(r)-1}$', fontsize=7.5, color=INK, zorder=9)
save(fig, Path(__file__).resolve().parent, 'figure', {'paths': {'dantzig': route('dantzig'), 'lowest_index': route('bland')}})
