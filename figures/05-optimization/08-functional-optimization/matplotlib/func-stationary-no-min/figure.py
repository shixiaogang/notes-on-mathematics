from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# J_rho 沿 t sin(pi x)：phi(t)=t^2 (pi^2-rho)/4。
fig, ax = figure(width_mm=78, height_mm=48)
panel(fig, left=.12, right=.97, bottom=.2, top=.96)
t = np.linspace(-1.5, 1.5, 300)
for rho, c, s, xy in ((5, BLUE, r'$\rho=5$', (1.0, 2.2)), (np.pi**2, YELLOW, r'$\rho=\pi^2$', (-1.48, .35)), (15, RED, r'$\rho=15$', (1.0, -2.6))):
    ax.plot(t, t**2*(np.pi**2-rho)/4, color=c, lw=1.4)
    ax.text(*xy, s, color=c, fontsize=7.5)
ax.plot([0], [0], 'o', ms=4.6, color=GREEN, mew=0, zorder=6)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-3.2, 3.2); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-2, 0, 2]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel(r'$J_\rho(t\sin\pi x)$', labelpad=0)
save(fig, HERE, 'figure', {'phi': 't^2 (pi^2-rho)/4', 'rho': [5, float(np.pi**2), 15]})
