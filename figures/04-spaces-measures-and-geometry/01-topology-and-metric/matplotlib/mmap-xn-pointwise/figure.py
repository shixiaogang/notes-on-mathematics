from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# (a) x^n, n=1,2,5,20,100, and the pointwise limit; (b) N(x)=ceil(ln 0.01/ln x), smallest n with x^n<=0.01.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.22, wspace=.27)
a = axes[0]
x = np.linspace(0, 1, 1500)
for n in (1, 2, 5, 20, 100):
    a.plot(x, x**n, color=BLUE, lw=1.3, zorder=2)
a.plot([0, 1], [0, 0], color=RED, lw=1.5, zorder=3, solid_capstyle='butt', clip_on=False)
a.plot([1], [1], 'o', ms=4, color=RED, mew=0, zorder=4, clip_on=False)
a.plot([1], [0], 'o', ms=4, mfc='white', mec=RED, mew=1, zorder=5, clip_on=False)
for n, xp, yp in ((1, .33, .42), (5, .62, .22)):
    a.text(xp, yp, f'$n={n}$', color=INK, ha='center', va='center')
a.set_xlim(0, 1.03); a.set_ylim(0, 1.12); a.set_xticks([0, .5, 1]); a.set_xticklabels(['0', '1/2', '1']); a.set_yticks([0, 1])
b = axes[1]
xx = np.linspace(.02, .995, 4000)
N = np.maximum(1, np.ceil(np.log(.01)/np.log(xx)))
b.step(xx, N, where='post', color=BLUE, lw=1.3)
for t, m, va, dx in ((.9, 44, 'center', -.05), (.99, 459, 'center', -.05)):
    b.plot([t], [m], 'o', ms=3.2, color=INK, mew=0, zorder=4)
    b.text(t+dx, m, f'$N={m}$', ha='right', va=va, color=INK)
b.set_yscale('log'); b.set_xlim(0, 1.0); b.set_ylim(1, 1200); b.set_xticks([0, .5, .9, 1]); b.set_xticklabels(['0', '1/2', '0.9', '1']); b.set_yticks([1, 10, 100, 1000]); b.set_yticklabels(['1', '10', '100', '1000']); b.minorticks_off()
b.set_xlabel(''); 
for ax, s in zip(axes, '(a) (b)'.split()):
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    q = ax.get_position(); fig.text((q.x0+q.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x^n, N(x)=max(1,ceil(ln(0.01)/ln x))'})
