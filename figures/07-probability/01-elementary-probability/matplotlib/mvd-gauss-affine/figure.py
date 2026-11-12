"""Affine construction of N(mu,Sigma), mu=(2,1), Sigma=[[2,1],[1,2]].
(a) 400 standard Gaussian points Z (seed 7) with circles |z|=1,2;
(b) the same points mapped by x = mu + Sigma^{1/2} z, ellipses Q(x)=1,4 and
principal axes along (1,1)/sqrt2 (half-length sqrt3) and (1,-1)/sqrt2 (half-length 1)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

rng = np.random.default_rng(7)
Z = rng.standard_normal((400, 2))
mu = np.array([2., 1.]); S = np.array([[2., 1.], [1., 2.]])
w, V = np.linalg.eigh(S); R = V @ np.diag(np.sqrt(w)) @ V.T
X = mu + Z @ R.T
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, left=.07, right=.98, top=.97, bottom=.22, wspace=.25)
ax = axes[0]; style(ax)
ax.plot(Z[:, 0], Z[:, 1], '.', ms=1.8, color=GREEN)
t = np.linspace(0, 2*pi, 300)
for c in (1, 2):
    ax.plot(c*np.cos(t), c*np.sin(t), color=BLUE, lw=1.2)
ax.set_xlim(-3.6, 3.6); ax.set_ylim(-3.6, 3.6); ax.set_aspect('equal')
ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2]); axlab(ax, '$z_1$', '$z_2$')
ax = axes[1]; style(ax)
ax.plot(X[:, 0], X[:, 1], '.', ms=1.8, color=GREEN)
for c in (1, 2):
    ex, ey = ellipse(mu, S, c); ax.plot(ex, ey, color=BLUE, lw=1.2)
for lam, v in zip(w, V.T):
    v = v*np.sign(v[0]); e = mu+np.sqrt(lam)*v
    ax.annotate('', xy=e, xytext=mu, arrowprops=dict(arrowstyle='-|>', color=STROKE, lw=.9, mutation_scale=7))
dot(ax, *mu)
lab(ax, mu[0]-.15, mu[1]+.25, r'$\bm{\mu}$', RED, ha='right') if False else lab(ax, mu[0]-.12, mu[1]+.22, r'$\mu$', RED, ha='right')
lab(ax, 3.45, 2.5, r'$\sqrt{3}$', STROKE, ha='left')
lab(ax, 2.95, -.25, '$1$', STROKE, ha='left')
ax.set_xlim(-2.4, 6.4); ax.set_ylim(-3.4, 5.4); ax.set_aspect('equal')
ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([-2, 0, 2, 4]); axlab(ax, '$x_1$', '$x_2$')
tags(fig, axes)
inside = [float(np.mean((Z**2).sum(1) <= c*c)) for c in (1, 2)]
save(fig, HERE(__file__), 'figure', {'seed': 7, 'n': 400, 'eig': w.tolist(), 'fraction_inside_c1_c2': inside})
