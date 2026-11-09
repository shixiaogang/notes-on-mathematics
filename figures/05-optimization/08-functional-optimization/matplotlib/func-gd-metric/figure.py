from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# E 用 n 段线性元离散，u(0)=0,u(1)=1，从 u=x 出发；两种内积下的最速下降，步长 1/L。
fig, ax = figure(width_mm=100, height_mm=54)
panel(fig, left=.11, right=.975, top=.96, bottom=.18)
res = {}
styles = {16: ('-', 1.4), 32: ((0, (4, 2)), 1.4), 64: ((0, (1.2, 1.4)), 1.5)}
for n in (16, 32, 64):
    K, M = hats(n); A = K+M
    Ai, K0 = A[1:-1, 1:-1], K[1:-1, 1:-1]
    b = -A[1:-1, -1]
    cs = np.linalg.solve(Ai, b)
    E = lambda c: .5*c@Ai@c-b@c
    Es = E(cs)
    MLi = np.full(n-1, n*1.0)  # 集中质量 Delta I
    L2 = np.linalg.eigvalsh(Ai*n).max()
    L1 = np.linalg.eigvals(np.linalg.solve(K0, Ai)).real.max()
    gaps = {'L2': [], 'H1': []}
    for name in gaps:
        c = (np.arange(1, n)/n).copy()
        for t in range(101):
            gaps[name].append(max(E(c)-Es, 1e-16))
            r = Ai@c-b
            c = c-(r*n)/L2 if name == 'L2' else c-np.linalg.solve(K0, r)/L1
    ax.semilogy(range(101), gaps['L2'], color=YELLOW, lw=styles[n][1], ls=styles[n][0])
    g1 = [g for g in gaps['H1'] if g > 3e-14]
    ax.semilogy(range(len(g1)), g1, color=GREEN, lw=styles[n][1], ls=styles[n][0])
    res[n] = {'alpha_L2': 1/L2, 'L_H1': float(L1), 'gap_L2_t100': gaps['L2'][100], 'gap_H1_t5': gaps['H1'][5]}
ax.text(84, 1.0e-3, 'L² 内积', color=YELLOW, fontsize=8, ha='center', va='top')
ax.text(13, 1e-10, '$H^1_0$', color=GREEN, fontsize=8); ax.text(20, 1e-10, '内积', color=GREEN, fontsize=8)
ax.set_xlim(0, 100); ax.set_ylim(1e-15, 3e-2); ax.set_yticks([1e-14, 1e-10, 1e-6, 1e-2]); ax.minorticks_off(); ax.set_xlabel('迭代步 t', labelpad=0); ax.set_ylabel('目标差', labelpad=0)
save(fig, HERE, 'figure', res)
