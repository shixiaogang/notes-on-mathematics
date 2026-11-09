"""Shared data and helpers for the multi-objective chapter (objective plane plots)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
EDGE = '#4C4D4F'
# Finite example: cost f1 and error f2 of candidate plans.
CANDS = {'A': (1, 8), 'B': (2, 5), 'C': (4, 4), 'D': (6, 1), 'E': (5, 6), 'F': (7, 1)}
PARETO = 'ABCD'
# Example with two isotropic quadratics, a=(1,0), b=(0,1); front (s^2,(1-s)^2).
A0 = np.array([1., 0.]); B0 = np.array([0., 1.])
def f_iso(x): 
    x = np.asarray(x, float); return np.array([.5*np.sum((x-A0)**2, axis=-1), .5*np.sum((x-B0)**2, axis=-1)])
def iso_front(n=300):
    s = np.linspace(0, 1, n); return s**2, (1-s)**2
def iso_region(umax, n=500):
    """Filled outline of {(p^2,q^2): p+q>=1, |p-q|<=1} clipped to u,v<=umax."""
    p = np.linspace(0, 1, n); low = (p**2, (1-p)**2)
    return low
# Front with a dent: v=(1-u)^2 + bump.
def bump(u): return (1-u)**2+.1*np.exp(-((u-.4)/.1)**2)
def lower_hull(xs, ys):
    pts = []
    for p in zip(xs, ys):
        while len(pts) >= 2 and (pts[-1][0]-pts[-2][0])*(p[1]-pts[-2][1])-(pts[-1][1]-pts[-2][1])*(p[0]-pts[-2][0]) <= 0: pts.pop()
        pts.append(p)
    return np.array(pts)
# Anisotropic pair for the MGDA example.
BM = np.array([4., 3.])
def fm(x):
    x = np.asarray(x, float); return np.array([.5*(x[..., 0]**2+9*x[..., 1]**2), .5*((x[..., 0]-4)**2+(x[..., 1]-3)**2)])
def gm(x): return np.array([x[0], 9*x[1]]), x-BM
def xm(w): 
    w = np.asarray(w, float); return np.stack([4*(1-w), 3*(1-w)/(8*w+1)], axis=-1)
def minnorm2(g1, g2):
    d = g1-g2; n = d@d
    if n < 1e-30: return .5, g1
    t = float(np.clip((g2@(g2-g1))/n, 0, 1)); return t, t*g1+(1-t)*g2
def mgda(x0, T, c=.5, beta=.5):
    x = np.array(x0, float); path = [x.copy()]; res = []; steps = []; thetas = []
    for _ in range(T):
        g1, g2 = gm(x); th, g = minnorm2(g1, g2); n2 = g@g; a = 1.; k = 0
        while np.any(fm(x-a*g) > fm(x)-c*a*n2+1e-14) and k < 50: a *= beta; k += 1
        res.append(np.sqrt(n2)); steps.append(a); thetas.append(th); x = x-a*g; path.append(x.copy())
    return np.array(path), np.array(res), np.array(steps), np.array(thetas)

def arrow(ax, a, b, color=GREEN, lw=1.2, ms=8, z=5):
    ax.annotate('', xy=tuple(b), xytext=tuple(a), arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=ms), zorder=z)
def dot(ax, p, color=RED, ms=5, z=7): ax.plot([p[0]], [p[1]], 'o', color=color, ms=ms, mew=0, zorder=z)
def hollow(ax, p, color=MUTED, ms=4.8, z=7): ax.plot([p[0]], [p[1]], 'o', mfc='white', mec=color, mew=1, ms=ms, zorder=z)
def setup(ax, xlim, ylim, xt=None, yt=None, xl='$f_1$', yl='$f_2$', equal=False):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if equal: ax.set_aspect('equal')
    if xt is not None: ax.set_xticks(list(xt))
    if yt is not None: ax.set_yticks(list(yt))
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    ax.set_xlabel(xl, labelpad=1); ax.set_ylabel(yl, labelpad=1)
    ax.tick_params(length=2.5, width=.7, pad=1.5)
def panels(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None); fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.012):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def cands(ax, names='ABCDEF', off=None, labels=True):
    """Pareto candidates red; dominated candidates hollow grey."""
    off = off or {}
    for k in names:
        p = CANDS[k]
        if k in PARETO: dot(ax, p)
        else: hollow(ax, p)
        if labels:
            dx, dy = off.get(k, (.13, .22))
            ax.text(p[0]+dx, p[1]+dy, k, color=INK, fontsize=8)
def iso_fill(ax, umax):
    """Reachable set of the isotropic pair clipped to [0,umax]^2, by a polygon in (sqrt u, sqrt v)."""
    r = np.sqrt(umax); t = np.linspace(0, 1, 200)
    # boundary in (p,q): p+q=1 from (0,1) to (1,0); p-q=1 from (1,0) to (r,r-1); top right corner; q-p=1 back to (0,1)
    pq = [np.c_[t, 1-t], np.c_[1+t*(r-1), t*(r-1)], np.c_[r+0*t, r-1+t], np.c_[r-t, r+0*t], np.c_[r-1-t*(r-1), r-t*(r-1)]]
    P = np.vstack(pq); ax.fill(P[:, 0]**2, P[:, 1]**2, facecolor=BLUE_FILL, edgecolor='none', zorder=1)
