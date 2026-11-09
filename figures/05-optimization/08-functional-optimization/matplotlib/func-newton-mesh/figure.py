from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# J=int u'^2/2+u^4/4，u(0)=0,u(1)=1，线性元、梯形求积；Newton 从 u=x 出发，不同 n 的 H^{-1} 残差。
fig, ax = figure(width_mm=86, height_mm=50)
panel(fig, left=.13, right=.975, top=.96, bottom=.19)
rec = {}
for n, col, ls in ((8, YELLOW, '-'), (32, BLUE, '-'), (128, GREEN, (0, (4, 2)))):
    K, _ = hats(n); K0 = K[1:n, 1:n]; d = 1/n
    u = np.arange(1, n)/n; hist = []
    bd = np.zeros(n-1); bd[-1] = K[n-1, n]
    for t in range(7):
        g = K0@u+bd+d*u**3
        res = float(np.sqrt(g@np.linalg.solve(K0, g)))
        hist.append(res)
        if res < 1e-13: break
        u = u-np.linalg.solve(K0+np.diag(3*d*u**2), g)
    rec[n] = hist
    ax.semilogy(range(len(hist)), hist, color=col, lw=1.4, ls=ls, marker='o', ms=3.4, mew=0)
ax.set_xticks(range(0, 4)); ax.set_xlim(-.1, 3.2); ax.set_ylim(1e-15, 1); ax.minorticks_off(); ax.set_yticks([1e-14, 1e-9, 1e-4]); ax.set_xlabel('牛顿迭代步 t', labelpad=1); ax.set_ylabel('残差', labelpad=0)
save(fig, HERE, 'figure', rec)
