from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# (a) Exp(1) density (blue) and the law of the clipped generator min(X, 2): same density on [0,2) plus an atom of
#     mass e^{-2} at x = 2 (yellow bar, height = mass); the tail mass removed from (2, inf) is shaded light blue.
#     d_TV = e^{-2}.
# (b) Perturbed law (1-eps) Exp(1) + eps delta_c with c = 1/eps^2; d_TV <= eps.  Absolute bias for the bounded
#     f = 1{x > 1}: eps(1 - e^{-1}) (blue); for f(x) = x: eps(c - 1) = 1/eps - eps (yellow); reference line eps (purple dashed).
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.3)
x = np.linspace(0, 5, 400)
a.fill_between(x[x >= 2], 0, np.exp(-x[x >= 2]), color=BLUE_FILL, lw=0)
a.plot(x, np.exp(-x), color=BLUE, lw=1.3)
m = math.exp(-2); a.plot([2, 2], [0, m], color=YELLOW, lw=2.6, solid_capstyle='butt'); dot(a, 2, m, YELLOW, ms=4)
lab(a, 2.12, m+.03, r'$\mathrm{e}^{-2}$', YELLOW); lab(a, 3.0, .2, '被移走的尾部', BLUE)
a.set_xlim(0, 5); a.set_ylim(0, 1.05); a.set_xticks([0, 2, 4]); a.set_yticks([0, .5, 1]); axlab(a, '$x$')
e = np.logspace(-4, -.5, 100)
b.loglog(e, e*(1-math.exp(-1)), color=BLUE, lw=1.3)
b.loglog(e, 1/e - e, color=YELLOW, lw=1.4)
b.loglog(e, e, color=PURPLE, lw=.9, ls=DASH)
lab(b, 1.5e-4, 2e2, '$f(x)=x$', YELLOW); lab(b, 3e-3, 3e-4, r'$f=\mathbf{1}_{\{x>1\}}$', BLUE); lab(b, 2e-2, 6e-2, r'$\varepsilon$', PURPLE)
b.set_xlim(1e-4, .3); b.set_ylim(1e-5, 1e5); logticks(b, [-4, -2], 'x'); logticks(b, [-4, 0, 4], 'y'); axlab(b, r'$\varepsilon$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'atom_mass': m})
