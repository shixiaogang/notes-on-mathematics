"""Monte Carlo Fisher matrix at Q=N(1,4), natural coordinates, T=(X,X^2), score T-(1,5). G_hat=(1/n) sum s s^T from n draws of Q,
d_hat=G_hat^{-1} g with exact g=(4,20); relative error ||d_hat-d||_G/||d||_G, root-mean-square over R=500 replications, seed 728.
Green: RMS error; purple dashed: reference c n^{-1/2} matched at n=20000."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

rng = np.random.default_rng(SEED)
G = fisher_nat(1.0, 4.0); g = np.array([4.0, 20.0]); d = np.linalg.solve(G, g); nd = np.sqrt(d@G@d)
ns = np.unique(np.round(np.logspace(np.log10(20), np.log10(20000), 13)).astype(int)); R = 500
rms = []
for n in ns:
    errs = []
    for _ in range(R):
        x = rng.normal(1.0, 2.0, n); s = np.stack([x-1.0, x*x-5.0], 1)
        Gh = s.T@s/n; dh = np.linalg.solve(Gh, g); e = dh-d
        errs.append((e@G@e)/nd**2)
    rms.append(np.sqrt(np.mean(errs)))
rms = np.array(rms)
fig, ax = figure(width_mm=80, height_mm=50)
ax.loglog(ns, rms, color=GREEN, lw=1.3); ax.scatter(ns, rms, s=8, color=GREEN, zorder=4)
c = rms[-1]*np.sqrt(ns[-1]); ax.loglog(ns, c/np.sqrt(ns), color=PURPLE, lw=1.0, ls='--')
ax.set_xlabel(r'$n$', labelpad=1); ax.set_ylabel('相对误差', labelpad=1)
save(fig, HERE, 'figure', {'n': ns.tolist(), 'rms': rms.tolist(), 'c': float(c), 'R': R, 'seed': SEED})
