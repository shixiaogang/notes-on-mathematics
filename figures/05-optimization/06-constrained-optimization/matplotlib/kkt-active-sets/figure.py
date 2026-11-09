from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Active sets at three feasible points of the budget triangle tau=2.
fig, axes = figure(width_mm=112, height_mm=40, ncols=3)
panels(fig, .03, .985, .985, .12, .1)
P = [(np.array([.6, .6]), []), (np.array([1.5, .5]), [((2, 0), (0, 2))]), (np.array([2., 0.]), [((2, 0), (0, 2)), ((0, 0), (2, 0))])]
th = np.linspace(0, 2*np.pi, 200); r = .42
for ax, (p, seg) in zip(axes, P):
    off(ax, (-.2, 2.75), (-.5, 2.1)); triangle(ax, 2)
    ax.plot(p[0]+r*np.cos(th), p[1]+r*np.sin(th), color=MUTED, lw=.85, ls=(0, (3, 2)), zorder=3)
    for a, b in seg: active(ax, a, b)
    dot(ax, p, GREEN)
labels = ['$A=\\varnothing$', '$A=\\{1\\}$', '$A=\\{1,3\\}$']
for ax, s in zip(axes, labels): ax.text(1.3, 1.65, s, color=INK, fontsize=8)
tags(fig, axes)
save(fig, HERE, 'figure', {'points': [p.tolist() for p, _ in P]})
