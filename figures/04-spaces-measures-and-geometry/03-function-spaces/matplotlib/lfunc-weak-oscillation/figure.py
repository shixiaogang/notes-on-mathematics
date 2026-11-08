from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# sin(nx) 在 g=1_{[0,1]} 下的读取：(1-cos n)/n；L2 范数恒为 sqrt(pi)。
fig, axes = figure(width_mm=112, height_mm=46, ncols=2, width_ratios=[1.1, 1])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.975, top=.97, bottom=.235, wspace=.18)
a = axes[0]
x = np.linspace(0, 2*np.pi, 3000); n = 12
y = np.sin(n*x)
a.axvline(1, color=GREEN, lw=1.0)
mask = x <= 1
a.fill_between(x[mask], 0, y[mask], color=YELLOW_FILL, lw=0)
a.plot(x, y, color=BLUE, lw=1.1)
a.plot(x[mask], y[mask], color=BLUE, lw=1.1)
a.axhline(0, color=MUTED, lw=.85)
a.set_xlim(0, 2*np.pi); a.set_ylim(-1.15, 1.3); a.set_xticks([0, 1, 2*np.pi]); a.set_xticklabels(['0', '1', r'$2\pi$']); a.set_yticks([-1, 0, 1])
a.text(.5, 1.14, '$g=1$', ha='center', va='center')
b = axes[1]
ns = np.arange(1, 41)
b.plot(ns, np.abs(1-np.cos(ns))/ns, 'o', color=BLUE, ms=3, mew=0)
nn = np.linspace(1, 40, 300)
b.plot(nn, 2/nn, color=MUTED, lw=.85, ls=(0, (3, 2)))
b.plot(nn, np.full_like(nn, np.sqrt(np.pi)), color=GREEN, lw=1.4)
b.set_xlim(0, 41); b.set_ylim(0, 2.25); b.set_xticks([1, 12, 40]); b.set_yticks([0, 1, np.sqrt(np.pi)]); b.set_yticklabels(['0', '1', r'$\sqrt{\pi}$'])
b.text(21, 1.84, r'$\Vert \sin(n\,\cdot)\Vert_2$', ha='center', va='bottom')
b.text(11, .53, '$2/n$', ha='left', va='bottom')
b.text(35, .24, '读数绝对值', ha='right', va='bottom')
b.text(1.0, .13, '$n$', transform=b.transAxes, ha='right', va='bottom')
for ax, s in zip(axes, '(a) (b)'.split()):
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'sin(12x) on [0,2pi]; reading (1-cos n)/n; envelope 2/n; norm sqrt(pi)'})
