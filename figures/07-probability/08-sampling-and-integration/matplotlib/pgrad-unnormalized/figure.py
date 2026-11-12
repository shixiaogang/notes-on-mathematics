from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# State space {0,1,2}, unnormalized mass ptilde_theta(x) = h(x) e^{theta x}, h = (1,2,1); Z(theta) = (1+e^theta)^2.
# (a) ptilde at theta = 0 (blue) and theta = 0.5 (yellow): every bar grows or stays (a(x) = x >= 0).
# (b) normalized p_theta at the same two parameters: mass moves from x = 0 to x = 2, total stays 1.
# (c) a(x) = x (gray outline) and the score s(x) = a(x) - E_0[a] = x - 1 at theta = 0 (blue).
xs = np.array([0, 1, 2]); hh = np.array([1., 2., 1.])
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.07, right=.98, bottom=.3, top=.95, wspace=.38)
a, b, c = axs
facts = {}
for k, (th, col, fill) in enumerate([(0.0, BLUE, BLUE_FILL), (0.5, YELLOW, YELLOW_FILL)]):
    pt = hh*np.exp(th*xs); Z = pt.sum(); p = pt/Z
    a.bar(xs+(k-.5)*.36, pt, width=.34, color=fill, edgecolor=col, lw=.9)
    b.bar(xs+(k-.5)*.36, p, width=.34, color=fill, edgecolor=col, lw=.9)
    facts[f'Z_{th}'] = float(Z); facts[f'p_{th}'] = p.tolist()
for ax in (a, b, c):
    ax.set_xticks([0, 1, 2]); ax.set_xlim(-.6, 2.6); axlab(ax, r'$x$')
a.set_ylim(0, 3.6); a.set_yticks([0, 1, 2, 3])
b.set_ylim(0, .6); b.set_yticks([0, .25, .5]); b.set_yticklabels(['0', '0.25', '0.5'])
c.axhline(0, color=STROKE, lw=.6)
c.bar(xs-.18, xs, width=.34, color='white', edgecolor=STROKE, lw=.9)
c.bar(xs+.18, xs-1.0, width=.34, color=BLUE_FILL, edgecolor=BLUE, lw=.9)
c.set_ylim(-1.3, 2.3); c.set_yticks([-1, 0, 1, 2])
tags(fig, axs)
save(fig, HERE, 'figure', facts)
