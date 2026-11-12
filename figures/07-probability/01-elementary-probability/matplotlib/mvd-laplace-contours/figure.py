"""Two models with Laplace(b=1/sqrt2) marginals, zero mean and identity covariance.
(a) elliptical Laplace X = sqrt(W) Z, W ~ Exp(1), Z ~ N(0,I_2): density g_2(|x|), circular contours;
(b) product of independent Laplace components: density (1/2) exp(-sqrt2(|x1|+|x2|)), diamond contours.
Both show contour levels 0.1, 0.03, 0.01, 0.003 (blue); 600 sampled points each (seeds 41, 42, green)."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

def g2(r):
    s = np.linspace(-30, 6, 6001); w = np.exp(s)
    vals = (2*pi*w)**(-1)*np.exp(-np.multiply.outer(r*r, 1/(2*w))-w)*w
    return np.trapezoid(vals, s, axis=-1)
xs = np.linspace(-4, 4, 161); X1, X2 = np.meshgrid(xs, xs)
R = np.sqrt(X1**2+X2**2); rr = np.linspace(0, 6, 601); E = np.interp(R, rr, g2(rr))
P = .5*np.exp(-np.sqrt(2)*(np.abs(X1)+np.abs(X2)))
levels = [.003, .01, .03, .1]
r1 = np.random.default_rng(41); A = np.sqrt(r1.exponential(1, 600))[:, None]*r1.standard_normal((600, 2))
r2 = np.random.default_rng(42); B = r2.laplace(0, 1/np.sqrt(2), (600, 2))
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, left=.07, right=.98, top=.97, bottom=.22, wspace=.22)
for ax, F, S in zip(axes, (E, P), (A, B)):
    style(ax)
    ax.plot(S[:, 0], S[:, 1], '.', ms=1.5, color=GREEN)
    ax.contour(X1, X2, F, levels=levels, colors=BLUE, linewidths=1.0, zorder=5)
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4); ax.set_aspect('equal')
    ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_yticks([-4, -2, 0, 2, 4]); axlab(ax, '$x_1$', '$x_2$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'levels': levels, 'seeds': [41, 42], 'n': 600,
     'E_X1sq_X2sq_elliptical_sample': float(np.mean(A[:, 0]**2*A[:, 1]**2)), 'E_X1sq_X2sq_product_sample': float(np.mean(B[:, 0]**2*B[:, 1]**2))})
