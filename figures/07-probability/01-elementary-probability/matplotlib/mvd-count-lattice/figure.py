"""Joint pmf of (N1,N2,N3) on the lattice k1+k2+k3=4.
(a) multinomial Mult(4,(0.5,0.3,0.2)); (b) multivariate hypergeometric with
class sizes K=(5,3,2), population M=10, n=4 draws without replacement.
Marker area is proportional to probability; the outcome (2,1,1) is ringed."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

n = 4; p = (.5, .3, .2); K = (5, 3, 2); M = 10
pts = [(a, b, n-a-b) for a in range(n+1) for b in range(n+1-a)]
def mult(k):
    return math.factorial(n)/math.prod(math.factorial(x) for x in k)*math.prod(q**x for q, x in zip(p, k))
def hyp(k):
    return math.prod(math.comb(Kc, x) for Kc, x in zip(K, k))/math.comb(M, n)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.03, right=.97, top=.97, bottom=.1, wspace=.12)
facts = {}
for ax, f, name in zip(axes, (mult, hyp), ('multinomial', 'hypergeometric')):
    tri_frame(ax, labels=None)
    probs = {k: f(k) for k in pts}; facts[name] = {str(k): round(v, 4) for k, v in probs.items()}
    for k, v in probs.items():
        x, y = tri_xy(np.array(k)/n)
        if v > 0:
            ax.scatter([x], [y], s=900*v, color=BLUE_FILL, edgecolor=BLUE, lw=.9, zorder=6)
            lab(ax, x, y-.075, f'{v:.3f}'.lstrip('0'), ha='center', va='top', fontsize=7)
        else:
            ax.plot([x], [y], marker='x', ms=4, color=RED, mew=1.0, zorder=6)
        if k == (2, 1, 1):
            ax.scatter([x], [y], s=900*v+60, facecolor='none', edgecolor=RED, lw=1.1, zorder=7)
    lab(ax, -.03, .0, '$(4,0,0)$', ha='right', va='center')
    lab(ax, 1.03, .0, '$(0,4,0)$', ha='left', va='center')
    lab(ax, .5, .91, '$(0,0,4)$', ha='center', va='bottom')
    ax.set_xlim(-.2, 1.2); ax.set_ylim(-.16, 1.0)
tags(fig, axes)
facts['sum'] = [sum(mult(k) for k in pts), sum(hyp(k) for k in pts)]
save(fig, HERE(__file__), 'figure', facts)
