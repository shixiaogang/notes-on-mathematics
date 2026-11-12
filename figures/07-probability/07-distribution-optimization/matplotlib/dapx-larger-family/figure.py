from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Target pi = 0.7 N(-2,0.6^2)+0.3 N(2,0.6^2), objective D(Q||Pi).
# Single-Gaussian family: global minimum near N(-2,0.6^2); local minimum near N(2,0.6^2) (grid search, s in [0.3,1.2]).
# Two-component Gaussian mixtures with free weight contain pi itself, so their infimum is 0.
# A mixture started with both components identical at the light mode keeps them identical (symmetry),
# so it ends at the single-Gaussian local minimum.
x = np.linspace(-10, 10, 20001); dx = x[1]-x[0]; pi = mix_pdf(x)
def rev(m, s):
    q = npdf(x, m, s); return float(np.sum(q*(np.log(q+1e-300)-np.log(pi)))*dx)
S = np.linspace(.3, 1.2, 181)
def best_s(m0):
    best = (9, None, None)
    for m in np.linspace(m0-.3, m0+.3, 61):
        for s in S:
            v = rev(m, s)
            if v < best[0]: best = (v, m, s)
    return best
g = best_s(-2.); l = best_s(2.)
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.27, wspace=.3)
ax = axs[0]
xx = np.linspace(-4.5, 4.5, 901)
ax.plot(xx, mix_pdf(xx), color=BLUE, lw=1.4)
ax.plot(xx, npdf(xx, g[1], g[2]), color=YELLOW, lw=1.6)
ax.plot(xx, npdf(xx, l[1], l[2]), color=GREEN, lw=1.4, ls=DASH)
lab(ax, 2.6, .5, '卡住', GREEN, fontsize=7); lab(ax, -1.2, .6, '族内最优', YELLOW, fontsize=7)
ax.set_xlim(-4.5, 4.5); ax.set_ylim(0, .72); axlab(ax, '$x$', None)
ax = axs[1]
vals = [g[0], 0.0, l[0]]
cols = [(YELLOW, YELLOW_FILL), (BLUE, BLUE_FILL), (GREEN, GREEN_FILL)]
for i, (v, (c, f)) in enumerate(zip(vals, cols)):
    bars(ax, [i], [v], c, f, width=.5)
    lab(ax, i, v+.04, f'{v:.3f}', INK, ha='center', fontsize=7)
ax.set_xticks([0, 1, 2]); ax.set_xticklabels(['高斯族\n最优', '混合族\n下确界', '混合族\n迭代结果'], fontsize=7)
ax.set_xlim(-.6, 2.6); ax.set_ylim(0, 1.45)
tags(fig, axs)
save(fig, HERE, 'figure', {'single_global': list(map(float, g)), 'single_local_light': list(map(float, l)), 'mixture_inf': 0.0})
