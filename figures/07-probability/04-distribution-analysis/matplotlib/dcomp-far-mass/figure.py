from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# Small mass far away, compared with delta_0.
# (a) P_n=(1-1/n)delta_0+(1/n)delta_n: d_TV=1/n (purple), MMD (sigma=1) = sqrt(2-2e^{-n^2/2})/n (yellow),
#     W_1 = 1 = mean (blue), second moment n (red dashed); log-log, n=1..100.
# (b) R_n=(1-1/n^2)delta_0+(1/n^2)delta_n: W_1=1/n (blue), W_2=1 (yellow).
n = np.arange(1, 101).astype(float)
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.26, wspace=.3)
ax = axs[0]
ax.loglog(n, 1/n, color=PURPLE, lw=1.4)
ax.loglog(n, np.sqrt(2-2*np.exp(-n**2/2))/n, color=YELLOW, lw=1.6)
ax.loglog(n, np.ones_like(n), color=BLUE, lw=1.4)
ax.loglog(n, n, color=RED, lw=1.2, ls=DASH)
lab(ax, 2.2, .2, r'$d_{\mathrm{TV}}$', PURPLE, ha='left', va='top')
lab(ax, 9, .2, 'MMD', YELLOW, ha='left')
lab(ax, 30, 1.25, r'$W_1$', BLUE, ha='center')
lab(ax, 22, 40, '二阶矩', RED, ha='right')
ax.set_xlim(1, 100); ax.set_ylim(.008, 150)
ax.minorticks_off(); ax.set_xticks([1, 10, 100]); ax.set_xticklabels(['$1$', '$10$', '$100$'])
ax.set_yticks([.01, .1, 1, 10, 100]); ax.set_yticklabels(['$10^{-2}$', '$10^{-1}$', '$1$', '$10$', '$10^{2}$'])
axlab(ax, '$n$', None)
ax = axs[1]
ax.loglog(n, 1/n, color=BLUE, lw=1.4)
ax.loglog(n, np.ones_like(n), color=YELLOW, lw=1.6)
lab(ax, 3, .2, r'$W_1=1/n$', BLUE, ha='left')
lab(ax, 30, 1.25, r'$W_2=1$', YELLOW, ha='center')
ax.set_xlim(1, 100); ax.set_ylim(.008, 3)
ax.minorticks_off(); ax.set_xticks([1, 10, 100]); ax.set_xticklabels(['$1$', '$10$', '$100$'])
ax.set_yticks([.01, .1, 1]); ax.set_yticklabels(['$10^{-2}$', '$10^{-1}$', '$1$'])
axlab(ax, '$n$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'n=10': {'tv': .1, 'mmd': math.sqrt(2-2*math.exp(-50))/10, 'W1': 1}})
