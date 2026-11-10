from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：无阻尼摆 q'=p, p'=-sin q，沿周期轨道的初值 Jacobian 最大奇异值随 t 增长，轨迹却有界。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1, 1.5]})
panel(fig, .08, .985, .96, .26, .3)
def F(t, z):
    q, p, a, b, c, d = z
    return np.array([p, -np.sin(q), c, d, -np.cos(q)*a, -np.cos(q)*b])
ts = np.linspace(0, 40, 8001); Z = rk4(F, [0., 1.2, 1., 0., 0., 1.], ts)
ax = axes[0]; ax.plot(Z[:, 0], Z[:, 1], color=BLUE, lw=1.4); ax.plot([0], [1.2], 'o', ms=4.4, color=RED, mew=0, zorder=5)
ax.set_aspect('equal'); ax.set_xlim(-1.7, 1.7); ax.set_ylim(-1.5, 1.5); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$q$', labelpad=0); ax.set_ylabel('$p$', labelpad=1)
s = np.array([np.linalg.svd(np.array([[a, b], [c, d]]), compute_uv=False)[0] for a, b, c, d in Z[:, 2:]])
ax = axes[1]; ax.plot(ts, s, color=RED, lw=1.1); ax.set_xlim(0, 40); ax.set_ylim(0, s.max()*1.08); ax.set_xticks([0, 20, 40]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$\\sigma_{\\max}$', labelpad=1)
tags(fig, axes)
print('smax', s[-1], s.max(), 'det dev', abs(Z[-1,2]*Z[-1,5]-Z[-1,3]*Z[-1,4]-1))
save(fig, HERE, 'figure', {'field': 'pendulum', 'z0': [0, 1.2], 'T': 40})
