from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Nonconvex one-dimensional path: f'(x)=(x-1)(x-3)(x-4), x>0.
dF = lambda x: (x-1)*(x-3)*(x-4)
ddF = lambda x: (x-3)*(x-4)+(x-1)*(x-4)+(x-1)*(x-3)
Fv = lambda x: x**4/4-8*x**3/3+19*x**2/2-12*x
fig, (a, b) = figure(width_mm=112, height_mm=54, ncols=2)
x = np.linspace(.2, 5.1, 500); a.plot(x, Fv(x)-Fv(1), color=BLUE, lw=1.4)
a.plot([1], [0], 'o', color=RED, ms=4.8, zorder=6); a.plot([4], [Fv(4)-Fv(1)], 'o', mfc='white', mec=RED, ms=4.8, zorder=6)
a.axvline(0, color=EDGE, lw=1.7); a.set_xlim(-.05, 5.1); a.set_ylim(-.6, 6.5); tag(a, '$x$', '(a)'); a.set_ylabel('$f(x)-f(1)$', labelpad=1)
xs = np.linspace(1.0001, 2.9999, 4000); mu = xs*dF(xs); B2 = ddF(xs)+mu/xs**2; i = np.argmax(mu)
b.plot(mu[:i+1], xs[:i+1], color=YELLOW, lw=1.7); b.plot(mu[i:], xs[i:], color=YELLOW, lw=1.3, ls='--')
xr = np.linspace(4.0001, 5.6, 2000); mr = xr*dF(xr); b.plot(mr, xr, color=GREEN, lw=1.7)
b.plot([mu[i]], [xs[i]], 'o', color=RED, ms=4.5, zorder=6)
b.plot([0], [1], 'o', color=RED, ms=4.5, clip_on=False, zorder=7); b.plot([0], [4], 'o', mfc='white', mec=RED, ms=4.5, clip_on=False, zorder=7)
b.text(mu[i]+.25, xs[i], '折叠点', fontsize=7.5, va='center')
b.text(2.6, 4.55, '大参数一侧延伸来的路径', fontsize=7.5)
b.set_xlim(0, 7); b.set_ylim(.5, 5.7); tag(b, '$\\mu$', '(b)'); b.set_ylabel('$x$', labelpad=1)
save(fig, OUT, 'figure', {'fold_mu': float(mu[i]), 'fold_x': float(xs[i]), 'f4-f1': float(Fv(4)-Fv(1)), 'B2_sign_change_at_fold': bool(abs(B2[i])<1e-2)})
