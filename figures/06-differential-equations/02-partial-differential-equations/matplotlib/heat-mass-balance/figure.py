from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Total heat under Dirichlet/Neumann ends; boundary outflow; with a source.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, left=.1, wspace=.38, bottom=.27)
T = np.linspace(.0002, .3, 300); k = np.arange(1, 4001, 2)
MD = np.array([(np.sin(k*pi/2)*8/(k*pi)**3*np.exp(-(k*pi)**2*t)).sum() for t in T])
kk = np.arange(1, 40001, 2)
out = np.array([2*(cs(kk)*np.exp(-(kk*pi)**2*t)*np.sqrt(2)*kk*pi).sum() for t in T])
ax = axes[0]
ax.plot(T, MD, color=BLUE, lw=1.4); ax.plot(T, .25+0*T, color=YELLOW, lw=1.4)
lab(ax, .15, .258, 'Neumann', YELLOW, ha='center', va='bottom'); lab(ax, .13, .12, 'Dirichlet', BLUE, ha='left')
ax.set_xlim(0, .3); ax.set_ylim(0, .31); ax.set_xticks([0, .15, .3]); ax.set_xticklabels(['0', '0.15', '0.3']); ax.set_yticks([0, .25]); ax.set_yticklabels(['0', '1/4']); axlab(ax, '$t$', '$M(t)$')
ax = axes[1]
ax.plot(T, out, color=RED, lw=1.4); ax.plot(T[1:-1], -(MD[2:]-MD[:-2])/(T[2:]-T[:-2]), color=GREEN, lw=.9, ls=DASH)
ax.set_xlim(0, .3); ax.set_ylim(0, 2.15); ax.set_xticks([0, .15, .3]); ax.set_xticklabels(['0', '0.15', '0.3']); ax.set_yticks([0, 1, 2]); axlab(ax, '$t$', '流出率')
ax = axes[2]; T2 = np.linspace(0, .6, 200)
fk = 2*np.sqrt(2)/(k*pi); lam = (k*pi)**2
MS = np.array([(fk/lam*(1-np.exp(-lam*t))*fk).sum() for t in T2])
ax.plot(T2, MS, color=BLUE, lw=1.4); ax.plot(T2, T2, color=YELLOW, lw=1.4); ax.axhline(1/12, color=STROKE, lw=.8, ls=DOT)
lab(ax, .42, .1, '$1/12$', MUTED, ha='center', va='bottom'); lab(ax, .3, .44, 'Neumann', YELLOW, ha='right')
ax.set_xlim(0, .6); ax.set_ylim(0, .62); ax.set_xticks([0, .3, .6]); ax.set_xticklabels(['0', '0.3', '0.6']); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '0.25', '0.5']); axlab(ax, '$t$', '$M(t)$')
tags(fig, axes)
save(fig, HERE, 'figure', {'M_D .1': float(np.interp(.1, T, MD)), 'out .1': float(np.interp(.1, T, out)), 'M_S(inf)': float((fk/lam*fk).sum())})
print(np.interp(.1, T, MD), np.interp(.1, T, out), (fk/lam*fk).sum())
