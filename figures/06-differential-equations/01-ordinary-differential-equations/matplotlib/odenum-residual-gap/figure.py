from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: same residual, opposite amplification: x'=+-5(x-cos t)-sin t, constant residual 1e-3.
r = 1e-3
t = np.linspace(0, 2, 400)
fig, ax = figure(width_mm=112, height_mm=52, ncols=2)
pert = np.cos(t)+r/5*(np.exp(5*t)-1)
ax[0].plot(t, np.cos(t), color=BLUE, lw=1.4)
ax[0].plot(t, pert, color=GREEN, lw=1.4)
ax[0].plot([0], [1], 'o', color=RED, ms=4.5, zorder=5)
ax[0].set_xlabel(r'$t$'); ax[0].set_ylabel(r'$x$')
ax[0].set_ylim(-1, 4.3)
ax[0].text(1.05, -.62, r'$\cos t$', color=BLUE)
ax[0].text(1.1, 2.6, '残差恒定的\n近似函数', color=GREEN, ha='center')
grow = r/5*(np.exp(5*t)-1); dec = r/5*(1-np.exp(-5*t))
ax[1].semilogy(t[1:], grow[1:], color=RED, lw=1.4)
ax[1].semilogy(t[1:], dec[1:], color=YELLOW, lw=1.4)
ax[1].semilogy(t, r+0*t, color=PURPLE, lw=.95, ls=(0, (4, 2)))
ax[1].set_xlabel(r'$t$'); ax[1].set_ylabel('绝对误差')
ax[1].set_ylim(1e-5, 30)
ax[1].text(1.34, 3e-1, r'$\sigma=5$', color=RED, ha='right')
ax[1].text(1.3, 5.3e-5, r'$\sigma=-5$', color=YELLOW)
ax[1].text(1.5, 1.6e-3, '残差', color=PURPLE)
panel(ax[0], '(a)', -.3); panel(ax[1], '(b)', -.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'x=sigma*(x-cos t)-sin t+r', 'r': r, 'final_error': float(grow[-1])})
