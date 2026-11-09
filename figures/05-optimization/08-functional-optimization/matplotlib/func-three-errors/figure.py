from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# (a) 线性元目标差：插值 vs Ritz；(b) n=32 时 CG 迭代的总目标差。
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.095, wspace=.3, bottom=.26)
Es = .5/np.tanh(1)
ns = np.array([2, 4, 8, 16, 32, 64, 128])
gr, gi = [], []
v = lambda x: x+.25*np.sin(2*np.pi*x)
Ev = .5*(1+np.pi**2/8+1/3-1/(4*np.pi)+1/32)
for n in ns:
    K, M = hats(n); A = K+M; nodes = np.arange(n+1)/n
    c = np.linalg.solve(A[1:n, 1:n], -A[1:n, n]); u = np.r_[0, c, 1]
    gr.append(.5*u@A@u-Es)
    ui = v(nodes)
    gi.append(abs(.5*ui@A@ui-Ev))
gr, gi = np.array(gr), np.array(gi)
ax = axes[0]
ax.loglog(ns, gi, '-o', color=YELLOW, lw=1.4, ms=3.6, mew=0)
ax.loglog(ns, gr, '-o', color=GREEN, lw=1.4, ms=3.6, mew=0)
ax.text(10, gi[2]*2.2, '固定函数', color=YELLOW, fontsize=7.5)
ax.text(5, gr[2]*.5, '离散极小者', color=GREEN, fontsize=7.5, va='top', ha='center')
ax.set_xticks([2, 8, 32, 128]); ax.set_xticklabels(['2', '8', '32', '128']); ax.minorticks_off(); ax.set_yticks([1e-6, 1e-4, 1e-2]); ax.set_xlabel('$n$', labelpad=1); ax.set_ylabel('目标差', labelpad=0)
n = 32
K, M = hats(n); A = K+M; Ai = A[1:n, 1:n]; b = -A[1:n, n]
E = lambda c: .5*c@Ai@c-b@c+.5*A[n, n]
cs = np.linalg.solve(Ai, b)
disc = E(cs)-Es
c = np.arange(1, n)/n; r = b-Ai@c; d = r.copy(); tot, sol = [], []
for t in range(32):
    tot.append(E(c)-Es); sol.append(max(E(c)-E(cs), 1e-18))
    al = (r@r)/(d@Ai@d); c = c+al*d; rn = r-al*Ai@d; d = rn+(rn@rn)/(r@r)*d; r = rn
ax = axes[1]
ax.semilogy(range(32), tot, color=GREEN, lw=1.4)
ax.semilogy(range(32), sol, color=BLUE, lw=1.4)
ax.axhline(disc, color=RED, lw=1.1, ls=(0, (4, 2)))
ax.text(1, disc*.4, '离散误差', color=RED, fontsize=7.5, va='top')
ax.text(30, tot[10]*1.1, '总误差', color=GREEN, fontsize=7.5, ha='right')
ax.text(26, 3e-9, '求解误差', color=BLUE, fontsize=7.5, ha='right', va='top')
ax.set_xlim(0, 31); ax.set_ylim(1e-13, .05); ax.set_yticks([1e-12, 1e-8, 1e-4]); ax.minorticks_off(); ax.set_xticks([0, 10, 20, 30]); ax.set_xlabel('迭代步 t', labelpad=1)
tags(fig, axes)
rate = np.log2(gr[:-1]/gr[1:])
save(fig, HERE, 'figure', {'n': ns.tolist(), 'gap_ritz': gr.tolist(), 'gap_interp': gi.tolist(), 'rate': rate.tolist(), 'disc_n32': float(disc), 'E(v)': Ev, 'tot': tot[:12], 'sol': sol[:32:5]})
