from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Target pi = 0.5 N(-5,1) + 0.5 N(5,1), I = E_pi[X] = 0.  Random-walk Metropolis-Hastings with proposal
# y = x + N(0,1), acceptance min{1, p(y)/p(x)}, 5000 steps per chain.
# (a) four chains started at -7, -3, 3, 7 (seed 3131); (b) four chains started at -7, -6, -4, -3 (seed 3132).
# Green: trace of each chain; red dashed: each chain's running mean at t = 5000; blue: I = 0.
T = 5000
def logp(x): return np.logaddexp(-(x+5)**2/2, -(x-5)**2/2)
def run(x0s, seed):
    rng = np.random.default_rng(seed); x = np.array(x0s, float); out = np.empty((len(x0s), T)); acc = 0
    for t in range(T):
        y = x + rng.standard_normal(len(x)); ok = np.log(rng.random(len(x))) < logp(y) - logp(x)
        x = np.where(ok, y, x); acc += ok.sum(); out[:, t] = x
    return out, acc/(T*len(x0s))
A, accA = run([-7, -3, 3, 7], 3131); B, accB = run([-7, -6, -4, -3], 3132)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
panel(fig, left=.07, right=.98, bottom=.28, top=.95, wspace=.1)
t = np.arange(1, T+1)
for ax, S in zip(axes, (A, B)):
    for x in S:
        ax.plot(t, x, color=GREEN, lw=.3)
        ax.plot([0, T], [x.mean()]*2, color=RED, lw=1.3, ls=DASH, zorder=5)
    ax.axhline(0, color=BLUE, lw=1.1)
    ax.set_xlim(0, T); ax.set_ylim(-9, 9); ax.set_xticks([0, 2000, 4000]); ax.set_yticks([-5, 0, 5]); axlab(ax, '$t$')
tags(fig, axes)
save(fig, HERE, 'figure', {'means_A': A.mean(1).tolist(), 'means_B': B.mean(1).tolist(), 'acc': [accA, accB],
     'sign_changes_A': [int(np.sum(np.diff(np.sign(x)) != 0)) for x in A], 'sign_changes_B': [int(np.sum(np.diff(np.sign(x)) != 0)) for x in B],
     'overall_mean_A': float(A.mean()), 'overall_mean_B': float(B.mean())})
