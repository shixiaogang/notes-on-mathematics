from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.015):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Spectrum and resolvent norm of A(x_n)=(x_n/n) on l2: ||R_lambda||=1/dist(lambda, {1/n} U {0}) for real lambda.
from matplotlib.gridspec import GridSpec
fig, _ = figure(width_mm=112, height_mm=66)
fig.set_layout_engine(None); fig.clear()
gs = GridSpec(2, 1, height_ratios=[1, 5.2], left=.1, right=.985, top=.98, bottom=.17, hspace=.85)
a0 = fig.add_subplot(gs[0]); a1 = fig.add_subplot(gs[1])
pts = 1/np.arange(1, 201)
a0.axhline(0, color=MUTED, lw=.85)
a0.plot(pts, 0*pts, 'o', color=BLUE, ms=3.0, mew=0, clip_on=False)
a0.plot([0], [0], 'o', mfc='white', mec=BLUE, ms=3.8, mew=.95, zorder=5)
a0.set_xlim(-.2, 1.25); a0.set_ylim(-1, 1); a0.set_yticks([]); a0.set_xticks([0, 1/3, .5, 1]); a0.set_xticklabels(['0', '1/3', '1/2', '1'])
a0.spines['left'].set_visible(False); a0.spines['bottom'].set_visible(False); a0.tick_params(length=0, pad=2)
S = np.concatenate([pts, [0.]])
g = np.linspace(-.2, 1.25, 12001)
g = np.setdiff1d(g, S)
d = np.array([np.min(np.abs(v-S)) for v in g])
a1.semilogy(g, 1/d, color=BLUE, lw=1.2)
a1.set_xlim(-.2, 1.25); a1.set_ylim(.8, 300); a1.set_xticks([0, .25, .5, .75, 1]); a1.set_xticklabels(['0', '0.25', '0.5', '0.75', '1'])
a1.set_xlabel(r'$\lambda$', labelpad=-1); a1.set_ylabel(r'$\Vert R_\lambda\Vert$', labelpad=1)
fig.canvas.draw()
q = a0.get_position(); fig.text((q.x0+q.x1)/2, q.y0-.125, '(a)', ha='center', va='bottom')
q = a1.get_position(); fig.text((q.x0+q.x1)/2, .005, '(b)', ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': '||R_lambda||=1/dist(lambda, sigma(A)), sigma(A)={1/n}U{0}'})
