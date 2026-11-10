"""Shared helpers for the chapter on solution sensitivity (odesens-*)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'

def rk4(f, x0, ts):
    """Classical RK4 on the given time grid; x may be scalar or array."""
    x = np.array(x0, dtype=float); out = [x.copy()]
    for a, b in zip(ts[:-1], ts[1:]):
        h = b-a; k1 = f(a, x); k2 = f(a+h/2, x+h/2*k1); k3 = f(a+h/2, x+h/2*k2); k4 = f(b, x+h*k3)
        x = x+h/6*(k1+2*k2+2*k3+k4); out.append(x.copy())
    return np.array(out)

def panel(fig, left, right, top, bottom, wspace=.2, hspace=None):
    fig.set_layout_engine(None)
    kw = dict(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
    if hspace is not None: kw['hspace'] = hspace
    fig.subplots_adjust(**kw)

def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')

def logistic(t, x0, theta=1.0):
    e = np.exp(theta*np.asarray(t, dtype=float))
    return x0*e/(1-x0+x0*e)

def shoelace(xy):
    x, y = xy[:, 0], xy[:, 1]
    return .5*abs(np.dot(x, np.roll(y, -1))-np.dot(y, np.roll(x, -1)))
