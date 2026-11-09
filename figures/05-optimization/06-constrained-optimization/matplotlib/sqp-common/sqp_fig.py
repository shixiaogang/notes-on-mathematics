"""Shared problems, SQP solvers and plot helpers for the sequential-quadratic-programming chapter."""
from pathlib import Path
import sys, itertools
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
EDGE = '#4C4D4F'

# ---------------------------------------------------------------- running example
# min -x1-x2  s.t. x1^2+x2^2-2 = 0,  x*=(1,1), nu*=1/2
def cf(x): return -x[0]-x[1]
def cg(x): return np.array([-1., -1.])
def ch(x): return np.array([x[0]**2+x[1]**2-2])
def cA(x): return np.array([[2*x[0], 2*x[1]]])
def cHL(x, nu): return 2*nu[0]*np.eye(2)

def kkt_step(g, B, A, h):
    """Solve the equality QP; returns step and the new multipliers."""
    n, m = len(g), len(h)
    K = np.block([[B, A.T], [A, np.zeros((m, m))]])
    s = np.linalg.solve(K, -np.r_[g, h])
    return s[:n], s[n:]

def newton_sqp(x, nu, T=8, f=cf, g=cg, h=ch, A=cA, HL=cHL):
    """Full-step SQP with the exact Lagrangian Hessian (equality constraints)."""
    x, nu = np.array(x, float), np.array(nu, float); out = [(x.copy(), nu.copy())]
    for t in range(T):
        p, nun = kkt_step(g(x), HL(x, nu), A(x), h(x))
        x, nu = x+p, nun; out.append((x.copy(), nu.copy()))
    return out

def qp_enum(B, c, G, b, tol=1e-10):
    """Global solution of the strictly convex QP min c.p+p.B.p/2, G p<=b by enumerating active sets."""
    n, m = len(c), len(b); best = None
    for k in range(0, min(n, m)+1):
        for S in itertools.combinations(range(m), k):
            S = list(S)
            K = np.block([[B, G[S].T], [G[S], np.zeros((k, k))]]) if k else B
            rhs = np.r_[-c, b[S]] if k else -c
            try: sol = np.linalg.solve(K, rhs)
            except np.linalg.LinAlgError: continue
            p, lam = sol[:n], sol[n:]
            if np.all(G@p <= b+tol) and np.all(lam >= -tol):
                v = c@p+.5*p@B@p
                if best is None or v < best[0]-1e-12: best = (v, p, S, lam)
    return best

# inequality version: disc, x2<=1.2, x1>=0
GS = [lambda x: x@x-2, lambda x: x[1]-1.2, lambda x: -x[0]]
DG = [lambda x: 2*x, lambda x: np.array([0., 1.]), lambda x: np.array([-1., 0.])]

def ineq_sqp(x0, lam0, T=8, floor=.1):
    x, lam = np.array(x0, float), np.array(lam0, float); log = []
    c = np.array([-1., -1.])
    for t in range(T):
        B = 2*lam[0]*np.eye(2)
        shifted = False
        if lam[0] <= 0: B = B+floor*np.eye(2); shifted = True
        G = np.array([d(x) for d in DG]); b = -np.array([q(x) for q in GS])
        v, p, S, l = qp_enum(B, c, G, b)
        new = np.zeros(3); new[S] = l
        log.append(dict(x=x.copy(), g=-b, S=[i+1 for i in S], p=p.copy(), lam=new.copy(), shifted=shifted))
        x, lam = x+p, new
    log.append(dict(x=x.copy(), g=np.array([q(x) for q in GS])))
    return log

# Maratos example: f=2(x1^2+x2^2-1)-x1, h=x1^2+x2^2-1, x*=(1,0), nu*=-3/2
def pf(x): return 2*(x[0]**2+x[1]**2-1)-x[0]
def pg(x): return np.array([4*x[0]-1, 4*x[1]])
def ph(x): return np.array([x[0]**2+x[1]**2-1])
def pA(x): return np.array([[2*x[0], 2*x[1]]])
def pHL(x, nu): return (4+2*nu[0])*np.eye(2)

# inconsistent example: f=((x1-2)^2+x2^2)/2, h1=x2-x1^2, h2=x2-1
def rf(x): return .5*((x[0]-2)**2+x[1]**2)
def rg(x): return np.array([x[0]-2, x[1]])
def rh(x): return np.array([x[1]-x[0]**2, x[1]-1])
def rA(x): return np.array([[-2*x[0], 1.], [0., 1.]])

# ---------------------------------------------------------------- drawing
def arrow(ax, a, b, color=GREEN, lw=1.4, ms=8, z=5, ls='-'):
    ax.annotate('', xy=tuple(b), xytext=tuple(a), arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, ls=ls, shrinkA=0, shrinkB=0, mutation_scale=ms), zorder=z)
