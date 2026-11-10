from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Same field u=sin(pi x)+x, h=1/4: grid values, hat-basis coefficients, cell averages.
X = np.linspace(0, 1, 801); n = 4; h = 1/n; xn = np.linspace(0, 1, n+1)
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.06, wspace=.14, bottom=.27)
for ax in axes:
    ax.plot(X, uex(X), color=BLUE, lw=1.4)
    ax.set_xlim(-.03, 1.03); ax.set_ylim(0, 1.75); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_xlabel('$x$', labelpad=1)
axes[0].set_yticks([0, 1]); axes[1].set_yticks([]); axes[2].set_yticks([])
axes[0].plot(xn[1:-1], uex(xn[1:-1]), 'o', ms=4.2, color=GREEN, mew=0, zorder=5)
axes[0].plot([0, 1], [0, 1], 'o', ms=4.4, color=RED, mew=0, zorder=6, clip_on=False)
axes[1].plot(xn, uex(xn), color=GREEN, lw=1.4)
for xi, c in zip(xn[1:-1], uex(xn[1:-1])):
    axes[1].plot([xi-h, xi, xi+h], [0, c, 0], color=YELLOW, lw=.9)
axes[1].plot([1-h, 1], [0, 1], color=RED, lw=.9)
axes[1].plot([0, 1], [0, 1], 'o', ms=4.4, color=RED, mew=0, zorder=6, clip_on=False)
avg = []
for i in range(n):
    a, b = i*h, (i+1)*h
    v = (np.cos(PI*a)-np.cos(PI*b))/(PI*h)+(a+b)/2; avg.append(v)
    axes[2].plot([a, b], [v, v], color=GREEN, lw=1.6)
    if i: axes[2].plot([a, a], [0, 1.75], color=STROKE, lw=.65, ls=DOT)
tags(fig, axes)
save(fig, HERE, 'figure', {'h': h, 'nodal': uex(xn).tolist(), 'cell_avg': avg})
print(avg)
