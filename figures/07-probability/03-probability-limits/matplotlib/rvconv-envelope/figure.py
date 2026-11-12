from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Envelopes of the rare-large-value families on U ~ Unif(0,1):
#   sup_n Y_n = sup_n n 1{U < 1/n} = ceil(1/U) - 1 =: N,  sup_n Z_n = sup_n sqrt(n) 1{U < 1/n} = sqrt(N).
# (a) the two envelopes as functions of U (blue: sup Y_n, yellow: sup Z_n).
# (b) partial integrals int_delta^1 envelope dU as delta -> 0: first ~ ln(1/delta) -> infinity, second -> E sqrt(N) = sum 1/(sqrt(n)(n+1)).
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.3)
ax = axes[0]; style(ax)
u = np.linspace(2e-3, 1, 40000, endpoint=False)
N = np.ceil(1/u) - 1
ax.plot(u, N, color=BLUE, lw=1.2, drawstyle='steps-post')
ax.plot(u, np.sqrt(N), color=YELLOW, lw=1.4, drawstyle='steps-post')
lab(ax, .13, 9.5, r'$\mathrm{sup}_n\,Y_n$', BLUE, ha='left')
lab(ax, .3, 3.0, r'$\mathrm{sup}_n\,Z_n$', YELLOW, ha='left')
ax.set_xlim(0, 1); ax.set_ylim(0, 20); ax.set_xticks([0, .5, 1])
axlab(ax, '$U$', None)
ax = axes[1]; style(ax)
# exact partial integrals: on [1/(n+1), 1/n) the envelope N equals n
nmax = 10**6
nn = np.arange(1, nmax + 1); w = 1/nn - 1/(nn + 1)
cY = np.cumsum(nn*w); cZ = np.cumsum(np.sqrt(nn)*w)
delta = 1/(nn + 1)
ax.semilogx(delta, cY, color=BLUE, lw=1.4)
ax.semilogx(delta, cZ, color=YELLOW, lw=1.4)
EZ = float(cZ[-1] + 2/np.sqrt(nmax))
ax.axhline(EZ, color=PURPLE, lw=.85, ls=DASH)
lab(ax, 1e-3, 8.2, r'$\mathrm{sup}_n\,Y_n$', BLUE, ha='right', va='bottom')
lab(ax, 1e-3, 1.1, r'$\mathrm{sup}_n\,Z_n$', YELLOW, ha='center', va='top')
lab(ax, 3e-5, EZ + .25, r'$%.2f$' % EZ, PURPLE, ha='center', va='bottom')
ax.set_xlim(1e-6, 1); ax.set_ylim(0, 15); ax.set_yticks([0, 5, 10, 15]); ax.invert_xaxis()
logticks(ax, [-6, -4, -2, 0], axis='x')
axlab(ax, r'$\delta$', None)
tags(fig, axes)
save(fig, HERE, 'figure', {'E_sup_Z': EZ, 'partial_Y_at_1e-6': float(cY[-1])})
