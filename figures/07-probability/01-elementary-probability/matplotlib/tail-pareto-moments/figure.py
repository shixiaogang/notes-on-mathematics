from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# Pareto alpha=3, x_m=1: P(X>t)=t^{-3} (t>=1); E[X^p]=3/(3-p) for 0<p<3.
# Moment bounds 3/((3-p) t^p) for p=1,2,2.5 and their envelope 3 e ln t / t^3 (optimal p = 3-1/ln t).
t = np.logspace(0, 2, 600)
fig, ax = figure(width_mm=96, height_mm=56)
for p, c in ((1, YELLOW), (2, GREEN), (2.5, PURPLE)):
    ax.loglog(t, np.minimum(1, 3/((3-p)*t**p)), color=c, lw=1.4)
te = t[t > np.exp(1/3)]
ax.loglog(te, np.minimum(1, 3*np.e*np.log(te)/te**3), color=RED, lw=1.1, ls=DASH)
ax.loglog(t, t**-3.0, color=BLUE, lw=1.4)
lab(ax, 60, 1.5/60*1.35, '$p=1$', YELLOW, ha='center', va='bottom')
lab(ax, 60, 3/60**2*1.35, '$p=2$', GREEN, ha='center', va='bottom')
lab(ax, 60, 6/60**2.5*1.35, '$p=2.5$', PURPLE, ha='center', va='bottom')
lab(ax, 25, 25**-3*.55, '$t^{-3}$', BLUE, ha='center', va='top')
lab(ax, 20, 3*np.e*np.log(20)/20**3*.45, r'$3\mathrm{e}\ln t/t^{3}$', RED, ha='center', va='top')
ax.set_xlim(1, 100); ax.set_ylim(1e-6, 1.5); ax.minorticks_off()
ax.set_xticks([1, 10, 100]); ax.set_xticklabels(['$1$', '$10$', '$100$'])
logticks(ax, [0, -2, -4, -6])
axlab(ax, '$t$', 'ℙ$(X\\geq t)$')
save(fig, HERE, 'figure', {'E[X^p]': '3/(3-p)', 'envelope_t10': float(3*np.e*np.log(10)/1000), 'exact_t10': 1e-3})
