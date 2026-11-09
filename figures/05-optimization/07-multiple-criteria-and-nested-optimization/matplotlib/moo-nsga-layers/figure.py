from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Non-dominated layers and crowding boxes of eight candidates.
C8 = dict(CANDS); C8.update(G=(3, 7), H=(6, 7))
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .985, .2, .22)
ax = axes[0]; setup(ax, (0, 8), (0, 9.5), range(0, 9, 2), range(0, 10, 2))
L = [('ABCD', RED), ('GEF', PURPLE), ('H', MUTED)]
for names, c in L:
    P = np.array([C8[k] for k in names]); ax.plot(P[:, 0], P[:, 1], color=c, lw=1.2, zorder=2)
    ax.plot(P[:, 0], P[:, 1], 'o', color=c, ms=5, mew=0, zorder=4)
for k, (dx, dy) in {'A': (.2, .1), 'B': (.2, .2), 'C': (.2, .25), 'D': (-.15, .35), 'E': (.2, .1), 'F': (.1, .35), 'G': (.15, .3), 'H': (.2, .2)}.items(): ax.text(C8[k][0]+dx, C8[k][1]+dy, k, color=INK)
ax = axes[1]; setup(ax, (0, 8), (0, 9.5), range(0, 9, 2), range(0, 10, 2))
P = np.array([C8[k] for k in 'ABCD']); ax.plot(P[:, 0], P[:, 1], color=RED, lw=1.0, zorder=2); ax.plot(P[:, 0], P[:, 1], 'o', color=RED, ms=5, mew=0, zorder=4)
for (l, r), col, fc in ((('A', 'C'), BLUE, BLUE_FILL), (('B', 'D'), GREEN, GREEN_FILL)):
    a, b = C8[l], C8[r]; ax.fill([a[0], b[0], b[0], a[0]], [b[1], b[1], a[1], a[1]], facecolor=fc, edgecolor=col, lw=.95, zorder=1)
for k, (dx, dy) in {'A': (.2, .1), 'B': (-.55, -.1), 'C': (.2, .25), 'D': (.15, .3)}.items(): ax.text(C8[k][0]+dx, C8[k][1]+dy, k, color=INK)
tags(fig, axes)
def crowd(names):
    pts = {k: np.array(C8[k], float) for k in names}; d = {k: 0. for k in names}
    for m in range(2):
        s = sorted(names, key=lambda k: pts[k][m]); span = pts[s[-1]][m]-pts[s[0]][m]
        d[s[0]] = d[s[-1]] = np.inf
        for i in range(1, len(s)-1): d[s[i]] += (pts[s[i+1]][m]-pts[s[i-1]][m])/span
    return d
save(fig, HERE, 'figure', {'crowd_F1': crowd('ABCD'), 'crowd_F2': crowd('GEF')}); print(crowd('ABCD'), crowd('GEF'))
