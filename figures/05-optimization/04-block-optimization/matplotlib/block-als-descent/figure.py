from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# (a) ALS on Y=[[3,1],[1,3]], r=1, v0=(1,0): objective after each half step; best rank-1 error is 4.
# (b) Y=rank-3 + noise, 40x25: objective minus truncated-SVD optimum for three random starts.
Y = np.array([[3., 1], [1, 3]]); v = np.array([1., 0]); H = []
for k in range(6):
    u = Y@v/(v@v); H.append(((Y-np.outer(u, v))**2).sum()); v = Y.T@u/(u@u); H.append(((Y-np.outer(u, v))**2).sum())
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, .085, .985, .97, .26, wspace=.3)
a.step(range(len(H)), H, where='post', color=GREEN, lw=1.4); a.plot(range(len(H)), H, 'o', color=GREEN, ms=3, mew=0)
a.axhline(4, color=PURPLE, lw=.95, ls=(0, (3, 2))); a.text(6.1, 4.4, '最优值 4', fontsize=7.5, color=INK)
a.set_xticks(range(0, 12, 2)); a.set_xlabel('半步编号', labelpad=1); a.set_ylabel('目标值', labelpad=1); a.set_ylim(3, 10.8)
rng = np.random.default_rng(2); p, q, r = 40, 25, 3
Y2 = (rng.standard_normal((p, r))*[3, 2, 1.2])@rng.standard_normal((q, r)).T + 2.5*rng.standard_normal((p, q))
s = np.linalg.svd(Y2, compute_uv=False); fs = (s[r:]**2).sum(); R = 60
for sd, c in zip([1, 2, 3], [GREEN, YELLOW, PURPLE]):
    g = np.random.default_rng(sd); V = g.standard_normal((q, r)); G = []
    for k in range(R):
        U = Y2@V@np.linalg.inv(V.T@V); V = Y2.T@U@np.linalg.inv(U.T@U); G.append(((Y2-U@V.T)**2).sum()-fs)
    b.semilogy(range(1, R+1), np.maximum(G, 1e-9), color=c, lw=1.4)
b.set_xlabel('轮数', labelpad=1); b.set_ylabel('目标差', labelpad=1)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'H': H, 'fs': float(fs)})
print(H)
