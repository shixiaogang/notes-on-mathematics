"""Maximum-entropy distributions on die faces {1,...,6} (counting reference measure).
(a) E[X]=3.5 -> uniform, (b) E[X]=4.5, (c) E[X]=5.5: q propto e^{theta x};
(d) E[X]=3.5 and E[(X-3.5)^2]=1: q propto e^{theta2 (x-3.5)^2} (by symmetry theta1-part vanishes).
theta solved by Newton's method on the dual function; bars blue, uniform level 1/6 grey dashed."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

f = np.arange(1, 7, dtype=float)
def solve(T, m, iters=60):
    th = np.zeros(T.shape[0])
    for _ in range(iters):
        w = np.exp(th@T); q = w/w.sum()
        mu = T@q; C = (T*q)@T.T - np.outer(mu, mu)
        th = th - np.linalg.solve(C, mu-m)
    w = np.exp(th@T); return th, w/w.sum()
cases = []
for m in (3.5, 4.5, 5.5):
    th, q = solve(f[None, :], np.array([m])); cases.append((th, q))
T2 = np.vstack([f-3.5, (f-3.5)**2]); th2, q2 = solve(T2, np.array([0.0, 1.0])); cases.append((th2, q2))
fig, axs = figure(width_mm=112, height_mm=38, ncols=4, sharey=True)
labels = ['(a)', '(b)', '(c)', '(d)']
facts = {}
for ax, (th, q), lab in zip(axs, cases, labels):
    ax.bar(f, q, width=0.62, color=BLUE_FILL, edgecolor=BLUE, lw=0.9)
    ax.axhline(1/6, color=STROKE, lw=0.7, ls='--')
    ax.set_xticks(f); ax.set_ylim(0, 0.72)
    H = float(-np.sum(q*np.log(q)))
    ax.text(0.5, 0.97, rf'$H={H:.3f}$', transform=ax.transAxes, ha='center', va='top', fontsize=7.5, color=MUTED)
    tag(ax, lab, y=-0.24)
    facts[lab] = {'theta': th.tolist(), 'q': q.tolist(), 'H': H}
save(fig, HERE, 'figure', facts)
