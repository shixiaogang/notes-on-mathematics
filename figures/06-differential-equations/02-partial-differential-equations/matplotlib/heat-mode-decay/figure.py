from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Two-mode solution and exponential decay of mode amplitudes.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, wspace=.3, bottom=.27)
ax = axes[0]; ts = [.002, .008, .03]; cc = shades(3)
u = lambda t: np.exp(-pi**2*t)*np.sin(pi*X)+.5*np.exp(-16*pi**2*t)*np.sin(4*pi*X)
ax.plot(X, u(0), color=RED, lw=1.5)
for t, c in zip(ts, cc): ax.plot(X, u(t), color=c, lw=1.4)
ax.set_xlim(0, 1); ax.set_ylim(-.15, 1.5); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1]); axlab(ax, yl='$u$')
ax = axes[1]; T = np.linspace(0, .2, 200)
for k, c in zip((1, 2, 3), (BLUE, YELLOW, PURPLE)):
    ax.semilogy(T, np.exp(-(k*pi)**2*T), color=c, lw=1.4)
    th = np.log(2)/(k*pi)**2; dot(ax, th, .5, RED, ms=3.8)
lab(ax, .155, np.exp(-pi**2*.155)*1.35, '$k=1$', BLUE, ha='center'); lab(ax, .085, np.exp(-4*pi**2*.085)*.25, '$k=2$', YELLOW, ha='right', va='top'); lab(ax, .076, 2.2e-3, '$k=3$', PURPLE, ha='left')
ax.axhline(.5, color=STROKE, lw=.7, ls=DOT)
ax.set_xlim(0, .2); ax.set_ylim(1e-3, 1.2); ax.set_xticks([0, .1, .2]); ax.minorticks_off(); ax.set_yticks([1, 1e-1, 1e-2, 1e-3]); ax.set_yticklabels(['1', '$10^{-1}$', '$10^{-2}$', '$10^{-3}$']); axlab(ax, '$t$', r'$\mathrm{e}^{-\lambda_k t}$')
tags(fig, axes)
save(fig, HERE, 'figure', {'half-lives': [float(np.log(2)/(k*pi)**2) for k in (1, 2, 3)]})
