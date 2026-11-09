from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# e_k=sqrt2 sin(k pi x)，读取 g=1_{[0,1/2]}。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, wspace=.26, bottom=.25)
ax = axes[0]
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(X, np.sqrt(2)*np.sin(3*np.pi*X), color=BLUE, lw=1.4)
ax.plot(X, np.sqrt(2)*np.sin(14*np.pi*X), color=GREEN, lw=1.0)
ax.set_xlim(0, 1); ax.set_ylim(-1.7, 1.7); ax.set_xticks([0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel('$e_k$', labelpad=0)
k = np.arange(1, 31)
read = np.sqrt(2)*(1-np.cos(k*np.pi/2))/(k*np.pi)
ax = axes[1]
ax.plot(k, np.ones_like(k), color=RED, lw=1.4)
ax.vlines(k, 0, read, color=GREEN, lw=1.0)
ax.plot(k, read, 'o', ms=2.8, color=GREEN, mew=0)
ax.text(30, 1.05, r'$\Vert e_k\Vert_2$', color=RED, ha='right', fontsize=8)
ax.text(8, .5, r'$\langle g,e_k\rangle$', color=GREEN, fontsize=8)
ax.set_xlim(0, 31); ax.set_ylim(-.04, 1.25); ax.set_xticks([1, 10, 20, 30]); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '0.5', '1']); ax.set_xlabel('$k$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'e_k': 'sqrt(2) sin(k pi x)', 'g': 'indicator of [0,1/2]', 'reading': read[:6].tolist()})
