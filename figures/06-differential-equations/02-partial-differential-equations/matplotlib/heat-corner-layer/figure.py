from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# u0=1 with zero Dirichlet ends: Gibbs at t=0, smooth at t>0, boundary layer in x/(2 sqrt t).
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, left=.07, wspace=.32, bottom=.27)
xx = np.linspace(0, 1, 3001)
def S(t, N): 
    k = np.arange(1, N+1, 2)
    return (4/(k*pi)[:, None]*np.exp(-(k*pi)**2*t)[:, None]*np.sin(np.outer(k, pi*xx))).sum(0)
ax = axes[0]
ax.plot(xx, 1+0*xx, color=RED, lw=1.5); ax.plot(xx, S(0, 15), color=GREEN, lw=.95); ax.plot(xx, S(0, 61), color=GREEN, lw=.95, ls=DASH)
m61 = float(S(0, 61).max())
ax.set_xlim(0, 1); ax.set_ylim(0, 1.35); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1]); axlab(ax, yl='$u$')
ax = axes[1]; cc = shades(3)
ax.plot(xx, 1+0*xx, color=RED, lw=1.5)
for t, c in zip((.001, .01, .05), cc): ax.plot(xx, S(t, 801), color=c, lw=1.4)
ax.set_xlim(0, 1); ax.set_ylim(0, 1.35); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1]); axlab(ax)
ax = axes[2]
for t, c in zip((.001, .01), cc):
    s = xx/(2*np.sqrt(t)); ax.plot(s, S(t, 1601), color=c, lw=1.5)
z = np.linspace(0, 3, 200); ax.plot(z, erf(z), color=YELLOW, lw=1.1, ls=DASH)
lab(ax, 1.3, .55, r'$\operatorname{erf}$', YELLOW, ha='left')
ax.set_xlim(0, 3); ax.set_ylim(0, 1.35); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1]); axlab(ax, r'$x/(2\sqrt{t})$')
tags(fig, axes)
save(fig, HERE, 'figure', {'partial sum max N=61': m61})
print(m61)