def dot(ax, p, color=RED, ms=5, z=7): ax.plot([p[0]], [p[1]], 'o', color=color, ms=ms, mew=0, zorder=z)
def hollow(ax, p, color=RED, ms=4.8, z=7): ax.plot([p[0]], [p[1]], 'o', mfc='white', mec=color, mew=1, ms=ms, zorder=z)
def setup(ax, xlim, ylim, xt=None, yt=None, xl='$x_1$', yl='$x_2$', equal=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if equal: ax.set_aspect('equal')
    if xt is not None: ax.set_xticks(list(xt))
    if yt is not None: ax.set_yticks(list(yt))
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    ax.set_xlabel(xl, labelpad=1); ax.set_ylabel(yl, labelpad=1)
def panels(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None); fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.012):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def circle(ax, r=np.sqrt(2), lw=2.0, color=EDGE, z=3, **kw):
    th = np.linspace(0, 2*np.pi, 500); ax.plot(r*np.cos(th), r*np.sin(th), color=color, lw=lw, zorder=z, **kw)
def linline(ax, x, a, h, span=4, lw=1.1, color=EDGE, ls=(0, (4, 2)), z=3):
    """Draw {x+p : a.p+h=0} through the affine model of one constraint."""
    a = np.asarray(a, float); p0 = -h*a/(a@a); t = np.array([-a[1], a[0]])/np.linalg.norm(a)
    u = np.array([x+p0-span*t, x+p0+span*t]); ax.plot(u[:, 0], u[:, 1], color=color, lw=lw, ls=ls, zorder=z)

def ls_merit_sqp(x, nu, rho, T=40, f=cf, g=cg, h=ch, A=cA, HL=cHL, soc=False, eta=.1, floor=1e-2):
    """Equality SQP with l1 merit backtracking; reduced curvature kept positive by shifting B."""
    x, nu = np.array(x, float), np.array(nu, float); log = []
    phi = lambda y: f(y)+rho*np.abs(h(y)).sum()
    for t in range(T):
        a = A(x); B = HL(x, nu); c = h(x); n = len(x); tau = 0.
        U, S, Vt = np.linalg.svd(a); Z = Vt[len(c):].T
        ev = np.linalg.eigvalsh(Z.T@B@Z).min() if Z.size else 1.
        if ev < floor: tau = floor-ev; B = B+tau*np.eye(n)
        p, nun = kkt_step(g(x), B, a, c)
        D = g(x)@p-rho*np.abs(c).sum()
        al, used = 1., 'full'; acc = None
        if phi(x+p) <= phi(x)+eta*D: acc = x+p
        elif soc:
            ph_ = -a.T@np.linalg.solve(a@a.T, h(x+p)); y = x+p+ph_
            if phi(y) <= phi(x)+eta*D: acc = y; used = 'soc'
        if acc is None:
            used = 'back'; al = .5
            while phi(x+al*p) > phi(x)+eta*al*D and al > 1e-12: al *= .5
            acc = x+al*p
        log.append(dict(x=x.copy(), nu=nu.copy(), p=p.copy(), alpha=al, kind=used, tau=tau, nun=nun.copy()))
        nu = nu+al*(nun-nu) if used == 'back' else nun; x = acc
    log.append(dict(x=x.copy(), nu=nu.copy()))
    return log

# five-variable test problem
def f5(x): return np.exp(np.prod(x))-.5*(x[0]**3+x[1]**3+1)**2
def g5(x):
    p = np.prod(x); gv = np.exp(p)*np.array([p/x[i] for i in range(5)]); s = x[0]**3+x[1]**3+1
    gv[0] -= s*3*x[0]**2; gv[1] -= s*3*x[1]**2; return gv
def h5(x): return np.array([x@x-10, x[1]*x[2]-5*x[3]*x[4], x[0]**3+x[1]**3+1])
def J5(x): return np.array([2*x, [0, x[2], x[1], -5*x[4], -5*x[3]], [3*x[0]**2, 3*x[1]**2, 0, 0, 0]], float)
def HL5(x, nu, e=1e-6):
    F = lambda y: g5(y)+J5(y).T@nu
    H = np.array([(F(x+e*d)-F(x-e*d))/(2*e) for d in np.eye(5)]).T
    return .5*(H+H.T)
def damped_bfgs(B, s, y, c=.2):
    ss = s@B@s; sy = s@y
    th = 1. if sy >= c*ss else (1-c)*ss/(ss-sy)
    r = th*y+(1-th)*(B@s)
    return B-np.outer(B@s, B@s)/ss+np.outer(r, r)/(s@r), th
