from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# Nested first-order method on f=-x^2/2+2xy-y^2/2: same runs, two horizontal axes.
def run(K, T, a=1/6, b=.5):
    x, y = 1., 0.; res = [3*abs(x)]
    for _ in range(T):
        for _ in range(K): y = y+b*(2*x-y)
        x = x-a*(-x+2*y); res.append(3*abs(x))
    return np.array(res)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panels(fig, .105, .985, .975, .25, .34)
cs = [(1, YELLOW, 1.6), (3, GREEN, 1.4), (10, BLUE, 1.4)]
ax = axes[0]; setup(ax, (0, 30), (1e-5, 5), (0, 10, 20, 30), xl='外层轮数', yl=r'$|\phi^\prime(x^{(t)})|$'); ax.set_yscale('log')
ex = 3*.5**np.arange(31); ax.semilogy(np.arange(31), ex, color=MUTED, lw=.9, ls=(0, (3, 2)))
ax2 = axes[1]; setup(ax2, (0, 80), (1e-5, 5), (0, 40, 80), xl='梯度读取次数', yl=r'$|\phi^\prime(x^{(t)})|$'); ax2.set_yscale('log')
for K, c, lw in cs:
    r = run(K, 80); ax.semilogy(np.arange(81), r, color=c, lw=lw); ax2.semilogy((K+1)*np.arange(81), r, color=c, lw=lw)
axes[0].text(22, 1.1e-1, '$K=1$', fontsize=7.5); axes[0].text(7.5, 1.2e-4, '$K=3$', fontsize=7.5, ha='right'); axes[0].text(14.5, 1.2e-3, '$K=10$', fontsize=7.5)
axes[1].text(58, .2, '$K=10$', fontsize=7.5); axes[1].text(14, 1.2e-4, '$K=3$', fontsize=7.5); axes[1].text(66, 4e-3, '$K=1$', fontsize=7.5)
tags(fig, axes)
save(fig, HERE, 'figure', {'f': '-x^2/2+2xy-y^2/2', 'alpha': '1/6', 'beta': .5, 'K': [1, 3, 10]})
print([run(K, 30)[[1, 2, 5, 10, 30]] for K in (1, 3, 10)])
