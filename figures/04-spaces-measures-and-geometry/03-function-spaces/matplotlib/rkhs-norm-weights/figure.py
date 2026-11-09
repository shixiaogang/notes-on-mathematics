from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
# (a) f=phi1 与 g=phi1+0.1 phi8，phi_j=sqrt2 sin((j-1/2)pi x)；(b) 权重：L2 恒 1，H_K 为 1/lambda_j=((j-1/2)pi)^2。
x = np.linspace(0, 1, 1201); om = lambda j: (j-.5)*np.pi; ph = lambda j: np.sqrt(2)*np.sin(om(j)*x)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.97, bottom=.265, wspace=.26)
a, b = axes
a.plot(x, ph(1), color=BLUE, lw=1.4); a.plot(x, ph(1)+.1*ph(8), color=GREEN, lw=1.1)
a.annotate('$f$', xy=(.45, .92), xytext=(.33, 1.3), color=INK, ha='center', va='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.7, shrinkA=1, shrinkB=0)); a.annotate('$g$', xy=(.875, 1.53), xytext=(.74, 1.66), color=INK, ha='center', va='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.7, shrinkA=1, shrinkB=0))
a.set_xlim(0, 1); a.set_ylim(0, 1.75); a.set_xticks([0, .5, 1]); a.set_xticklabels(['0', '0.5', '1']); a.set_yticks([0, 1]); a.set_xlabel('$x$', labelpad=1)
j = np.arange(1, 13)
b.semilogy(j, om(j)**2, 'o-', color=BLUE, ms=3.3, lw=1.2)
b.semilogy(j, 0*j+1, 's-', color=GREEN, ms=3.3, lw=1.2)
b.text(8, 18, r'$1/\lambda_j$', color=INK, ha='left', va='top'); b.text(8.2, 1.35, r'$L^2$', color=INK, va='bottom')
b.set_xticks([1, 4, 8, 12]); b.set_xlim(.5, 12.5); b.set_ylim(.6, 2200); b.set_yticks([1, 10, 100, 1000]); b.set_yticklabels(['1', '10', '100', '1000']); b.minorticks_off(); b.set_xlabel('$j$', labelpad=1)
fig.canvas.draw()
for ax, s in zip(axes, '(a) (b)'.split()):
    r = ax.get_position(); fig.text((r.x0+r.x1)/2, .015, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'f=phi1, g=phi1+.1phi8; weights 1 and ((j-1/2)pi)^2'})
