from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# (a) Re phi of Bin(n,2/n), n=4,10, vs Poisson(2) Re exp(2(e^{it}-1)); (b) N(0,n) cf exp(-n t^2/2), n=1,10,100.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.27)
ax = axes[0]; t = np.linspace(0, 2*np.pi, 800)
ax.axhline(0, color=GRID, lw=.6, zorder=0)
for n, c, lw in ((4, YELLOW, 1.6), (10, GREEN, 1.3)): ax.plot(t, ((1+2*(np.exp(1j*t)-1)/n)**n).real, color=c, lw=lw)
ax.plot(t, np.exp(2*(np.exp(1j*t)-1)).real, color=BLUE, lw=1.4)
dot(ax, np.pi, np.exp(-4), RED, ms=3.8)
lab(ax, 1.3, .62, r'$n=4$', YELLOW)
ax.set_xlim(0, 2*np.pi); ax.set_ylim(-.45, 1.05)
ax.set_xticks([0, np.pi, 2*np.pi]); ax.set_xticklabels(['$0$', r'$\pi$', r'$2\pi$']); ax.set_yticks([0, .5, 1])
axlab(ax, r'$t$')
ax = axes[1]; t = np.linspace(-2, 2, 1601)
for n, c in ((1, BLUE), (10, GREEN), (100, YELLOW)): ax.plot(t, np.exp(-n*t**2/2), color=c, lw=1.4)
dot(ax, 0, 1, RED, ms=4)
lab(ax, 1.05, .62, r'$n=1$', BLUE)
ax.set_xlim(-2, 2); ax.set_ylim(0, 1.08); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$t$')
tags(fig, axes)
save(fig, HERE, 'figure', {'phi_n(pi)': {n: (1-4/n)**n for n in (4, 10, 40)}, 'limit': float(np.exp(-4))})
