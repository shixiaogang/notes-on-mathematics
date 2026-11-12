from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# X ~ N(theta,1) at theta = 0, f(x) = 1{x > 0}.  Score s(x) = x - theta.
# (a) score s(x) (gray) and the single-sample estimator value f(x) s(x) (green): zero for x < 0, equal to x for x > 0.
# (b) d p_theta / d theta = p s (blue curve); the part with f = 1 (x > 0) is shaded; its area is phi(0) = 0.3989,
#     which equals J'(0).  The part x < 0 (dashed) carries f = 0 and does not contribute.
x = np.linspace(-3.2, 3.2, 800)
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.26)
a, b = axs
a.axhline(0, color=STROKE, lw=.6)
a.plot(x, x, color=STROKE, lw=.9, ls=DASH)
a.plot(x, np.where(x > 0, x, 0), color=GREEN, lw=1.4)
lab(a, -3.0, -1.1, r'$s(x)=x$', STROKE); lab(a, .9, 2.5, r'$f(x)\,s(x)$', GREEN)
a.set_xlim(-3.2, 3.2); a.set_ylim(-3.2, 3.2); a.set_xticks([-2, 0, 2]); a.set_yticks([-2, 0, 2])
axlab(a, r'$x$')
d = npdf(x)*x
b.axhline(0, color=STROKE, lw=.6)
b.fill_between(x, d, 0, where=x >= 0, color=BLUE_FILL, lw=0)
b.plot(x[x >= 0], d[x >= 0], color=BLUE, lw=1.4)
b.plot(x[x < 0], d[x < 0], color=BLUE, lw=1.0, ls=DASH)
xx = np.linspace(0, 12, 20001); area = float(np.trapezoid(npdf(xx)*xx, xx))
lab(b, 1.15, .07, f'{area:.4f}', BLUE)
b.axvline(0, color=RED, lw=1.1)
b.set_xlim(-3.2, 3.2); b.set_ylim(-.3, .3); b.set_xticks([-2, 0, 2]); b.set_yticks([-.2, 0, .2])
axlab(b, r'$x$')
tags(fig, axs)
save(fig, HERE, 'figure', {'area_x_pos': area, 'phi0': float(npdf(0.0))})
