from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c) (d)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f=|x-1/2|, weak derivative sgn(x-1/2); H=1_[1/2,1); bump phi(x)=exp(1-1/(1-((x-.5)/.4)^2)), phi(1/2)=1.
fig, axes = figure(width_mm=112, height_mm=46, ncols=4)
fig.set_layout_engine(None); fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.27, wspace=.42)
xl = np.linspace(0, .5, 200); xr = np.linspace(.5, 1, 200)
ax = axes[0]; ax.plot(np.r_[xl, xr], np.abs(np.r_[xl, xr]-.5), color=BLUE, lw=1.4)
ax.text(.5, .22, '$f$', ha='center')
ax.set_ylim(-.05, .75); ax.set_yticks([0, .5])
ax = axes[1]; ax.plot(xl, -1+0*xl, color=GREEN, lw=1.4); ax.plot(xr, 1+0*xr, color=GREEN, lw=1.4)
ax.plot([.5, .5], [-1, 1], color=MUTED, lw=.85, ls=(0, (2, 2)))
ax.text(.25, -.72, "$f'$", ha='center'); ax.axhline(0, color=MUTED, lw=.85)
ax.set_ylim(-1.35, 1.35); ax.set_yticks([-1, 0, 1])
ax = axes[2]; ax.plot(xl, 0*xl, color=BLUE, lw=1.4); ax.plot(xr, 1+0*xr, color=BLUE, lw=1.4)
ax.plot([.5], [0], 'o', mfc='white', mec=BLUE, ms=3.2, mew=.9); ax.plot([.5], [1], 'o', color=BLUE, ms=3.2)
ax.text(.75, .82, '$H$', ha='center'); ax.set_ylim(-.12, 1.2); ax.set_yticks([0, 1])
ax = axes[3]; x = np.linspace(.1001, .8999, 500); u = (x-.5)/.4; phi = np.exp(1-1/(1-u**2))
ax.plot(x, phi, color=MUTED, lw=1.1); ax.plot([.5, .5], [0, 1], color=YELLOW, lw=.95); ax.plot([.5], [1], 'o', color=YELLOW, ms=3.6)
ax.text(.82, .72, r'$\varphi$', ha='center'); ax.text(.5, 1.07, r'$\varphi(1/2)$', ha='center'); ax.set_ylim(-.05, 1.3); ax.set_yticks([0, 1])
for ax in axes: ax.set_xlim(0, 1); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'kink, weak derivative, step, bump test function'})
