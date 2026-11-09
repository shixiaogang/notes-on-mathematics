from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Indefinite barrier Hessian: Newton direction versus a shifted direction.
mu = .1
B = lambda u, v: v**2+.12*(u-.5)**2 - mu*np.log(u**2+v**2-1)
def gh(x):
    r = x@x-1; gr = np.array([.24*(x[0]-.5), 2*x[1]]) - mu*2*x/r
    H = np.diag([.24, 2.]) - mu*(2*np.eye(2)/r - 4*np.outer(x, x)/r**2)
    return gr, H
x0 = np.array([.35, 1.08]); gr, H = gh(x0); ev = np.linalg.eigvalsh(H)
dN = -np.linalg.solve(H, gr); delta = -ev[0]+.15; dR = -np.linalg.solve(H+delta*np.eye(2), gr)
fig, ax = figure(width_mm=88, height_mm=56)
u, v = np.meshgrid(np.linspace(-.8, 1.6, 600), np.linspace(.55, 1.65, 400)); r2 = u**2+v**2
with np.errstate(all='ignore'): Z = np.ma.masked_where(r2 <= 1.0005, B(u, v))
ax.fill_between([-.8, 1.6], .55, 1.65, color=BLUE_FILL, lw=0, zorder=0)
th = np.linspace(0, np.pi, 300); ax.fill(np.cos(th), np.sin(th), color='white', zorder=1); ax.plot(np.cos(th), np.sin(th), color=EDGE, lw=1.7, zorder=2)
ax.contour(u, v, Z, levels=np.arange(.72, 2.6, .12), colors=BLUE, linewidths=.7, zorder=1.5)
sc = .32/np.linalg.norm(dN) if np.linalg.norm(dN) > .32 else 1
ax.annotate('', xy=x0+sc*dN, xytext=x0, arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.4), zorder=5)
scr = .32/np.linalg.norm(dR)
ax.annotate('', xy=x0+scr*dR, xytext=x0, arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.4), zorder=5)
ax.plot(*x0, 'o', color=INK, ms=3.6, zorder=6)
ax.set_xlim(-.8, 1.6); ax.set_ylim(.55, 1.65); ax.set_aspect('equal'); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
save(fig, OUT, 'figure', {'x0': x0.tolist(), 'H': H.tolist(), 'eig': ev.tolist(), 'grad': gr.tolist(), 'dN': dN.tolist(), 'delta': delta, 'dR': dR.tolist(), 'dec_N': float(gr@dN), 'dec_R': float(gr@dR)})
