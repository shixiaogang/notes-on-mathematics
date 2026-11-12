from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# Y=|Z|, Z ~ N(0,1): exact P(Y>=t)=2Q(t); best moment bound inf_p E[Y^p]/t^p (p>0 real);
# exponential bound inf_lam e^{-lam t} E[e^{lam Y}], E[e^{lam Y}] = 2 e^{lam^2/2} Phi(lam).
import math
from math import lgamma
ts = np.linspace(.6, 5, 120)
ps = np.linspace(.05, 40, 4000)
lam = np.linspace(0, 8, 4001)
Phi = 1-Q(lam)
logabs = lambda p: (p/2)*np.log(2)+np.vectorize(lgamma)((p+1)/2)-0.5*np.log(np.pi)
LA = logabs(ps)
mom = np.array([np.exp(np.min(LA-ps*np.log(t))) for t in ts])
che = np.array([np.min(2*np.exp(lam**2/2-lam*t)*Phi) for t in ts])
fig, ax = figure(width_mm=96, height_mm=54)
ax.semilogy(ts, 2*Q(ts), color=BLUE, lw=1.4)
ax.semilogy(ts, np.minimum(1, mom), color=YELLOW, lw=1.6)
ax.semilogy(ts, np.minimum(1, che), color=PURPLE, lw=1.4)
lab(ax, 3.6, .01, '指数矩', PURPLE, ha='left', va='bottom')
j = np.searchsorted(ts, 3.2); ax.annotate('最优矩', xy=(ts[j], mom[j]), xytext=(1.6, 1e-4), color=YELLOW, fontsize=7.5, arrowprops=dict(arrowstyle='->', color=STROKE, lw=.8))
lab(ax, 2.6, 2*Q(2.6)*.4, '精确值', BLUE, ha='right', va='top')
ax.set_xlim(.6, 5); ax.set_ylim(1e-6, 1.5); logticks(ax, [0, -2, -4, -6])
axlab(ax, '$t$', 'ℙ$(|Z|\\geq t)$')
i3 = int(np.argmin(np.abs(ts-3)))
save(fig, HERE, 'figure', {'t~3': float(ts[i3]), 'exact': float(2*Q(ts[i3])), 'best_moment': float(mom[i3]), 'exp_moment': float(che[i3])})
