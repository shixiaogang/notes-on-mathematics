from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Isotropic pair: min f2 s.t. f1<=tau. (a) tau=1/4, tangent slope -lambda=-1. (b) multiplier lambda(tau)=(1-sqrt tau)/sqrt tau.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .2, .24)
ax = axes[0]; setup(ax, (0, 1.2), (0, 1.2), [0, .25, .5, 1], [0, .25, .5, 1], equal=True); iso_fill(ax, 1.2)
ax.fill([.25, 1.2, 1.2, .25], [0, 0, 1.2, 1.2], color='white', lw=0, zorder=1.1)
u, v = iso_front(); ax.plot(u, v, color=BLUE, lw=1.2, zorder=3)
m = u <= .25; ax.plot(u[m], v[m], color=RED, lw=2, zorder=4)
ax.plot([.25, .25], [0, 1.2], color=EDGE, lw=2, zorder=4)
t = np.array([0, .62]); ax.plot(t, .5-t, color=PURPLE, lw=1.1, zorder=5); dot(ax, (.25, .25))
ax.text(.29, .98, r'$f_1\leq\tau$', color=INK, fontsize=8, ha='left')
ax.text(.41, .15, r'斜率$-\lambda=-1$', color=PURPLE, fontsize=7.5) if 0 else ax.text(.47, .12, '斜率 -1', color=PURPLE, fontsize=7.5)
ax = axes[1]; setup(ax, (0, 1.05), (0, 5), [0, .25, .5, 1], [0, 1, 2, 3, 4, 5], r'$\tau$', r'$\lambda$')
t = np.linspace(.025, 1, 400); ax.plot(t, (1-np.sqrt(t))/np.sqrt(t), color=PURPLE, lw=1.4)
dot(ax, (.25, 1), PURPLE); ax.text(.28, 1.1, r'$(1/4,1)$', color=INK, fontsize=7.5)
tags(fig, axes)
save(fig, HERE, 'figure', {'lambda': '(1-sqrt(tau))/sqrt(tau)', 'tau': .25})
