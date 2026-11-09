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

"""Affine least-squares fit on the square; ill-conditioned source; non-invertible exact solution."""
W, H = 112, 46
fig, ax = canvas(W, H)
y = np.array([[0, 0], [1, 0], [0, 1], [2, 2.0]]); fit = y-np.array([1, -1, -1, 1])[:, None]*np.array([1, 1])/4
order = [0, 1, 3, 2]
# (a)
s, cx, cy = 13.5, 9, 9.5
P = lambda p: cx+s*np.asarray(p)
ax.plot(*P(y[order+[0]]).T, color=GREEN, lw=1.1, zorder=3); ax.plot(*P(fit[order+[0]]).T, color=BLUE, lw=1.1, zorder=3)
for a, b in zip(y, fit):
    arrow(ax, P(b), P(a), color=RED, lw=.85, scale=5, zorder=5)
for a in y: dot(ax, P(a), GREEN)
for a in fit: dot(ax, P(a), BLUE, size=1.25)
label(ax, P(y[3])+np.array([-3.4, .8]), r'$\mathbf{y}_4$', 7.5, GREEN)
label(ax, P(fit[3])+np.array([3, -.6]), r'$\widehat{\mathbf{y}}_4$', 7.5, BLUE)
panel_tag(ax, 24, 1.7, '(a)')
# (b) source triangle with epsilon=.1; a target perturbation eta on y_3 changes the 2nd column by eta/eps
s, cx, cy = 20, 54, 9.5
P = lambda p: np.array([cx+s*p[0], cy+s*p[1]])
eps = .12
src = np.array([[0, 0], [1, 0], [0, eps]])
ax.fill(*P(src.T).T.T if 0 else zip(*[P(p) for p in src]), color=BLUE_FILL, zorder=1)
ax.plot(*zip(*[P(p) for p in np.r_[src, src[:1]]]), color=BLUE, lw=1.1, zorder=3)
for p in src: dot(ax, P(p), BLUE)
ax.annotate('', xy=P((0, eps)), xytext=P((0, 0)), arrowprops=dict(arrowstyle='<->,head_length=.25,head_width=.12', color=RED, lw=.8, shrinkA=2.5, shrinkB=2.5), zorder=6)
label(ax, P((0, eps/2))+np.array([-2.0, 0]), r'$\varepsilon$', 7.5, RED, ha='right')
panel_tag(ax, 63, 1.7, '(b)')
# (c) triangle collapses to the axis
s, cx, cy = 10.5, 86, 13
P = lambda p: np.array([cx+s*p[0], cy+s*p[1]])
tgt = np.array([[0, 0], [1, 0], [2, 0]])
axis(ax, P((-.3, 0)), P((2.25, 0)))
ax.plot(*zip(*[P(p) for p in tgt[[0, 2]]]), color=RED, lw=1.25, zorder=3)
for p in tgt: dot(ax, P(p), GREEN)
xlbl = [r'$(0,0)$', r'$(1,0)$', r'$(2,0)$']
for p, l in zip(tgt, xlbl): label(ax, P(p)+np.array([0, -2.8]), l, 7, GREEN)
panel_tag(ax, 96.5, 1.7, '(c)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'affine fit on square; residual c^T Y/4 pattern; epsilon=.12 source; target (0,0),(1,0),(2,0)'})
