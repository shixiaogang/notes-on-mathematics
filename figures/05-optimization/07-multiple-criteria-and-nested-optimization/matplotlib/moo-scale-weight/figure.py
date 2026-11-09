from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Same candidates and weight w=(0.6,0.4), with f1 measured in units and tenths of the unit.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .985, .2, .22)
ax = axes[0]; setup(ax, (0, 8), (0, 9.5), range(0, 9, 2), range(0, 10, 2), '成本（万元）', '误差')
cands(ax, 'ABCD', off={'A': (.2, .1), 'B': (.2, .2), 'C': (.15, .25), 'D': (-.1, .35)})
c = .6*2+.4*5; t = np.array([0, 8.]); ax.plot(t, (c-.6*t)/.4, color=PURPLE, lw=1.1, zorder=3)
dot(ax, (2, 5), RED, ms=8)
ax = axes[1]; setup(ax, (0, 80), (0, 9.5), range(0, 81, 20), range(0, 10, 2), '成本（千元）', '误差')
for k in 'ABCD':
    p = CANDS[k]; dot(ax, (10*p[0], p[1]))
for k, d in zip('ABCD', [(2.5, .2), (2.5, .2), (2, .25), (-1, .35)]):
    p = CANDS[k]; ax.text(10*p[0]+d[0], p[1]+d[1], k, color=INK)
c = .6*10+.4*8; t = np.array([0, 15.5]); ax.plot(t, (c-.6*t)/.4, color=PURPLE, lw=1.1, zorder=3)
dot(ax, (10, 8), RED, ms=8)
tags(fig, axes)
save(fig, HERE, 'figure', {'w': [.6, .4], 'scores_wan': {k: .6*v[0]+.4*v[1] for k, v in CANDS.items()}, 'scores_qian': {k: 6*v[0]+.4*v[1] for k, v in CANDS.items()}})
