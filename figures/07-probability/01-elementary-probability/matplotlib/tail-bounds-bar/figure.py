from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# X ~ Bin(20,1/2), event {X>=15}: exact value and the bounds of this chapter (log scale).
raw = [float((PB*KB.astype(float)**p).sum())/15**p for p in range(1, 60)]
pbest = int(np.argmin(raw))+1
rows = [('精确值', bin_tail(15), BLUE, BLUE_FILL),
        ('Markov', 10/15, PURPLE, PURPLE_FILL),
        ('Chebyshev', 5/25, PURPLE, PURPLE_FILL),
        ('四阶中心矩', bin_central_moment(4)/5**4, PURPLE, PURPLE_FILL),
        ('六阶中心矩', bin_central_moment(6)/5**6, PURPLE, PURPLE_FILL),
        ('指数矩', 2**20/3**15, PURPLE, PURPLE_FILL),
        ('最优原点矩', min(raw), PURPLE, PURPLE_FILL)]
fig, ax = figure(width_mm=96, height_mm=54)
y = np.arange(len(rows))[::-1]
for yi, (name, v, ec, fc) in zip(y, rows):
    ax.barh(yi, np.log10(v)+2.2, left=-2.2, height=.6, color=fc, edgecolor=ec, lw=.8)
    ax.text(np.log10(v)+.04, yi, '%.4f' % v, va='center', ha='left', fontsize=7.5, color=INK)
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows])
ax.set_xlim(-2.2, .45); ax.set_xticks([-2, -1, 0]); ax.set_xticklabels(['$10^{-2}$', '$10^{-1}$', '$1$'])
ax.tick_params(axis='y', length=0)
ax.set_xlabel('ℙ$(X\\geq15)$ 及其上界'.replace(' 及其上界', ''), labelpad=1)
save(fig, HERE, 'figure', {name: v for name, v, _, _ in rows} | {'best_raw_order': pbest})
