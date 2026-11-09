from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# One-dimensional boundary example: min x s.t. x^2-1<=0.
B = lambda x, m: x - m*np.log(1-x**2)
cen = lambda m: m - np.sqrt(m**2+1)
fig, (a, b) = figure(width_mm=112, height_mm=54, ncols=2)
x = np.linspace(-.9995, .9995, 900)
for m, ls in ((.75, '-'), (5/12, '--'), (.1, ':')):
    a.plot(x, B(x, m), color=BLUE, lw=1.4, ls=ls); a.plot([cen(m)], [B(cen(m), m)], 'o', color=GREEN, ms=4, zorder=5)
a.plot([-1], [-1], 'o', color=RED, ms=5, zorder=6, clip_on=False)
for v in (-1, 1): a.axvline(v, color=EDGE, lw=1.7)
a.set_xlim(-1.12, 1.12); a.set_ylim(-1.3, 2.4); tag(a, '$x$', '(a)')
m1 = .05; x0 = -.5
d1 = 1 + m1*2*x0/(1-x0**2); d2 = 2*m1*(1+x0**2)/(1-x0**2)**2; nt = -d1/d2
xx = np.linspace(-5.4, .95, 900); q = B(x0, m1) + d1*(xx-x0) + .5*d2*(xx-x0)**2
xb = np.linspace(-.9995, .95, 700)
b.plot(xx, q, color=YELLOW, lw=1.6); b.plot(xb, B(xb, m1), color=BLUE, lw=1.4)
for v in (-1, 1): b.axvline(v, color=EDGE, lw=1.7)
b.plot([x0], [B(x0, m1)], 'o', color=GREEN, ms=4.2, zorder=6)
b.plot([x0+nt], [B(x0, m1)+d1*nt+.5*d2*nt**2], 'o', color=RED, ms=4.5, zorder=6)
b.plot([cen(m1)], [B(cen(m1), m1)], 'o', mfc='white', mec=GREEN, ms=4.2, zorder=6)
b.text(x0+nt, -2.75, '$x_{\\rm N}=-4.7$', fontsize=7.5, ha='center'); b.text(-.42, -.1, '$x^{(0)}$', fontsize=7.5)
b.set_xlim(-5.4, 1.2); b.set_ylim(-3.1, 1.2); tag(b, '$x$', '(b)')
save(fig, OUT, 'figure', {'formula': 'B=x-mu*log(1-x^2)', 'center(3/4)': cen(.75), 'center(5/12)': cen(5/12), 'center(.05)': cen(.05), 'newton_step_mu.05': nt})
