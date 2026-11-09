"""Shared drawing helpers for the LP interior-point chapter."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent/'simplex-common'))
from lp_plot import *
from ipm_core import *
V3 = {'e1': np.array([1., 0.]), 'e2': np.array([0., np.sqrt(3.)]), 'e3': np.array([-1., 0.])}

def draw_tri(ax, labels=True, pad=.12):
    v = np.array([V3['e1'], V3['e2'], V3['e3']])
    ax.fill(v[:, 0], v[:, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.0, zorder=1)
    if labels:
        ax.text(1.04, -.03, '$\\mathbf{e}_1$', ha='left', va='top', fontsize=8)
        ax.text(0, np.sqrt(3.) + .05, '$\\mathbf{e}_2$', ha='center', va='bottom', fontsize=8)
        ax.text(-1.04, -.03, '$\\mathbf{e}_3$', ha='right', va='top', fontsize=8)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-.16 - pad, np.sqrt(3.) + .2)

def tri_grid(N=500):
    X, Y = np.meshgrid(np.linspace(-1, 1, N), np.linspace(0, np.sqrt(3.), N))
    x2 = Y / np.sqrt(3.); x1 = (1 - x2 + X) / 2; x3 = (1 - x2 - X) / 2
    return X, Y, x1, x2, x3

def central_run(c, ys):
    """Closed-form central points of min c'x, sum x=1, x>=0, parametrized by y<min c."""
    pts = []; mus = []
    for y in ys:
        s = c - y; mu = 1. / np.sum(1. / s); pts.append(mu / s); mus.append(mu)
    return np.array(pts), np.array(mus)

def sublabel(ax, text, y=-.12):
    ax.text(.5, y, text, transform=ax.transAxes, ha='center', va='top', fontsize=8)

_base_figure = figure
def figure(*a, **k):
    out = _base_figure(*a, **k)
    import matplotlib as mpl
    mpl.rcParams['mathtext.fallback'] = 'stix'
    return out

def xlab(ax, math, tail=None):
    """Math x-label with an optional plain Chinese line below; matplotlib cannot mix CJK and math in one string."""
    ax.set_xlabel(math, labelpad=1)
    if tail:
        ax.annotate(tail, xy=(.5, 0), xycoords=ax.xaxis.label, xytext=(0, -1.5), textcoords='offset points', ha='center', va='top', fontsize=8)
