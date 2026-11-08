from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# f(x)=x, f_5(x)=x+sin(8 pi x)/5. (a) tube eps=1/4 around f; (b) the same pair at x=0.3, x'=0.36: three segments of the epsilon/3 argument.
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.2, wspace=.2)
x = np.linspace(0, 1, 1200)
f = lambda t: t
g = lambda t: t+np.sin(8*np.pi*t)/5
a = axes[0]
a.fill_between(x, f(x)-.25, f(x)+.25, color=GREEN_FILL, lw=0, zorder=1)
a.plot(x, f(x)-.25, color=GREEN, lw=.85, zorder=2); a.plot(x, f(x)+.25, color=GREEN, lw=.85, zorder=2)
a.plot(x, f(x), color=INK, lw=1.1, zorder=3)
a.plot(x, g(x), color=BLUE, lw=1.4, zorder=4)
a.text(.1, .78, '$f_5$', color=INK, ha='center'); a.text(.87, .62, '$f$', color=INK, ha='center')
a.set_xlim(0, 1); a.set_ylim(-.35, 1.35); a.set_xticks([0, 1]); a.set_yticks([0, 1])
b = axes[1]
xz = np.linspace(.18, .48, 500)
b.plot(xz, f(xz), color=INK, lw=1.1, zorder=3)
b.plot(xz, g(xz), color=BLUE, lw=1.4, zorder=4)
p, q = .30, .36
b.plot([p, p], [f(p), g(p)], color=RED, lw=1.5, zorder=5)
b.plot([q, q], [f(q), g(q)], color=RED, lw=1.5, zorder=5)
b.plot([p, q], [g(p), g(q)], color=RED, lw=1.5, zorder=5)
for t, v in ((p, f(p)), (p, g(p)), (q, f(q)), (q, g(q))):
    b.plot([t], [v], 'o', ms=3, color=RED, mew=0, zorder=6)
b.text(p-.012, (f(p)+g(p))/2, '①', ha='right', va='center', color=INK)
b.text(q+.012, (f(q)+g(q))/2, '③', ha='left', va='center', color=INK)
b.text((p+q)/2, (g(p)+g(q))/2+.022, '②', ha='center', va='bottom', color=INK)
b.text(.195, .155, '$f$', color=INK, ha='center', va='center'); b.text(.205, .36, '$f_N$', color=INK, ha='center', va='center')
b.set_xlim(.18, .48); b.set_ylim(.1, .62); b.set_xticks([p, q]); b.set_xticklabels(['$x$', r"$x'$"]); b.set_yticks([])
for ax, s in zip(axes, '(a) (b)'.split()):
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    q0 = ax.get_position(); fig.text((q0.x0+q0.x1)/2, .03, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f(x)=x; f_N(x)=x+sin(8 pi x)/5; tube half-width 1/4'})
