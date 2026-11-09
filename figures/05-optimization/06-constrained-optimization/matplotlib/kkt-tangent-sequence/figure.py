from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Unit circle, xbar=(1,0), x^(k)=(cos t_k, sin t_k), t_k=1/2^(k-1): scaled differences tend to (0,1).
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panels(fig, .08, .985, .985, .27, .28)
a, b = axes
tk = [1/2**j for j in range(0, 6)]
xb = np.array([1., 0.])
s = np.linspace(-.3, 1.4, 300)
a.plot(np.cos(s), np.sin(s), color=BLUE, lw=1.4)
setup(a, (.2, 1.12), (-.12, 1.0), [.4, .6, .8, 1], [0, .5, 1])
for k, t in enumerate(tk):
    p = np.array([np.cos(t), np.sin(t)]); a.plot([xb[0], p[0]], [xb[1], p[1]], color=GREEN, lw=.85, zorder=2); dot(a, p, GREEN, ms=3.8)
dot(a, xb, INK, ms=4.5); a.text(1.05, -.08, '$\\bar{x}$', fontsize=8, ha='left', clip_on=False)
Q = [(np.array([np.cos(t), np.sin(t)])-xb)/t for t in tk]
th = np.linspace(0, 2*np.pi, 300)
b.axhline(0, color=MUTED, lw=.6, zorder=1); b.axvline(0, color=MUTED, lw=.6, zorder=1)
setup(b, (-.65, .3), (-.1, 1.15), [-.5, 0], [0, .5, 1], xl='$d_1$', yl='$d_2$')
for q in Q:
    arrow(b, (0, 0), q, color=GREEN, lw=.85, ms=6, z=3)
    dot(b, q, GREEN, ms=3.8)
arrow(b, (0, 0), (0, 1), color=RED, lw=1.5)
b.text(.04, 1.03, '$d=(0,1)$', fontsize=8, color=RED)
tags(fig, axes, y=.01)
save(fig, HERE, 'figure', {'t_k': tk, 'scaled': [q.tolist() for q in Q]})
print(Q)
