from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Energy of the tent solution under two boundaries, and stability of the difference.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.11, wspace=.3, bottom=.27)
T = np.linspace(0, .25, 300)
k = np.arange(1, 2001, 2); j = np.arange(2, 2001, 4)
ED = np.array([.5*((cs(k)*np.exp(-(k*pi)**2*t))**2).sum() for t in T])
EN = np.array([.5*(1/16+((np.sqrt(2)*4/(j*pi)**2*np.exp(-(j*pi)**2*t))**2).sum()) for t in T])
ax = axes[0]
ax.plot(T, ED, color=BLUE, lw=1.4); ax.plot(T, EN, color=YELLOW, lw=1.4); ax.axhline(1/32, color=STROKE, lw=.8, ls=DOT)
dot(ax, 0, 1/24, RED)
lab(ax, .13, .0335, 'Neumann', YELLOW, ha='left', va='bottom'); lab(ax, .12, .008, 'Dirichlet', BLUE, ha='left', va='bottom'); lab(ax, .24, .0288, '$1/32$', MUTED, ha='right', va='top')
ax.set_xlim(0, .25); ax.set_ylim(0, .046); ax.set_xticks([0, .1, .2]); ax.set_yticks([0, 1/32, 1/24]); ax.set_yticklabels(['0', '1/32', '1/24']); axlab(ax, '$t$', '$E(t)$')
ax = axes[1]; T2 = np.linspace(0, .25, 300); d = lambda t: .1*np.sqrt(.5*np.exp(-2*pi**2*t)+.5*np.exp(-18*pi**2*t))
ax.semilogy(T2, d(T2), color=BLUE, lw=1.4); ax.semilogy(T2, d(0)*np.exp(-pi**2*T2), color=PURPLE, lw=1.1, ls=DASH)
lab(ax, .09, .062, r'上界', PURPLE, ha='left', va='bottom'); lab(ax, .02, .012, r'$\| u_1-u_2\|_2$', BLUE, ha='left', va='top')
ax.set_xlim(0, .25); ax.set_ylim(3e-3, .2); ax.minorticks_off(); ax.set_xticks([0, .1, .2]); ax.set_yticks([.1, .01]); ax.set_yticklabels(['$10^{-1}$', '$10^{-2}$']); axlab(ax, '$t$')
tags(fig, axes)
save(fig, HERE, 'figure', {'E0': float(ED[0])})
