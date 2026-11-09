from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
ax = axs[0]; T = np.arange(1, 121); P = pgd(T=120); M = md(T=120); X1, *_ = fw(T=120); X2, *_ = fw(T=120, rule='exact')
for Xk, c, lw in ((P, GREEN, 1.4), (M, PURPLE, 1.4), (X1, YELLOW, 1.4), (X2, RED, 1.1)):
    e = np.maximum(f(Xk[1:121])-FS, 1e-13); ax.semilogy(T, np.minimum.accumulate(e), color=c, lw=lw)
ax.text(5.5, 2e-9, '投影梯度', color=GREEN, fontsize=7.5); ax.text(58, 2.2e-6, '镜像', color=PURPLE, fontsize=7.5); ax.text(60, 8e-4, '条件梯度', color=YELLOW, fontsize=7.5); ax.text(64, 2.2e-2, '线搜索', color=RED, fontsize=7.5)
setup(ax, (0, 120), (1e-11, 3), [0, 40, 80, 120], [1e-9, 1e-5, 1e-1], xl='$t$', yl='$f-f^*$')
# High-dimensional simplex least squares with sparse optimum: nonzeros vs iteration.
rng = np.random.default_rng(5); n = 300; m = 60; B = rng.normal(size=(m, n))/np.sqrt(m); w = np.zeros(n); w[rng.choice(n, 8, replace=False)] = 1/8; b = B@w
Hn = B.T@B; Lh = float(np.linalg.eigvalsh(Hn)[-1]); gr = lambda x: B.T@(B@x-b)
def proj_n(z):
    u = np.sort(z)[::-1]; c = np.cumsum(u)-1; k = np.where(u-c/np.arange(1, n+1) > 0)[0][-1]; return np.maximum(z-c[k]/(k+1), 0)
x = np.ones(n)/n; a = 1/Lh; Tn = 150; P_ = []; 
for t in range(Tn): P_.append((x > 1e-12).sum()); x = proj_n(x-a*gr(x))
x = np.eye(n)[0]; Fw = []
for t in range(Tn): Fw.append((x > 1e-12).sum()); g = gr(x); i = int(np.argmin(g)); d = np.eye(n)[i]-x; x = x+2/(t+2)*d
x = np.ones(n)/n; M_ = []; a2 = 1/float(np.max(np.abs(Hn)))
for t in range(Tn): M_.append((x > 1e-12).sum()); w_ = x*np.exp(-a2*gr(x)); x = w_/w_.sum()
ax = axs[1]; ax.semilogy(P_, color=GREEN, lw=1.4); ax.semilogy(M_, color=PURPLE, lw=1.4); ax.semilogy(Fw, color=YELLOW, lw=1.4)
ax.text(62, 170, '镜像', color=PURPLE, fontsize=7.5); ax.text(62, 62, '投影梯度', color=GREEN, fontsize=7.5); ax.text(62, 8.5, '条件梯度', color=YELLOW, fontsize=7.5)
setup(ax, (0, 150), (1, 500), [0, 50, 100, 150], [1, 10, 100], xl='$t$', yl='非零元个数')
panels(fig, .1, .985, .98, .2, .36); tags(fig, axs)
save(fig, HERE, 'figure', {'seed': 5, 'n': n, 'm': m, 'P_final': int(P_[-1]), 'FW_final': int(Fw[-1])})
print(P_[:10], P_[-1], Fw[:6], Fw[-1], M_[-1])
