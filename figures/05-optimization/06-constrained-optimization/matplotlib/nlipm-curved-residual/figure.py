from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Linearization of the curved constraint at an infeasible point of the running example.
x0 = np.array([2., 1.]); s0 = np.array([1., 3.]); l0 = np.array([1., 1/3])
mt = .2*(s0@l0)/2
d = direction(x0, s0, l0, mt)
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
region(a)
u = np.linspace(.2, 2.6, 50)
a.plot(u, 3+4*(u-2)+1, color=YELLOW, lw=1.6, ls='--', zorder=3)
xp = x0 + d['dx']
a.annotate('', xy=xp, xytext=x0, arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.3), zorder=5)
a.plot(*x0, 'o', color=GREEN, ms=4.5, zorder=6); a.plot(*xp, 'o', mfc='white', mec=GREEN, ms=4.5, zorder=6); a.plot(*XSTAR, 'o', color=RED, ms=4.5, zorder=6)
a.text(2.08, .72, '$x^{(0)}$', fontsize=7.5); a.text(xp[0]+.1, xp[1]-.42, '$x^{(0)}+\\Delta x$', fontsize=7.5)
a.set_xlim(-.3, 2.8); a.set_ylim(-.3, 3.6); tag(a, '$x_1$', '(a)'); a.set_ylabel('$x_2$', labelpad=1)
al = np.linspace(0, 1, 100); r = np.array([(g(x0+t*d['dx'])+s0+t*d['ds'])[0] for t in al])
b.plot(al, (1-al)*d['rp'][0], color=YELLOW, lw=1.6, ls='--'); b.plot(al, r, color=RED, lw=1.5)
b.set_xlim(0, 1); b.set_ylim(0, None); tag(b, '$\\alpha$', '(b)'); b.set_ylabel('$r_{\\rm p,1}$', labelpad=1)
save(fig, OUT, 'figure', {'dx': d['dx'].tolist(), 'ds': d['ds'].tolist(), 'rp': d['rp'].tolist(), 'r_at_1': float(r[-1]), 'dx1_sq': float(d['dx'][0]**2)})
