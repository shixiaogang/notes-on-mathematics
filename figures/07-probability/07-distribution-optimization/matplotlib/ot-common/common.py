"""Shared data and numerics for chapter 7.29 (optimal transport).

Running example of the chapter: supplies a=(0.5,0.3,0.2) at x=(0,1,2),
demands b=(0.2,0.3,0.5) at y=(0,1,2), cost c(x,y)=(x-y)^2.
All numbers come from exact finite computations, closed forms or fine
quadrature grids; no hand-entered results.  Random draws (if any) use SEED.
"""
from pathlib import Path
import sys
import math
import itertools
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401
import numpy as np

STROKE = '#4C4D4F'
DASH = (0, (4, 2))
DOT = (0, (1.5, 1.8))
SEED = 729
A_EX = np.array([.5, .3, .2])
B_EX = np.array([.2, .3, .5])
X_EX = np.array([0., 1., 2.])
Y_EX = np.array([0., 1., 2.])
C_EX = (X_EX[:, None]-Y_EX[None, :])**2
PI_OPT = np.array([[.2, .3, 0], [0, 0, .3], [0, 0, .2]])
PI_JUMP = np.array([[.2, 0, .3], [0, .3, 0], [0, 0, .2]])
F_EX = np.array([0., -1., -2.])
G_EX = np.array([0., 1., 2.])


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32, hspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)


def tags(fig, axes, y=.015, labels=('(a)', '(b)', '(c)', '(d)')):
    for ax, s in zip(axes, labels):
        p = ax.get_position()
        fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False)


def heat(ax, P, vmax=None, fmt='{:.2f}', cmap=None, zero='0'):
    from matplotlib.colors import LinearSegmentedColormap
    cmap = cmap or LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE_FILL, BLUE])
    m, n = P.shape
    ax.imshow(P, cmap=cmap, vmin=0, vmax=vmax or P.max())
    for i in range(m):
        for j in range(n):
            v = P[i, j]
            ax.text(j, i, zero if abs(v) < 1e-12 else fmt.format(v), ha='center', va='center',
                    fontsize=7, color=INK if v < .7*(vmax or P.max()) else 'white')
    for k in range(m+1):
        ax.plot([-.5, n-.5], [k-.5, k-.5], color=GRID, lw=.65)
    for k in range(n+1):
        ax.plot([k-.5, k-.5], [-.5, m-.5], color=GRID, lw=.65)
    ax.set_xticks(range(n)); ax.set_yticks(range(m))
    ax.xaxis.tick_top(); ax.tick_params(length=0, pad=2)
    for s in ax.spines.values():
        s.set_visible(False)


def logsumexp(M, axis):
    m = M.max(axis=axis, keepdims=True)
    return (m+np.log(np.exp(M-m).sum(axis=axis, keepdims=True))).squeeze(axis)


def sinkhorn_log(a, b, C, eps, iters, record=False):
    """Log-domain Sinkhorn for min <C,pi> + eps KL(pi || a b^T).
    f_i = -eps log sum_j b_j exp((g_j-c_ij)/eps), g_j = -eps log sum_i a_i exp((f_i-c_ij)/eps)."""
    f = np.zeros(len(a)); g = np.zeros(len(b)); hist = []
    la, lb = np.log(a), np.log(b)
    for t in range(iters):
        f = -eps*logsumexp(lb[None, :]+(g[None, :]-C)/eps, axis=1)
        g = -eps*logsumexp(la[:, None]+(f[:, None]-C)/eps, axis=0)
        if record:
            hist.append(diagnostics(a, b, C, eps, f, g))
    return f, g, hist


def plan(a, b, C, eps, f, g):
    return a[:, None]*b[None, :]*np.exp((f[:, None]+g[None, :]-C)/eps)


def kl_ref(P, a, b):
    m = P > 0
    R = a[:, None]*b[None, :]
    return float(np.sum(P[m]*np.log(P[m]/R[m])))


def round_plan(P, a, b):
    """Make P feasible: scale down rows exceeding a, columns exceeding b, add rank-one correction."""
    r = P.sum(1); s = np.minimum(1, a/np.maximum(r, 1e-300)); P = P*s[:, None]
    c = P.sum(0); s = np.minimum(1, b/np.maximum(c, 1e-300)); P = P*s[None, :]
    er = a-P.sum(1); ec = b-P.sum(0)
    if er.sum() > 0:
        P = P+np.outer(er, ec)/er.sum()
    return P


def diagnostics(a, b, C, eps, f, g):
    P = plan(a, b, C, eps, f, g)
    row_res = float(np.abs(P.sum(1)-a).sum()); col_res = float(np.abs(P.sum(0)-b).sum())
    D = float(a@f+b@g-eps*(P.sum()-1))
    Pt = round_plan(P, a, b)
    primal = float((C*Pt).sum()+eps*kl_ref(Pt, a, b))
    return {'row_res': row_res, 'col_res': col_res, 'dual': D, 'primal_rounded': primal,
            'gap': primal-D, 'cost': float((C*P).sum())}


def lp_bruteforce(a, b, C):
    """Exact transport LP by enumerating basic solutions (support sets of size m+n-1)."""
    m, n = C.shape
    cells = [(i, j) for i in range(m) for j in range(n)]
    Aeq = np.zeros((m+n, m*n))
    for i in range(m):
        for j in range(n):
            Aeq[i, i*n+j] = 1; Aeq[m+j, i*n+j] = 1
    rhs = np.concatenate([a, b])
    best = None
    for S in itertools.combinations(range(m*n), m+n-1):
        M = Aeq[:, S]
        if np.linalg.matrix_rank(M) < m+n-1:
            continue
        sol, *_ = np.linalg.lstsq(M, rhs, rcond=None)
        if np.max(np.abs(M@sol-rhs)) > 1e-10 or sol.min() < -1e-12:
            continue
        x = np.zeros(m*n); x[list(S)] = sol
        val = float(C.reshape(-1)@x)
        if best is None or val < best[0]-1e-12:
            best = (val, x.reshape(m, n), S)
    return best


def quantile(points, weights, u):
    cw = np.cumsum(weights)
    idx = np.searchsorted(cw-1e-12, u, side='left')
    return np.asarray(points)[np.minimum(idx, len(points)-1)]
