"""Shared objective, solvers and plot helpers for the trust-region chapter.
Objective: f(x)=x1^4/4-x1^2/2+x1+1.5*x2^2+x2, the running example of the chapter."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.patches import Circle
EDGE = '#4C4D4F'
import matplotlib
matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
XSTAR = np.array([-1.3247179572, -1/3])
A_X, A_G, A_B = np.array([2., 2.]), np.array([7., 7.]), np.diag([11., 3.])
O_X, O_G, O_B = np.zeros(2), np.array([1., 1.]), np.diag([-1., 3.])

def f(x):
    s, v = x[0], x[1]
    return s**4/4 - s**2/2 + s + 1.5*v**2 + v
def grad(x): return np.array([x[0]**3 - x[0] + 1, 3*x[1] + 1.])
def hess(x): return np.diag([3*x[0]**2 - 1, 3.])
def mdec(p, g, B):
    """m(p)-m(0)."""
    return g @ p + .5 * p @ B @ p
def boundary(p, d, D):
    a, b, c = d @ d, 2 * p @ d, p @ p - D**2
    return (-b + np.sqrt(b*b - 4*a*c)) / (2*a)
def tcg(g, B, D, eps=0., maxit=None, mv=None):
    """Steihaug truncated CG. Returns step, stop reason, list of iterates, matvec count."""
    mv = mv or (lambda v: B @ v)
    p = 0*g; r = g.copy(); d = -r; pth = [p.copy()]; cnt = 0
    if np.linalg.norm(r) <= eps: return p, 'res', pth, cnt
    maxit = maxit or len(g)
    for _ in range(maxit):
        Bd = mv(d); cnt += 1; k = d @ Bd
        if k <= 0:
            p = p + boundary(p, d, D)*d; pth.append(p.copy()); return p, 'neg', pth, cnt
        a = r @ r / k
        if np.linalg.norm(p + a*d) >= D:
            p = p + boundary(p, d, D)*d; pth.append(p.copy()); return p, 'bnd', pth, cnt
        p = p + a*d; pth.append(p.copy()); rn = r + a*Bd
        if np.linalg.norm(rn) <= eps: return p, 'res', pth, cnt
        d = -rn + (rn @ rn)/(r @ r)*d; r = rn
    return p, 'res', pth, cnt
def exact(g, B, D):
    """Global solution of the subproblem (non hard case), by bisection on lambda."""
    w, Q = np.linalg.eigh(B); gt = Q.T @ g
    nrm = lambda l: np.linalg.norm(gt/(w + l))
    if w[0] > 0 and nrm(0) <= D: return np.linalg.solve(B, -g), 0.
    lo = max(0., -w[0]) + 1e-13; hi = max(lo, 1.)*2
    while nrm(hi) > D: hi *= 2
    for _ in range(200):
        c = .5*(lo + hi)
        if nrm(c) > D: lo = c
        else: hi = c
    return Q @ (-gt/(w + hi)), hi
def cauchy(g, B, D):
    k = g @ B @ g; n = np.linalg.norm(g)
    t = D/n if k <= 0 else min(D/n, n*n/k)
    return -t*g
def run_tr(x0, D0, eta1=.25, eta2=.75, theta=.5, Dmax=8., tol=1e-8, maxit=60):
    x = np.array(x0, float); D = D0; hist = []
    for t in range(maxit):
        g, B = grad(x), hess(x); n = np.linalg.norm(g)
        if n < tol: break
        p, why, pth, _ = tcg(g, B, D, min(.1, np.sqrt(n))*n)
        pr = -mdec(p, g, B); ar = f(x) - f(x + p); rho = ar/pr
        ok = rho >= eta1
        hist.append(dict(t=t, x=x.copy(), D=D, p=p.copy(), why=why, pr=pr, ar=ar, rho=rho, ok=ok, gn=n, f=f(x)))
        if rho < eta1: D = theta*D
        elif rho >= eta2 and abs(np.linalg.norm(p) - D) < 1e-9: D = min(2*D, Dmax)
        if ok: x = x + p
    return hist
def disk(ax, c, D, **kw):
    o = dict(facecolor=BLUE_FILL, edgecolor=BLUE, lw=.9, zorder=0); o.update(kw)
    ax.add_patch(Circle(c, D, **o))
def arrow(ax, p, q, c=INK, lw=1.15, z=5):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', color=c, lw=lw, mutation_scale=8, shrinkA=0, shrinkB=0), zorder=z)
def panels(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.012):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0 + p.x1)/2, y, s, ha='center', va='bottom')
