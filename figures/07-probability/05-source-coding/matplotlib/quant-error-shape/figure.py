from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# (a) Error e(x) = Q(x) - x of the N = 8, step 1 mid-rise uniform quantizer (green); in range |e| <= 1/2
#     (gray band), beyond L = 4 the error grows linearly (red).
# (b) Exact density of the normalized rounding error E/delta given no overload, for Laplace(0,1):
#     step 1 with N = 8 (yellow) and step 1/4 with N = 32 (green, same range L = 4); blue: uniform density 1.
x = np.linspace(-6.5, 6.5, 6001); e = uniform_q(x, 8, 1.0) - x
fig, (a, b) = figure(width_mm=108, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.3)
a.fill_between([-4, 4], -.5, .5, color=BLUE_FILL, lw=0)
inr = np.abs(x) <= 4
a.plot(np.where(inr, x, np.nan), np.where(inr, e, np.nan), color=GREEN, lw=1.0)
a.plot(np.where(x > 4, x, np.nan), np.where(x > 4, e, np.nan), color=RED, lw=1.4)
a.plot(np.where(x < -4, x, np.nan), np.where(x < -4, e, np.nan), color=RED, lw=1.4)
a.axhline(0, color=STROKE, lw=.6)
for t in (-4, 4): a.axvline(t, color=STROKE, lw=.85, ls=DASH)
a.set_xlim(-6.5, 6.5); a.set_ylim(-3, 3); a.set_xlabel('$x$', labelpad=1)
lab(a, 4.2, 2.3, '$L$', MUTED); lab(a, -6.2, -2.6, '$-L$', MUTED)
u = np.linspace(-.5, .5, 401)
def dens(N, d):
    L = N*d/2; cs = -L + (np.arange(N)+.5)*d; P = mass(-L, L)
    return np.array([sum(d*pdf(c - ui*d) for c in cs) for ui in u])/P
# Q(x) - x = c - x = u*d  ->  x = c - u*d
b.axhline(1, color=BLUE, lw=1.4)
b.plot(u, dens(8, 1.0), color=YELLOW, lw=1.6); b.plot(u, dens(32, .25), color=GREEN, lw=1.2)
lab(b, -.47, 1.45, '$\\Delta=1$', YELLOW); lab(b, .05, 1.08, '$\\Delta=1/4$', GREEN)
b.set_xlim(-.5, .5); b.set_ylim(0, 1.7); b.set_xticks([-.5, 0, .5]); b.set_xlabel('$E/\\Delta$', labelpad=1)
tags(fig, (a, b))
save(fig, HERE, 'figure', {'dens_delta1_at_-0.5_0_0.5': [float(dens(8, 1.0)[i]) for i in (0, 200, 400)],
     'dens_delta025_at_-0.5_0_0.5': [float(dens(32, .25)[i]) for i in (0, 200, 400)]})
