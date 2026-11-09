from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 沿 -g 的模型值 psi(a)=-a||g||+kappa a^2/2 的三种情形（||g||=2，Delta=2）。
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
n = 2.; D = 2.; data = [(-.5, D), (2., 1.), (.6, D)]
for ax, (k, a0) in zip(axs, data):
    a = np.linspace(0, 3.2, 300); psi = -a*n + .5*k*a*a
    ax.axvspan(0, D, facecolor=BLUE_FILL, edgecolor='none', zorder=0)
    ax.plot(a, psi, color=BLUE, lw=1.4); ax.axvline(D, color=EDGE, lw=1.1)
    ax.plot([a0], [-a0*n + .5*k*a0*a0], 'o', color=GREEN, ms=5, mew=0, zorder=6)
    ax.set_xlim(0, 3.2); ax.set_ylim(-7, 1); ax.set_xticks([0, 2]); ax.set_xticklabels(['$0$', '$\\Delta$']); ax.set_yticks([]); ax.set_xlabel('$a$', labelpad=1)
axs[0].set_ylabel(r'$\psi(a)$', labelpad=1)
panels(fig, .045, .985, .98, .27, .12); tags(fig, axs)
save(fig, HERE, 'figure', {'psi': '-a||g||+kappa a^2/2', 'kappa': [-.5, 2., .6], 'gnorm': 2, 'radius': 2})
