from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Error versus truncation level at several noise sizes; truncation and Tikhonov filters.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.09, wspace=.3, bottom=.26)
T = .05; odd = np.arange(1, 200001, 2); b2 = (cs(odd)**2)[::-1].cumsum()[::-1]
Ns = np.arange(1, 13, 2)
ax = axes[0]
for d, c in zip((1e-3, 1e-6, 1e-12), (BLUE, YELLOW, PURPLE)):
    e = []
    for N in Ns:
        k = np.arange(1, N+1, 2); n = (d**2*np.exp(2*(k*pi)**2*T)).sum(); idx = len(k); e.append(np.sqrt(n+b2[idx]))
    e = np.array(e); ax.semilogy(Ns, e, 'o-', ms=3.2, color=c, mew=0, lw=1.2)
    i = e.argmin(); dot(ax, Ns[i], e[i], RED, ms=5)
lab(ax, .8, 30, r'$\delta=10^{-3}$', BLUE, ha='left'); lab(ax, 6.3, 1e-1 , r'$10^{-6}$', YELLOW, ha='center', va='bottom'); lab(ax, 9.6, 8e-3, r'$10^{-12}$', PURPLE, ha='center', va='top')
ax.set_xlim(.5, 11.5); ax.set_ylim(3e-3, 1e3); ax.minorticks_off(); ax.set_xticks([1, 3, 5, 7, 9, 11]); ax.set_yticks([1e2, 1, 1e-2]); ax.set_yticklabels(['$10^2$', '1', '$10^{-2}$']); axlab(ax, '$N$', '误差')
ax = axes[1]; k = np.linspace(.8, 7, 400); s = np.exp(-(k*pi)**2*T); a = 1e-4
ax.semilogy(k, 1/s, color=RED, lw=1.3); ax.semilogy(k, s/(s**2+a), color=GREEN, lw=1.4)
ax.plot([.8, 3.5], [np.exp((.8*pi)**2*T), np.exp((3.5*pi)**2*T)], lw=0)
t = k[k <= 3.5]; ax.semilogy(t, np.exp((t*pi)**2*T), color=PURPLE, lw=1.4, ls=DASH); ax.plot([3.5, 3.5], [np.exp((3.5*pi)**2*T), 1e-3], color=PURPLE, lw=1.1, ls=DASH)
ax.axhline(50, color=STROKE, lw=.7, ls=DOT)
lab(ax, 5.2, 3e6, r'$\mathrm{e}^{\lambda T}$', RED, ha='right'); lab(ax, 4.7, 2, 'Tikhonov', GREEN, ha='left'); lab(ax, 6.85, 80, '50', MUTED, ha='right', va='bottom'); lab(ax, 3.45, 3, '截断', PURPLE, ha='right')
ax.set_xlim(.8, 7); ax.set_ylim(1e-3, 1e9); ax.minorticks_off(); ax.set_xticks([1, 3, 5, 7]); ax.set_yticks([1e8, 1e4, 1, 1e-3]); ax.set_yticklabels(['$10^8$', '$10^4$', '1', '$10^{-3}$']); axlab(ax, '$k$', '增益')
tags(fig, axes)
save(fig, HERE, 'figure', {'alpha': a})
