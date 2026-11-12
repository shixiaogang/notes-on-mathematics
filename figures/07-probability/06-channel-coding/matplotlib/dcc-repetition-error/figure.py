from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Repetition codes of odd length n over BSC(p=0.1) with majority decoding.
# (a) exact block error P(at least (n+1)/2 flips) versus n (log scale);  (b) the same codes in the rate-error plane,
# rate 1/n, with the BSC capacity C = 1 - h2(0.1) = 0.531 as a vertical dashed line.
p = BSC_P; C = 1-float(h2(p))
ns = np.arange(1, 22, 2)
pe = np.array([binpmf(n, p)[(n+1)//2:].sum() for n in ns])
fig, axs = figure(width_mm=110, height_mm=50, ncols=2)
panel(fig, left=.1, right=.97, top=.95, bottom=.27, wspace=.36)
ax = axs[0]
ax.plot(ns, pe, color=BLUE, lw=1.1); ax.plot(ns, pe, 'o', ms=3, color=BLUE, mew=0)
dot(ax, 3, pe[1]); lab(ax, 4, pe[1]*1.5, r'$0.028$', RED)
ax.set_yscale('log'); logticks(ax, [-8, -6, -4, -2, 0]); ax.set_ylim(1e-8, 1.5)
ax.set_xticks([1, 5, 9, 13, 17, 21]); ax.set_xlabel(r'$n$', labelpad=1); ax.set_ylabel('块错误概率', labelpad=1)
ax = axs[1]
ax.plot(1/ns, pe, 'o', ms=3, color=BLUE, mew=0)
ax.axvline(C, color=PURPLE, lw=1.1, ls=DASH)
lab(ax, C+.03, 2e-6, r'$C\approx0.531$', PURPLE)
for n, e in zip(ns[:3], pe[:3]): lab(ax, 1/n+.04, e*0.5, r'$n=%d$' % n, MUTED)
ax.set_yscale('log'); logticks(ax, [-8, -6, -4, -2, 0]); ax.set_ylim(1e-8, 1.5); ax.set_xlim(0, 1.2)
ax.set_xticks([0, .5, 1]); ax.set_xlabel(r'$R=1/n$', labelpad=1)
tags(fig, axs)
save(fig, HERE, 'figure', {'p': p, 'capacity': C, 'pe': dict(zip(map(int, ns), map(float, pe)))})
