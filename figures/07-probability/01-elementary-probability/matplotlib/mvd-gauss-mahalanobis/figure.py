"""Mahalanobis distance for mu=(2,1), Sigma=[[2,1],[1,2]].
(a) density contours Q(x)=c^2, c=0.5,1,1.5,2 (Q=(x-mu)^T Sigma^{-1}(x-mu)); points a=mu+(1,1), b=mu+(1,-1)
have the same Euclidean distance sqrt2 from mu but Q(a)=2/3, Q(b)=2.
(b) P(Q(X)<=c^2)=1-exp(-c^2/2) (d=2) against the fraction of 4000 simulated points (seed 11)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'mvd-common'))
from mvd_fig import *

mu = np.array([2., 1.]); S = np.array([[2., 1.], [1., 2.]]); Si = np.linalg.inv(S)
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.07, right=.97, top=.96, bottom=.26, wspace=.3)
ax = axes[0]; style(ax)
for c in (.5, 1, 1.5, 2):
    ex, ey = ellipse(mu, S, c); ax.plot(ex, ey, color=BLUE, lw=1.0)
t = np.linspace(0, 2*pi, 300)
ax.plot(mu[0]+np.sqrt(2)*np.cos(t), mu[1]+np.sqrt(2)*np.sin(t), color=STROKE, lw=.8, ls=DASH)
a = mu+np.array([1, 1.]); b = mu+np.array([1, -1.])
Q = lambda x: float((x-mu) @ Si @ (x-mu))
dot(ax, *mu, color=STROKE, ms=3)
dot(ax, *a); dot(ax, *b)
lab(ax, a[0]+.22, a[1]+.12, '$a$', RED); lab(ax, b[0]+.2, b[1]-.45, '$b$', RED)
ax.set_xlim(-1.2, 5.2); ax.set_ylim(-2.2, 4.2); ax.set_aspect('equal')
ax.set_xticks([0, 2, 4]); ax.set_yticks([-2, 0, 2, 4]); axlab(ax, '$x_1$', '$x_2$')
ax = axes[1]; style(ax)
rng = np.random.default_rng(11); Z = rng.standard_normal((4000, 2)); q = (Z**2).sum(1)
cc = np.linspace(0, 3.2, 300); ax.plot(cc, 1-np.exp(-cc**2/2), color=BLUE, lw=1.4)
cs = np.array([.5, 1, 1.5, 2, 2.5, 3]); emp = [float(np.mean(q <= c*c)) for c in cs]
ax.plot(cs, emp, 'o', ms=3.2, color=GREEN, zorder=5)
for c in (1, 2, 3):
    ax.plot([c, c], [0, 1-np.exp(-c*c/2)], color=STROKE, lw=.6, ls=DOT)
lab(ax, 1.05, .3, '$0.393$', ha='left'); lab(ax, 2.05, .74, '$0.865$', ha='left'); lab(ax, 2.92, .86, '$0.989$', ha='right')
ax.set_xlim(0, 3.2); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, .5, 1])
axlab(ax, '$c$', r'$\mathrm{P}(Q\leq c^{2})$')
tags(fig, axes)
save(fig, HERE(__file__), 'figure', {'Qa': Q(a), 'Qb': Q(b), 'seed': 11, 'n': 4000, 'c': cs.tolist(), 'empirical': emp})
