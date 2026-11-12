from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Feasible (skewness, kurtosis) pairs satisfy kappa >= 1 + gamma^2; two-point laws lie on the boundary.
fig, ax = figure(width_mm=90, height_mm=56)
panel(fig, left=.13, right=.97, bottom=.17, top=.97)
g = np.linspace(-2.2, 2.2, 400)
ax.fill_between(g, 1+g**2, 6.5, color=BLUE_FILL, lw=0)
ax.plot(g, 1+g**2, color=BLUE, lw=1.4)
pts = {
    '奖金表': moments(XV, PV)[2:],
    '密度 2x': (-2*np.sqrt(2)/5, 12/5),
    '$\\{-5,-1,4\\}$': moments([-5, -1, 4], [1/6, 1/2, 1/3])[2:],
    '对称三点': (0., 12/5),
}
off = {'奖金表': (.12, -.05, 'left'), '密度 2x': (-.12, .1, 'right'), '$\\{-5,-1,4\\}$': (.1, -.35, 'left'), '对称三点': (.1, .12, 'left')}
for name, (gg, kk) in pts.items():
    dot(ax, gg, kk, color=RED, ms=4.4)
    dx, dy, ha = off[name]
    ax.text(gg+dx, kk+dy, name, color=INK, fontsize=7.5, ha=ha, va='bottom')
for p in (1/6, 1/2, 5/6):
    gg = (1-2*p)/np.sqrt(p*(1-p)); dot(ax, gg, 1+gg**2, color=BLUE, ms=3.6)
lab(ax, 1.95, 5.5, '两点分布', BLUE, ha='right', va='top')
ax.set_xlim(-2.2, 2.2); ax.set_ylim(0, 6.5); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([0, 1, 3, 5])
axlab(ax, '偏度', '峰度')
save(fig, HERE, 'figure', {k: [float(v[0]), float(v[1])] for k, v in pts.items()})
