from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Random codes of rate R = 1/2 on the Gaussian channel with sigma^2 = 1: M = 2^(n/2) codewords, each an iid N(0,1)
# vector rescaled to length sqrt(nP) (so every codeword meets the budget with equality); maximum-likelihood
# (nearest codeword) decoding. Block error rate estimated by simulation (seed 11, 40000 uniformly drawn messages per
# point) for n = 8, 16, 24, 32 (yellow, purple, green, blue). Red line: P/sigma^2 = 1 (0 dB), where C = 1/2.
rng = np.random.default_rng(11); R = .5; T = 40000
db = np.arange(-2, 8.01, 1.0)
fig, ax = figure(width_mm=92, height_mm=52)
panel(fig, left=.13, right=.97, top=.95, bottom=.2)
facts = {}
for n, col in ((8, YELLOW), (16, PURPLE), (24, GREEN), (32, BLUE)):
    M = int(round(2**(n*R)))
    cb = rng.normal(size=(M, n)).astype(np.float32)
    cb *= np.sqrt(n)/np.linalg.norm(cb, axis=1, keepdims=True)
    pe = []
    for d in db:
        P = 10**(d/10); err = 0
        for start in range(0, T, 500):
            m = rng.integers(0, M, 500)
            y = cb[m]*np.float32(math.sqrt(P)) + rng.normal(size=(500, n)).astype(np.float32)
            err += int((np.argmax(y @ cb.T, axis=1) != m).sum())
        pe.append(err/T)
    pe = np.array(pe); facts['n=%d' % n] = dict(zip([float(x) for x in db], [float(x) for x in pe]))
    k = pe > 0
    ax.plot(db[k], pe[k], color=col, lw=1.5 if col == YELLOW else 1.4, marker='o', ms=2.4, mew=0)
ax.axvline(0, color=RED, lw=1.1)
ax.set_yscale('log'); ax.set_ylim(1e-4, 1.2); ax.set_xlim(-2, 8)
ax.set_xlabel(r'$10\log_{10}(P/\sigma^2)$ (dB)', labelpad=1); ax.set_ylabel('块错误率', labelpad=2)
lab(ax, 6.6, .03, r'$n=8$', YELLOW); lab(ax, 6.1, 1.5e-3, r'$n=16$', PURPLE)
lab(ax, 5.3, 2.5e-4, r'$n=24$', GREEN); lab(ax, 2.6, 4e-4, r'$n=32$', BLUE)
save(fig, HERE, 'figure', facts)
