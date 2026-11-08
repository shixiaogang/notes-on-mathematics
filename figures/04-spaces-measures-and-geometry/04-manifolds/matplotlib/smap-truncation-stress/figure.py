from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/04-spaces-measures-and-geometry/04-manifolds/matplotlib/mfd-common"))
from mfd3d import *
def axes_box(ax, x0, y0, w, h, xlim, ylim):
    """Plain axes at mm position on the canvas (data coordinates in the returned callable)."""
    sx, sy = w/(xlim[1]-xlim[0]), h/(ylim[1]-ylim[0])
    return (lambda x, y: (x0+(np.asarray(x)-xlim[0])*sx, y0+(np.asarray(y)-ylim[0])*sy))
def axis(ax, a, b, **kw):
    arrow(ax, a, b, color=MUTED, lw=.75, scale=5.5, zorder=2)

"""Truncation of the three-point reconstruction to one dimension, and the stress profile."""
W, H = 112, 46
fig, ax = canvas(W, H)
y = np.array([[1, 1/3], [0, -2/3], [-1, 1/3]])
cx, cy, s = 28, 24, 14.5
P = lambda p: (cx+s*np.asarray(p)[0], cy+s*np.asarray(p)[1])
axis(ax, (cx-23, cy), (cx+23, cy)); axis(ax, (cx, cy-14), (cx, cy+12))
closed = np.r_[y, y[:1]]
ax.plot(*zip(*[P(p) for p in closed]), color=GREEN, lw=1.1, zorder=3)
names = [r'$\mathbf{y}_1$', r'$\mathbf{y}_2$', r'$\mathbf{y}_3$']
for p, nm in zip(y, names):
    a = P(p); b = P((p[0], 0))
    if abs(p[1]) > 0:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=MUTED, lw=.7, ls=(0, (2.2, 1.8)), zorder=2)
    dot(ax, a, GREEN); dot(ax, b, BLUE, hollow=False)
label(ax, P(y[0])+np.array([3.4, 1.4]), names[0], 7.5, GREEN); label(ax, P(y[1])+np.array([3.8, -.8]), names[1], 7.5, GREEN); label(ax, P(y[2])+np.array([-3.4, 1.4]), names[2], 7.5, GREEN)
label(ax, P((1, 0))+np.array([1.2, -2.6]), '1', 7.5, BLUE); label(ax, P((0, 0))+np.array([1.4, -2.6]), '0', 7.5, BLUE); label(ax, P((-1, 0))+np.array([-1.2, -2.6]), '$-1$', 7.5, BLUE)
panel_tag(ax, 28, 1.7, '(a)')
# (b) stress
x0, y0, w, h = 72, 9, 37, 34
xlim, ylim = (.6, 1.65), (0, .75)
T = axes_box(ax, x0, y0, w, h, xlim, ylim)
axis(ax, T(xlim[0], 0), T(xlim[1], 0)); axis(ax, T(xlim[0], 0), T(xlim[0], ylim[1]))
sv = np.linspace(.62, 1.62, 400); st = 2*(sv-np.sqrt(2))**2+(2*sv-2)**2; keep = st <= .72; sv, st = sv[keep], st[keep]
ax.plot(*T(sv, st), color=BLUE, lw=1.4, zorder=3)
s1, sopt = 1.0, (2+np.sqrt(2))/3
for sx, c in ((s1, GREEN), (sopt, RED)):
    f = 2*(sx-np.sqrt(2))**2+(2*sx-2)**2
    ax.plot(*T([sx, sx], [0, f]), color=c, lw=.75, ls=(0, (2.2, 1.8)), zorder=2)
    dot(ax, T(sx, f), c)
label(ax, T(s1, 0)+np.array([0, -2.7]), '1', 7.5, GREEN); label(ax, T(sopt, 0)+np.array([0, -2.7]), '1.14', 7.5, RED)
label(ax, T(s1, .343)+np.array([-1.5, 2]), '0.343', 7.5, GREEN, ha='right'); label(ax, T(sopt, .229)+np.array([.8, -2.4]), '0.229', 7.5, RED, ha='left')
label(ax, T(1.63, 0)+np.array([-.5, 2]), '$s$', 7.5, MUTED, ha='right')
panel_tag(ax, 90, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'y=(1,1/3),(0,-2/3),(-1,1/3); stress(s)=2(s-sqrt2)^2+(2s-2)^2'})
