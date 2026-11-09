from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# 尖峰 tau_n(t)=max(1-nt,0)：tau_n(0)=1，||tau_n||_1=1/(2n)，||tau_n||_2=1/sqrt(3n)。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2, width_ratios=[1, 1.15])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.97, top=.97, bottom=.225, wspace=.2)
a = axes[0]
t = np.linspace(0, 1, 2000)
for n in (2, 4, 8, 16):
    a.plot(t, np.maximum(1-n*t, 0), color=BLUE, lw=1.4)
    a.text(1/n-.005, .055, f'$\\tau_{{{n}}}$', ha='left', va='bottom') if n <= 4 else None
a.plot([0], [1], 'o', color=BLUE, ms=4.2, mew=0, clip_on=False, zorder=4)
a.set_xlim(0, 1.03); a.set_ylim(0, 1.15); a.set_xticks([0, .25, .5, 1]); a.set_xticklabels(['0', '1/4', '1/2', '1']); a.set_yticks([0, 1])
b = axes[1]
ns = 2.0**np.arange(0, 8)
b.plot(ns, np.ones_like(ns), '-o', color=BLUE, lw=1.4, ms=3.4, mew=0)
b.plot(ns, 1/np.sqrt(3*ns), '-o', color=GREEN, lw=1.4, ms=3.4, mew=0)
b.plot(ns, 1/(2*ns), '-o', color=YELLOW, lw=1.4, ms=3.4, mew=0)
b.set_xscale('log', base=2); b.set_yscale('log', base=2)
b.set_xticks([1, 4, 16, 64, 256]); b.set_xticklabels(['1', '4', '16', '64', '256']); b.minorticks_off()
b.set_yticks([1, 1/8, 1/64, 1/512]); b.set_yticklabels(['1', '1/8', '1/64', '1/512'])
b.set_xlim(.85, 330); b.set_ylim(1/900, 2.2)
b.text(19, 1.18, r'$\tau_n(0)$', ha='center', va='bottom')
b.text(20, 1/np.sqrt(3*20)*1.45, r'$\Vert\tau_n\Vert_2$', ha='left', va='bottom')
b.text(9.5, 1/(2*9.5)*.5, r'$\Vert\tau_n\Vert_1$', ha='right', va='top')
b.text(1.0, .035, '$n$', transform=b.transAxes, ha='right', va='bottom')
for ax, s in zip(axes, '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'tau_n(t)=max(1-nt,0); tau_n(0)=1; L1 norm 1/(2n); L2 norm (3n)^(-1/2); n=2^k'})
