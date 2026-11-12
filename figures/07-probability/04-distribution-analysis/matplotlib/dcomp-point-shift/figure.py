from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# P=delta_0, Q=delta_h on the real line.
# (a) the two unit masses and the shift by h (drawn for h=1.2).
# (b) as functions of h>0: d_TV = d_H = 1 (purple), W_p = h (blue), MMD with Gaussian kernel sigma=1:
#     sqrt(2-2exp(-h^2/2)) (yellow). KL is +infinity for every h>0.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2, gridspec_kw={'width_ratios': [1, 1.5]})
panel(fig, left=.06, right=.98, top=.95, bottom=.27, wspace=.25)
ax = axs[0]
h = 1.2
ax.plot([0, 0], [0, 1], color=BLUE, lw=1.6); dot(ax, 0, 1, BLUE, ms=4.4)
ax.plot([h, h], [0, 1], color=YELLOW, lw=1.8); dot(ax, h, 1, YELLOW, ms=4.4)
ax.annotate('', xy=(h-.05, .55), xytext=(.05, .55), arrowprops=dict(arrowstyle='-|>', color=STROKE, lw=.9, mutation_scale=7))
lab(ax, h/2, .6, '$h$', INK, ha='center')
lab(ax, 0, 1.08, r'$\delta_0$', BLUE, ha='center', fontsize=8)
lab(ax, h, 1.08, r'$\delta_h$', YELLOW, ha='center', fontsize=8)
ax.axhline(0, color=STROKE, lw=.85)
ax.set_xlim(-.6, h+.6); ax.set_ylim(0, 1.25); ax.set_xticks([0, h]); ax.set_xticklabels(['0', '$h$']); ax.set_yticks([])
ax.spines['left'].set_visible(False)
axlab(ax, '$x$', None)
ax = axs[1]
hs = np.linspace(0, 3, 400)
ax.plot(hs, hs, color=BLUE, lw=1.4)
ax.plot(hs[1:], np.ones_like(hs[1:]), color=PURPLE, lw=1.4)
dot(ax, 0, 0, PURPLE, ms=3.6)
ax.plot([0], [1], 'o', ms=3.6, mfc='white', mec=PURPLE, mew=.9, clip_on=False, zorder=7)
ax.plot(hs, np.sqrt(2-2*np.exp(-hs**2/2)), color=YELLOW, lw=1.6)
lab(ax, 2.35, 2.5, '$W_p$', BLUE, ha='center')
lab(ax, 2.9, 1.07, r'$d_{\mathrm{TV}}=d_{\mathrm{H}}$', PURPLE, ha='right')
lab(ax, 2.9, 1.5, 'MMD', YELLOW, ha='right')
ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1, 2, 3])
axlab(ax, '$h$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'mmd(h=1)': math.sqrt(2-2*math.exp(-.5)), 'mmd(h=3)': math.sqrt(2-2*math.exp(-4.5))})
