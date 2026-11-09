"""Shared numerics for chapter 5.16 figures: the running one-dimensional example.

Target: natural cubic spline through integer readings on [0,8]; surrogate: zero-mean GP
with k(x,x') = 2^{-(x-x')^2}. Numerics only (numpy + math.erf).
"""
import math
import sys
from pathlib import Path
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL, STROKE

KX = np.arange(0.0, 9.0)
KY = np.array([0.9, 0.2, -0.5, 0.1, 0.7, 0.3, -1.0, -0.3, 0.8])


def _spline_second_derivs():
    n = len(KX)
    A = np.zeros((n, n)); b = np.zeros(n)
    A[0, 0] = A[-1, -1] = 1.0
    for i in range(1, n - 1):
        A[i, i - 1], A[i, i], A[i, i + 1] = 1.0, 4.0, 1.0
        b[i] = 6.0 * (KY[i + 1] - 2 * KY[i] + KY[i - 1])
    return np.linalg.solve(A, b)


_M = _spline_second_derivs()


def f(x):
    """Target: natural cubic spline through (KX, KY)."""
    x = np.asarray(x, float)
    i = np.clip(np.floor(x).astype(int), 0, len(KX) - 2)
    t = x - KX[i]; u = 1.0 - t
    return (_M[i] * u**3 + _M[i + 1] * t**3) / 6.0 + (KY[i] - _M[i] / 6.0) * u + (KY[i + 1] - _M[i + 1] / 6.0) * t


def k(a, b, ell2=None, amp=1.0):
    """Kernel; default 2^{-(x-x')^2}. ell2 = ell^2 gives exp(-d^2/(2 ell^2))."""
    a = np.atleast_1d(a)[:, None]; b = np.atleast_1d(b)[None, :]
    d2 = (a - b) ** 2
    if ell2 is None:
        return amp * 2.0 ** (-d2)
    return amp * np.exp(-d2 / (2 * ell2))


def posterior(xo, yo, xs, tau2=0.0, ell2=None, amp=1.0, full=False):
    xo = np.atleast_1d(np.asarray(xo, float)); yo = np.atleast_1d(np.asarray(yo, float)); xs = np.atleast_1d(np.asarray(xs, float))
    if len(xo) == 0:
        K = k(xs, xs, ell2, amp)
        return np.zeros_like(xs), K if full else np.diag(K).copy()
    K = k(xo, xo, ell2, amp) + (tau2 + 1e-12) * np.eye(len(xo))
    Ks = k(xs, xo, ell2, amp)
    L = np.linalg.cholesky(K)
    alpha = np.linalg.solve(L.T, np.linalg.solve(L, yo))
    m = Ks @ alpha
    V = np.linalg.solve(L, Ks.T)
    if full:
        return m, k(xs, xs, ell2, amp) - V.T @ V
    return m, np.maximum(np.diag(k(xs, xs, ell2, amp)) - np.sum(V * V, axis=0), 0.0)


def Phi(z):
    return np.vectorize(lambda u: 0.5 * math.erfc(-u / math.sqrt(2)))(z) * 1.0


def phi(z):
    return np.exp(-0.5 * np.asarray(z, float) ** 2) / math.sqrt(2 * math.pi)


def ei(b, m, s):
    m = np.asarray(m, float); s = np.asarray(s, float)
    out = np.maximum(b - m, 0.0)
    pos = s > 1e-5
    z = (b - m[pos]) / s[pos]
    out[pos] = (b - m[pos]) * Phi(z) + s[pos] * phi(z)
    return out


def pi(b, m, s, xi=0.0):
    m = np.asarray(m, float); s = np.asarray(s, float)
    out = (m < b - xi - 1e-9) * 1.0
    pos = s > 1e-5
    out[pos] = Phi((b - xi - m[pos]) / s[pos])
    return out


def norm_ppf(p):
    lo, hi = -9.0, 9.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if 0.5 * math.erfc(-mid / math.sqrt(2)) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def band(ax, x, m, s, c=2.0, fill=BLUE_FILL):
    ax.fill_between(x, m - c * s, m + c * s, color=fill, lw=0, zorder=1)


def obs(ax, xo, yo, **kw):
    style = dict(s=13, color=GREEN, zorder=5, lw=0)
    style.update(kw)
    ax.scatter(xo, yo, **style)


def axes_style(ax, xlabel=None, ylabel=None):
    for sp in ('left', 'bottom'):
        ax.spines[sp].set_linewidth(.95)
    ax.tick_params(width=.85, length=2.5)
    if xlabel: ax.set_xlabel(xlabel, labelpad=1.5)
    if ylabel: ax.set_ylabel(ylabel, labelpad=1.5)


def panel_label(ax, s, y=-.34):
    ax.text(.5, y, s, transform=ax.transAxes, ha='center', va='top')


RUN_X = [1.0, 4.0, 7.0, 8.0, 6.0, 0.0]  # noiseless EI run on integer candidates
XG = np.linspace(0, 8, 401)
C = np.arange(9.0)
