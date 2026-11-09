from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Scaling matrix entries and the conditioning of the normal matrix: factory LP and a degenerate variant.
x0 = np.array([1., 1., 5., 7., 2.]); y0 = -3. * np.ones(3); s0 = C_FAC - A_FAC.T @ y0
h = predictor_corrector(A_FAC, B_FAC, C_FAC, x0, y0, s0, eta=.99, tol=1e-9)
T = [r['t'] for r in h]; D = np.array([r['x'] / r['s'] for r in h])
K = [np.linalg.cond((A_FAC * d) @ A_FAC.T) for d in D]
# Degenerate variant: the extra constraint x1+x2+x6=6 is also active at (4,2).
A2 = np.hstack([np.vstack([A_FAC, [1., 1., 0., 0., 0.]]), [[0.], [0.], [0.], [1.]]])
b2 = np.append(B_FAC, 6.); c2 = np.append(C_FAC, 0.)
x2 = np.array([1., 1., 5., 7., 2., 4.]); y2 = -3. * np.ones(4); s2 = c2 - A2.T @ y2
h2 = predictor_corrector(A2, b2, c2, x2, y2, s2, eta=.99, tol=1e-9)
T2 = [r['t'] for r in h2]; K2 = [np.linalg.cond((A2 * (r['x'] / r['s'])) @ A2.T) for r in h2]
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
for i in (0, 1, 4): a.semilogy(T, D[:, i], color=GREEN, lw=1.4, marker='o', ms=2.2)
for i in (2, 3): a.semilogy(T, D[:, i], color=YELLOW, lw=1.5, marker='o', ms=2.2)
a.text(2.9, 3e9, '$x_1,x_2,x_5$', fontsize=7.5, ha='center'); a.text(2.9, 3e-9, '$x_3,x_4$', fontsize=7.5, ha='center')
xlab(a, '$t$', '(a) 缩放矩阵的对角元')
b.semilogy(T, K, color=GREEN, lw=1.5, marker='o', ms=2.4)
b.semilogy(T2, K2, color=RED, lw=1.5, marker='o', ms=2.4)
b.text(5.2, 80, '非退化', fontsize=7.5); b.text(2.0, 3e9, '退化', fontsize=7.5)
xlab(b, '$t$', '(b) 正规方程矩阵的条件数')
save(fig, OUT, 'figure', {'rounds': len(h) - 1, 'cond': [float(k) for k in K], 'cond_degenerate': [float(k) for k in K2]})
print(T, [f'{k:.3g}' for k in K], [f'{k:.3g}' for k in K2])
