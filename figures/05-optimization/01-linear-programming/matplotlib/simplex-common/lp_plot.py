"""Plot helpers for the two-dimensional examples of the simplex chapter."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

EDGE = '#4C4D4F'
# resource example: a'x <= b, profit p'x
RES_A = np.array([[1., 2.], [2., 1.], [0., 1.]])
RES_B = np.array([8., 10., 3.])
PROFIT = np.array([4., 5.])


def polygon(A, b):
    """Vertices (ccw) of {x: Ax<=b}; A,b must include the sign constraints."""
    A, b = np.asarray(A, float), np.asarray(b, float)
    pts = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            M = A[[i, j]]
            if abs(np.linalg.det(M)) < 1e-9:
                continue
            p = np.linalg.solve(M, b[[i, j]])
            if np.all(A @ p <= b + 1e-9) and not any(np.allclose(p, q) for q in pts):
                pts.append(p)
    pts = np.array(pts)
    c = pts.mean(0)
    return pts[np.argsort(np.arctan2(pts[:, 1] - c[1], pts[:, 0] - c[0]))]


def with_sign(A, b):
    return np.vstack([A, [[-1., 0.], [0., -1.]]]), np.concatenate([b, [0., 0.]])


def draw_region(ax, verts):
    ax.fill(verts[:, 0], verts[:, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.0, zorder=1)


def draw_line(ax, a, b, xlim, ylim, **kw):
    """Draw a1 x1 + a2 x2 = b, clipped to the axes box."""
    kw.setdefault('color', EDGE); kw.setdefault('lw', 0.85); kw.setdefault('zorder', 2)
    a1, a2 = a
    if abs(a2) < 1e-12:
        xs = np.array([b / a1] * 2); ys = np.array(ylim)
    else:
        xs = np.linspace(xlim[0], xlim[1], 400); ys = (b - a1 * xs) / a2
        m = (ys >= ylim[0]) & (ys <= ylim[1]); xs, ys = xs[m], ys[m]
    ax.plot(xs, ys, **kw)


def contours(ax, p, levels, xlim, ylim, **kw):
    kw.setdefault('colors', BLUE); kw.setdefault('linewidths', 0.8); kw.setdefault('zorder', 1.5)
    X, Y = np.meshgrid(np.linspace(xlim[0], xlim[1], 240), np.linspace(ylim[0], ylim[1], 240))
    ax.contour(X, Y, p[0] * X + p[1] * Y, levels=levels, linestyles='--', **kw)


def setup(ax, xlim, ylim, xticks=None, yticks=None, label='(x1)'):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if xticks is not None: ax.set_xticks(xticks)
    if yticks is not None: ax.set_yticks(yticks)
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    ax.set_ylabel('$x_2$', labelpad=1)
    ax.set_xlabel('$x_1$' if label == '(x1)' else '$x_1$\n' + label, labelpad=1)


def path(ax, pts, color=GREEN, lw=1.5, ms=3.6, zorder=5, **kw):
    pts = np.asarray(pts, float)
    for a, b in zip(pts[:-1], pts[1:]):
        ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=8), zorder=zorder)
    ax.plot(pts[:, 0], pts[:, 1], 'o', color=color, ms=ms, zorder=zorder + 1, **kw)


def opt_point(ax, p, ms=5):
    ax.plot([p[0]], [p[1]], 'o', color=RED, ms=ms, zorder=8)
