from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Gradient cone and linearized cone at a corner. (a) tau=.5: -grad f=(1.5,1) in cone. (b) tau=2 at (2,0): -grad f=(0,1) outside; d=(-1,1).
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panels(fig, .02, .99, .985, .12, .08)
for ax, r in zip(axes, [(1.5, 1.), (0., 1.)]):
    off(ax, (-2.0, 2.0), (-1.45, 1.7))
    R = 1.38; th = np.radians(np.linspace(-90, 45, 40))
    ax.fill(np.r_[0, R*np.cos(th)], np.r_[0, R*np.sin(th)], facecolor=PURPLE_FILL, edgecolor='none', zorder=1)
    th = np.radians(np.linspace(135, 180, 30))
    ax.fill(np.r_[0, R*np.cos(th)], np.r_[0, R*np.sin(th)], facecolor=GREEN_FILL, edgecolor='none', zorder=1)
    ax.plot([-1.9, 1.9], [0, 0], color=MUTED, lw=.6, zorder=1); ax.plot([0, 0], [-1.4, 1.6], color=MUTED, lw=.6, zorder=1)
    arrow(ax, (0, 0), (1, 1), color=PURPLE); arrow(ax, (0, 0), (0, -1), color=PURPLE)
    arrow(ax, (0, 0), r, color=BLUE, lw=1.7, z=6)
    ax.text(1.05, 1.02, '$\\nabla g_1$', color=PURPLE, fontsize=8); ax.text(.08, -1.12, '$\\nabla g_3$', color=PURPLE, fontsize=8)
    ax.text(-1.5, .28, '$F$', color=GREEN, fontsize=8)
    dot(ax, (0, 0), INK, ms=4.2)
a, b = axes
a.text(1.55, .72, '$-\\nabla f$', color=BLUE, fontsize=8)
b.text(.08, 1.08, '$-\\nabla f$', color=BLUE, fontsize=8)
arrow(b, (0, 0), (-1, 1), color=RED, lw=1.5, z=6); b.text(-1.05, 1.08, '$d$', color=RED, fontsize=8, ha='right')
tags(fig, axes)
save(fig, HERE, 'figure', {'cone': [[1, 1], [0, -1]], 'a': [1.5, 1], 'b': [0, 1], 'd': [-1, 1]})
