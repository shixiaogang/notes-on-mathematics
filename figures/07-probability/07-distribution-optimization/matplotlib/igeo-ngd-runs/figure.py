"""Runs from N(1,4) to Pi=N(0,1), L=D_KL(Q||Pi). Green: natural gradient, alpha=1/2 (theta-theta_Pi halves each step).
Yellow: Euclidean gradient in natural parameters theta, alpha=0.02. Purple: Euclidean gradient in (mu,v), alpha=1/2.
(a) iterates in the (mu,sigma) plane with L contours; (b) L versus iteration (log scale), 40 iterations."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

N = 40
def ngd(a=0.5):
    t = nat_from_mv(1.0, 4.0); out = []
    for k in range(N+1):
        out.append(mv_from_nat(t)); t = t-a*(t-THETA_PI)
    return np.array(out)
def gd_nat(a=0.02):
    t = nat_from_mv(1.0, 4.0); out = []
    for k in range(N+1):
        m, v = mv_from_nat(t); out.append((m, v)); t = t-a*fisher_nat(m, v)@(t-THETA_PI)
    return np.array(out)
def gd_mv(a=0.5):
    m, v = 1.0, 4.0; out = []
    for k in range(N+1):
        out.append((m, v)); m, v = m-a*m, v-a*(0.5-0.5/v)
    return np.array(out)
runs = [(gd_nat(), YELLOW), (gd_mv(), PURPLE), (ngd(), GREEN)]
fig, (a, b) = figure(width_mm=108, height_mm=52, ncols=2)
M, S = np.meshgrid(np.linspace(-0.2, 1.1, 200), np.linspace(0.1, 2.1, 200))
a.contour(M, S, L_mv(M, S*S), levels=[0.02, 0.1, 0.3, 0.7, 1.2], colors=[GRID], linewidths=0.6)
for r, col in runs:
    a.plot(r[:, 0], np.sqrt(r[:, 1]), color=col, lw=0.9)
    a.scatter(r[:, 0], np.sqrt(r[:, 1]), s=5, color=col, zorder=4)
a.scatter([1], [2], s=16, color=RED, zorder=6); a.scatter([0], [1], s=18, color=RED, marker='x', zorder=6)
a.set_xlim(-0.2, 1.1); a.set_ylim(0.1, 2.1); a.set_xlabel(r'$\mu$', labelpad=1); a.set_ylabel(r'$\sigma$', labelpad=1)
facts = {}
for (r, col), name in zip(runs, ('gd_nat', 'gd_mv', 'ngd')):
    Ls = L_mv(r[:, 0], r[:, 1]); Ls = np.maximum(Ls, 1e-16)
    b.semilogy(np.arange(N+1), Ls, color=col, lw=1.3)
    facts[name] = [float(x) for x in Ls[:6]]+[float(Ls[-1])]
b.set_xlim(0, N); b.set_ylim(1e-12, 3); b.set_xlabel('迭代次数', labelpad=1); b.set_ylabel(r'$L$', labelpad=1)
tag(a, '(a)', y=-0.30); tag(b, '(b)', y=-0.30)
save(fig, HERE, 'figure', facts)
