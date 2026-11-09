from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# A=[[2,1],[1,2]], u=(cos t, sin t): R=2+sin 2t; ||Au-3u||^2=4 sin^2(t-pi/4) <= 18-6R = 12 sin^2(t-pi/4).
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.065, right=.985, top=.96, bottom=.25, wspace=.24)
t = np.linspace(0, np.pi, 401)
ticks = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]; lbl = ['0', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$']
ax = axes[0]
ax.plot(t, 2+np.sin(2*t), color=BLUE, lw=1.4)
ax.plot([np.pi/4], [3], 'o', color=BLUE, ms=3.6, mew=0); ax.plot([3*np.pi/4], [1], 'o', color=BLUE, ms=3.6, mew=0)
ax.text(np.pi/4, 3.12, '$3$', ha='center'); ax.text(3*np.pi/4, .62, '$1$', ha='center')
ax.set_xlim(0, np.pi); ax.set_ylim(0, 3.7); ax.set_yticks([0, 1, 2, 3]); ax.set_ylabel(r'$\langle u,Au\rangle$', labelpad=1)
ax = axes[1]
s2 = np.sin(t-np.pi/4)**2
ax.plot(t, 4*s2, color=BLUE, lw=1.4); ax.plot(t, 12*s2, color=RED, lw=1.2, ls='--')
ax.plot([np.pi/4], [0], 'o', color=BLUE, ms=3.6, mew=0)
ax.text(2.0, 10.8, r'$18-6\langle u,Au\rangle$', ha='right'); ax.text(2.55, 2.1, r'$\Vert Au-3u\Vert^2$', ha='center')
ax.set_xlim(0, np.pi); ax.set_ylim(0, 13.5); ax.set_yticks([0, 4, 8, 12])
for ax in axes: ax.set_xticks(ticks); ax.set_xticklabels(lbl); ax.set_xlabel(r'$\theta$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'R(t)=2+sin 2t; residual^2=4 sin^2(t-pi/4); bound 12 sin^2(t-pi/4)'})
