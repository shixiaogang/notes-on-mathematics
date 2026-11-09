from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# Extragradient with alpha=1/L=1 on f=xy over the box: last iterates cycle, averages converge.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .07, .985, .975, .235, .28)
P = lambda z: np.clip(z, -1, 1); F = lambda z: np.array([z[1], -z[0]])
z = np.array([1., 0]); Zs = [z]; Ts = []
for t in range(32):
    w = P(z-F(z)); z = P(z-F(w)); Ts.append(w); Zs.append(z)
Zs = np.array(Zs); Ts = np.array(Ts); gap = lambda v: np.abs(v[..., 0])+np.abs(v[..., 1])
ax = axes[0]; setup(ax, (-1.5, 1.5), (-1.5, 1.5), (-1, 0, 1), (-1, 0, 1), equal=True)
ax.fill([-1, 1, 1, -1], [-1, -1, 1, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=.85, zorder=0)
path(ax, Zs[:5], GREEN, ms=3.6); ax.plot(Ts[:4, 0], Ts[:4, 1], 's', color=YELLOW, ms=4, mew=0, zorder=6); dot(ax, (0, 0))
ax = axes[1]; T = np.arange(1, 33); avg = np.cumsum(Ts, axis=0)/T[:, None]
setup(ax, (0, 32), (0, 4.2), (0, 8, 16, 24, 32), (0, 1, 2, 3, 4), xl='$T$', yl='间隙')
ax.plot(T, gap(Zs[1:]), color=GREEN, lw=1.3); ax.plot(T, gap(avg), color=YELLOW, lw=1.5); ax.plot(T, 4/T, color=PURPLE, lw=1.3, ls=(0, (3, 2)))
ax.text(31.5, 1.1, '最后一点', fontsize=7.5, ha='right'); ax.text(9, .65, '平均', fontsize=7.5, color=INK); ax.text(3.0, 2.1, '$4/T$', fontsize=7.5, color=PURPLE)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': 'xy', 'alpha': 1, 'Z': '[-1,1]^2', 'bound': '4/T'})
print(Zs[:5], Ts[:4], gap(avg)[:8])
