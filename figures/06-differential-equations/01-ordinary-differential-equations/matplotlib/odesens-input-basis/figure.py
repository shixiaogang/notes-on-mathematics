from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=-x+g(t)，g 在 [0,1)、[1,2) 上分别取 theta1=1, theta2=2，x0=0；P_j 的变分方程在开关处有折点。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .07, .985, .955, .28, .26)
ts = np.linspace(0, 2, 2001); th = (1., 2.)
e1 = lambda t: 1. if t < 1 else 0.
e2 = lambda t: 0. if t < 1 else 1.
def F(t, z): return np.array([-z[0]+th[0]*e1(t)+th[1]*e2(t), -z[1]+e1(t), -z[2]+e2(t)])
Z = rk4(F, [0., 0., 0.], ts)
ax = axes[0]; ax.step([0, 1, 2], [1, 2, 2], where='post', color=YELLOW, lw=1.4); ax.plot(ts, Z[:, 0], color=BLUE, lw=1.4)
ax.text(.5, 1.08, '$g$', color=YELLOW, fontsize=7.5, ha='center', va='bottom'); ax.text(.72, .35, '$x$', color=BLUE, fontsize=7.5, ha='left')
ax.set_xlim(0, 2); ax.set_ylim(0, 2.3); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2]); ax.set_xlabel('$t$', labelpad=0)
ax = axes[1]; ax.plot(ts, Z[:, 1], color=GREEN, lw=1.4); ax.plot(ts, Z[:, 2], color=PURPLE, lw=1.4)
ax.vlines(1, 0, .75, color=MUTED, lw=.85, ls=(0, (2, 2)))
ax.plot([2, 2], [Z[-1, 1], Z[-1, 2]], 'o', ms=4.2, color=RED, mew=0, zorder=5, clip_on=False)
ax.text(.75, .3, '$P_1$', color=GREEN, fontsize=7.5, ha='right', va='bottom'); ax.text(1.5, .55, '$P_2$', color=PURPLE, fontsize=7.5, ha='right')
ax.set_xlim(0, 2); ax.set_ylim(0, .75); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .25, .5, .75]); ax.set_xlabel('$t$', labelpad=0)
tags(fig, axes)
print(Z[-1], np.exp(-1)*(1-np.exp(-1)), 1-np.exp(-1))
save(fig, HERE, 'figure', {'theta': th, 'finals': Z[-1].tolist()})
