from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Approximate update X' = (1-h) X + sqrt(2h) xi, xi ~ N(0,1), intended target N(0,1).
# (a) variance of its invariant law 2/(2-h) for 0 < h < 2 (yellow) against target variance 1 (blue); red dot h = 0.5.
# (b) histogram of 10^5 steps of the chain with h = 0.5 started at 0 (seed 3121, green), target N(0,1) density (blue),
#     invariant N(0, 4/3) density (yellow).
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.28)
h = np.linspace(0.001, 1.9, 300)
a.plot(h, 2/(2-h), color=YELLOW, lw=1.4); a.axhline(1, color=BLUE, lw=1.2); a.axvline(2, color=STROKE, lw=.7, ls=DASH)
dot(a, .5, 4/3); lab(a, .3, 2.2, '$h=0.5$', RED)
lab(a, 1.0, 5.2, r'$2/(2-h)$', YELLOW)
a.set_xlim(0, 2.1); a.set_ylim(0, 8); a.set_xticks([0, 1, 2]); a.set_yticks([1, 4, 8]); axlab(a, '$h$')
rng = np.random.default_rng(3121); n = 10**5; xi = rng.standard_normal(n); x = 0.0; X = np.empty(n); hh = .5; c = math.sqrt(2*hh)
for t in range(n):
    x = (1-hh)*x + c*xi[t]; X[t] = x
bins = np.linspace(-4.5, 4.5, 46); hist, e = np.histogram(X, bins=bins, density=True)
b.bar(e[:-1], hist, width=e[1]-e[0], align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.5)
g = np.linspace(-4.5, 4.5, 300); b.plot(g, npdf(g), color=BLUE, lw=1.3); b.plot(g, npdf(g, 0, 4/3), color=YELLOW, lw=1.4)
b.set_xlim(-4.5, 4.5); b.set_ylim(0, .46); b.set_xticks([-4, 0, 4]); b.set_yticks([0, .2, .4]); axlab(b, '$x$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'sample_var_h05': float(X.var()), 'theory': 4/3, 'mean_x2': float((X**2).mean())})
