from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# 单位球面上的集中：u_k=sqrt(k) 1_[0,1/k]，J=int x u^2=1/(2k)。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.075, wspace=.26, bottom=.25)
ax = axes[0]
for k, c in ((2, YELLOW), (8, BLUE), (32, GREEN)):
    h = np.sqrt(k)
    ax.plot([0, 0, 1/k, 1/k, 1], [0, h, h, 0, 0], color=c, lw=1.4)
    ax.text(1/k+.02, h-.1, f'$k={k}$', color=c, fontsize=7.5, va='top' if k==2 else 'center')
ax.set_xlim(-.02, 1); ax.set_ylim(-.15, 6.4); ax.set_xticks([0, 1]); ax.set_yticks([0, 2, 4, 6]); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('$u^{(k)}$', labelpad=0)
k = np.arange(1, 41)
ax = axes[1]
ax.plot(k, np.ones_like(k), color=RED, lw=1.4)
ax.plot(k, 1/np.sqrt(k), color=GREEN, lw=1.4)
ax.plot(k, 1/(2*k), color=BLUE, lw=1.4)
ax.text(40, 1.05, r'$\Vert u^{(k)}\Vert_2$', color=RED, ha='right', fontsize=8)
ax.text(13, .4, r'$\langle 1,u^{(k)}\rangle$', color=GREEN, fontsize=8)
ax.text(17, .06, '$J(u^{(k)})$', color=BLUE, fontsize=8, va='bottom')
ax.set_xlim(0, 41); ax.set_ylim(0, 1.25); ax.set_xticks([1, 20, 40]); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '0.5', '1']); ax.set_xlabel('$k$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'u_k': 'sqrt(k) on [0,1/k]', 'J': '1/(2k)', 'reading': 'k^{-1/2}'})
