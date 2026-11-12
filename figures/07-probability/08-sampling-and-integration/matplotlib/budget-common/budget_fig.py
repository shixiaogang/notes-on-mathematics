"""Shared helpers for the chapter 7.34 figures (budget and method selection).

Every curve is computed from a closed-form formula, a numerical quadrature, or a
seeded simulation; no hand-entered data except the fixed teaching uniforms that
the text uses for hand computation.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
E = math.e
# teaching uniforms used throughout the chapter text
U5 = [0.37, 0.81, 0.06, 0.52, 0.23]


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6, **k):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False, **k)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)


def axlab(ax, xl=None, yl=None, pad=1):
    if xl: ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)


def logticks(ax, exps, axis='y'):
    ax.minorticks_off()
    vals = [10.0**e for e in exps]
    labs = ['$1$' if e == 0 else '$10$' if e == 1 else '$10^{%d}$' % e for e in exps]
    if axis == 'y':
        ax.set_yticks(vals); ax.set_yticklabels(labs)
    else:
        ax.set_xticks(vals); ax.set_xticklabels(labs)


def phi(x, m=0.0, s=1.0):
    return np.exp(-(np.asarray(x)-m)**2/(2*s*s))/(s*math.sqrt(2*math.pi))


def Phi(x):
    return 0.5*(1+math.erf(x/math.sqrt(2)))


def tquant(nu, p=0.975):
    """Student-t quantile by bisection on a numerically integrated cdf (no scipy)."""
    if nu == 1:
        return math.tan(math.pi*(p-0.5))
    c = math.exp(math.lgamma((nu+1)/2)-math.lgamma(nu/2))/math.sqrt(nu*math.pi)
    def cdf(t):
        x = np.linspace(0, t, 20001)
        y = c*(1+x*x/nu)**(-(nu+1)/2)
        return 0.5+np.trapezoid(y, x)
    lo, hi = 0.0, 50.0
    for _ in range(60):
        mid = (lo+hi)/2
        if cdf(mid) < p: lo = mid
        else: hi = mid
    return (lo+hi)/2


def c4(R):
    """E[s]/sigma for a normal sample of size R."""
    return math.sqrt(2/(R-1))*math.exp(math.lgamma(R/2)-math.lgamma((R-1)/2))
