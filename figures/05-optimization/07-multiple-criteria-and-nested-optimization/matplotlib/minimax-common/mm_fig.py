"""Shared helpers for the minimax chapter's Matplotlib figures."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
EDGE = '#4C4D4F'
def setup(ax, xlim, ylim, xt=None, yt=None, xl='$x$', yl='$y$', equal=False):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if equal: ax.set_aspect('equal')
    if xt is not None: ax.set_xticks(list(xt))
    if yt is not None: ax.set_yticks(list(yt))
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    ax.set_xlabel(xl, labelpad=1); ax.set_ylabel(yl, labelpad=1)
    ax.tick_params(length=2.5, width=.7, pad=1.5)
def panels(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None); fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.012):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def dot(ax, p, color=RED, ms=5, z=7): ax.plot([p[0]], [p[1]], 'o', color=color, ms=ms, mew=0, zorder=z)
def hollow(ax, p, color=MUTED, ms=4.8, z=7): ax.plot([p[0]], [p[1]], 'o', mfc='white', mec=color, mew=1, ms=ms, zorder=z)
def arrow(ax, a, b, color=GREEN, lw=1.2, ms=8, z=5):
    ax.annotate('', xy=tuple(b), xytext=tuple(a), arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=ms), zorder=z)
def path(ax, P, color=GREEN, lw=1.2, ms=3, z=4, ls='-'):
    P = np.asarray(P); ax.plot(P[:, 0], P[:, 1], ls, color=color, lw=lw, zorder=z); ax.plot(P[:, 0], P[:, 1], 'o', color=color, ms=ms, mew=0, zorder=z+.1)
A = np.array([[0., 1.], [-1., 0.]])   # F(z)=Az for f=xy
E2 = np.eye(2)
def gda(J, a, T, z0):
    z = np.array(z0, float); out = [z.copy()]
    for _ in range(T): z = z-a*J@z; out.append(z.copy())
    return np.array(out)
def alt_xy(a, T, z0):
    x, y = z0; out = [(x, y)]
    for _ in range(T):
        x = x-a*y; y = y+a*x; out.append((x, y))
    return np.array(out)
def eg(J, a, T, z0):
    z = np.array(z0, float); out = [z.copy()]
    for _ in range(T):
        t = z-a*J@z; z = z-a*J@t; out.append(z.copy())
    return np.array(out)
def ogda(J, a, T, z0):
    z = np.array(z0, float); zp = z.copy(); out = [z.copy()]
    for _ in range(T):
        n = z-2*a*J@z+a*J@zp; zp, z = z, n; out.append(z.copy())
    return np.array(out)
def rho(M): return float(max(abs(np.linalg.eigvals(M))))
