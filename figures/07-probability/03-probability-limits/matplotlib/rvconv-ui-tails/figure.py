from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Uniform tail contribution t(M) = sup_n E[|X_n| 1{|X_n| > M}] for the running examples on U ~ Unif(0,1):
#   Y_n = n 1{U<1/n}:       E[Y_n; Y_n > M] = 1 for n > M, so t(M) = 1 (blue).
#   Z_n = sqrt(n) 1{U<1/n}: E[Z_n; Z_n > M] = 1/sqrt(n) for n > M^2, so t(M) = 1/sqrt(floor(M^2)+1) (yellow).
#   second-moment bound sup_n E Z_n^2 / M = 1/M (purple dashed); M_n in [0,1]: t(M) = 0 for M >= 1 (green).
fig, ax = figure(width_mm=86, height_mm=48)
fig.set_layout_engine(None); fig.subplots_adjust(left=.13, right=.97, top=.95, bottom=.2)
style(ax)
M = np.linspace(.01, 10, 4000)
ax.plot(M, np.ones_like(M), color=BLUE, lw=1.4)
tz = 1/np.sqrt(np.floor(M**2) + 1)
ax.plot(M, tz, color=YELLOW, lw=1.4, drawstyle='steps-post')
ax.plot(M[M > .9], 1/M[M > .9], color=PURPLE, lw=1.1, ls=DASH)
ax.plot([0, 1], [1, 1], color=GREEN, lw=0)
ax.plot([1, 10], [0, 0], color=GREEN, lw=1.6, clip_on=False, zorder=6)
lab(ax, 9.8, 1.03, r'$Y_n$', BLUE, ha='right', va='bottom')
lab(ax, 6.2, .07, r'$Z_n$', YELLOW, ha='center', va='bottom')
lab(ax, 3.2, 1/3.2 + .03, r'$1/M$', PURPLE, ha='left', va='bottom')
lab(ax, 9.8, .02, r'$M_n$', GREEN, ha='right', va='bottom')
ax.set_xlim(0, 10); ax.set_ylim(0, 1.2)
axlab(ax, '$M$', r'$\mathrm{sup}_n\,\mathrm{E}[\,|X_n|;\,|X_n|>M\,]$')
save(fig, HERE, 'figure', {'Z_tail_M3': float(1/np.sqrt(10)), 'Y_tail': 1.0})
