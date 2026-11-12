from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Gaussian AR(1) chain with rho = 0.9: K^t(x, .) = N(rho^t x, 1 - rho^{2t}), target N(0,1).
# Total variation d_TV(K^t(x,.), N(0,1)) = (1/2) int |p - q|, by numerical quadrature on a fine grid,
# for starting points x = 0, 3, 10 (green solid, dashed, dotted); reference 0.01*0.9^t (purple dashed), log y-axis.
rho = 0.9; g = np.linspace(-14, 24, 40001); dg = g[1]-g[0]; q = npdf(g)
t = np.arange(1, 121); out = {}
fig, ax = figure(width_mm=96, height_mm=50)
panel(fig, left=.12, right=.8, bottom=.2, top=.95)
for x0, ls in [(0, '-'), (3, DASH), (10, DOT)]:
    tv = np.array([.5*np.sum(np.abs(npdf(g, rho**k*x0, 1-rho**(2*k)) - q))*dg for k in t])
    ax.semilogy(t, tv, color=GREEN, lw=1.2, ls=ls); out[x0] = tv[[0, 9, 29, 59]].tolist()
ax.semilogy(t, .01*rho**t, color=PURPLE, lw=.9, ls=(0, (6, 3))); lab(ax, 122, .01*rho**120, r'$0.01\times0.9^{t}$', PURPLE, va='center')
lab(ax, 72, 1e-7, '$x=0$', GREEN, va='center'); lab(ax, 122, 3.5e-6, '$x=3$', GREEN, va='center'); lab(ax, 122, 1.6e-5, '$x=10$', GREEN, va='center')
ax.set_xlim(0, 120); ax.set_ylim(1e-8, 2); ax.set_xticks([0, 40, 80, 120]); logticks(ax, [-8, -6, -4, -2, 0], 'y'); axlab(ax, '$t$')
save(fig, HERE, 'figure', {'tv_at_t_1_10_30_60': out})
