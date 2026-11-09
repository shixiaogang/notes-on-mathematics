from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# min -x1 x2 s.t. x1^2+x2^2<=2: five candidates.
fig, ax = figure(width_mm=88, height_mm=78)
xs = np.linspace(-1.9, 1.9, 500); X, Y = np.meshgrid(xs, xs)
ax.fill(np.sqrt(2)*np.cos(np.linspace(0, 2*np.pi, 300)), np.sqrt(2)*np.sin(np.linspace(0, 2*np.pi, 300)), facecolor=BLUE_FILL, edgecolor=EDGE, lw=1.8, zorder=1)
ax.contour(X, Y, -X*Y, levels=[-2.5, -1, -.4, .4, 1, 2.5], colors=BLUE, linewidths=.7, linestyles='solid', zorder=2)
setup(ax, (-1.9, 1.9), (-1.9, 1.9), [-1, 0, 1], [-1, 0, 1])
dot(ax, (1, 1)); dot(ax, (-1, -1)); dot(ax, (0, 0), YELLOW); hollow(ax, (1, -1), PURPLE); hollow(ax, (-1, 1), PURPLE)
ax.text(1.09, 1.12, '$(1,1)$', color=RED, fontsize=8); ax.text(-1.09, -1.2, '$(-1,-1)$', color=RED, fontsize=8, ha='right')
ax.text(.08, -.2, '$(0,0)$', fontsize=8); ax.text(1.09, -1.2, '$(1,-1)$', color=PURPLE, fontsize=8); ax.text(-1.09, 1.12, '$(-1,1)$', color=PURPLE, fontsize=8, ha='right')
save(fig, HERE, 'figure', {'problem': 'min -x1*x2, x1^2+x2^2<=2'})
