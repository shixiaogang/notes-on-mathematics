from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：摆的相空间。小圆盘在无阻尼下面积保持，有阻尼 c=0.4 下面积以 exp(-c t) 收缩。
fig, axes = figure(width_mm=112, height_mm=52, ncols=2, sharey=True)
panel(fig, .07, .985, .96, .22, .08)
def field(c):
    return lambda t, Z: np.c_[Z[:, 1], -np.sin(Z[:, 0])-c*Z[:, 1]]
th = np.linspace(0, 2*np.pi, 721); D0 = np.c_[1.5+.35*np.cos(th), .35*np.sin(th)]
q = np.linspace(-3.6, 3.6, 300); p = np.linspace(-2.6, 2.6, 300); Q, P = np.meshgrid(q, p); H = P**2/2+1-np.cos(Q)
out = {}
for ax, c in zip(axes, (0., .4)):
    ax.contour(Q, P, H, levels=[.25, .75, 1.25, 2.0, 2.8], colors=[GRID], linewidths=.6)
    ts = np.linspace(0, 6, 1201); f = field(c); Z = D0.copy(); areas = {0: shoelace(D0)}
    idx = {600: 3, 1200: 6}
    for i, (a, b) in enumerate(zip(ts[:-1], ts[1:]), 1):
        h = b-a; k1 = f(a, Z); k2 = f(a, Z+h/2*k1); k3 = f(a, Z+h/2*k2); k4 = f(a, Z+h*k3); Z = Z+h/6*(k1+2*k2+2*k3+k4)
        if i in idx:
            ax.fill(Z[:, 0], Z[:, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1); areas[idx[i]] = shoelace(Z)
    ax.plot(D0[:, 0], D0[:, 1], color=RED, lw=1.2)
    ax.set_xlim(-3.6, 3.6); ax.set_ylim(-2.6, 2.6); ax.set_aspect('equal'); ax.set_xticks([-3, 0, 3]); ax.set_xlabel('$q$', labelpad=0); out[c] = areas
axes[0].set_yticks([-2, 0, 2]); axes[0].set_ylabel('$p$', labelpad=1)
tags(fig, axes)
print(out, np.pi*.35**2*np.exp(-.4*np.array([3, 6])))
save(fig, HERE, 'figure', {'areas': {str(k): v for k, v in out.items()}})
