from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：logistic，x0=1/4，T=ln3：一阶预测 1/2+(4/3)v 与余项的二阶衰减，以及余项界 6v^2。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .08, .985, .96, .26, .26)
T = np.log(3); x0 = .25; phi = lambda y: logistic(T, y)
ax = axes[0]; y = np.linspace(.02, .7, 400); ax.plot(y, phi(y), color=BLUE, lw=1.4); ax.plot(y, .5+4/3*(y-x0), color=GREEN, lw=1.4, ls=(0, (4, 2)))
ax.plot([x0], [.5], 'o', ms=4.4, color=RED, mew=0, zorder=5)
ax.text(.5, .62, '$\\varphi_T(y_0)$', color=BLUE, fontsize=7.5, va='top', ha='left'); ax.text(.46, .95, '一阶预测', color=GREEN, fontsize=7.5, ha='right')
ax.set_xlim(0, .7); ax.set_ylim(0, 1.2); ax.set_xticks([0, .25, .5]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$y_0$', labelpad=0)
ax = axes[1]; v = np.logspace(-3, np.log10(.2), 40); R = np.abs(phi(x0+v)-.5-4/3*v)
ax.loglog(v, R, 'o', ms=2.6, color=BLUE, mew=0); ax.loglog(v, 6*v**2, color=RED, lw=1.4); ax.loglog(v, R[0]/v[0]**2*v**2, color=PURPLE, lw=.85, ls=(0, (3, 2)))
ax.text(.012, 3e-3, '$6v^2$', color=RED, fontsize=7.5, ha='right'); ax.text(.035, 8e-5, '斜率 2', color=PURPLE, fontsize=7.5, ha='left')
ax.set_xlim(8e-4, .3); ax.set_xlabel('$v$', labelpad=0); ax.set_ylabel('$|R|$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'x0': x0, 'T': 'ln 3', 'S': 4/3, 'R(+.1)': float(phi(.35)-.5-4/3*.1), 'R(-.1)': float(phi(.15)-.5+4/3*.1)})
