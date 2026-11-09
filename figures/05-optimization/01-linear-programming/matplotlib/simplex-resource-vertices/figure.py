from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Resource example: max 4x1+5x2, x1+2x2<=8, 2x1+x2<=10, x2<=3, x>=0.
xlim, ylim = (-.5, 6.9), (-.5, 5.3)
fig, ax = figure(width_mm=100, height_mm=66)
A, b = with_sign(RES_A, RES_B); V = polygon(A, b)
draw_region(ax, V)
contours(ax, PROFIT, [8, 15, 26], xlim, ylim)
draw_line(ax, RES_A[0], 8, xlim, ylim); draw_line(ax, RES_A[1], 10, xlim, ylim); draw_line(ax, RES_A[2], 3, xlim, ylim)
ax.text(6.05, 1.18, '原料', fontsize=7.5, color=MUTED); ax.text(4.72, 1.68, '', fontsize=7.5)
ax.text(3.45, 4.0, '工时', fontsize=7.5, color=MUTED); ax.text(5.7, 3.1, '设备', fontsize=7.5, color=MUTED)
for p, t, off, ha in [((0,0), '$(3,4,5)$', (.12,.12), 'left'), ((5,0), '$(3,1,5)$', (.1,.14), 'left'), ((4,2), '$(1,5,2)$', (.14,.1), 'left'),
                      ((2,3), '$(1,4,2)$', (-.1,-.34), 'right'), ((0,3), '$(3,4,2)$', (.12,.17), 'left')]:
    ax.plot(*p, 'o', color=INK, ms=3.2, zorder=6)
    ax.text(p[0]+off[0], p[1]+off[1], t, fontsize=7.5, ha=ha, color=INK, zorder=7)
opt_point(ax, (4,2))
ax.annotate('', xy=(2.1, 2.02), xytext=(1.1, .77), arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.1, mutation_scale=8), zorder=4)
ax.text(2.2, 1.8, '$\\mathbf{p}$', fontsize=8, color=BLUE)
for lv, xp, yp in [(8,.5,1.0),(15,.7,2.08),(26,.62,5.0)]:
    ax.text(xp+.08, yp-.02, f'${lv}$', fontsize=7.5, color=BLUE)
setup(ax, xlim, ylim, range(0,7), range(0,6))
save(fig, Path(__file__).resolve().parent, 'figure', {'problem':'max 4x1+5x2; x1+2x2<=8; 2x1+x2<=10; x2<=3; x>=0'})
