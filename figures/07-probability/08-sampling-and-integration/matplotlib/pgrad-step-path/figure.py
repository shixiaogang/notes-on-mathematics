from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# f(x) = 1{x > 0}, X = theta + eps, eps ~ N(0,1).  J(theta) = Phi(theta), J'(theta) = phi(theta).
# (a) Phi (blue) and the average over the four teaching normals of 1{theta + eps_i > 0} (green staircase):
#     piecewise constant in theta, so the pathwise derivative is 0 except at the jumps theta = -eps_i.
# (b) phi(theta) (blue); mean of the pathwise derivative = 0 (red); score-estimator means
#     1{X>0}(X - theta) averaged over n = 20000 seeded samples at each grid point (green dots).
rng = np.random.default_rng(SEED+2)
eps = np.array(EPS4)
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.26)
a, b = axs
t = np.linspace(-2.5, 2.5, 1001)
a.plot(t, ncdf(t), color=BLUE, lw=1.4)
stair = ((t[:, None]+eps[None, :]) > 0).mean(axis=1)
a.step(t, stair, where='post', color=GREEN, lw=1.2)
a.set_xlim(-2.5, 2.5); a.set_ylim(0, 1.05); a.set_xticks([-2, 0, 2]); a.set_yticks([0, .5, 1])
axlab(a, r'$\theta$')
b.plot(t, npdf(t), color=BLUE, lw=1.4)
b.axhline(0, color=RED, lw=1.3)
tg = np.linspace(-2.25, 2.25, 10); means = []
for th in tg:
    E = rng.standard_normal(20000); X = th+E
    means.append(float(np.mean((X > 0)*E)))
b.plot(tg, means, 'o', color=GREEN, ms=3.4, mew=0)
lab(b, .45, .33, r'$\varphi(\theta)$', BLUE); lab(b, -.95, .022, '沿路径求导', RED)
b.set_xlim(-2.5, 2.5); b.set_ylim(-.05, .45); b.set_xticks([-2, 0, 2]); b.set_yticks([0, .2, .4])
axlab(b, r'$\theta$')
tags(fig, axs)
save(fig, HERE, 'figure', {'theta_grid': tg.tolist(), 'score_means': means, 'phi': npdf(tg).tolist()})
