from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
fig, axs = figure(width_mm=108, height_mm=46, ncols=2)
S = np.linspace(0, 3, 300)
for ax, x2, ym, ytk in zip(axs, (.5, .05), (.62, .062), ([0, .25, .5], [0, .025, .05])):
    ax.plot(S, np.maximum(x2-S/2, 0)*(x2-S/2 < 1)+0, color=YELLOW, lw=1.4)
    e = x2*np.exp(-S); ax.plot(S, e/((1-x2)+e), color=GREEN, lw=1.4)
    setup(ax, (0, 3), (0, ym), [0, 1, 2, 3], ytk, xl='$\\alpha(g_2-g_1)$', yl='$x_2^{+}$')
axs[0].text(1.45, .19, '镜像', color=GREEN, fontsize=7.5); axs[0].text(.55, .08, '投影', color=YELLOW, fontsize=7.5)
axs[1].text(.9, .03, '镜像', color=GREEN, fontsize=7.5); axs[1].text(.14, .004, '投影', color=YELLOW, fontsize=7.5)
panels(fig, .1, .985, .98, .25, .34); tags(fig, axs)
save(fig, HERE, 'figure', {'x2': [.5, .05]})
