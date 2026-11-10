"""Shared helpers for the figures of the chapter on initial value problems."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.collections import LineCollection

STROKE = '#4C4D4F'
FIELD = '#A9B0BA'


def panel(fig, left, right, top, bottom, wspace=.3, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015):
    """Put (a), (b), ... centred below each panel on one baseline."""
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position()
        fig.text((p.x0 + p.x1)/2, y, s, ha='center', va='bottom')


def slope_field(ax, f, nt=17, nx=11, length_mm=2.8, skip=None, color=FIELD, lw=.6):
    """Short segments of equal printed length with slope f(t, x). Call after limits and layout."""
    fig = ax.figure
    p = ax.get_position()
    W = p.width*fig.get_figwidth()*25.4
    H = p.height*fig.get_figheight()*25.4
    (t0, t1), (x0, x1) = ax.get_xlim(), ax.get_ylim()
    mx, my = W/(t1 - t0), H/(x1 - x0)
    dt = (t1 - t0)/nt
    dx = (x1 - x0)/nx
    segs = []
    for t in t0 + dt*(np.arange(nt) + .5):
        for x in x0 + dx*(np.arange(nx) + .5):
            if skip is not None and skip(t, x):
                continue
            s = f(t, x)
            ux, uy = mx, s*my
            n = np.hypot(ux, uy)
            hx, hy = length_mm*ux/n/mx/2, length_mm*uy/n/my/2
            segs.append([(t - hx, x - hy), (t + hx, x + hy)])
    ax.add_collection(LineCollection(segs, colors=color, linewidths=lw, zorder=1))


def rk4(f, t0, x0, t1, n=4000):
    """Classical Runge-Kutta integration; returns the time grid and states."""
    ts = np.linspace(t0, t1, n + 1)
    h = ts[1] - ts[0]
    xs = np.zeros((n + 1,) + np.shape(x0))
    xs[0] = x0
    for k in range(n):
        t, x = ts[k], xs[k]
        a = np.asarray(f(t, x))
        b = np.asarray(f(t + h/2, x + h/2*a))
        c = np.asarray(f(t + h/2, x + h/2*b))
        d = np.asarray(f(t + h, x + h*c))
        xs[k + 1] = x + h/6*(a + 2*b + 2*c + d)
    return ts, xs


def dot(ax, t, x, ms=4.2, zorder=6):
    ax.plot([t], [x], 'o', ms=ms, color=RED, mew=0, zorder=zorder)


def hollow(ax, t, x, ms=4.6, zorder=6):
    ax.plot([t], [x], 'o', ms=ms, mfc='white', mec=RED, mew=1, zorder=zorder)
