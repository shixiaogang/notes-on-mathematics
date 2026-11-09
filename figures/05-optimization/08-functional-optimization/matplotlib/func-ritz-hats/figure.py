from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# n=3 段线性 Ritz，E，u(0)=0,u(1)=1。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, wspace=.25, bottom=.27)
n = 3; nodes = np.arange(n+1)/n
ax = axes[0]
for i, c, ls in ((1, BLUE, '-'), (2, YELLOW, '-'), (3, STROKE, (0, (3, 2)))):
    y = np.zeros(n+1); y[i] = 1
    ax.plot(nodes, y, color=c, lw=1.4, ls=ls)
    ax.text(nodes[i], 1.07, {1: r'$\phi_1$', 2: r'$\phi_2$', 3: r'$\phi_3$'}[i], color=c, fontsize=8, ha='center')
ax.set_xlim(-.03, 1.05); ax.set_ylim(-.06, 1.25); ax.set_xticks(nodes); ax.set_xticklabels(['0', '1/3', '2/3', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=1)
K, M = hats(n); A = K+M
c = np.linalg.solve(A[1:3, 1:3], -A[1:3, 3])
ax = axes[1]
ex = np.sinh(X)/np.sinh(1)
un = np.r_[0, c, 1]
ax.plot(X, ex-X, color=BLUE, lw=1.4)
ax.plot(nodes, un-nodes, color=GREEN, lw=1.4, marker='o', ms=3.8, mew=0)
ax.axhline(0, color=MUTED, lw=.85)
ax.set_xlim(-.03, 1.03); ax.set_ylim(-.07, .012); ax.set_xticks(nodes); ax.set_xticklabels(['0', '1/3', '2/3', '1']); ax.set_yticks([-.06, -.03, 0]); ax.set_yticklabels(['$-0.06$', '$-0.03$', '0']); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u-x$', labelpad=-1)
ax.text(.16, -.0505, '$u^*-x$', color=BLUE, fontsize=8, ha='center', va='top')
ax.text(.74, -.0155, '$u_3-x$', color=GREEN, fontsize=8, ha='left', va='bottom')
tags(fig, axes)
E3 = .5*np.r_[0, c, 1]@A@np.r_[0, c, 1]
save(fig, HERE, 'figure', {'c': c.tolist(), 'exact_nodal': (np.sinh(nodes[1:3])/np.sinh(1)).tolist(), 'E3': float(E3), 'E*': .5/np.tanh(1), 'A11': float(A[1, 1]), 'A12': float(A[1, 2])})
