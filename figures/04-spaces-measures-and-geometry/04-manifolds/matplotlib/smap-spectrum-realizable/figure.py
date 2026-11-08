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

"""d12=d23=1: eigenvalues b/2 and (4a-b)/6 with a=1, b=d13^2 as d13 varies; three realizations."""
W, H = 112, 52
fig, ax = canvas(W, H)
# (a) three cases of the two-bar length vs d13
def case(cx, cy, d):
    s = 5.2  # mm per unit
    L = cx-d/2*s; R = cx+d/2*s
    t = np.linspace(0, 2*np.pi, 241)
    ax.plot(L+s*np.cos(t), cy+s*np.sin(t), color=BLUE, lw=.65, ls=(0,(2.2,1.8)))
    ax.plot(R+s*np.cos(t), cy+s*np.sin(t), color=BLUE, lw=.65, ls=(0,(2.2,1.8)))
    if d <= 2:
        h = np.sqrt(max(1-(d/2)**2, 0))
        mid = (cx, cy+s*h)
        ax.plot([L, mid[0], R], [cy, mid[1], cy], color=BLUE, lw=1.2, zorder=3)
        dot(ax, mid, BLUE)
    ax.plot([L, R], [cy, cy], color=(GREEN if d <= 2 else RED), lw=1.1, zorder=2)
    dot(ax, (L, cy), INK); dot(ax, (R, cy), INK)
case(16, 41, 1.2); case(16, 25.5, 2.0); case(24, 11.2, 3.0)
label(ax, (39, 41), '$d_{1,3}=1.2$', 7.5, MUTED, ha='left')
label(ax, (39, 25.5), '$d_{1,3}=2$', 7.5, MUTED, ha='left')
label(ax, (47, 11.2), '$d_{1,3}=3$', 7.5, RED, ha='left')
panel_tag(ax, 28, 1.7, '(a)'); panel_tag(ax, 88, 1.7, '(b)')
# (b) eigenvalues
x0, y0, w, h = 68, 12, 40, 36
d = np.linspace(0, 3.25, 400)
xlim, ylim = (0, 3.3), (-1.3, 5.6)
T = axes_box(ax, x0, y0, w, h, xlim, ylim)
axis(ax, T(0, ylim[0]), T(0, ylim[1])); axis(ax, T(0, 0), T(xlim[1], 0))
ax.plot(*T(d, d**2/2), color=BLUE, lw=1.4, zorder=3)
l2 = (4-d**2)/6
ax.plot(*T(d[l2 >= 0], l2[l2 >= 0]), color=GREEN, lw=1.4, zorder=3)
ax.plot(*T(d[l2 < 0], l2[l2 < 0]), color=RED, lw=1.4, zorder=3)
for xv, yv, c in ((2, 0, INK), (3, -5/6, RED), (3, 4.5, BLUE)):
    dot(ax, T(xv, yv), c)
label(ax, T(2.15, 3.2), '$d^2/2$', 7.5, BLUE, ha='right')
label(ax, T(.1, 1.15), '$(4-d^2)/6$', 7.5, GREEN, ha='left')
label(ax, T(3, -5/6)+np.array([-1.8,-1.6]), '$-5/6$', 7.5, RED, ha='right'); label(ax, T(3, 4.5)+np.array([1.6,-1.4]), '$9/2$', 7.5, BLUE, ha='left')
label(ax, T(2, -.42), '2', 7.5, MUTED); label(ax, T(3.3, .35), '$d_{1,3}$', 7.5, MUTED, ha='right')
label(ax, T(-.05, 5.6), r'$\lambda$', 7.5, MUTED, ha='right')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'a=1, b=d13^2: lambda=b/2 and (4a-b)/6'})
