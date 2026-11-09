from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
# (a) 最小值核 [0,1] Lebesgue 下 phi_j=sqrt2 sin((j-1/2)pi x)；(b) 特征值：最小值核 ((j-1/2)pi)^-2，
# 高斯核 sigma=.5,[-1,1],dx/2（40 点 Gauss-Legendre 离散），仿射核 1,1/3。
from numpy.polynomial.legendre import leggauss
x = np.linspace(0, 1, 501); om = lambda j: (j-.5)*np.pi
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.245, wspace=.28)
a, b = axes
for j, c in zip((1, 2, 3), (BLUE, GREEN, YELLOW)):
    a.plot(x, np.sqrt(2)*np.sin(om(j)*x), color=c, lw=1.4)
a.axhline(0, color=GRID, lw=.85, zorder=0)
a.text(.74, 1.42, r'$\phi_1$', color=INK, ha='center'); a.text(.43, 1.5, r'$\phi_2$', color=INK, ha='center'); a.text(.2, 1.55, r'$\phi_3$', color=INK, ha='center')
a.set_xlim(0, 1); a.set_ylim(-1.6, 1.9); a.set_xticks([0, .5, 1]); a.set_xticklabels(['0', '0.5', '1']); a.set_yticks([-1, 0, 1]); a.set_xlabel('$x$', labelpad=1)
t, w = leggauss(40); G = np.exp(-(t[:, None]-t[None])**2/(2*.25)); S = np.sqrt(w/2)
eg = np.linalg.eigvalsh(S[:, None]*G*S[None])[::-1][:8]
j = np.arange(1, 9)
b.semilogy(j, om(j)**-2, 'o-', color=BLUE, ms=3.3, lw=1.2)
b.semilogy(j, eg, 's-', color=GREEN, ms=3.3, lw=1.2)
b.semilogy([1, 2], [1, 1/3], '^', color=YELLOW, ms=4, ls='-', lw=1.2)
b.text(7, 6e-3, '最小值', color=INK, ha='center', va='bottom'); b.text(5.6, 3e-4, '高斯', color=INK, ha='right', va='center'); b.text(2.25, .42, '仿射', color=INK, va='center')
b.set_xticks([1, 2, 4, 6, 8]); b.set_xlim(.7, 8.3); b.set_ylim(1e-5, 2.5); b.set_yticks([1, 1e-2, 1e-4]); b.minorticks_off(); b.set_xlabel('$j$', labelpad=1); b.set_ylabel(r'$\lambda_j$', labelpad=2, rotation=0, va='center')
fig.canvas.draw()
for ax, s in zip(axes, '(a) (b)'.split()):
    r = ax.get_position(); fig.text((r.x0+r.x1)/2, .015, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'lambda_j=((j-1/2)pi)^-2; phi_j=sqrt2 sin((j-1/2)pi x); gaussian via 40-pt GL', 'gauss': eg.tolist()})
