from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Independent events A_n = {U_n < p_n}; count C_n = sum_{k<=n} 1{A_k} along 6 simulated paths (seed 2026), n <= 10^5.
# (a) p_n = 1/n: E C_n = H_n (harmonic number, blue) -> infinity; second Borel-Cantelli: A_n occurs i.o. a.s.
# (b) p_n = 1/n^2: E C_n -> pi^2/6 = 1.645 (blue); first Borel-Cantelli: only finitely many A_n occur a.s.
NMAX = 10**5; R = 6
rng = np.random.default_rng(2026)
n = np.arange(1, NMAX + 1)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.28, bottom=.3)
finals = {}
for ax, p, name, ymax in ((axes[0], 1/n, '1/n', 21), (axes[1], 1/n**2, '1/n^2', 5.5)):
    style(ax)
    fin = []
    for r in range(R):
        c = np.cumsum(rng.random(NMAX) < p)
        ax.step(n, c, where='post', color=GREEN, lw=.9)
        fin.append(int(c[-1]))
    ax.plot(n, np.cumsum(p), color=BLUE, lw=1.4)
    finals[name] = fin
    ax.set_xscale('log'); ax.set_xlim(1, NMAX); ax.set_ylim(0, ymax)
    logticks(ax, [0, 1, 2, 3, 4, 5], axis='x')
    axlab(ax, '$n$', '$C_n$')
lab(axes[0], 4e4, 12.4, r'$H_n$', BLUE, ha='center', va='bottom')
lab(axes[1], 3e4, 1.35, r'$\pi^2/6$', BLUE, ha='center', va='top')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 2026, 'paths': R, 'final_counts': finals, 'H_1e5': float(np.sum(1/n)), 'pi2_6': float(np.pi**2/6)})
