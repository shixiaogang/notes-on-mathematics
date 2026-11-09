from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Feasible set, level sets and KKT geometry of the running example.
fig, ax = figure(width_mm=76, height_mm=58)
lim = (-2.6, 3.9, -.6, 4.7)
region(ax); f_contours(ax, lim, [.5, 1.5, 2.5, 4.5, 7, 10, 14])
ax.plot(*XSTAR, 'o', color=RED, ms=5, zorder=6)
ax.annotate('', xy=(3, 0), xytext=(1, 1), arrowprops=dict(arrowstyle='-|>', color=PURPLE, lw=1.2), zorder=5)
ax.plot([3], [0], 'x', color=INK, ms=4.5, mew=1)
ax.text(2.15, .72, r'$-\nabla f(\bm{x}^*)=\nabla g_1(\bm{x}^*)$'.replace(r'\bm{x}', r'x'), fontsize=7.5, ha='left')
ax.text(.72, 1.28, '$x^*$', fontsize=8, ha='right'); ax.text(3.1, -.42, '$c$', fontsize=7.5)
ax.text(-1.42, 1.25, '$g_1=0$', fontsize=7.5, ha='right'); ax.text(0, 4.15, '$g_2=0$', fontsize=7.5, ha='center')
ax.text(-.25, 2.6, '$C$', fontsize=8)
ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3]); ax.set_aspect('equal')
ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
save(fig, OUT, 'figure', {'formula': 'f=((x1-3)^2+x2^2)/2, g1=x1^2-x2, g2=x2-4', 'x_star': [1, 1], 'lambda_star': [1, 0]})
