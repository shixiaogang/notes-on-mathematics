from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# E(u)=int (u'^2+u^2)/2，u=x，eta=x(1-x)：phi(t)=2/3+t/12+11 t^2/60。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.27, bottom=.27)
eta = X*(1-X)
ax = axes[0]
for t in (-1, 1):
    ax.plot(X, X+t*eta, color=YELLOW, lw=1.1)
ax.plot(X, X, color=STROKE, lw=1.4)
ax.plot(X, X-5/22*eta, color=GREEN, lw=1.4)
ax.plot([0, 1], [0, 1], 'o', ms=4.4, color=STROKE, mew=0, zorder=6)
ax.text(.28, .6, '$t=1$', color=YELLOW, fontsize=7.5, ha='right'); ax.text(.72, .4, '$t=-1$', color=YELLOW, fontsize=7.5); ax.text(.5, .59, '$t=0$', color=STROKE, fontsize=7.5, ha='right')
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.06, 1.12); ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel(r'$x+t\eta$', labelpad=-2)
phi = lambda t: 2/3+t/12+11*t**2/60
t = np.linspace(-1.05, 1.05, 300)
ax = axes[1]
ax.plot(t, phi(t), color=BLUE, lw=1.4)
ax.plot(t, 2/3+t/12, color=PURPLE, lw=1.1, ls=(0, (4, 2)))
dot(ax, 0, 2/3, STROKE); dot(ax, -5/22, phi(-5/22), GREEN)
ax.text(1.03, .695, '斜率 1/12', color=PURPLE, fontsize=7.5, ha='right', va='top')
ax.text(-5/22, .625, r'$t=-\frac{5}{22}$', color=GREEN, fontsize=7.5, ha='center', va='top')
ax.set_xlim(-1.05, 1.05); ax.set_ylim(.57, .96); ax.set_xticks([-1, 0, 1]); ax.set_yticks([.6, .8]); ax.set_yticklabels(['0.6', '0.8']); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel(r'$\phi(t)=E(x+t\eta)$', labelpad=0)
tags(fig, axes)
Xm = (X[1:]+X[:-1])/2; d = X[1]-X[0]
num = [float(d*np.sum(.5*(1+t_*(1-2*Xm))**2+.5*(Xm+t_*Xm*(1-Xm))**2)) for t_ in (0, 1)]
save(fig, HERE, 'figure', {'phi': '2/3+t/12+11t^2/60', 'check_quad_at_0_1': num, 'exact_0_1': [2/3, phi(1)]})
