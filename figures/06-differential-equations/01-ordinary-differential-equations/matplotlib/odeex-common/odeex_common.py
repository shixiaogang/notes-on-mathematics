"""Shared helpers for the chapter on existence of solutions (prefix odeex)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.patches import Rectangle
STROKE = '#4C4D4F'
__all__ = ['figure','save','BLUE','GREEN','YELLOW','RED','PURPLE','INK','MUTED','GRID','BLUE_FILL','GREEN_FILL','YELLOW_FILL','RED_FILL','PURPLE_FILL','STROKE','np','Rectangle','panel','tags','rk4','field','dot']
def panel(fig, left, right, top, bottom, wspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def rk4(f, t0, x0, t1, n):
    """Classical RK4 on a uniform grid; x0 may be a scalar or an array."""
    t = np.linspace(t0, t1, n+1); h = (t1-t0)/n
    x = np.empty((n+1,)+np.shape(x0)); x[0] = x0
    for i in range(n):
        k1 = np.asarray(f(t[i], x[i])); k2 = np.asarray(f(t[i]+h/2, x[i]+h/2*k1))
        k3 = np.asarray(f(t[i]+h/2, x[i]+h/2*k2)); k4 = np.asarray(f(t[i]+h, x[i]+h*k3))
        x[i+1] = x[i]+h/6*(k1+2*k2+2*k3+k4)
    return t, x
def field(ax, f, nt=17, nx=11, length=.035, color=None, lw=.7):
    """Short segments of the direction field, equal display length in axes units."""
    fig = ax.figure; xl, yl = ax.get_xlim(), ax.get_ylim(); p = ax.get_position()
    W, H = fig.get_figwidth()*p.width, fig.get_figheight()*p.height
    ts = np.linspace(xl[0], xl[1], nt+2)[1:-1]; xs = np.linspace(yl[0], yl[1], nx+2)[1:-1]
    sx, sy = W/(xl[1]-xl[0]), H/(yl[1]-yl[0]); L = length*W; segs = []
    for t in ts:
        for x in xs:
            s = f(t, x); dx, dy = 1.0*sx, s*sy; n = np.hypot(dx, dy)
            ux, uy = dx/n*L/2/sx, dy/n*L/2/sy
            segs.append([(t-ux, x-uy), (t+ux, x+uy)])
    ax.add_collection(LineCollection(segs, colors=color or GRID, linewidths=lw, zorder=1))
def dot(ax, t, x, ms=4.4, color=None, zorder=6):
    ax.plot([t], [x], 'o', ms=ms, color=color or RED, mew=0, zorder=zorder, clip_on=False)
