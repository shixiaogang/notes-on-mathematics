from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Reference Q=N(0,1), g(x)=x.
# (a) Q (yellow), exponential tilt Q_g with dQ_g/dQ = e^{lam x}/E_Q e^{lam X} = N(lam,1) for lam=1 (purple dashed),
#     and P=N(1,0.7^2) (blue).
# (b) P=N(m,s^2): true E_P g - E_Q g = m (blue) and the KL bound sqrt(2 D(P||Q)),
#     D = -ln s + (s^2+m^2)/2 - 1/2, for s=1 (equal to m, yellow), s=0.5 (purple), s=2 (red dashed).
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.98, top=.95, bottom=.26, wspace=.28)
ax = axs[0]
x = np.linspace(-3.5, 4, 900)
ax.plot(x, npdf(x), color=YELLOW, lw=1.6)
ax.plot(x, npdf(x, 1.), color=PURPLE, lw=1.3, ls=DASH)
ax.plot(x, npdf(x, 1., .7), color=BLUE, lw=1.4)
lab(ax, -1.75, .33, '$Q$', YELLOW, ha='center', fontsize=8)
lab(ax, 2.55, .3, '$Q_g$', PURPLE, ha='left', fontsize=8)
lab(ax, 1.6, .54, '$P$', BLUE, ha='left', fontsize=8)
ax.set_xlim(-3.5, 4); ax.set_ylim(0, .64); ax.set_yticks([0, .2, .4, .6])
axlab(ax, '$x$', '密度')
ax = axs[1]
m = np.linspace(0, 2, 300)
facts = {}
for s, c, ls in ((1., YELLOW, '-'), (.5, PURPLE, '-'), (2., RED, DASH)):
    D = -math.log(s)+(s*s+m*m)/2-.5
    b = np.sqrt(2*D)
    ax.plot(m, b, color=c, lw=1.5 if c == YELLOW else 1.3, ls=ls, zorder=2 if c == YELLOW else 3)
    facts[str(s)] = float(np.sqrt(2*(-math.log(s)+(s*s+1)/2-.5)))
ax.plot(m, m, color=BLUE, lw=1.2, ls=DOT, zorder=4)
lab(ax, 1.95, 1.62, '$m$', BLUE, ha='right', va='top')
lab(ax, .08, .58, '$s=1/2$', PURPLE, ha='left')
lab(ax, .08, 1.37, '$s=2$', RED, ha='left')
ax.set_xlim(0, 2); ax.set_ylim(0, 2.6); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
axlab(ax, '$m$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'bound_at_m=1': facts})
