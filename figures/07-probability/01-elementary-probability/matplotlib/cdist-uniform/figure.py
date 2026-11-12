"""Unif(0,10) waiting time: (a) density with P(W>7) shaded; (b) distribution function."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

a, b = 0, 10
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
panel(fig, left=.1, bottom=.28, wspace=.32)
ax = axes[0]; style(ax)
ax.fill_between([7, 10], 0, .1, color=BLUE_FILL, lw=0)
ax.plot([-2, 0], [0, 0], color=BLUE, lw=1.4); ax.plot([0, 10], [.1, .1], color=BLUE, lw=1.4); ax.plot([10, 12], [0, 0], color=BLUE, lw=1.4)
ax.plot([0, 0], [0, .1], color=BLUE, lw=.85, ls=DOT); ax.plot([10, 10], [0, .1], color=BLUE, lw=.85, ls=DOT)
ax.plot([7, 7], [0, .1], color=RED, lw=1.2)
lab(ax, 8.5, .045, '0.3', ha='center')
ax.set_xlim(-2, 12); ax.set_ylim(0, .14); ax.set_xticks([0, 5, 7, 10]); ax.set_yticks([0, .1])
ax.set_xlabel('$w$', labelpad=1); ax.set_ylabel('$f_W(w)$', labelpad=1)
ax = axes[1]; style(ax)
x = np.array([-2, 0, 10, 12]); ax.plot(x, np.clip(x/10, 0, 1), color=BLUE, lw=1.4)
ax.plot([7, 7], [0, .7], color=RED, lw=.85, ls=DASH); ax.plot([-2, 7], [.7, .7], color=RED, lw=.85, ls=DASH); dot(ax, 7, .7)
ax.set_xlim(-2, 12); ax.set_ylim(0, 1.08); ax.set_xticks([0, 5, 7, 10]); ax.set_yticks([0, .5, .7, 1])
ax.set_xlabel('$w$', labelpad=1); ax.set_ylabel('$F_W(w)$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'P(W>7)': .3, 'mean': 5, 'var': 100/12})
