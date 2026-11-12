"""Shared helpers for chapter 7.27 (approximation of probability distributions).

All values come from closed forms, exact finite sums or quadrature on fine grids;
simulations use the fixed seed SEED. No hand-entered data.
Running examples of the chapter:
  * three-point target PI3=(3/5,3/10,1/10), candidates Q_t=(t,1-2t,t);
  * binary table PI2=[[0.45,0.05],[0.05,0.45]] (rows x1, columns x2);
  * correlated Gaussian N(0,[[1,rho],[rho,1]]) with rho=0.8;
  * quartic target pi~(x)=exp(-x^4/4) with Gaussian candidates N(m, e^{2w});
  * bimodal target 0.7 N(-2,0.6^2)+0.3 N(2,0.6^2).
"""
from pathlib import Path
import sys
import math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401
import numpy as np

STROKE = '#4C4D4F'
DASH = (0, (4, 2))
DOT = (0, (1.5, 1.8))
SEED = 727
PI3 = np.array([.6, .3, .1])
PI2 = np.array([[.45, .05], [.05, .45]])
RHO = 0.8
W_MIX, M_MIX, S_MIX = 0.7, 2.0, 0.6
LNZ4 = math.log(2*4**0.25*math.gamma(1.25))   # ln of int exp(-x^4/4) dx
C_GAUSS = 0.5*math.log(2*math.pi*math.e)       # entropy of N(0,1)


def Q3(t):
    return np.array([t, 1-2*t, t])


def kl(p, q):
    p = np.asarray(p, float); q = np.asarray(q, float); m = p > 0
    if np.any(q[m] == 0):
        return math.inf
    return float(np.sum(p[m]*np.log(p[m]/q[m])))


def npdf(x, m=0., s=1.):
    x = np.asarray(x, dtype=float)
    return np.exp(-(x-m)**2/(2*s*s))/(s*math.sqrt(2*math.pi))


def mix_pdf(x):
    return W_MIX*npdf(x, -M_MIX, S_MIX)+(1-W_MIX)*npdf(x, M_MIX, S_MIX)


def mf_obj(a, b, pi=PI2):
    """D(q1 x q2 || pi) with q1=(1-a,a), q2=(1-b,b)."""
    Q = np.outer([1-a, a], [1-b, b])
    return float(np.sum(Q*np.log(Q/pi)))


def sig(z):
    return 1/(1+math.exp(-z))


def cavi_table(b0, rounds, pi=PI2):
    """Mean-field coordinate updates on a 2x2 table; returns list of (a,b) after each half step."""
    lr = np.log(pi)
    b = b0; a = 0.5; out = [(a, b)]
    for _ in range(rounds):
        za = (1-b)*(lr[1, 0]-lr[0, 0])+b*(lr[1, 1]-lr[0, 1]); a = sig(za); out.append((a, b))
        zb = (1-a)*(lr[0, 1]-lr[0, 0])+a*(lr[1, 1]-lr[1, 0]); b = sig(zb); out.append((a, b))
    return out


def quartic_J(m, s):
    """J(Q)=E_Q[ln q - ln pi~] for Q=N(m,s^2), pi~=exp(-x^4/4)."""
    return -np.log(s)-C_GAUSS+(m**4+6*m*m*s*s+3*s**4)/4


def quartic_grad(m, w):
    s = math.exp(w)
    return m**3+3*m*s*s, -1+3*m*m*s*s+3*s**4


def gd_path(m0=1., w0=0., eta=0.1, steps=40):
    m, w = m0, w0; out = [(m, w)]
    for _ in range(steps):
        gm, gw = quartic_grad(m, w); m -= eta*gm; w -= eta*gw; out.append((m, w))
    return out


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position()
        fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5)
    ax.text(x, y, s, color=color, **k)


def axlab(ax, xl='$x$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl:
        ax.set_ylabel(yl, labelpad=1)


def bars(ax, x, h, color=BLUE, fill=BLUE_FILL, width=.34, offset=0., lw=.8, z=2):
    ax.bar(np.asarray(x)+offset, h, width=width, color=fill, edgecolor=color, linewidth=lw, zorder=z)


def table_heat(ax, T, fmt='{:.3f}', vmax=None):
    """2x2 probability table as white-to-blue cells with values; rows x1 (top=0), columns x2."""
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE_FILL, BLUE])
    vmax = vmax or 0.6
    ax.imshow(T, cmap=cmap, vmin=0, vmax=vmax, origin='upper', extent=(-.5, 1.5, 1.5, -.5))
    for i in range(2):
        for j in range(2):
            ax.text(j, i, fmt.format(T[i, j]), ha='center', va='center', color=INK, fontsize=7.5)
    for v in (-.5, .5, 1.5):
        ax.plot([-.5, 1.5], [v, v], color=STROKE, lw=.65)
        ax.plot([v, v], [-.5, 1.5], color=STROKE, lw=.65)
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.set_xlim(-.5, 1.5); ax.set_ylim(1.5, -.5)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
