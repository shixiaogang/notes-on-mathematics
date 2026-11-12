from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Capacity C = 0.5 log2(1 + s) of the scalar Gaussian channel against s = P / sigma^2.
# (a) linear axis 0..16, red dots (3, 1) and (15, 2); purple dashed: low-SNR tangent (log2 e / 2) s.
# (b) s in dB from -10 to 30; purple dotted: high-SNR asymptote 0.5 log2 s, 1 bit per 6.02 dB.
fig, axs = figure(width_mm=110, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.3, wspace=.28)
ax = axs[0]
s = np.linspace(0, 16, 800)
ax.plot(s, LOG2E/2*s, color=PURPLE, lw=1.0, ls=DASH)
ax.plot(s, cap(s), color=BLUE, lw=1.4)
for x in (3, 15):
    dot(ax, x, float(cap(x)))
ax.set_xlim(0, 16); ax.set_ylim(0, 2.4); ax.set_xticks([0, 3, 7, 15]); ax.set_yticks([0, 1, 2])
ax.set_xlabel(r'$P/\sigma^2$', labelpad=1); ax.set_ylabel('bit/次', labelpad=2)
lab(ax, 3.5, .78, r'$(3,1)$', RED); lab(ax, 12.0, 2.1, r'$(15,2)$', RED)
lab(ax, 3.4, 1.55, r'$\frac{\log_2\mathrm{e}}{2}\cdot\frac{P}{\sigma^2}$', PURPLE)
ax = axs[1]
db = np.linspace(-10, 30, 800); s = 10**(db/10)
ax.plot(db, .5*np.log2(s), color=PURPLE, lw=1.0, ls=DOT)
ax.plot(db, cap(s), color=BLUE, lw=1.4)
dot(ax, 10*math.log10(3), 1.0)
ax.set_xlim(-10, 30); ax.set_ylim(0, 5.2); ax.set_xticks([-10, 0, 10, 20, 30]); ax.set_yticks([0, 1, 2, 3, 4, 5])
ax.set_xlabel(r'$10\log_{10}(P/\sigma^2)$ (dB)', labelpad=1)
lab(ax, 17.5, 1.3, r'$\frac{1}{2}\log_2\frac{P}{\sigma^2}$', PURPLE)
tags(fig, axs)
save(fig, HERE, 'figure', {'C(3)': 1.0, 'C(15)': 2.0, 'slope_bits_per_dB': 1/(20*math.log10(2))})
