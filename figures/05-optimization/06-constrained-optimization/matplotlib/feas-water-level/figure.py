from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
z = np.array([.521875, .625, .034375]); p, nu, k = proj(z)
fig, axs = figure(width_mm=104, height_mm=48, ncols=2, gridspec_kw={'width_ratios': [1, 1.25]})
ax = axs[0]
for i, v in enumerate(z):
    low = min(v, nu); ax.bar(i, low, width=.56, color=BLUE_FILL, edgecolor=BLUE, lw=.8)
    if v > nu: ax.bar(i, v-nu, bottom=nu, width=.56, color=GREEN_FILL, edgecolor=GREEN, lw=.8); ax.text(i, v+.02, f'{v-nu:.3f}', ha='center', fontsize=7.5)
    else: ax.text(i, v+.06, '0', ha='center', fontsize=7.5)
ax.axhline(nu, color=EDGE, lw=1.1, ls=(0, (3, 2))); ax.text(2.55, nu+.012, '$\\nu$', fontsize=8, ha='right')
setup(ax, (-.55, 2.6), (0, .78), [0, 1, 2], [0, .25, .5, .75], yl='$z_i$'); ax.set_xticklabels(['$z_1$', '$z_2$', '$z_3$'])
ax = axs[1]; N = np.linspace(-.25, .72, 500); ax.plot(N, np.maximum(z[None, :]-N[:, None], 0).sum(axis=1), color=BLUE, lw=1.4)
ax.axhline(1, color=MUTED, lw=.85, ls=(0, (3, 2))); ax.plot([nu], [1], 'o', color=GREEN, ms=4.6, mew=0, zorder=6); ax.plot([nu, nu], [0, 1], color=MUTED, lw=.85, ls=(0, (1, 1.5)))
ax.text(nu+.03, 1.08, '$\\varphi(\\nu)=1$', fontsize=8); 
setup(ax, (-.25, .72), (0, 2), [0, .25, .5], [0, 1, 2], xl='$\\nu$', yl='$\\varphi(\\nu)$')
panels(fig, .11, .985, .98, .2, .42); tags(fig, axs)
save(fig, HERE, 'figure', {'z': z.tolist(), 'nu': float(nu), 'p': p.tolist()})
