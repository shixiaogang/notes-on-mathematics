from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# 从原点到直线 y=2-x 的最短曲线；终点 (b,2-b)，b=1 最优。
fig, ax = figure(width_mm=78, height_mm=62)
panel(fig, left=.11, right=.97, top=.97, bottom=.15)
ax.plot([-.1, 2.3], [2.1, -.3], color=STROKE, lw=2.0)
for b in (.35, 1.7):
    ax.plot([0, b], [0, 2-b], color=YELLOW, lw=1.2)
xx = np.linspace(0, 1, 100)
ax.plot(xx, xx+.5*np.sin(np.pi*xx)*(1-xx)*.8, color=BLUE, lw=1.2)
ax.plot([0, 1], [0, 1], color=GREEN, lw=1.5)
dot(ax, 0, 0, STROKE); dot(ax, 1, 1, RED)
# 直角记号
e = .1; t = np.array([1, 1])/np.sqrt(2); n = np.array([1, -1])/np.sqrt(2); p0 = np.array([1., 1.])
pts = np.array([p0-e*t, p0-e*t+e*n, p0+e*n])
ax.plot(pts[:, 0], pts[:, 1], color=STROKE, lw=.85)
ax.text(1.5, .78, '$y=\\psi(x)=2-x$', fontsize=7.5, color=STROKE)
ax.text(.68, .47, '$y=x$', fontsize=7.5, color=GREEN)
ax.set_aspect('equal'); ax.set_xlim(-.1, 2.45); ax.set_ylim(-.2, 2.1); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$x$', labelpad=0); ax.set_ylabel('$y$', labelpad=0)
save(fig, HERE, 'figure', {'line': 'y=2-x', 'optimal': 'y=x to (1,1)', 'len': 2**.5, 'other_len': [float(np.hypot(b, 2-b)) for b in (.35, 1.7)]})
