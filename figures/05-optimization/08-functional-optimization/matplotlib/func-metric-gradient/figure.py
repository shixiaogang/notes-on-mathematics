from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# f=(x1^2+9x2^2)/2，x=(9,1)；欧氏梯度 (9,9)，M=diag(1,9) 梯度 (9,1)。
fig, ax = figure(width_mm=100, height_mm=52)
panel(fig, left=.08, right=.985, top=.97, bottom=.16)
a = np.linspace(-11, 11, 500); b = np.linspace(-4, 4, 500); A, B_ = np.meshgrid(a, b)
F = (A**2+9*B_**2)/2
ax.contour(A, B_, F, levels=[2, 8, 18, 32, 49, 72], colors=BLUE, linewidths=.8)
x0 = np.array([9., 1.]); g = np.array([9., 9.])
Mg = g/np.array([1, 9])
end1 = x0-g/9; end2 = x0-Mg
ax.annotate('', xy=end1, xytext=x0, arrowprops=dict(arrowstyle='-|>', color=YELLOW, lw=1.5, shrinkA=0, shrinkB=0))
ax.annotate('', xy=end2, xytext=x0, arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.5, shrinkA=0, shrinkB=0))
dot(ax, *x0, STROKE); dot(ax, 0, 0, RED)
ax.text(9.25, 1.15, '$(9,1)$', fontsize=7.5)
ax.text(8.6, -1.55, r'$-\frac{1}{9}\nabla f$', color=YELLOW, fontsize=8, ha='right')
ax.text(4.6, 1.3, r'$-\bm{M}^{-1}\nabla f$'.replace(r'\bm{M}', 'M'), color=GREEN, fontsize=8, ha='center')
ax.set_aspect('equal'); ax.set_xlim(-11, 11.5); ax.set_ylim(-3.6, 3.6); ax.set_xticks([-9, 0, 9]); ax.set_yticks([-3, 0, 3]); ax.set_xlabel('$x_1$', labelpad=0); ax.set_ylabel('$x_2$', labelpad=0)
save(fig, HERE, 'figure', {'f': '(x1^2+9 x2^2)/2', 'x0': x0.tolist(), 'grad': g.tolist(), 'M_grad': Mg.tolist(), 'euclid_end': end1.tolist()})
