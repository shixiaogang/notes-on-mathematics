from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.patches import Rectangle

def labels(fig, axes, y=.03):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)']):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')

# f(x)=1.4+sin(2.2x) on [0,3]: Riemann strips against the level layer 1.6<=f<2.0.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.95, bottom=.2, wspace=.14)
f = lambda t: 1.4+np.sin(2.2*t)
x = np.linspace(0, 3, 1201)
a = axes[0]
edges = np.linspace(0, 3, 13)
for l, r in zip(edges[:-1], edges[1:]):
    m = f(np.linspace(l, r, 200)).min()
    a.add_patch(Rectangle((l, 0), r-l, m, fc=GREEN_FILL, ec=GREEN, lw=.65))
a.plot(x, f(x), color=BLUE, lw=1.4)
b = axes[1]
t0, t1 = 1.6, 2.0
b.axhspan(t0, t1, fc=YELLOW_FILL, ec='none')
mask = (f(x) >= t0) & (f(x) < t1)
idx = np.flatnonzero(np.diff(np.r_[0, mask.astype(int), 0]))
segs = [(x[idx[i]], x[idx[i+1]-1]) for i in range(0, len(idx), 2)]
for l, r in segs:
    b.add_patch(Rectangle((l, 0), r-l, t0, fc=GREEN_FILL, ec=GREEN, lw=.65))
    b.plot([l, r], [0, 0], color=RED, lw=2.6, solid_capstyle='butt', clip_on=False)
b.plot(x, f(x), color=BLUE, lw=1.4)
b.text(2.05, (t0+t1)/2, '层', ha='center', va='center', color=MUTED, fontsize=7.5)
b.text(1.5, -.03, '', ha='center')
for ax in axes:
    ax.set_xlim(0, 3.2); ax.set_ylim(0, 2.7); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1, 2])
    ax.text(3.05, f(3.0), '$f$', color=INK, ha='left', va='center')
b.set_yticks([0, t0, t1, 2.5]); b.set_yticklabels(['0', '$t_k$', '$t_{k+1}$', ''])
labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f(x)=1.4+sin(2.2x) on [0,3]; 12 equal strips with lower heights; layer 1.6<=f<2.0'})
