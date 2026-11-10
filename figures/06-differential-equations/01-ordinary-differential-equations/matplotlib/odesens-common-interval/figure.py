from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=x^2 的邻近解在 [0,1] 上是否存在；管道半径 0.5。解析解 x=x0/(1-x0 t)。
fig, ax = figure(width_mm=90, height_mm=52)
panel(fig, .085, .985, .96, .15)
t = np.linspace(0, 1.45, 1201)
xbar = .5/(1-.5*t)
tt = t[t <= 1]; xb = .5/(1-.5*tt)
ax.fill_between(tt, xb-.5, xb+.5, color=BLUE_FILL, lw=0)
ax.plot(tt, xb-.5, color=BLUE, lw=.85); ax.plot(tt, xb+.5, color=BLUE, lw=.85)
def curve(x0, col, lw=1.4):
    tend = min(1.45, (1/x0-1e-4) if x0 > 0 else 1.45); s = np.linspace(0, tend, 1500); v = x0/(1-x0*s); m = v <= 3.6
    ax.plot(s[m], v[m], color=col, lw=lw)
    return tend
curve(.5, BLUE, 1.6); curve(.62, YELLOW); curve(.8, YELLOW); curve(1.25, RED)
ax.vlines(1, 0, 3.6, color=STROKE, lw=.95, ls=(0, (3, 2)))
ax.vlines(.8, 0, 3.6, color=RED, lw=.85, ls=':')
ax.plot([0], [.5], 'o', ms=4.4, color=RED, mew=0, zorder=5, clip_on=False)
ax.text(1.02, 3.3, '$T=1$', color=STROKE, fontsize=7.5); ax.text(.2, 3.28, '$x_0=1.25$', color=RED, fontsize=7.5)
ax.text(1.42, .95, '$x_0=0.5$', color=BLUE, fontsize=7.5, ha='right'); ax.text(1.05, 2.95, '$x_0=0.8$', color=YELLOW, fontsize=7.5, ha='left')
ax.text(1.3, 2.2, '$x_0=0.62$', color=YELLOW, fontsize=7.5, ha='left')
ax.set_xlim(0, 1.45); ax.set_ylim(0, 3.6); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1, 2, 3]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$x$', labelpad=1)
save(fig, HERE, 'figure', {'equation': "x'=x^2", 'tube': .5, 'T': 1, 'x0': [.5, .62, .8, 1.25]})
