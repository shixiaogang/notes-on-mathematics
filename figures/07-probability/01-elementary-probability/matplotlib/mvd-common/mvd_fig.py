"""Shared helpers for the chapter 7.7 (common multivariate distributions) figures."""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
FIELD = LinearSegmentedColormap.from_list('field', ['#FFFFFF', BLUE_FILL, BLUE])
HERE = lambda f: Path(f).resolve().parent
pi = np.pi
erf = np.vectorize(math.erf)
lgamma = np.vectorize(math.lgamma)


def style(ax, lw=.95):
    for s in ax.spines.values():
        s.set_linewidth(lw)
    ax.tick_params(width=.85, length=2.5, pad=1.5)


def panel(fig, left=.09, right=.97, top=.96, bottom=.26, wspace=.3):
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


def npdf(x, m=0., v=1.):
    return np.exp(-(x-m)**2/(2*v))/np.sqrt(2*pi*v)


def Phi(x):
    return .5*(1+erf(np.asarray(x)/np.sqrt(2)))


def tpdf(x, nu, s=1.):
    c = math.exp(math.lgamma((nu+1)/2)-math.lgamma(nu/2))/(math.sqrt(nu*pi)*s)
    return c*(1+(x/s)**2/nu)**(-(nu+1)/2)


def lappdf(x, b):
    return np.exp(-np.abs(x)/b)/(2*b)


def ellipse(mu, S, c, n=400):
    w, V = np.linalg.eigh(S); t = np.linspace(0, 2*pi, n)
    pts = V @ (np.sqrt(w)[:, None]*np.vstack([np.cos(t), np.sin(t)]))*c
    return mu[0]+pts[0], mu[1]+pts[1]


def tri_xy(p):
    """Barycentric (p1,p2,p3) -> plane coordinates of an equilateral triangle
    with vertices e1=(0,0), e2=(1,0), e3=(1/2, sqrt3/2)."""
    p = np.asarray(p, float)
    return p[..., 1]+.5*p[..., 2], np.sqrt(3)/2*p[..., 2]


def tri_frame(ax, labels=('$p_1=1$', '$p_2=1$', '$p_3=1$'), lw=.85):
    xs = [0, 1, .5, 0]; ys = [0, 0, np.sqrt(3)/2, 0]
    ax.plot(xs, ys, color=STROKE, lw=lw, zorder=5)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_xlim(-.06, 1.06); ax.set_ylim(-.13, .95)
    if labels:
        lab(ax, 0, -.04, labels[0], ha='center', va='top')
        lab(ax, 1, -.04, labels[1], ha='center', va='top')
        lab(ax, .5, .89, labels[2], ha='center', va='bottom')
