from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'tail-common'))
from tail_fig import *
# Right tails of three models with tail value 1 at t=1: normal Q(t)/Q(1)? No -- plain models:
# N(0,1): Q(t); Exp(1): e^{-t}; Pareto(alpha=3, x_m=1): t^{-3} for t>=1.
t = np.linspace(0, 8, 801)
fig, ax = figure(width_mm=90, height_mm=56)
ax.semilogy(t, Q(t), color=BLUE, lw=1.4)
ax.semilogy(t, np.exp(-t), color=YELLOW, lw=1.6)
tp = t[t >= 1]
ax.semilogy(np.r_[0, 1, tp], np.r_[1, 1, tp**-3.0], color=PURPLE, lw=1.4)
lab(ax, 3.55, Q(3.55)*1.6, r'$\mathcal{N}(0,1)$', BLUE, ha='left', va='bottom')
lab(ax, 6.3, np.exp(-6.3)*0.55, r'$\operatorname{Exp}(1)$', YELLOW, ha="left", va="top")
lab(ax, 5.2, 5.2**-3*1.8, r'Pareto $\alpha=3$', PURPLE, ha="left", va="bottom")
ax.set_xlim(0, 8); ax.set_ylim(1e-6, 1.5)
logticks(ax, [0, -2, -4, -6])
axlab(ax, '$t$', r'$ℙ(X>t)$')
save(fig, HERE, 'figure', {'normal': 'Q(t)', 'exponential': 'e^{-t}', 'pareto': 't^{-3}, t>=1', 'values_t5': [float(Q(5)), float(np.exp(-5)), 5**-3]})
