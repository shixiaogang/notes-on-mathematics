"""Shared helpers for chapter 7.22 (rate distortion).

All values come from closed forms, exact finite sums, exhaustive search or
Blahut-Arimoto iterations; simulations use the fixed seed SEED.
Running example of the chapter: X ~ Bern(0.3) with Hamming distortion;
Gaussian example: X ~ N(0, 1) with squared error. Information in bits.
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
SEED = 722
P_SRC = 0.3


def h2(t):
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    m = (t > 0) & (t < 1)
    tm = t[m]
    out[m] = -tm*np.log2(tm)-(1-tm)*np.log2(1-tm)
    return out if out.ndim else float(out)


def rd_binary(D, p=P_SRC):
    p = min(p, 1-p)
    D = np.asarray(D, dtype=float)
    return np.where(D < p, h2(p)-h2(np.minimum(D, p)), 0.0)


def mutual_info(px, q):
    """px: (nx,), q: (nx, ny) rows conditional distributions. bits."""
    px = np.asarray(px, float); q = np.asarray(q, float)
    r = px @ q
    J = px[:, None]*q
    m = J > 0
    return float(np.sum(J[m]*np.log2(q[m]/np.broadcast_to(r, q.shape)[m])))


def exp_dist(px, q, d):
    return float(np.sum(np.asarray(px)[:, None]*q*d))


def blahut_arimoto(px, d, s, r0=None, iters=200, tol=None):
    """Minimise I(p,q)+s*E d (bits). Returns history list of dicts."""
    px = np.asarray(px, float); d = np.asarray(d, float)
    ny = d.shape[1]
    r = np.full(ny, 1/ny) if r0 is None else np.asarray(r0, float)
    A = 2.0**(-s*d)
    hist = []
    for t in range(iters):
        Z = A @ r                      # Z(x)
        q = A*r[None, :]/Z[:, None]    # q(xhat|x)
        c = (px/Z) @ A                 # c(xhat)
        rn = r*c
        J = -float(np.sum(px*np.log2(Z)))
        gap = float(np.max(np.log2(c)))
        hist.append(dict(t=t+1, Z=Z, q=q, c=c, r_old=r, r=rn, J=J, gap=gap,
                         I=mutual_info(px, q), D=exp_dist(px, q, d)))
        r = rn
        if tol is not None and gap <= tol:
            break
    return hist


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


def axlab(ax, xl='$D$', yl=None, pad=1):
    ax.set_xlabel(xl, labelpad=pad)
    if yl:
        ax.set_ylabel(yl, labelpad=1)


_erf = np.vectorize(math.erf)


def Phi(x):
    return 0.5*(1+_erf(np.asarray(x, dtype=float)/math.sqrt(2)))


def npdf(x, m=0., s=1.):
    x = np.asarray(x, dtype=float)
    return np.exp(-(x-m)**2/(2*s*s))/(s*math.sqrt(2*math.pi))


def gauss_cell(a, b):
    """For N(0,1): probability, first moment and second moment on (a,b)."""
    pa, pb = npdf(a), npdf(b)
    P = float(Phi(b)-Phi(a))
    m1 = float(pa-pb)
    fa = 0.0 if np.isinf(a) else a*pa
    fb = 0.0 if np.isinf(b) else b*pb
    m2 = float(P+fa-fb)
    return P, m1, m2


def lloyd_max_gauss(N, iters=3000):
    """Lloyd-Max quantizer with N levels for N(0,1); returns (levels, mse)."""
    y = np.linspace(-2, 2, N) if N > 1 else np.array([0.])
    for _ in range(iters):
        t = np.concatenate([[-np.inf], (y[1:]+y[:-1])/2, [np.inf]])
        ynew = []
        for a, b in zip(t[:-1], t[1:]):
            P, m1, _ = gauss_cell(a, b)
            ynew.append(m1/P)
        y = np.array(ynew)
    t = np.concatenate([[-np.inf], (y[1:]+y[:-1])/2, [np.inf]])
    mse = 0.
    for a, b, c in zip(t[:-1], t[1:], y):
        P, m1, m2 = gauss_cell(a, b)
        mse += m2-2*c*m1+c*c*P
    return y, mse


def ecsq_gauss(step, K=400):
    """Uniform cells of width step centred at 0 (midtread), centroid recon; (H bits, mse)."""
    H = 0.; mse = 0.
    for k in range(-K, K+1):
        a, b = (k-.5)*step, (k+.5)*step
        P, m1, m2 = gauss_cell(a, b)
        if P <= 1e-300:
            continue
        c = m1/P
        H -= P*math.log2(P)
        mse += m2-2*c*m1+c*c*P
    return H, mse
