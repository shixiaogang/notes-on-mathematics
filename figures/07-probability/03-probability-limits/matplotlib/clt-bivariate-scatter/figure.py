from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# xi, eta independent Rademacher (+-1). n = 100, M = 1500 replications, seed 3.
# (a) X = (xi, xi+eta), Sigma = [[1,1],[1,2]]: points sqrt(n) Xbar_n with N(0,Sigma)
#     contours at Mahalanobis radius 1 and 2;
# (b) X = (xi, 2 xi), Sigma = [[1,2],[2,4]] singular: points on the line y = 2x;
#     direction a = (2,-1)/sqrt5 has zero variance.
rng = np.random.default_rng(3)
n, M = 100, 1500
A = (2*rng.binomial(n, .5, M)-n)/math.sqrt(n)
B = (2*rng.binomial(n, .5, M)-n)/math.sqrt(n)
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, left=.08, right=.98, bottom=.24, wspace=.25)
a.plot(A, A+B, 'o', ms=1.3, color=GREEN, mew=0)
S = np.array([[1, 1], [1, 2]]); w, V = np.linalg.eigh(S); th = np.linspace(0, 2*np.pi, 300)
for r in (1, 2):
    E = V @ np.diag(np.sqrt(w)) @ np.vstack([np.cos(th), np.sin(th)])*r
    a.plot(E[0], E[1], color=BLUE, lw=1.2)
b.plot(A, 2*A, 'o', ms=1.6, color=GREEN, mew=0)
u = np.array([1, 2])/math.sqrt(5); v = np.array([2, -1])/math.sqrt(5)
b.annotate('', xy=(2.2*v[0], 2.2*v[1]), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.0, mutation_scale=7))
b.annotate('', xy=(2.6*u[0], 2.6*u[1]), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=STROKE, lw=.9, mutation_scale=7))
lab(b, 2.2*v[0]+.15, 2.2*v[1]-.1, r'$\mathbf{a}$', RED, ha='left', va='top')
lab(b, 2.6*u[0]+.2, 2.6*u[1], r'$\mathbf{u}$', STROKE, ha='left', va='center')
for ax in (a, b):
    ax.set_xlim(-4, 4); ax.set_ylim(-5.5, 5.5); ax.set_aspect('equal'); ax.set_xticks([-4, -2, 0, 2, 4])
    ax.axhline(0, color=STROKE, lw=.5); ax.axvline(0, color=STROKE, lw=.5)
axlab(a, '第一坐标', '第二坐标'); axlab(b, '第一坐标', None)
tags(fig, (a, b))
C = np.cov(np.vstack([A, A+B]))
save(fig, HERE, 'figure', {'seed': 3, 'n': n, 'M': M, 'sample_cov_a': C.round(3).tolist()})
