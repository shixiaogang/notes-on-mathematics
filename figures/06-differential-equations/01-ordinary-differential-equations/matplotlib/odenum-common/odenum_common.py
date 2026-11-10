"""Shared definitions for the figures of the chapter on numerical initial value problems."""
from pathlib import Path
import sys
import math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, STROKE, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa
import numpy as np

X0 = 0.2


def f(t, x):
    """Running example right-hand side."""
    return x*(1-x)


def exact(t, s=0.0, y=X0):
    """Exact logistic solution through x(s)=y."""
    return y/(y+(1-y)*np.exp(-(np.asarray(t)-s)))


def euler_step(g, t, x, h):
    return x+h*g(t, x)


def midpoint_step(g, t, x, h):
    return x+h*g(t+h/2, x+h/2*g(t, x))


def rk4_step(g, t, x, h):
    k1 = g(t, x)
    k2 = g(t+h/2, x+h/2*k1)
    k3 = g(t+h/2, x+h/2*k2)
    k4 = g(t+h, x+h*k3)
    return x+h/6*(k1+2*k2+2*k3+k4)


def integrate(step, g, h, n, x=X0, t0=0.0):
    xs = [x]
    for k in range(n):
        x = step(g, t0+k*h, x, h)
        xs.append(x)
    return np.array(xs)


def panel(ax, text, y=-0.34):
    ax.text(0.5, y, text, transform=ax.transAxes, ha='center', va='top', fontsize=8, color=INK)


def direction_field(ax, g, ts, xs, length, aspect):
    """Draw short slope segments of equal visual length; aspect = data dx per data dt on screen."""
    for t in ts:
        for x in xs:
            s = g(t, x)
            dt = length/np.sqrt(1+(s/aspect)**2)
            ax.plot([t-dt/2, t+dt/2], [x-s*dt/2, x+s*dt/2], color=GRID, lw=.8, solid_capstyle='round', zorder=1)


def heun_euler_adaptive(g, t0, T, x0, h0, atol, rtol, fac=0.9, fmin=0.2, fmax=5.0):
    """Embedded Heun-Euler 2(1) pair with local extrapolation; x may be a scalar or an array."""
    t, x, h = t0, np.atleast_1d(np.array(x0, float)), h0
    acc, rej, nf = [(t, x.copy(), h)], [], 0
    failed = False
    while t < T-1e-12:
        h = min(h, T-t)
        k1 = np.atleast_1d(g(t, x)); k2 = np.atleast_1d(g(t+h, x+h*k1)); nf += 2
        hi = x+h/2*(k1+k2)
        est = h/2*(k2-k1)
        sc = atol+rtol*np.maximum(np.abs(x), np.abs(hi))
        err = float(np.max(np.abs(est)/sc))
        new = h*min(1.0 if failed else fmax, max(fmin, fac*max(err, 1e-12)**-0.5))
        if err <= 1:
            t, x = t+h, hi
            acc.append((t, x.copy(), h))
            failed = False
        else:
            rej.append((t, x.copy(), h))
            failed = True
        h = new
    return acc, rej, nf
