from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'tail-common'))
from tail_fig import *
# X ~ Exp(1): area under the survival curve s -> P(X>s) equals E[X]=1;
# the rectangle [0,t] x [0,P(X>=t)] with t=2 sits under the curve, so t P(X>=t) <= E[X].
s = np.linspace(0, 5, 1001); S = np.exp(-s); t = 2.0; h = np.exp(-t)
fig, ax = figure(width_mm=86, height_mm=48)
ax.fill_between(s, 0, S, color=BLUE_FILL, lw=0)
ax.add_patch(__import__('matplotlib').patches.Rectangle((0, 0), t, h, facecolor=YELLOW_FILL, edgecolor=YELLOW, lw=1.2, zorder=3))
ax.plot(s, S, color=BLUE, lw=1.4, zorder=4)
ax.plot([t, t], [0, 1.0], color=RED, lw=1.2, zorder=5)
dot(ax, t, h, RED)
lab(ax, t+.08, 1.0, '$t=2$', RED, va='top')
lab(ax, 1.0, h/2, r'$t\,ℙ(X\geq t)$', INK, ha='center', va='center', zorder=6)
ax.annotate(r"$\mu$", xy=(.45, .3), xytext=(1.05, .62), color=INK, fontsize=7.5, arrowprops=dict(arrowstyle="->", color=STROKE, lw=.8))
lab(ax, 3.2, np.exp(-3.2)+.05, r'$ℙ(X>s)$', BLUE, ha='left')
ax.set_xlim(0, 5); ax.set_ylim(0, 1.08); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, h, .5, 1]); ax.set_yticklabels(['0', '$\\mathrm{e}^{-2}$', '0.5', '1'])
axlab(ax, '$s$')
save(fig, HERE, 'figure', {'E[X]': 1.0, 't': t, 'rectangle_area': float(t*h)})
