from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# Monitoring simultaneous GDA on f=xy: the objective value oscillates, the distance grows.
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panels(fig, .08, .985, .975, .26, .3)
a = .5; T = 16; S = gda(A, a, T, (1, 0)); t = np.arange(T+1)
ax = axes[0]; setup(ax, (0, T), (-6, 6), (0, 4, 8, 12, 16), (-5, 0, 5), xl='$t$', yl='$f(x^{(t)},y^{(t)})$')
ax.axhline(0, color=MUTED, lw=.85, ls=':'); ax.plot(t, S[:, 0]*S[:, 1], '-o', color=GREEN, lw=1.2, ms=2.6, mew=0)
ax = axes[1]; setup(ax, (0, T), (0, 6.5), (0, 4, 8, 12, 16), (0, 2, 4, 6), xl='$t$', yl=r'梯度范数')
ax.plot(t, np.linalg.norm(S, axis=1), color=RED, lw=1.4)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': 'xy', 'alpha': a, 'z0': [1, 0]})
print(S[:6], (S[:6, 0]*S[:6, 1]))
