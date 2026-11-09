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

"""Mirror data: M=diag(2,-8); best rotation -I, residuals; tr(R^T M)=-6 cos(theta)."""
W, H = 112, 46
fig, ax = canvas(W, H)
x = np.array([[1, 0], [0, 2], [-1, 0], [0, -2.0]]); y = x*np.array([1, -1]); rot = -x
s = 7.5; cx, cy = 28, 24
axis(ax, (cx-16, cy), (cx+16, cy)); axis(ax, (cx, cy-18), (cx, cy+18))
P = lambda p: (cx+s*p[0], cy+s*p[1])
for i in range(4):
    a = P(rot[i]); b = P(y[i])
    if np.linalg.norm(rot[i]-y[i]) > .1:
        ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='<->,head_length=.25,head_width=.12', color=RED, lw=.8, shrinkA=2.4, shrinkB=2.4, connectionstyle='arc3,rad=-.45'), zorder=5)
for i in range(4):
    dot(ax, P(y[i]), GREEN, size=2.0, zorder=5)
    dot(ax, P(rot[i]), BLUE, size=1.1, zorder=6)
panel_tag(ax, cx, 1.7, '(a)')
x0, y0, w, h = 66, 9, 42, 33
xlim, ylim = (0, 2*np.pi), (-7, 7.4)
T = axes_box(ax, x0, y0, w, h, xlim, ylim)
axis(ax, T(0, 0), T(xlim[1], 0)); axis(ax, T(0, ylim[0]), T(0, ylim[1]))
th = np.linspace(0, 2*np.pi, 400); ax.plot(*T(th, -6*np.cos(th)), color=BLUE, lw=1.4, zorder=3)
dot(ax, T(np.pi, 6), RED); label(ax, T(np.pi, 6)+np.array([0, 2.5]), '6', 7.5, RED)
ax.plot(*T([np.pi, np.pi], [0, 6]), color=RED, lw=.7, ls=(0, (2.2, 1.8)))
label(ax, T(np.pi, 0)+np.array([0, -2.6]), r'$\pi$', 7.5, MUTED); label(ax, T(xlim[1], 0)+np.array([-.2, 2.1]), r'$\theta$', 7.5, MUTED, ha='right')
label(ax, T(-.0, ylim[1])+np.array([1.4, -.7]), r'$\mathrm{tr}(\mathbf{R}^{T}\mathbf{M})$', 7.5, MUTED, ha='left')
panel_tag(ax, 87, 1.7, '(b)')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'y mirror of x; R=-I; tr(R^T M)=-6cos theta'})
