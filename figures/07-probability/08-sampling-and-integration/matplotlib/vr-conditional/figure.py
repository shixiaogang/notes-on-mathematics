from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# X, Y iid Unif(0,1), f(X,Y) = 1{X^2+Y^2 <= 1}, I = pi/4.  g(x) = E[f | X=x] = sqrt(1-x^2).
# (a) 300 seeded points (seed 2) plus the four teaching points (X, Y) = (0.37,0.23), (0.81,0.68), (0.06,0.45), (0.52,0.91).
# (b) g(x) with the four teaching X values: each slice is averaged exactly instead of sampling Y.
X4 = np.array([.37, .81, .06, .52]); Y4 = np.array([.23, .68, .45, .91])
rng = np.random.default_rng(2); P = rng.random((300, 2))
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, left=.07, right=.98, bottom=.24, top=.96, wspace=.25)
a, b = axs
t = np.linspace(0, 1, 300)
for ax in axs:
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect('equal'); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
    axlab(ax, '$x$')
a.plot(t, np.sqrt(1-t*t), color=BLUE, lw=1.2)
ins = (P**2).sum(1) <= 1
a.plot(P[ins, 0], P[ins, 1], 'o', ms=1.6, color=GREEN, mew=0)
a.plot(P[~ins, 0], P[~ins, 1], 'o', ms=1.6, color=RED, mew=0)
for x, y in zip(X4, Y4):
    a.plot([x], [y], 'o', ms=4.2, mfc='white', mec=GREEN if x*x+y*y <= 1 else RED, mew=1.2, zorder=6)
a.set_ylabel('$y$', labelpad=1)
b.fill_between(t, 0, np.sqrt(1-t*t), color=BLUE_FILL, lw=0)
b.plot(t, np.sqrt(1-t*t), color=BLUE, lw=1.4)
for x in X4:
    g = math.sqrt(1-x*x)
    b.plot([x, x], [0, g], color=GREEN, lw=1.4); dot(b, x, g, color=GREEN, ms=3.6)
b.axhline(math.pi/4, color=PURPLE, lw=.85, ls=DASH)
lab(b, .03, math.pi/4-.08, r'$\pi/4$', PURPLE)
tags(fig, axs)
save(fig, HERE, 'figure', {'frac_inside_300': float(ins.mean()), 'g4': [math.sqrt(1-x*x) for x in X4],
     'plain4': float(((X4**2+Y4**2) <= 1).mean()), 'cond4': float(np.mean(np.sqrt(1-X4**2))),
     'var_f': math.pi/4*(1-math.pi/4), 'var_g': 2/3-math.pi**2/16})
