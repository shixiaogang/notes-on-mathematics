from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 贯穿例子的完整运行：(a) 轨迹与信赖域；(b) 半径与 rho。
H = run_tr(O_X, 2.)
fig, axs = figure(width_mm=112, height_mm=62, ncols=2, width_ratios=[1.25, 1])
ax = axs[0]; X1, X2 = np.meshgrid(np.linspace(-3.0, 1.2, 500), np.linspace(-2.2, 1.2, 500))
ax.contour(X1, X2, f(np.array([X1, X2])), levels=[-1.5, -1.2, -.85, -.4, 0, .6, 1.5, 3], colors=[BLUE], linewidths=.7)
for h in H:
    if h['t'] > 4: continue
    if h['ok']:
        ax.add_patch(Circle(h['x'], h['D'], fill=False, ec=MUTED, lw=.6, ls=(0, (3, 2))))
xs = np.array([h['x'] for h in H if h['ok']] + [H[-1]['x'] + H[-1]['p']]); ax.plot(xs[:, 0], xs[:, 1], color=GREEN, lw=1.5, marker='o', ms=3.6, mew=0, zorder=5)
for h in H:
    if not h['ok']:
        q = h['x'] + h['p']; ax.plot([h['x'][0], q[0]], [h['x'][1], q[1]], color=RED, lw=.9, ls=(0, (2, 2)), zorder=4); ax.plot(*q, 'o', mfc='white', mec=RED, mew=.9, ms=4.4, zorder=6)
ax.plot(*XSTAR, 'o', color=RED, ms=4.8, mew=0, zorder=7); ax.set_aspect('equal'); ax.set_xlim(-3.0, 1.2); ax.set_ylim(-2.2, 1.2); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
ax = axs[1]; T = [h['t'] for h in H]
ax.step(T, [h['D'] for h in H], where='mid', color=GREEN, lw=1.4)
ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$\\Delta^{(t)}$', labelpad=1); ax.set_ylim(0, 2.6); ax.set_xlim(-.4, len(H)-.6)
for h in H:
    ax.plot([h['t']], [h['D']], 'o' if h['ok'] else 'o', color=GREEN if h['ok'] else 'white', mec=GREEN if h['ok'] else RED, mew=.9, ms=4, zorder=6)
panels(fig, .09, .985, .985, .2, .26); tags(fig, axs)
save(fig, HERE, 'figure', {'x0': [0, 0], 'D0': 2, 'eta': [.25, .75], 'rounds': len(H), 'rho': [float(h['rho']) for h in H]})
