from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Isotropic pair: gradients at an off-segment point p=(1,1) and on-segment point q=(0.6,0.4).
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panels(fig, .08, .985, .985, .19, .24)
X, Y = np.meshgrid(np.linspace(-.5, 2.3, 300), np.linspace(-.5, 2.3, 300)); F1, F2 = f_iso(np.stack([X, Y], -1))
P = [np.array([1., 1.]), np.array([.6, .4])]
for ax, p in zip(axes, P):
    setup(ax, (-.3, 2.2), (-.3, 2.2), [0, 1], [0, 1], '$x_1$', '$x_2$', equal=True)
    a, b = f_iso(p); ax.contour(X, Y, F1, levels=[a], colors=BLUE, linewidths=.8); ax.contour(X, Y, F2, levels=[b], colors=BLUE, linewidths=.8, linestyles=[(0, (3, 2))])
    ax.plot([1, 0], [0, 1], color=RED, lw=1.6, zorder=3)
    g1, g2 = p-A0, p-B0; th, g = minnorm2(g1, g2)
    arrow(ax, p, p+g1, BLUE); arrow(ax, p, p+g2, BLUE); ax.plot([p[0]+g1[0], p[0]+g2[0]], [p[1]+g1[1], p[1]+g2[1]], color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=4)
    dot(ax, p, GREEN)
    if g@g > 1e-9: arrow(ax, p, p-g, GREEN, lw=1.5)
axes[0].text(1.03, 1.03, '$p$', color=INK); axes[0].text(.8, 1.96, r'$g_1$', color=BLUE, va='top'); axes[0].text(1.95, .88, r'$g_2$', color=BLUE, ha='right', va='top'); axes[0].text(.32, .78, r'$-\bar g$', color=GREEN)
axes[1].text(.65, .42, '$q$', color=INK); axes[1].text(.1, .85, r'$g_1$', color=BLUE); axes[1].text(1.2, -.2, r'$g_2$', color=BLUE)
tags(fig, axes)
save(fig, HERE, 'figure', {'p': [1, 1], 'q': [.6, .4]})
