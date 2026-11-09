from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# J_rho 的 Hessian 特征值 (k pi)^2-rho，rho=15；差分 Hessian 的最大特征值随 n。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.085, wspace=.3, bottom=.28)
ax = axes[0]
k = np.arange(1, 6); ev = (k*np.pi)**2-15
ax.axhline(0, color=MUTED, lw=.85)
for a, b in zip(k, ev):
    c = RED if b < 0 else BLUE
    ax.vlines(a, 0, b, color=c, lw=1.4); ax.plot([a], [b], 'o', ms=4, color=c, mew=0)
ax.set_xlim(.4, 5.6); ax.set_ylim(-30, 260); ax.set_xticks(k); ax.set_yticks([0, 100, 200]); ax.set_xlabel('$k$', labelpad=0); ax.set_ylabel(r'$(k\pi)^2-\rho$', labelpad=0)
ax = axes[1]
ns = np.array([8, 16, 32, 64, 128, 256]); L = []
for n in ns:
    T = 2*np.eye(n-1)-np.eye(n-1, k=1)-np.eye(n-1, k=-1)
    L.append(np.linalg.eigvalsh(T*n*n).max())
L = np.array(L)
ax.loglog(ns, L, '-o', color=BLUE, lw=1.4, ms=3.6, mew=0)
ax.loglog(ns, np.pi**2*np.ones_like(ns), color=GREEN, lw=1.4)
ax.text(256, 3.2e5/8, r'$\lambda_{\max}$', color=BLUE, fontsize=8, ha='right', va='bottom')
ax.text(256, 15, r'$\lambda_{\min}\approx\pi^2$', color=GREEN, fontsize=8, ha='right', va='bottom')
ax.set_xticks([8, 32, 128]); ax.set_xticklabels(['8', '32', '128']); ax.minorticks_off(); ax.set_yticks([1e1, 1e3, 1e5]); ax.set_xlabel('$n$', labelpad=0); ax.set_ylim(3,6e5)
tags(fig, axes)
save(fig, HERE, 'figure', {'ev': ev.tolist(), 'lmax': L.tolist(), 'n': ns.tolist()})
