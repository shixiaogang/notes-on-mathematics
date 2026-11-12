from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
# McMillan counting argument. For lengths l_1..l_m put K = sum 2^{-l_i}. Concatenating k codewords,
# K^k = sum_{s=k}^{k l_max} N_s 2^{-s} <= k(l_max-1)+1 whenever the code is uniquely decodable (N_s <= 2^s).
# Blue: lengths (1,2,3,3), K = 1. Red: lengths (1,1,2), K = 1.25, violates the bound from k = 12 on.
# Purple: the bound k(l_max-1)+1 for l_max = 2 and 3.
k = np.arange(1, 31)
fig, ax = figure(width_mm=92, height_mm=52)
panel(fig, left=.12, right=.97, bottom=.2, top=.95)
ax.plot(k, k*(3-1)+1, color=PURPLE, lw=1.1, ls=DASH)
ax.plot(k, k*(2-1)+1, color=PURPLE, lw=1.4)
ax.plot(k, np.ones_like(k, dtype=float), color=BLUE, lw=1.4)
ax.plot(k, 1.25**k, color=RED, lw=1.4)
kc = int(k[np.argmax(1.25**k > k+1)])
dot(ax, kc, 1.25**kc)
ax.set_yscale('log'); ax.set_xlim(1, 30); ax.set_ylim(.7, 1000)
ax.minorticks_off(); ax.set_yticks([1, 10, 100, 1000]); ax.set_yticklabels(['$1$', '$10$', '$10^{2}$', '$10^{3}$'])
lab(ax, 25, 1.25**25*1.25, r'$1.25^{k}$', RED, ha='right')
lab(ax, 29.5, 31*.55, r'$k+1$', PURPLE, ha='right', va='top')
lab(ax, 29.5, 61*1.2, r'$2k+1$', PURPLE, ha='right')
lab(ax, 29.5, 1.15, r'$K=1$', BLUE, ha='right')
lab(ax, kc+.8, 1.25**kc*.62, r'$k=%d$' % kc, RED)
ax.set_xlabel('$k$', labelpad=1)
save(fig, HERE, 'figure', {'crossing_k_lmax2': kc, 'K_bad': 1.25})
