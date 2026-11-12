from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Target N(0,[[1,rho],[rho,1]]), rho=0.8. Mean-field factors q_j=N(m_j, 1-rho^2); coordinate updates
# m1 <- rho*m2, m2 <- rho*m1, started at (m1,m2)=(-1.5,2).
# (a) target contours c=1,2 (blue), path of (m1,m2) (green), optimum (0,0) (red).
# (b) |m2| after each full round (green, log scale) and reference rho^{2t} * 2 (purple dashed).
rho = RHO
L = np.linalg.cholesky(np.array([[1, rho], [rho, 1]]))
th = np.linspace(0, 2*np.pi, 400)
m1, m2 = -1.5, 2.0; P = [(m1, m2)]; rounds = []
for t in range(8):
    m1 = rho*m2; P.append((m1, m2)); m2 = rho*m1; P.append((m1, m2)); rounds.append(abs(m2))
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.08, right=.98, top=.96, bottom=.24, wspace=.3)
ax = axs[0]
for c, lw in ((1, 1.2), (2, .9)):
    e = c*(L@np.vstack([np.cos(th), np.sin(th)])); ax.plot(e[0], e[1], color=BLUE, lw=lw)
xs = [p[0] for p in P]; ys = [p[1] for p in P]
ax.plot(xs, ys, color=GREEN, lw=1.1, marker='o', ms=2.4)
dot(ax, 0, 0, RED, ms=4.5)
lab(ax, -1.45, 2.12, '起点', GREEN, fontsize=7)
ax.set_aspect('equal'); ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2]); axlab(ax, '$m_1$', '$m_2$')
ax = axs[1]
t = np.arange(1, len(rounds)+1)
ax.semilogy(t, rounds, color=GREEN, lw=0, marker='o', ms=3.4, zorder=5)
ax.semilogy(t, 2*rho**(2*t), color=PURPLE, lw=.9, ls=DASH)
lab(ax, 4.5, .35, r'$2\rho^{2t}$', PURPLE)
ax.set_xlim(.5, 8.5); axlab(ax, '轮次', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'path': [[round(a, 4), round(b, 4)] for a, b in P[:7]], 'rate_per_round': rho**2})
