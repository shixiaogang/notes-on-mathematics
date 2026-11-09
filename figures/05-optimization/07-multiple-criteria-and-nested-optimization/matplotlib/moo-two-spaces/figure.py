from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# f1=||x-a||^2/2, f2=||x-b||^2/2, a=(1,0), b=(0,1): decision plane and its image.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .2, .28)
ax = axes[0]; setup(ax, (-.55, 1.6), (-.55, 1.6), [0, 1], [0, 1], '$x_1$', '$x_2$', equal=True)
X, Y = np.meshgrid(np.linspace(-.6, 1.7, 300), np.linspace(-.6, 1.7, 300))
F1, F2 = f_iso(np.stack([X, Y], -1))
ax.contour(X, Y, F1, levels=[.125, .5, 1.], colors=BLUE, linewidths=.7)
ax.contour(X, Y, F2, levels=[.125, .5, 1.], colors=BLUE, linewidths=.7, linestyles=[(0, (3, 2))])
hollow(ax, A0, BLUE); hollow(ax, B0, BLUE)
ax.text(1.06, -.17, '$a$', color=BLUE); ax.text(-.2, 1.05, '$b$', color=BLUE)
P = [(1, 1), (0, 0), (.5, .5)]
for p, t, d in zip(P, ['$p$', "$p'$", '$q$'], [(.06, .05), (-.2, -.2), (.06, .05)]):
    dot(ax, p, GREEN); ax.text(p[0]+d[0], p[1]+d[1], t, color=INK)
ax = axes[1]; setup(ax, (0, 1.5), (0, 1.5), [0, .5, 1, 1.5], [0, .5, 1, 1.5], equal=True); iso_fill(ax, 1.5)
u, v = iso_front(); ax.plot(u, v, color=BLUE, lw=1.2, zorder=2)
dot(ax, (.5, .5), GREEN); dot(ax, (.25, .25), GREEN)
ax.text(.56, .55, "$f(p)=f(p')$", color=INK); ax.text(.05, .08, '$f(q)$', color=INK)
ax.text(.8, 1.2, '$Y$', color=BLUE, fontsize=8)
tags(fig, axes)
save(fig, HERE, 'figure', {'p': [1, 1], "p'": [0, 0], 'f(p)': f_iso([1, 1]).tolist(), 'f(q)': f_iso([.5, .5]).tolist()})
