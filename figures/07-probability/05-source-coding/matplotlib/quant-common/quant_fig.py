"""Shared helpers for the chapter 7.21 figures (quantization).

Running source: X ~ Laplace(0,1), density f(x) = exp(-|x|)/2, variance 2.
All quantities are computed from closed-form truncated moments of this density,
exact finite sums, or seeded simulations; no hand-entered data.
"""
from pathlib import Path
import sys, math
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))


def panel(fig, left=.1, right=.97, top=.96, bottom=.27, wspace=.32):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)


def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')


def dot(ax, x, y, color=RED, ms=4.2, z=6, **k):
    ax.plot([x], [y], 'o', ms=ms, color=color, mew=0, zorder=z, clip_on=False, **k)


def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)


# ---------- Laplace(0,1) truncated moments ----------
def pdf(x):
    return 0.5*np.exp(-np.abs(x))


def _G(k, x):
    """int_0^x t^k e^{-|t|}/2 dt (signed), k = 0, 1, 2; x may be +-inf."""
    if math.isinf(x):
        v = math.factorial(k)/2
        return v if x > 0 else (-1)**(k+1)*v
    a = abs(x); e = math.exp(-a)
    if k == 0: g = (1-e)/2
    elif k == 1: g = (1-(a+1)*e)/2
    else: g = (2-(a*a+2*a+2)*e)/2
    return g if x >= 0 else (-1)**(k+1)*g


def moment(k, a, b):
    "int_a^b x^k f(x) dx"
    return _G(k, b) - _G(k, a)


def mass(a, b): return moment(0, a, b)


def cmean(a, b): return moment(1, a, b)/moment(0, a, b)


def cell_mse(a, b, c):
    "int_a^b (x-c)^2 f(x) dx"
    return moment(2, a, b) - 2*c*moment(1, a, b) + c*c*moment(0, a, b)


def mse(t, c):
    """thresholds t (len N-1, increasing), points c (len N). Exact E(X-Q(X))^2."""
    edges = [-math.inf] + list(t) + [math.inf]
    return sum(cell_mse(edges[j], edges[j+1], c[j]) for j in range(len(c)))


def lloyd(c, rounds):
    "Lloyd-Max on Laplace(0,1); returns list of (t, c, D) after each half-step pair"
    c = np.array(c, float); out = []
    for _ in range(rounds):
        t = (c[:-1]+c[1:])/2
        edges = [-math.inf] + list(t) + [math.inf]
        c = np.array([cmean(edges[j], edges[j+1]) for j in range(len(c))])
        out.append((t.copy(), c.copy(), mse(t, c)))
    return out


def uniform_q(x, N, delta):
    "mid-rise uniform quantizer with N levels, step delta, saturation outside [-N delta/2, N delta/2]"
    i = np.clip(np.floor(x/delta) + N//2, 0, N-1)
    return (i - N/2 + 0.5)*delta


def uniform_parts(N, delta):
    "exact granular and overload MSE of the N-level mid-rise uniform quantizer for Laplace(0,1)"
    L = N*delta/2
    gran = 0.0
    for i in range(N):
        a = -L + i*delta; b = a + delta; c = a + delta/2
        gran += cell_mse(a, b, c)
    # remove the outer cells' unbounded parts: overload regions x > L and x < -L
    ov = 2*cell_mse(L, math.inf, L - delta/2)
    return gran, ov


def entropy_bits(p):
    p = np.asarray(p, float); p = p[p > 0]
    return float(-(p*np.log2(p)).sum())


# ---------- standard Gaussian (for the two-dimensional example) ----------
def Phi(x):
    return 0.5*(1+math.erf(x/math.sqrt(2))) if not math.isinf(x) else (1.0 if x > 0 else 0.0)


def phi(x):
    return 0.0 if math.isinf(x) else math.exp(-x*x/2)/math.sqrt(2*math.pi)


def gauss_lloyd(N, rounds=2000):
    "Lloyd-Max for N(0,1): returns thresholds, points, MSE"
    c = np.linspace(-1.5, 1.5, N)
    for _ in range(rounds):
        t = (c[:-1]+c[1:])/2; e = [-math.inf]+list(t)+[math.inf]
        c = np.array([(phi(e[j])-phi(e[j+1]))/(Phi(e[j+1])-Phi(e[j])) for j in range(N)])
    t = (c[:-1]+c[1:])/2; e = [-math.inf]+list(t)+[math.inf]
    D = 1 - sum((Phi(e[j+1])-Phi(e[j]))*c[j]**2 for j in range(N))
    return t, c, D


def nearest(X, C):
    d2 = ((X[:, None, :]-C[None, :, :])**2).sum(-1)
    return d2.argmin(1), d2.min(1)


def lloyd_samples(X, C, rounds=60):
    C = C.copy()
    for _ in range(rounds):
        j, _ = nearest(X, C)
        for k in range(len(C)):
            if (j == k).any(): C[k] = X[j == k].mean(0)
    return C


def voronoi_edges(C, box, n=1500):
    """Segments of the Voronoi diagram of points C clipped to box=(x0,x1,y0,y1); computed by testing
    sample points on every perpendicular bisector."""
    x0, x1, y0, y1 = box; segs = []
    for i in range(len(C)):
        for k in range(i+1, len(C)):
            m = (C[i]+C[k])/2; v = C[k]-C[i]; u = np.array([-v[1], v[0]])/np.linalg.norm(v)
            s = np.linspace(-20, 20, 40001); P = m[None, :]+s[:, None]*u[None, :]
            inb = (P[:, 0] >= x0) & (P[:, 0] <= x1) & (P[:, 1] >= y0) & (P[:, 1] <= y1)
            di = ((P-C[i])**2).sum(1)
            others = np.delete(np.arange(len(C)), [i, k])
            dmin = ((P[:, None, :]-C[None, others, :])**2).sum(-1).min(1) if len(others) else np.full(len(P), np.inf)
            ok = inb & (di <= dmin+1e-9)
            if ok.sum() >= 2:
                idx = np.where(ok)[0]; segs.append((P[idx[0]], P[idx[-1]]))
    return segs


def midtread(delta, recon='mid'):
    """Infinite-range mid-tread uniform quantizer Q(x) = delta*round(x/delta) for Laplace(0,1).
    Returns (cell probabilities, exact MSE). recon='mid' uses k*delta, 'centroid' the conditional means."""
    K = int(math.ceil(45/delta)); ps = []; D = 0.0
    for k in range(-K, K+1):
        a, b = (k-.5)*delta, (k+.5)*delta
        p = mass(a, b); ps.append(p)
        if p > 0:
            c = k*delta if recon == 'mid' else cmean(a, b)
            D += cell_mse(a, b, c)
    return np.array(ps), D


H_LAPLACE = math.log2(2*math.e)   # differential entropy of Laplace(0,1) in bits
