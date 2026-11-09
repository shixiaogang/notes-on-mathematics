from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Barrier of a nonconvex constraint: outside of the unit disc.
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2, width_ratios=[1.35, 1])
mu = .1
u, v = np.meshgrid(np.linspace(-2.2, 2.2, 700), np.linspace(-1.6, 1.6, 600))
r2 = u**2+v**2
with np.errstate(all='ignore'):
    Z = v**2+.12*(u-.5)**2 - mu*np.log(r2-1)
Z = np.ma.masked_where(r2 <= 1.0005, Z)
a.fill_between([-2.2, 2.2], -1.6, 1.6, color=BLUE_FILL, lw=0, zorder=0)
th = np.linspace(0, 2*np.pi, 300); a.fill(np.cos(th), np.sin(th), color='white', zorder=1); a.plot(np.cos(th), np.sin(th), color=EDGE, lw=1.7, zorder=2)
a.contour(u, v, Z, levels=[.08, .14, .22, .32, .5, .8, 1.2, 1.8], colors=BLUE, linewidths=.75, zorder=1.5)
h = lambda t: .12*(t-.5)**2 - mu*np.log(t**2-1)
tr = np.linspace(1.0005, 2.2, 40000); tl = -tr
xr, xl = tr[np.argmin(h(tr))], tl[np.argmin(h(tl))]
a.plot([xr], [0], 'o', color=GREEN, ms=4.5, zorder=6); a.plot([xl], [0], 'o', color=GREEN, ms=4.5, zorder=6)
a.plot([1.], [0], 'o', color=RED, ms=4.5, zorder=7)
a.set_xlim(-2.2, 2.2); a.set_ylim(-1.6, 1.6); a.set_aspect('equal'); tag(a, '$x_1$', '(a)'); a.set_ylabel('$x_2$', labelpad=1)
w = np.linspace(-1.2, 1.2, 400)
b.plot(w, -np.log(1.25+w**2), color=RED, lw=1.5); b.plot(w, -np.log(1.75-w**2), color=BLUE, lw=1.5)
b.text(.55, -.72, '$g=1-\\|x\\|_2^2$', fontsize=7.5, color=INK, ha='center'); b.text(.05, .5, '$g=\\|x\\|_2^2-4$', fontsize=7.5, color=INK, ha='center')
b.set_xlim(-1.25, 1.25); tag(b, '$w$', '(b)'); b.set_ylabel('$-\\log(-g(1.5,\\,w))$', labelpad=1)
save(fig, OUT, 'figure', {'formula': 'f=x2^2+0.12(x1-0.5)^2,g=1-|x|^2,mu=.1', 'x_right': xr, 'x_left': xl})
