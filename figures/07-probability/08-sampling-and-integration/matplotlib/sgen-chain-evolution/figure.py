from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: three-state kernel K = [[.5,.5,0],[.2,.5,.3],[0,.5,.5]] with invariant pi = (0.2, 0.5, 0.3).
# (a) mu_t = delta_1 K^t for t = 0, 1, 2, 3, 5 against pi.
# (b) running fraction of time spent in state 3 along one path from state 1 (seed 6, 2000 steps) for K (green)
#     and for the stay-put kernel I (red), for which every distribution is invariant.
K = np.array([[.5, .5, 0], [.2, .5, .3], [0, .5, .5]]); pi = np.array([.2, .5, .3])
assert np.allclose(pi@K, pi)
mus = {}; mu = np.array([1., 0, 0])
for t in range(6):
    mus[t] = mu.copy(); mu = mu@K
fig, (A, B) = figure(width_mm=112, height_mm=50, ncols=2)
style(A); style(B)
ts = [0, 1, 2, 3, 5]; w = .14
cols = [GREEN_FILL]*5
for j, t in enumerate(ts):
    A.bar(np.arange(1, 4)+(j-2.5)*w, mus[t], width=w, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
A.bar(np.arange(1, 4)+2.5*w, pi, width=w, color=BLUE_FILL, edgecolor=BLUE, lw=.8)
A.set_xticks([1, 2, 3]); A.set_ylim(0, 1.05); A.set_yticks([0, .2, .5, 1])
A.set_ylabel('概率'); sub(A, 'a', '状态')
rng = np.random.default_rng(6); n = 2000; x = 0; frac = np.empty(n); c3 = 0
for t in range(n):
    x = rng.choice(3, p=K[x]); c3 += (x == 2); frac[t] = c3/(t+1)
B.plot(np.arange(1, n+1), frac, color=GREEN, lw=1.1)
B.plot([1, n], [0, 0], color=RED, lw=1.4)
B.axhline(.3, color=BLUE, lw=1.0, ls='--')
B.set_xscale('log'); B.set_xlim(1, n); B.set_ylim(-.03, .6); B.set_yticks([0, .3, .6])
B.set_ylabel('状态3的时间比例'); sub(B, 'b', '步数 $t$'.replace('步数 ', ''))
save(fig, HERE(__file__), 'figure', {'mu': {t: mus[t].tolist() for t in mus}, 'final_frac': float(frac[-1])})
print({t: mus[t] for t in ts}, frac[-1])
