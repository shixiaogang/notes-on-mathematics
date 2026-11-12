from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# (a) Z ~ N(0,1): exact Q(t), Chernoff e^{-t^2/2}, Chebyshev min(1,1/t^2).
# (b) X ~ Exp(1): exact e^{-t}, Chernoff min(1, t e^{1-t}), Markov min(1,1/t).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, wspace=.34, bottom=.28)
ax = axes[0]; t = np.linspace(0, 5, 600)
ax.semilogy(t, Q(t), color=BLUE, lw=1.4)
ax.semilogy(t, np.exp(-t**2/2), color=PURPLE, lw=1.4)
ax.semilogy(t, np.minimum(1, 1/np.maximum(t, 1e-9)**2), color=YELLOW, lw=1.6)
lab(ax, 4.9, 1/4.9**2*.5, 'Chebyshev', YELLOW, ha='right', va='top')
lab(ax, 3.95, 3e-3, 'Chernoff', PURPLE, ha='left', va='center')
lab(ax, 3.1, Q(3.1)*.5, '精确值', BLUE, ha='right', va='top')
ax.set_xlim(0, 5); ax.set_ylim(1e-6, 1.5); logticks(ax, [0, -2, -4, -6]); axlab(ax, '$t$', 'ℙ$(Z\\geq t)$')
ax = axes[1]; t = np.linspace(.01, 12, 800)
ax.semilogy(t, np.exp(-t), color=BLUE, lw=1.4)
ax.semilogy(t, np.minimum(1, np.where(t > 1, t*np.exp(1-t), 1)), color=PURPLE, lw=1.4)
ax.semilogy(t, np.minimum(1, 1/t), color=YELLOW, lw=1.6)
lab(ax, 11.8, 1/11.8*1.25, 'Markov', YELLOW, ha='right', va='bottom')
lab(ax, 8.3, .012, 'Chernoff', PURPLE, ha='left', va='bottom')
lab(ax, 6.3, np.exp(-6.3)*.45, '精确值', BLUE, ha='right', va='top')
ax.set_xlim(0, 12); ax.set_ylim(1e-5, 1.5); logticks(ax, [0, -1, -2, -3, -4, -5]); ax.set_xticks([0, 2, 4, 6, 8, 10, 12]); axlab(ax, '$t$', 'ℙ$(X\\geq t)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'normal_t3': [float(Q(3)), float(np.exp(-4.5)), 1/9], 'exp_t5': [float(np.exp(-5)), float(5*np.exp(-4)), .2]})
