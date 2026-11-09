from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Basis (1,4,2) at vertex (2,3): entering x3 moves by (-1,0) at rate s3=4; entering x5 moves by (2,-1) at rate s5=-3.
xlim, ylim = (-.4, 5.6), (-.4, 4.6)
fig, ax = figure(width_mm=92, height_mm=60)
A, b = with_sign(RES_A, RES_B); V = polygon(A, b)
draw_region(ax, V)
contours(ax, PROFIT, [23], xlim, ylim)
draw_line(ax, RES_A[0], 8, xlim, ylim, lw=1.4); draw_line(ax, RES_A[2], 3, xlim, ylim, lw=1.4)
ax.plot([2],[3],'o',color=GREEN,ms=4.5,zorder=7)
ax.annotate('', xy=(3.6,2.2), xytext=(2,3), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.6, mutation_scale=9), zorder=6)
ax.annotate('', xy=(.8,3), xytext=(2,3), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.6, mutation_scale=9), zorder=6)
ax.text(2.25, 2.12, '$s_5=-3$', fontsize=7.5, color=INK)
ax.text(.1, 3.18, '$s_3=4$', fontsize=7.5, color=INK)
ax.text(4.72,4.15,'',fontsize=7.5)
ax.text(.32, 4.17, '$f=-23$', fontsize=7.5, color=BLUE)
ax.text(1.98, 3.22, '$(2,3)$', fontsize=7.5, color=INK)
setup(ax, xlim, ylim, range(0,6), range(0,5))
save(fig, Path(__file__).resolve().parent, 'figure', {'basis':'(1,4,2)','s3':4,'s5':-3,'moves':{'x3':[-1,0],'x5':[2,-1]}})
