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

"""Grid image under rigid/affine/projective models.  Same data as the examples in section 30.3."""
W, H = 112, 30
fig, ax = canvas(W, H)
def grid(fun, n=4):
    lines = []
    t = np.linspace(0, 1, 60)
    for k in np.linspace(0, 1, n+1):
        lines.append(fun(np.stack([np.full_like(t, k), t], 1)))
        lines.append(fun(np.stack([t, np.full_like(t, k)], 1)))
    return lines
corners = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], float)
def draw(fun, cx, cy, s, colour, labels=False):
    for ln in grid(fun):
        ax.plot(cx+s*ln[:, 0], cy+s*ln[:, 1], color=colour, lw=.7, zorder=2)
    c = fun(corners)
    for k, p in enumerate(c):
        dot(ax, (cx+s*p[0], cy+s*p[1]), RED if k == 1 else colour, size=1.3)
    return c
ident = lambda p: p
R90 = np.array([[0, -1], [1, 0.0]])
rigid = lambda p: p@R90.T+np.array([3, 1.0])
A = np.array([[1.5, .5], [.5, 1.5]]); b = np.array([-.25, -.25])
aff = lambda p: p@A.T+b
Hm = np.array([[2, 0, 0], [0, 2, 0], [-1, -1, 3.0]])
def proj(p):
    z = np.c_[p, np.ones(len(p))]@Hm.T
    return z[:, :2]/z[:, 2:]
tags = ('(a)', '(b)', '(c)', '(d)')
draw(ident, 7, 8, 14.5, BLUE)
draw(rigid, 2.75, -6.5, 14.5, GREEN)
draw(aff, 60, 10, 10, GREEN)
draw(proj, 90, 8, 9, GREEN)
for x, tag in zip((14.2, 39, 67.5, 99), tags):
    panel_tag(ax, x, 1.7, tag)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'rigid R90 x + (3,1); affine A=[1.5,.5;.5,1.5], b=(-.25,-.25); projective H=[2,0,0;0,2,0;-1,-1,3]'})
