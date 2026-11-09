"""Shared data and helpers for the matplotlib figures of the manifold optimization chapter (prefix mfo-)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL  # noqa: F401,E402
import numpy as np  # noqa: E402

GRAY = '#4C4D4F'
A3 = np.diag([1., 2., 4.])
X0 = np.array([2., 2., 1.]) / 3
E1 = np.array([1., -2., 2.]) / 3
E2 = np.array([2., -1., -2.]) / 3


def f3(x):
    return .5 * x @ A3 @ x


def grad3(x):
    return A3 @ x - (x @ A3 @ x) * x


def retr(x, v):
    return (x + v) / np.linalg.norm(x + v)


def tangent_basis(x):
    Q = np.linalg.qr(np.c_[x, np.eye(len(x))[:, 1:]])[0]
    return Q[:, 1:]


class Disk:
    """Orthographic view of the unit sphere drawn in plain 2-D axes."""
    def __init__(self, az, el, N=500):
        a, e = np.radians(az), np.radians(el)
        self.view = np.array([np.cos(e)*np.cos(a), np.cos(e)*np.sin(a), np.sin(e)])
        self.right = np.array([-np.sin(a), np.cos(a), 0.])
        self.up = np.cross(self.view, self.right)
        u = np.linspace(-1, 1, N)
        self.U, self.V = np.meshgrid(u, u)
        r2 = self.U**2 + self.V**2
        self.mask = r2 >= 1
        W = np.sqrt(np.maximum(1 - r2, 0))
        self.P = (self.U[..., None]*self.right + self.V[..., None]*self.up + W[..., None]*self.view)

    def rayleigh(self):
        F = .5*(self.P[..., 0]**2 + 2*self.P[..., 1]**2 + 4*self.P[..., 2]**2)
        return np.ma.array(F, mask=self.mask)

    def xy(self, p):
        p = np.asarray(p)
        return p @ self.right, p @ self.up

    def front(self, p):
        return np.asarray(p) @ self.view >= 0

    def outline(self, ax):
        th = np.linspace(0, 2*np.pi, 400)
        ax.fill(np.cos(th), np.sin(th), color=BLUE_FILL, lw=0, zorder=0)
        ax.plot(np.cos(th), np.sin(th), color=BLUE, lw=1.1, zorder=1)
        ax.set_aspect('equal')
        ax.axis('off')


def arc(a, b, n=40):
    t = np.linspace(0, 1, n)[:, None]
    p = (1 - t)*a + t*b
    return p / np.linalg.norm(p, axis=1, keepdims=True)


def sphere_exact_step(x, Ax, d, Ad):
    """Exact minimizer over a>0 of f(normalize(x+a d)), f = x'Ax/2, d tangent, descent."""
    q, b, c, s = x @ Ax, Ax @ d, d @ Ad, d @ d
    D = (c - q*s)**2 + 4*b*b*s
    return ((c - q*s) - np.sqrt(D)) / (2*b*s)


def tcg(grad, hess, radius, forcing, inner=lambda u, v: u @ v, maxit=500):
    """Steihaug-Toint truncated CG in a tangent space; returns step, status, Hv count, partial steps."""
    v = 0*grad
    r = grad.copy()
    d = -r
    r0 = np.sqrt(inner(r, r))
    cnt = 0
    if r0 == 0:
        return v, 'zero', 0
    for _ in range(maxit):
        Hd = hess(d)
        cnt += 1
        dHd = inner(d, Hd)
        def to_boundary():
            vd, dd, vv = inner(v, d), inner(d, d), inner(v, v)
            return (-vd + np.sqrt(vd*vd + dd*(radius*radius - vv))) / dd
        if dHd <= 0:
            return v + to_boundary()*d, 'neg', cnt
        a = inner(r, r) / dHd
        vn = v + a*d
        if np.sqrt(inner(vn, vn)) >= radius:
            return v + to_boundary()*d, 'bd', cnt
        v = vn
        rn = r + a*Hd
        if np.sqrt(inner(rn, rn)) <= r0*forcing:
            return v, 'conv', cnt
        d = -rn + inner(rn, rn)/inner(r, r)*d
        r = rn
    return v, 'max', cnt
