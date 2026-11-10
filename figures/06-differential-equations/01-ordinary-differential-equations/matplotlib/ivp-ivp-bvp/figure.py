from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：x''+x=0 的初值问题与两点边值问题对比。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .075, .985, .96, .26, .26)
t = np.linspace(0, 3.6, 400)
a, b = axes
for v, c in [(1, BLUE), (.5, YELLOW), (-.7, YELLOW)]:
    a.plot(t, v*np.sin(t), color=c, lw=1.4)
    a.annotate('', xy=(.62, .62*v), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=PURPLE, lw=.9, mutation_scale=7, shrinkA=0, shrinkB=0), zorder=5)
dot(a, 0, 0)
for c_, col in [(1, BLUE), (.5, YELLOW), (-.7, YELLOW)]:
    b.plot(t[t <= np.pi], c_*np.sin(t[t <= np.pi]), color=col, lw=1.4)
dot(b, 0, 0); dot(b, np.pi, 0); hollow(b, np.pi, 1.2)
b.text(np.pi - .1, 1.22, '$x(\\pi)=1.2$', ha='right', va='center', fontsize=7.5, color=INK)
for ax in axes:
    ax.set_xlim(-.12, 3.72); ax.set_ylim(-1.05, 1.45); ax.axhline(0, color=GRID, lw=.65, zorder=0)
    ax.set_xticks([0, np.pi/2, np.pi]); ax.set_xticklabels(['0', '$\\pi/2$', '$\\pi$']); ax.set_yticks([-1, 0, 1])
    ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$x$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': "x''+x=0", 'ivp_speeds': [1, .5, -.7], 'bvp_amplitudes': [1, .5, -.7]})
