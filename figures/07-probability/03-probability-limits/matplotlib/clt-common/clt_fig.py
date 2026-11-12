"""Shared helpers for the chapter 7.15 figures (central limit theorem).

Every curve is computed from a closed-form formula, an exact finite sum, or a
seeded simulation; no hand-entered data.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
BE_C = 0.4748  # Shevtsova (2011) constant for the i.i.d. Berry-Esseen bound
_erf = np.vectorize(math.erf)


def Phi(x):
    return 0.5*(1+_erf(np.asarray(x, dtype=float)/math.sqrt(2)))


def phi(x):
    x = np.asarray(x, dtype=float)
    return np.exp(-x*x/2)/math.sqrt(2*math.pi)


def shade(c, w):
    "mix colour c with white; w=0 gives c, w=1 gives white"
    c = c.lstrip('#'); r, g, b = (int(c[i:i+2], 16) for i in (0, 2, 4))
    f = lambda v: int(round(v+(255-v)*w))
    return '#%02X%02X%02X' % (f(r), f(g), f(b))


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)


def axlab(ax, xl='$x$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)


def logticks(ax, exps, axis='y'):
    ax.minorticks_off()
    vals = [10.0**e for e in exps]
    labs = ['$1$' if e == 0 else '$10$' if e == 1 else '$10^{%d}$' % e for e in exps]
    if axis == 'y':
        ax.set_yticks(vals); ax.set_yticklabels(labs)
    else:
        ax.set_xticks(vals); ax.set_xticklabels(labs)


def binpmf(n, p=.5):
    "exact Bin(n,p) masses via log-gamma"
    k = np.arange(n+1)
    lg = np.array([math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1) for i in k])
    with np.errstate(divide='ignore'):
        return np.exp(lg + k*np.log(p) + (n-k)*np.log1p(-p))


def bin_sup_error(n, p):
    "sup_x |P((S_n-np)/sd <= x) - Phi(x)| for S_n ~ Bin(n,p); checked at both one-sided limits of every jump"
    pm = binpmf(n, p); F = np.cumsum(pm); Fm = F - pm
    z = (np.arange(n+1) - n*p)/math.sqrt(n*p*(1-p)); P = Phi(z)
    return float(max(np.max(np.abs(F-P)), np.max(np.abs(Fm-P))))


def erlang_cdf(n, x):
    "P(Gamma(n,1) <= x) for integer n via the Poisson identity, computed in logs"
    x = np.atleast_1d(np.asarray(x, dtype=float)); out = np.zeros_like(x)
    for i, xi in enumerate(x):
        if xi <= 0: continue
        if xi < n:  # sum the Poisson masses k >= n directly (no cancellation in the left tail)
            k = np.arange(n, n+400)
            lt = -xi + k*math.log(xi) - np.array([math.lgamma(j+1) for j in k])
            out[i] = np.exp(lt).sum()
        else:
            k = np.arange(n)
            lt = -xi + k*math.log(xi) - np.array([math.lgamma(j+1) for j in k])
            out[i] = max(0.0, 1 - np.exp(lt).sum())
    return out


def erlang_sf(n, x):
    "P(Gamma(n,1) > x), accurate in the far right tail"
    x = np.atleast_1d(np.asarray(x, dtype=float)); out = np.ones_like(x)
    for i, xi in enumerate(x):
        if xi <= 0: continue
        k = np.arange(n)
        lt = -xi + k*math.log(xi) - np.array([math.lgamma(j+1) for j in k])
        out[i] = np.exp(lt).sum()
    return out


def gamma_pdf(n, x):
    x = np.asarray(x, dtype=float); out = np.zeros_like(x); m = x > 0
    out[m] = np.exp((n-1)*np.log(x[m]) - x[m] - math.lgamma(n))
    return out
