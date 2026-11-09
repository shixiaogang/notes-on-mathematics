"""Shared problem data and plot helpers for the feasible-iterations chapter.
Running example: f(x)=((x1-1)^2+4(x2-5/8)^2+2x3^2)/2 on the probability simplex in R^3.
L=4, mu=1, x*=(1/2,1/2,0), f*=5/32."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
EDGE = '#4C4D4F'
A = np.array([1., 4., 2.]); C_ = np.array([1., 5/8, 0.])
XS = np.array([.5, .5, 0.]); FS = 5/32; L = 4.; X0 = np.array([.1, .2, .7]); E3 = np.array([0., 0., 1.])
H = np.diag(A)

def f(x): x = np.asarray(x, float); return .5*np.sum(A*(x-C_)**2, axis=-1)
def grad(x): return A*(np.asarray(x, float)-C_)

def proj(z):
    """Euclidean projection on the probability simplex by sorting; returns (p, nu, support size)."""
    z = np.asarray(z, float); u = np.sort(z)[::-1]; s = 0.; k = 0; nu = 0.
    for j, v in enumerate(u, 1):
        s += v
        t = (s-1)/j
        if v-t > 0: k, nu = j, t
    return np.maximum(z-nu, 0.), nu, k

def pgd(x0=X0, a=1/L, T=40):
    xs = [np.array(x0, float)]
    for _ in range(T): xs.append(proj(xs[-1]-a*grad(xs[-1]))[0])
    return np.array(xs)

def fw(x0=E3, T=200, rule='open'):
    """Frank-Wolfe. rule: open (2/(t+2)), exact (line search), smooth (min(1, gap/(L||d||^2)))."""
    xs = [np.array(x0, float)]; gaps = []; steps = []; verts = []
    for t in range(T):
        x = xs[-1]; g = grad(x); i = int(np.argmin(g)); s = np.eye(3)[i]; d = s-x; gap = -g@d
        gaps.append(gap); verts.append(i)
        if rule == 'open': a = 2/(t+2)
        else:
            denom = d@(H@d) if rule == 'exact' else L*d@d
            a = 0. if denom == 0 else min(1., gap/denom)
        steps.append(a); xs.append(x+a*d)
    return np.array(xs), np.array(gaps), np.array(steps), verts

def pairwise(x0=E3, T=30):
    """Pairwise FW with exact line search on the running example; keeps vertex weights."""
    w = np.array(x0, float); xs = [w.copy()]; info = []
    for _ in range(T):
        g = grad(w); s = int(np.argmin(g)); act = np.where(w > 1e-14)[0]; v = int(act[::-1][np.argmax(g[act[::-1]])])
        d = np.eye(3)[s]-np.eye(3)[v]; gd = g@d
        if abs(gd) < 1e-14 or s == v: info.append((s, v, 0., 0.)); xs.append(w.copy()); continue
        a = -gd/(d@(H@d)); am = w[v]; a2 = min(a, am); w = w+a2*d; w[np.abs(w) < 1e-15] = 0; xs.append(w.copy()); info.append((s, v, a, am))
    return np.array(xs), info

def md(x0=X0, a=1/L, T=40, gradf=grad):
    xs = [np.array(x0, float)]
    for _ in range(T):
        x = xs[-1]; w = x*np.exp(-a*gradf(x)); xs.append(w/w.sum())
    return np.array(xs)

# Triangle (barycentric) drawing: e1=(0,0), e2=(1,0), e3=(.5,sqrt3/2); a similarity of the plane sum x=1.
V = np.array([[0., 0.], [1., 0.], [.5, np.sqrt(3)/2]])
def bary(x): return np.asarray(x, float)@V
def unbary(X, Y):
    x3 = Y/(np.sqrt(3)/2); x2 = X-.5*x3; x1 = 1-x2-x3
    return x1, x2, x3

def triangle(ax, fc=BLUE_FILL, ec=BLUE, lw=.95, z=1, labels=True, pad=.035):
    ax.fill(V[:, 0], V[:, 1], facecolor=fc, edgecolor=ec, lw=lw, zorder=z)
    if labels:
        ax.text(V[0, 0]-.02, V[0, 1]-pad, '$e_1$', ha='right', va='top', fontsize=8)
        ax.text(V[1, 0]+.02, V[1, 1]-pad, '$e_2$', ha='left', va='top', fontsize=8)
        ax.text(V[2, 0], V[2, 1]+pad, '$e_3$', ha='center', va='bottom', fontsize=8)

def contours(ax, levels=None, fn=f, lw=.65, z=1.5, n=500, inside=True):
    xs = np.linspace(-.25, 1.25, n); ys = np.linspace(-.3, 1.05, n); X, Y = np.meshgrid(xs, ys)
    x1, x2, x3 = unbary(X, Y); Z = fn(np.stack([x1, x2, x3], axis=-1))
    if inside: Z = np.ma.masked_where((x1 < -1e-9) | (x2 < -1e-9) | (x3 < -1e-9), Z)
    if levels is None: levels = FS+np.array([.03, .1, .25, .5, .9, 1.4, 2.0])
    ax.contour(X, Y, Z, levels=levels, colors=BLUE, linewidths=lw, zorder=z)

def active(ax, a, b, z=4, lw=2.0): ax.plot([a[0], b[0]], [a[1], b[1]], color=EDGE, lw=lw, solid_capstyle='round', zorder=z)
def arrow(ax, a, b, color=GREEN, lw=1.2, ms=7, z=5, ls='-'):
    ax.annotate('', xy=tuple(b), xytext=tuple(a), arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=ms, linestyle=ls), zorder=z)
def dot(ax, p, color=RED, ms=5, z=7): ax.plot([p[0]], [p[1]], 'o', color=color, ms=ms, mew=0, zorder=z)
def hollow(ax, p, color=RED, ms=4.8, z=7): ax.plot([p[0]], [p[1]], 'o', mfc='white', mec=color, mew=1, ms=ms, zorder=z)
def path(ax, xy, color=GREEN, lw=1.3, ms=3.2, z=5, ls='-'):
    ax.plot(xy[:, 0], xy[:, 1], marker='o', color=color, lw=lw, ms=ms, mew=0, zorder=z, ls=ls)
def setup(ax, xlim=None, ylim=None, xt=None, yt=None, xl=None, yl=None, equal=False):
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    if equal: ax.set_aspect('equal')
    if xt is not None: ax.set_xticks(list(xt))
    if yt is not None: ax.set_yticks(list(yt))
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    if xl: ax.set_xlabel(xl, labelpad=1)
    if yl: ax.set_ylabel(yl, labelpad=1)
def off(ax, xlim=(-.12, 1.12), ylim=(-.12, .98)):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect('equal'); ax.axis('off')
def panels(fig, left=.02, right=.98, top=.98, bottom=.1, wspace=.1):
    h = fig.get_figheight()*25.4
    if bottom >= .15: bottom = 13.8/h; right = min(right, .955)   # room for tick labels, axis label and panel tag
    if left >= .05: left += .03
    fig.set_layout_engine(None); fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.012):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
