"""Shared helpers for chapter 'linear differential equations' figures (prefix lde-)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
FIELD = '#B4BCC8'
MAIN, AUX, AXIS = 1.4, .85, .95

def panel(fig, left, right, top, bottom, wspace=.3, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)

def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position()
        fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')

def axes_style(ax):
    for s in ('left', 'bottom'):
        ax.spines[s].set_linewidth(AXIS)
    ax.tick_params(width=.7, length=2.5, pad=1.5)

def label(ax, xl, yl):
    ax.set_xlabel(xl, labelpad=1)
    ax.set_ylabel(yl, labelpad=1)
    axes_style(ax)

def field(ax, f, xlim, ylim, nx=19, ny=11, lw=.5, frac=.55):
    """Direction field of x'=f(t,x): equal-length short segments in screen units."""
    fig = ax.figure
    bb = ax.get_position()
    W = bb.width*fig.get_figwidth()
    H = bb.height*fig.get_figheight()
    sx = W/(xlim[1]-xlim[0])
    sy = H/(ylim[1]-ylim[0])
    dx = (xlim[1]-xlim[0])/nx
    dy = (ylim[1]-ylim[0])/ny
    L = frac*min(dx*sx, dy*sy)/2
    for t in xlim[0]+dx*(np.arange(nx)+.5):
        for x in ylim[0]+dy*(np.arange(ny)+.5):
            m = f(t, x)
            vx, vy = sx, m*sy
            n = np.hypot(vx, vy)
            ax.plot([t-L*vx/n/sx, t+L*vx/n/sx], [x-L*vy/n/sy, x+L*vy/n/sy], color=FIELD, lw=lw, solid_capstyle='round', zorder=1)

def phase_field(ax, A, xlim, ylim, nx=15, ny=15, lw=.5, frac=.55):
    fig = ax.figure
    bb = ax.get_position()
    sx = bb.width*fig.get_figwidth()/(xlim[1]-xlim[0])
    sy = bb.height*fig.get_figheight()/(ylim[1]-ylim[0])
    dx = (xlim[1]-xlim[0])/nx
    dy = (ylim[1]-ylim[0])/ny
    L = frac*min(dx*sx, dy*sy)/2
    for a in xlim[0]+dx*(np.arange(nx)+.5):
        for b in ylim[0]+dy*(np.arange(ny)+.5):
            v = A@np.array([a, b])
            vx, vy = v[0]*sx, v[1]*sy
            n = np.hypot(vx, vy)
            if n < 1e-12:
                continue
            ax.plot([a-L*vx/n/sx, a+L*vx/n/sx], [b-L*vy/n/sy, b+L*vy/n/sy], color=FIELD, lw=lw, solid_capstyle='round', zorder=1)

def arrow_on(ax, xs, ys, i, color=BLUE, scale=7):
    ax.annotate('', xy=(xs[i+1], ys[i+1]), xytext=(xs[i], ys[i]),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=.8, mutation_scale=scale, shrinkA=0, shrinkB=0), zorder=3)

def expm(M, K=60):
    """Matrix exponential by scaling and truncated Taylor series (real computation)."""
    M = np.asarray(M, float)
    s = max(0, int(np.ceil(np.log2(max(np.linalg.norm(M, 2), 1e-16))))+2)
    B = M/2.0**s
    R = T = np.eye(M.shape[0])
    for k in range(1, K):
        T = T@B/k
        R = R+T
    for _ in range(s):
        R = R@R
    return R

def rk4(f, t0, x0, t1, n):
    h = (t1-t0)/n
    ts = [t0]
    xs = [np.array(x0, float)]
    for k in range(n):
        t = ts[-1]
        x = xs[-1]
        k1 = f(t, x)
        k2 = f(t+h/2, x+h/2*k1)
        k3 = f(t+h/2, x+h/2*k2)
        k4 = f(t+h, x+h*k3)
        xs.append(x+h/6*(k1+2*k2+2*k3+k4))
        ts.append(t+h)
    return np.array(ts), np.array(xs)
