from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# One-step factors on the negative axis; dots are z=-tau*lambda for h=1/4, tau=0.05.
z = np.linspace(-8, 0, 800); lams = [4*16*np.sin(m*PI/8)**2 for m in (1, 2, 3)]; tau = .05
fig, ax = figure(width_mm=100, height_mm=56)
ax.axhspan(-1, 1, color=BLUE_FILL, lw=0, zorder=0); ax.axhline(0, color=STROKE, lw=.6)
ax.plot(z, np.exp(z), color=BLUE, lw=1.4)
ax.plot(z[z >= -3.1], 1+z[z >= -3.1], color=RED, lw=1.3)
ax.plot(z, 1/(1-z), color=GREEN, lw=1.4); ax.plot(z, (1+z/2)/(1-z/2), color=YELLOW, lw=1.6)
zs = [-tau*l for l in lams]
ax.plot(zs, [1+s for s in zs], 'o', ms=4, color=RED, mew=0, zorder=6)
ax.plot(zs, [1/(1-s) for s in zs], 'o', ms=4, color=GREEN, mew=0, zorder=6)
ax.plot(zs, [(1+s/2)/(1-s/2) for s in zs], 'o', ms=4, color=YELLOW, mew=0, zorder=6)
lab(ax, -2.72, -1.62, '显式', RED, ha='right', va='center'); lab(ax, -6.4, .29, '后向', GREEN, ha='center'); lab(ax, -6.4, -.73, 'Crank–Nicolson', YELLOW, ha='center'); lab(ax, -1.25, .17, r'$\mathrm{e}^{z}$', BLUE, ha='right')
ax.set_xlim(-8, 0); ax.set_ylim(-2.2, 1.2); ax.set_xticks([-8, -4, -2, 0]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel(r'$z=-\tau\lambda$', labelpad=1); ax.set_ylabel(r'$R(z)$', labelpad=1)
save(fig, HERE, 'figure', {'tau': tau, 'lams': lams, 'z': zs}); print(zs)
