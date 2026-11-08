from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# V f = g, f=1, g=x. Perturbation delta*u_20 with delta=0.01, u_k=sqrt2 sin(w_k x), v_k=sqrt2 cos(w_k x), w_k=(k-1/2)pi, sigma_k=1/w_k.
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.945, top=.96, bottom=.28, wspace=.2)
x = np.linspace(0, 1, 6001); w = 19.5*np.pi; d = .01
ax = axes[0]
ax.plot(x, x+d*2**.5*np.sin(w*x), color=RED, lw=.85)
ax.plot(x, x, color=BLUE, lw=1.4)
ax.text(.12, .62, '$g=x$', ha='left'); ax.text(.1, .47, '$g+\\delta u_{20}$', ha='left')
ax.set_xlim(0, 1); ax.set_ylim(-.05, 1.1); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '0.5', '1']); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ax.plot(x, 1+(d*w)*2**.5*np.cos(w*x), color=RED, lw=.85)
ax.plot(x, np.ones_like(x), color=BLUE, lw=1.4)
ax.text(1.02, 1, '$f=1$', ha='left', va='center', clip_on=False, fontsize=7.5)
ax.text(.5, 2.2, '$f+(\\delta/\\sigma_{20})v_{20}$', ha='center', va='bottom', fontsize=7.5)
ax.set_xlim(0, 1); ax.set_ylim(-.1, 2.6); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'g=x, f=1, delta=0.01, k=20; f_perturbed=1+(delta/sigma_20) v_20'})
