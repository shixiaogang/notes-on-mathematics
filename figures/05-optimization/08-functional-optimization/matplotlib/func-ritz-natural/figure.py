from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# 左端自由 u(1)=1：试探空间不约束 u(0)，自然边界 u'(0)=0 自动逼近。
fig, ax = figure(width_mm=86, height_mm=50)
panel(fig, left=.11, right=.975, top=.96, bottom=.19)
ax.plot(X, np.cosh(X)/np.cosh(1), color=BLUE, lw=1.4)
rec = {}
for n, c, ms in ((3, GREEN, 4.0), (1, YELLOW, 4.0)):
    K, M = hats(n); A = K+M
    sol = np.linalg.solve(A[:-1, :-1], -A[:-1, -1])
    nodes = np.arange(n+1)/n; un = np.r_[sol, 1]
    ax.plot(nodes, un, color=c, lw=1.4, marker='o', ms=ms, mew=0)
    rec[n] = {'u': un.tolist(), 'E': float(.5*un@A@un), 'slope0': float((un[1]-un[0])*n)}
ax.set_xlim(-.03, 1.05); ax.set_ylim(.55, 1.06); ax.set_xticks([0, 1/3, 2/3, 1]); ax.set_xticklabels(['0', '1/3', '2/3', '1']); ax.set_yticks([.6, .8, 1]); ax.set_yticklabels(['0.6', '0.8', '1']); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u$', labelpad=0)
ax.text(.1, .595, '$n=1$', color=YELLOW, fontsize=7.5, ha='center', va='top') if rec[1]['u'][0] < .64 else ax.text(.1, rec[1]['u'][0]-.06, '$n=1$', color=YELLOW, fontsize=7.5)
ax.text(.5, .67, '$n=3$', color=GREEN, fontsize=7.5, ha='center', va='bottom')
save(fig, HERE, 'figure', {'ritz': rec, 'E*': .5*np.tanh(1), 'exact_u0': 1/np.cosh(1)})
