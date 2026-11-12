from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# (a) densities f_n(x) = 1 + sin(2 pi n x) on [0,1] for n = 1 (yellow) and n = 6 (blue);
#     they converge weakly to Unif(0,1) (purple dashed) but h(f_n) = ln2 - 1 = -0.307 for every n.
# (b) differential entropy h(f_n) (blue points, numerical quadrature) versus the limit's h = 0 (purple);
#     green points: entropy ln n of the uniform distribution on {1/n,...,1}, which also converges weakly to Unif(0,1).
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.3)
x = np.linspace(0, 1, 2000)
a.plot(x, 1+np.sin(2*math.pi*x), color=YELLOW, lw=1.2); a.plot(x, 1+np.sin(12*math.pi*x), color=BLUE, lw=1.0)
a.axhline(1, color=PURPLE, lw=.85, ls=DASH)
lab(a, .27, 2.05, '$n=1$', YELLOW); lab(a, .55, 2.05, '$n=6$', BLUE)
a.set_xlim(0, 1); a.set_ylim(0, 2.3); axlab(a, '$x$', '密度')
u = np.linspace(0, 1, 400001)
def h(n):
    f = 1+np.sin(2*math.pi*n*u); g = np.where(f > 0, f*np.log(np.where(f > 0, f, 1)), 0); return -float(np.trapezoid(g, u))
ns = np.arange(1, 9); hv = [h(int(k)) for k in ns]
b.plot(ns, hv, 'o', color=BLUE, ms=3.2, mew=0); b.plot(ns, np.log(ns), 'o', color=GREEN, ms=3.2, mew=0)
b.axhline(0, color=PURPLE, lw=.85, ls=DASH)
lab(b, 5.2, -.55, r'$h(f_n)=\ln 2-1$', BLUE); lab(b, 4.9, 1.85, r'$H=\ln n$', GREEN); lab(b, 2.3, .08, r'$h(\mathrm{Unif})=0$', PURPLE)
b.set_xlim(.5, 8.5); b.set_ylim(-.8, 2.3); axlab(b, '$n$', 'nat')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'h_fn': hv, 'ln2-1': LN2-1})
