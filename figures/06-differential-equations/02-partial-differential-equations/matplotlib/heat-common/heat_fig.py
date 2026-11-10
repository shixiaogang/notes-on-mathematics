from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, to_rgb
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
X = np.linspace(0, 1, 801)
FIELD = LinearSegmentedColormap.from_list('field', ['#FFFFFF', BLUE_FILL, BLUE])
pi = np.pi
erf = np.vectorize(math.erf); erfc = np.vectorize(math.erfc)
def shades(n):
    a = np.array(to_rgb('#BCC9D8')); b = np.array(to_rgb('#4E6784'))
    return [tuple(a + (b-a)*i/max(n-1, 1)) for i in range(n)]
def panel(fig, left=.09, right=.97, top=.96, bottom=.26, wspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def dot(ax, x, y, color=RED, ms=4.6, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)
def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)
def axlab(ax, xl='$x$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl: ax.set_ylabel(yl, labelpad=1)
def cs(k):
    "sine coefficients of the tent u0=min(x,1-x) against e_k=sqrt2 sin(k pi x)"
    return 2*np.sqrt(2)*np.sin(k*pi/2)/(k*pi)**2
def tent(x): return np.minimum(x, 1-x)
def uD(x, t, K=2001):
    k = np.arange(1, K, 2)
    return (cs(k)[:, None]*np.exp(-(k*pi)**2*t)[:, None]*np.sqrt(2)*np.sin(np.outer(k, pi*np.atleast_1d(x)))).sum(0)
def uN(x, t, K=2001):
    k = np.arange(2, K, 4)
    return .25-(8/(k*pi)[:, None]**2*np.exp(-(k*pi)**2*t)[:, None]*np.cos(np.outer(k, pi*np.atleast_1d(x)))).sum(0)
def gauss(x, t): return np.exp(-x**2/(4*t))/np.sqrt(4*pi*t)
def box(x, t, a=.5):
    s = 2*np.sqrt(t); return .5*(erf((x+a)/s)-erf((x-a)/s))
