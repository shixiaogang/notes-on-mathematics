from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
from types_exact import types, class_prob
# Fixed-length block code with M = floor(2^{nR}) codewords that represents the M most probable blocks of
# p = (0.4,0.3,0.2,0.1) (this choice minimizes the error probability for given M). Exact error probability
# 1 - P(top M blocks) against n via type classes, for R = 1.95 > H (blue) and R = 1.75 < H (yellow); H = 1.846.
def err(n, R):
    K, lc, si = types(n); o = np.argsort(si, kind='stable'); lc, si = lc[o], si[o]
    cnt = np.exp2(lc); M = np.floor(2.0**(n*R)); cum = np.cumsum(cnt)
    j = np.searchsorted(cum, M, side='right')
    full = (np.exp2(lc[:j]-si[:j])).sum()
    rest = M - (cum[j-1] if j > 0 else 0)
    part = rest*np.exp2(-si[j]) if j < len(si) else 0
    return float(max(0., 1-full-part))
ns = np.arange(4, 251, 4)
E1 = np.array([err(n, 1.95) for n in ns]); E2 = np.array([err(n, 1.75) for n in ns])
fig, ax = figure(width_mm=96, height_mm=52)
panel(fig, left=.13, right=.97, bottom=.2, top=.95)
ax.plot(ns, E2, color=YELLOW, lw=1.5)
ax.plot(ns, E1, color=BLUE, lw=1.4)
ax.set_yscale('log'); ax.set_xlim(0, 250); ax.set_ylim(1e-5, 2)
ax.minorticks_off(); ax.set_yticks([1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]); ax.set_yticklabels(['$10^{-5}$', '$10^{-4}$', '$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$1$'])
lab(ax, 160, .35, r'$R=1.75<H$', YELLOW); lab(ax, 120, 2e-3, r'$R=1.95>H$', BLUE)
ax.set_xlabel('$n$', labelpad=1); ax.set_ylabel('错误概率', labelpad=1)
save(fig, HERE, 'figure', {'H': H, 'err_R195': dict(zip(map(int, ns[::8]), map(float, E1[::8]))),
     'err_R175': dict(zip(map(int, ns[::8]), map(float, E2[::8])))})
