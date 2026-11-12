from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Unbiased sample variance S_n^2 = (1/(n-1)) sum (X_i - Xbar_n)^2 along five paths each, n = 2..10^5, log x-axis.
# (a) fair die, sigma^2 = 35/12 (blue line), seed 41.  (b) t distribution with nu = 3 (T = Z / sqrt(W/3),
# W = sum of three squared standard normals), sigma^2 = 3, E T^4 = infinity; seed 42.
N, M = 10**5, 5
n = np.arange(1, N+1)
def svar(X):
    s1 = np.cumsum(X, axis=1); s2 = np.cumsum(X**2, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        return (s2-s1**2/n)/(n-1)
D = np.random.default_rng(41).integers(1, 7, (M, N)).astype(float)
r = np.random.default_rng(42)
T = r.standard_normal((M, N))/np.sqrt((r.standard_normal((M, N, 3))**2).sum(2)/3)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, bottom=.28, wspace=.28)
for s in svar(D): a.plot(n[1:], s[1:], color=GREEN, lw=.8)
for s in svar(T): b.plot(n[1:], s[1:], color=GREEN, lw=.8)
a.axhline(35/12, color=BLUE, lw=1.2); b.axhline(3, color=BLUE, lw=1.2)
lab(a, 1e4, 2.3, r'$35/12$', BLUE, ha='center'); lab(b, 1e4, 2.2, r'$3$', BLUE, ha='center')
a.set_ylim(0, 6); b.set_ylim(0, 8)
for ax in (a, b): ax.set_xscale('log'); ax.set_xlim(2, N); logticks(ax, [1, 2, 3, 4, 5], 'x'); axlab(ax, '$n$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'die_final': svar(D)[:, -1].tolist(), 't3_final': svar(T)[:, -1].tolist(), 'seeds': [41, 42]})
