from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# P=N(0,1) and Q=Unif(-sqrt3, sqrt3): equal mean 0 and variance 1.
# (a) densities; (b) E_P g - E_Q g for g = x, x^2, cos x, 1{|x|<=1}:
#     0, 0, e^{-1/2} - sin(sqrt3)/sqrt3 = 0.0367, (2Phi(1)-1) - 1/sqrt3 = 0.1053.
r3 = math.sqrt(3)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.98, top=.95, bottom=.26, wspace=.3)
ax = axs[0]
x = np.linspace(-3.5, 3.5, 1000)
ax.plot(x, npdf(x), color=BLUE, lw=1.4)
ax.plot([-3.5, -r3, -r3, r3, r3, 3.5], [0, 0, 1/(2*r3), 1/(2*r3), 0, 0], color=YELLOW, lw=1.6)
lab(ax, -1.9, .36, '$P$', BLUE, ha='center', fontsize=8)
lab(ax, 2.15, .3, '$Q$', YELLOW, ha='center', fontsize=8)
ax.set_xlim(-3.5, 3.5); ax.set_ylim(0, .46); ax.set_yticks([0, .2, .4])
axlab(ax, '$x$', '密度')
ax = axs[1]
vals = [0., 0., math.exp(-.5)-math.sin(r3)/r3, (2*float(Phi(1))-1)-1/r3]
names = ['$x$', '$x^2$', r'$\cos x$', r'$\mathbf{1}_{\{|x|\leq1\}}$']
for i, v in enumerate(vals):
    if abs(v) > 1e-12:
        ax.bar([i], [v], width=.5, color=BLUE_FILL, edgecolor=BLUE, linewidth=.8)
        lab(ax, i, v+.004, f'{v:.4f}', BLUE, ha='center', fontsize=6.8)
    else:
        dot(ax, i, 0, RED, ms=4)
ax.axhline(0, color=STROKE, lw=.85)
ax.set_xticks(range(4)); ax.set_xticklabels(names)
ax.set_xlim(-.6, 3.6); ax.set_ylim(-.01, .125); ax.set_yticks([0, .05, .1])
ax.set_ylabel('期望差', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', {'diffs': vals})
