from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Z_n = sqrt(n) 1{U < 1/n} on U ~ Unif(0,1).
# (a) Z_n as a function of U for n = 4, 16, 64 (heights 2, 4, 8; widths 1/4, 1/16, 1/64).
# (b) exact moments E|Z_n|^p = n^{p/2 - 1} for p = 1, 2, 3 and P(|Z_n| > eps) = 1/n (eps < 1), log-log axes.
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.08, wspace=.3, bottom=.29)
ax = axes[0]; style(ax)
for n, c in ((4, BLUE), (16, YELLOW), (64, PURPLE)):
    h = np.sqrt(n); w = 1/n
    ax.plot([0, 0, w, w, .6], [0, h, h, 0, 0], color=c, lw=1.3)
    lab(ax, w + .012, h, r'$n=%d$' % n, c, va='center')
ax.set_xlim(0, .6); ax.set_ylim(0, 9); ax.set_xticks([0, 1/64, 1/16, 1/4, .5]); ax.set_xticklabels(['$0$', '', '', r'$\frac{1}{4}$', r'$\frac{1}{2}$'])
axlab(ax, '$U$', r'$Z_n$')
ax = axes[1]; style(ax)
n = np.logspace(0, 3, 200)
for p, c in ((1, BLUE), (2, YELLOW), (3, PURPLE)):
    ax.loglog(n, n**(p/2 - 1), color=c, lw=1.4)
ax.loglog(n, 1/n, color=GREEN, lw=1.2, ls=DASH)
lab(ax, 300, 300**(-.5)*1.5, '$p=1$', BLUE, ha='center', va='bottom')
lab(ax, 300, 1.25, '$p=2$', YELLOW, ha='center', va='bottom')
lab(ax, 60, 60**.5*1.3, '$p=3$', PURPLE, ha='right', va='bottom')
lab(ax, 40, 1/40*.7, 'ℙ$(Z_n>\\varepsilon)$', GREEN, ha='right', va='top')
ax.set_xlim(1, 1000); ax.set_ylim(1e-3, 60); logticks(ax, [0, 1, 2, 3], axis='x'); logticks(ax, [-3, -2, -1, 0, 1])
axlab(ax, '$n$', r'$\mathrm{E}|Z_n|^p$')
tags(fig, axes)
save(fig, HERE, 'figure', {'E_Z_n^p': 'n^(p/2-1)', 'n=16': {'p1': 16**-.5, 'p2': 1.0, 'p3': 16**.5}})
