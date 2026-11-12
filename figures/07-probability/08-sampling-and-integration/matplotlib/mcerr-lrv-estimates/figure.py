from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Stationary Gaussian AR(1), rho = 0.9, f(x) = x, record length N = 2^16; ten independent runs (seed 3130).
# (a) batch-means estimate b/(a-1) sum_j (Ybar_j - hat I)^2 against batch length b = 1, 2, 4, ..., 2^13 (green);
#     long-run variance 19 (blue); gamma_0 = 1 (yellow dashed), which is what b = 1 reproduces.
# (b) truncated autocovariance sums hat gamma_0 + 2 sum_{k<=L} hat gamma_k against L (green), same runs.
rho, N = 0.9, 2**16
X = ar1(np.random.default_rng(3130), rho, N, reps=10)
bs = 2**np.arange(0, 14)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.28)
bm_all = []; tr_all = []
L = np.unique(np.round(np.logspace(0, 3.6, 60)).astype(int))
for x in X:
    I = x.mean(); est = []
    for bb in bs:
        a_ = N//bb; Y = x[:a_*bb].reshape(a_, bb).mean(1); est.append(bb*np.sum((Y-I)**2)/(a_-1))
    a.semilogx(bs, est, color=GREEN, lw=.6, marker='o', ms=1.6); bm_all.append(est)
    y = x - I; F = np.fft.rfft(y, 2*N); acov = np.fft.irfft(F*np.conj(F))[:L.max()+1]/N
    cs = acov[0] + 2*np.cumsum(acov[1:]); tr = np.r_[acov[0], cs][L]
    b.semilogx(L, tr, color=GREEN, lw=.6); tr_all.append(tr)
for ax in (a, b):
    ax.axhline(19, color=BLUE, lw=1.2); ax.axhline(1, color=YELLOW, lw=1.3, ls=DASH)
    ax.set_ylim(0, 30); ax.set_yticks([1, 10, 19, 30])
a.set_xlim(.8, 1.2e4); logticks(a, [0, 1, 2, 3, 4], 'x'); axlab(a, '$b$')
b.set_xlim(.8, 5e3); logticks(b, [0, 1, 2, 3], 'x'); axlab(b, '$L$')
tags(fig, (a, b))
bm = np.array(bm_all); tr = np.array(tr_all)
save(fig, HERE, 'figure', {'bs': bs.tolist(), 'bm_mean': bm.mean(0).tolist(), 'bm_sd': bm.std(0).tolist(),
     'L': L.tolist(), 'tr_mean': tr.mean(0).tolist(), 'tr_sd': tr.std(0).tolist()})
