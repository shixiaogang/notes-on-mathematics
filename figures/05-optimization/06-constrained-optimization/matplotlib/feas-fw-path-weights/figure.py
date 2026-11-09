from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
X, gp, st, v = fw(T=8)
W = [np.array([0, 0, 1.])]
for t in range(7):
    w = (1-st[t])*W[-1]; w[v[t]] += st[t]; W.append(w)
W = np.array(W)
fig, axs = figure(width_mm=112, height_mm=52, ncols=2, gridspec_kw={'width_ratios': [1, 1.05]})
ax = axs[0]; triangle(ax); contours(ax); active(ax, V[0], V[1]); XY = bary(X); path(ax, XY[:9]); dot(ax, bary(XS)); off(ax, (-.1, 1.1), (-.1, .95))
ax = axs[1]; b = np.zeros(8)
for j, c, f_, n in ((0, BLUE, BLUE_FILL, '$e_1$'), (1, GREEN, GREEN_FILL, '$e_2$'), (2, YELLOW, YELLOW_FILL, '$e_3$')):
    ax.bar(np.arange(8), W[:, j], bottom=b, width=.66, facecolor=f_, edgecolor=c, lw=.9, label=n); b += W[:, j]
setup(ax, (-.6, 7.6), (0, 1.3), range(8), [0, .5, 1], xl='$t$', yl='权重')
ax.legend(loc='upper center', ncol=3, handlelength=1, columnspacing=.9, handletextpad=.3, borderaxespad=0)
panels(fig, .01, .985, .98, .17, .2); tags(fig, axs)
save(fig, HERE, 'figure', {'rule': '2/(t+2)', 'start': [0, 0, 1], 'weights': W.tolist()})
