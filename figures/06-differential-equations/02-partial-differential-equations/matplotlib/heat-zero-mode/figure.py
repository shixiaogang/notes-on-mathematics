from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Zero Neumann mode remains; Dirichlet lowest mode decays. Point temperatures of the tent solution.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, wspace=.36, bottom=.27)
T = np.linspace(1e-6, .25, 300)
ax = axes[0]
ax.plot(T, np.array([uN(.5, t)[0] for t in T]), color=YELLOW, lw=1.5); ax.plot(T, np.array([uN(0., t)[0] for t in T]), color=YELLOW, lw=1.5, ls=DASH)
ax.plot(T, np.array([uD(.5, t)[0] for t in T]), color=BLUE, lw=1.5); ax.plot(T, 0*T, color=BLUE, lw=1.5, ls=DASH, clip_on=False)
ax.axhline(.25, color=STROKE, lw=.7, ls=DOT)
lab(ax, .25, .275, 'Neumann，x=1/2', YELLOW, ha='right', va='bottom', fontsize=7.5); lab(ax, .25, .22, 'Neumann，x=0', YELLOW, ha='right', va='top'); lab(ax, .025, .05, 'Dirichlet，x=1/2', BLUE, ha='left')
ax.set_xlim(0, .25); ax.set_ylim(-.01, .52); ax.set_xticks([0, .1, .2]); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '1/4', '1/2']); axlab(ax, '$t$', '$u$')
ax = axes[1]
ax.semilogy(T, 0*T+.25, color=YELLOW, lw=1.5); ax.semilogy(T, 2/pi**2*np.exp(-4*pi**2*T), color=YELLOW, lw=1.5, ls=DASH)
ax.semilogy(T, 4/pi**2*np.exp(-pi**2*T), color=BLUE, lw=1.5)
lab(ax, .15, .31, '零模式 1/4', YELLOW, ha='center', va='bottom'); lab(ax, .1, 3e-4, r'$k=2$', YELLOW, ha='right'); lab(ax, .25, .03, r'Dirichlet $k=1$', BLUE, ha='right', va='top')
ax.set_xlim(0, .25); ax.set_ylim(1e-4, 1); ax.minorticks_off(); ax.set_xticks([0, .1, .2]); ax.set_yticks([1, 1e-2, 1e-4]); ax.set_yticklabels(['1', '$10^{-2}$', '$10^{-4}$']); axlab(ax, '$t$', '幅度')
tags(fig, axes)
save(fig, HERE, 'figure', {'rates': 'pi^2 vs 4 pi^2'})
