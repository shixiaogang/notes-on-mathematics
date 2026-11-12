"""Shared helpers for chapter 7.8 (random-variable transformations) figures.

All curves are computed from closed forms in this file; simulations fix their seeds
in the individual figure scripts.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
pi = np.pi
erf = np.vectorize(math.erf)

def panel(fig, left=.09, right=.97, top=.96, bottom=.26, wspace=.3, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)

def tags(fig, axes, y=.015, start=0):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)', '(e)', '(f)')[start:]):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')

def dot(ax, x, y, color=RED, ms=4.2, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)

def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)

def axlab(ax, xl='$x$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)

def phi(x, mu=0., s=1.):
    return np.exp(-(x-mu)**2/(2*s*s))/(np.sqrt(2*pi)*s)

def Phi(x):
    return .5*(1+erf(np.asarray(x)/np.sqrt(2)))

def gamma_pdf(x, a, b):
    x = np.asarray(x, float); out = np.zeros_like(x); m = x > 0
    out[m] = np.exp(a*np.log(b)+(a-1)*np.log(x[m])-b*x[m]-math.lgamma(a))
    return out

def beta_pdf(x, a, b):
    x = np.asarray(x, float); out = np.zeros_like(x); m = (x > 0) & (x < 1)
    lB = math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b)
    out[m] = np.exp((a-1)*np.log(x[m])+(b-1)*np.log(1-x[m])-lB)
    return out

def t_pdf(x, nu):
    c = math.exp(math.lgamma((nu+1)/2)-math.lgamma(nu/2))/math.sqrt(nu*pi)
    return c*(1+np.asarray(x)**2/nu)**(-(nu+1)/2)

def bars(ax, xs, ps, color=BLUE, fill=BLUE_FILL, w=.7, lw=.8, **k):
    ax.bar(xs, ps, width=w, color=fill, edgecolor=color, linewidth=lw, **k)

def hist(ax, data, bins, rng=None, **k):
    h, e = np.histogram(data, bins=bins, range=rng, density=True)
    ax.bar(e[:-1], h, width=np.diff(e), align='edge', color=GREEN_FILL, edgecolor=GREEN, linewidth=.5, **k)
    return h, e
