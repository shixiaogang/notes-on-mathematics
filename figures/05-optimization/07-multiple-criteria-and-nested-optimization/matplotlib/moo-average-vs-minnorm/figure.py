from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# g1=(10,1), g2=(-1,1): average direction leaves the half-plane of g2; min-norm direction stays inside both.
g1, g2 = np.array([10., 1.]), np.array([-1., 1.]); avg = .5*(g1+g2); th, gb = minnorm2(g1, g2)
fig, ax = figure(width_mm=100, height_mm=48)
setup(ax, (-6, 11.5), (-3.2, 2.2), [-5, 0, 5, 10], [-2, 0, 2], '$d_1$', '$d_2$', equal=True)
# descent wedge: <g1,d><0 and <g2,d><0
t = np.array([0, 40.]); e1 = np.array([1, -10.])/np.hypot(1, 10); e2 = np.array([-1, -1.])/np.hypot(1, 1)
ax.fill([0, 40*e1[0], 40*e2[0]], [0, 40*e1[1], 40*e2[1]], color=GREEN_FILL, lw=0, zorder=1)
for e in (e1, e2): ax.plot([-20*e[0], 20*e[0]], [-20*e[1], 20*e[1]], color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=2)
arrow(ax, (0, 0), g1, BLUE); arrow(ax, (0, 0), g2, BLUE); arrow(ax, (0, 0), -avg, YELLOW, lw=1.8); arrow(ax, (0, 0), -gb, GREEN, lw=1.8)
ax.text(10.2, 1.25, r'$g_1$', color=BLUE, ha='right'); ax.text(-1.45, 1.1, r'$g_2$', color=BLUE, ha='right')
ax.text(-5.9, -1.5, r'$-\frac{1}{2}(g_1+g_2)$', color=YELLOW); ax.text(.25, -1.3, r'$-\bar g$', color=GREEN); hollow(ax, (0, 0), INK, ms=4)
save(fig, HERE, 'figure', {'avg': avg.tolist(), 'theta1': th, 'bar_g': gb.tolist(), 'd_avg_on_g2': float(g2@(-avg))}); print(th, gb, g2@(-avg))
