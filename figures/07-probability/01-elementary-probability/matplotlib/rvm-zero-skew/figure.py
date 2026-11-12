from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Asymmetric table Y in {-5,-1,4}, probs 1/6,1/2,1/3: mean 0, variance 10, third central moment 0.
# (b) contributions p_i (y_i - 0)^3 = -125/6, -1/2, 64/3 sum to 0.
ys = np.array([-5., -1., 4.]); ps = np.array([1/6, 1/2, 1/3])
m, v, g, k = moments(ys, ps)
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
panel(fig, left=.11, right=.98, bottom=.3, wspace=.34)
ax = axes[0]
bars(ax, ys, ps, width=.6)
ax.axvline(0, color=RED, lw=1.2)
for y, p, s in zip(ys, ps, ['1/6', '1/2', '1/3']):
    lab(ax, y, p+.02, s, INK, ha='center', va='bottom')
ax.set_xlim(-6.5, 5.5); ax.set_ylim(0, .62); ax.set_xticks([-5, -1, 0, 4]); ax.set_yticks([0, .25, .5])
axlab(ax, '$y$', '$p_Y(y)$')
ax = axes[1]
contrib = ps*ys**3
cols = [RED if c < 0 else BLUE for c in contrib]
fills = [RED_FILL if c < 0 else BLUE_FILL for c in contrib]
ax.bar(ys, contrib, width=.6, color=fills, edgecolor=cols, lw=.9)
ax.axhline(0, color=STROKE, lw=.85)
for y, c, s in zip(ys, contrib, ['$-125/6$', '$-1/2$', '$64/3$']):
    lab(ax, y, c+(1 if c > 0 else -1), s, INK, ha='center', va='bottom' if c > 0 else 'top')
ax.set_xlim(-6.5, 5.5); ax.set_ylim(-30, 30); ax.set_xticks([-5, -1, 0, 4]); ax.set_yticks([-20, 0, 20])
axlab(ax, '$y$', '$p_Y(y)\\,y^3$')
tags(fig, axes)
save(fig, HERE, 'figure', {'mean': m, 'var': v, 'skew': g, 'kurt': k})
print(m, v, g, k)
