from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# B(x)=[[1+x,1],[1,3-x]]: eigenvalues 2 +- sqrt((1-x)^2+1); Z=(1/2)[[1,1],[1,1]] gives the flat bound 3.
fig, ax = figure(width_mm=88, height_mm=56)
x = np.linspace(-1.5, 3.5, 400)
e = np.array([np.linalg.eigvalsh(np.array([[1+s, 1], [1, 3-s]])) for s in x])
ax.fill_between(x, e[:, 1], 5.05, facecolor=BLUE_FILL, edgecolor='none', zorder=0)
ax.plot(x, e[:, 1], color=BLUE, lw=1.5, zorder=3); ax.plot(x, e[:, 0], color=MUTED, lw=1.2, ls=(0, (4, 2)), zorder=3)
ax.axhline(3, color=PURPLE, lw=1.3, zorder=2); ax.axhline(2, color=PURPLE, lw=1.0, ls=(0, (3, 2)), zorder=2)
dot(ax, (1, 3))
setup(ax, (-1.5, 3.5), (0, 5.05), [-1, 0, 1, 2, 3], [0, 1, 2, 3, 4, 5], xl='$x$', yl='特征值', equal=False)
ax.text(-1.4, 4.68, '$\\lambda_{\\max}$', color=BLUE, fontsize=8); ax.text(-1.3, .42, '$\\lambda_{\\min}$', color=MUTED, fontsize=8)
ax.text(3.45, 3.1, '$Z_1$', color=PURPLE, fontsize=8, ha='right'); ax.text(3.45, 2.1, '$Z_2$', color=PURPLE, fontsize=8, ha='right')
ax.text(1, 3.32, '$(1,3)$', color=RED, fontsize=7.5, ha='center')
save(fig, HERE, 'figure', {'t*': 3, 'x*': 1, 'Z1': [[.5, .5], [.5, .5]], 'Z2': [[.5, 0], [0, .5]]})
