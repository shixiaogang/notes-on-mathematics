from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Quartic target pi~=exp(-x^4/4); candidates N(m, e^{2w}); objective J(m,w)=-w-C+(m^4+6m^2 e^{2w}+3e^{4w})/4.
# Gradient descent, eta=0.1, start (m,w)=(1,0); optimum (0, -ln3/4)=(0,-0.2747), J*=-0.8943, D*=J*+lnZ=0.0472.
# (a) contours of J and the path (green). (b) D(Q^(t)||Pi)=J+lnZ per step (green) and the floor D* (red).
P = gd_path(1., 0., .1, 40)
m = np.linspace(-1.2, 1.2, 241); w = np.linspace(-1.2, .5, 241)
MM, WW = np.meshgrid(m, w)
JJ = quartic_J(MM, np.exp(WW))
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.98, top=.96, bottom=.25, wspace=.3)
ax = axs[0]
Js = quartic_J(0, 3**-0.25)
ax.contour(m, w, JJ, levels=Js+np.array([.02, .08, .2, .4, .7, 1.1, 1.6]), colors=[BLUE], linewidths=.7, linestyles='solid')
ax.plot([p[0] for p in P], [p[1] for p in P], color=GREEN, lw=1.0, marker='o', ms=2)
dot(ax, 0, -math.log(3)/4, RED, ms=4.5)
ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, .5); axlab(ax, '$m$', r'$\omega=\ln s$')
ax = axs[1]
D = [quartic_J(a, math.exp(b))+LNZ4 for a, b in P]
ax.plot(range(len(D)), D, color=GREEN, lw=1.2, marker='o', ms=2)
ax.axhline(Js+LNZ4, color=RED, lw=.9)
lab(ax, 22, .075, r'$D^{*}\approx0.047$', RED, fontsize=7)
ax.set_yscale('log'); ax.set_xlim(0, 40); ax.set_ylim(.03, 3)
axlab(ax, '步数', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'path_first': [[round(a, 4), round(b, 4)] for a, b in P[:4]],
                           'D_t': {t: round(D[t], 4) for t in (0, 1, 2, 5, 10, 20, 40)}, 'D_star': Js+LNZ4})
