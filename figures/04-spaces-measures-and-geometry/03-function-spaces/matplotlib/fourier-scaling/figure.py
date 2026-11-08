from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# B(x) 与 B(x/2)，变换 sinc(xi) 与 2 sinc(2 xi)。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.96, bottom=.32, wspace=.19)
ax = axes[0]
ax.plot([-1.6, -1, -1, 1, 1, 1.6], [0, 0, 1, 1, 0, 0], color=PURPLE, lw=1.4)

ax.plot([-1.6, -.5, -.5, .5, .5, 1.6], [0, 0, 1, 1, 0, 0], color=BLUE, lw=1.4, ls=(0, (4, 1.5)))
ax.set_xlim(-1.6, 1.6); ax.set_ylim(-.05, 1.25); ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax.text(.0, 1.08, r'$B(x)$', color=BLUE, ha='center'); ax.text(1.05, .62, r'$B(x/2)$', color=PURPLE, ha='left')
ax = axes[1]
xi = np.linspace(-3, 3, 1500)
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(xi, np.sinc(xi), color=GREEN, lw=1.4)
ax.plot(xi, 2*np.sinc(2*xi), color=PURPLE, lw=1.4)
ax.set_xlim(-3, 3); ax.set_ylim(-.55, 2.25); ax.set_xticks([-2, -1, -.5, .5, 1, 2]); ax.set_xticklabels(['$-2$', '$-1$', r'$-\frac{1}{2}$', r'$\frac{1}{2}$', '$1$', '$2$']); ax.set_yticks([0, 1, 2]); ax.set_xlabel(r'$\xi$', labelpad=0)
tag(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'B(x/2) has transform 2 sinc(2 xi) = sin(2 pi xi)/(pi xi)'})
