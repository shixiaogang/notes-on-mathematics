"""Plot helpers for the worked examples of the linear programming chapter."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

EDGE = '#4C4D4F'
# Workshop example: max 3x1+2x2, x1+x2<=4 (hours), 2x1+x2<=6 (material), x>=0.
WS_A = np.array([[1., 1.], [2., 1.]])
WS_B = np.array([4., 6.])
WS_P = np.array([3., 2.])
SIGN = np.array([[-1., 0.], [0., -1.]])


def polygon(G, h):
    """Vertices (ccw) of the bounded set {x: Gx<=h} in the plane."""
    G, h = np.asarray(G, float), np.asarray(h, float)
    pts = []
    for i in range(len(G)):
        for j in range(i+1, len(G)):
            M = G[[i, j]]
            if abs(np.linalg.det(M)) < 1e-9:
                continue
            p = np.linalg.solve(M, h[[i, j]])
            if np.all(G @ p <= h + 1e-9) and not any(np.allclose(p, q) for q in pts):
                pts.append(p)
    pts = np.array(pts)
    c = pts.mean(0)
    return pts[np.argsort(np.arctan2(pts[:, 1]-c[1], pts[:, 0]-c[0]))]


def workshop(b=WS_B):
    return polygon(np.vstack([WS_A, SIGN]), np.concatenate([b, [0., 0.]]))


def region(ax, V, fc=BLUE_FILL, ec=BLUE, lw=.95, z=1):
    ax.fill(V[:, 0], V[:, 1], facecolor=fc, edgecolor=ec, lw=lw, zorder=z)


def line(ax, a, b, xlim, ylim, **kw):
    kw.setdefault('color', EDGE); kw.setdefault('lw', .85); kw.setdefault('zorder', 2)
    if abs(a[1]) < 1e-12:
        ax.plot([b/a[0]]*2, ylim, **kw); return
    xs = np.linspace(xlim[0], xlim[1], 800); ys = (b-a[0]*xs)/a[1]
    m = (ys >= ylim[0]) & (ys <= ylim[1])
    ax.plot(xs[m], ys[m], **kw)


def levels(ax, p, vals, xlim, ylim, **kw):
    kw.setdefault('color', BLUE); kw.setdefault('lw', .85); kw.setdefault('ls', (0, (4, 2))); kw.setdefault('zorder', 1.6)
    for v in vals:
        line(ax, p, v, xlim, ylim, **kw)


def arrow(ax, a, b, color=GREEN, lw=1.4, ms=8, z=5):
    ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=ms), zorder=z)


def dot(ax, p, color=INK, ms=3.6, z=6):
    ax.plot([p[0]], [p[1]], 'o', color=color, ms=ms, mew=0, zorder=z)


def hollow(ax, p, color=RED, ms=4.6, z=6):
    ax.plot([p[0]], [p[1]], 'o', mfc='white', mec=color, mew=1, ms=ms, zorder=z)


def setup(ax, xlim, ylim, xt=None, yt=None, xl='$x_1$', yl='$x_2$'):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if xt is not None: ax.set_xticks(list(xt))
    if yt is not None: ax.set_yticks(list(yt))
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    ax.set_xlabel(xl, labelpad=1); ax.set_ylabel(yl, labelpad=1)


def panels(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)


def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
