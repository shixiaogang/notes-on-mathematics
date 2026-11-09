from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Factory LP: predictor-corrector iterates against simplex pivots.
x0 = np.array([1., 1., 5., 7., 2.]); y0 = -3. * np.ones(3); s0 = C_FAC - A_FAC.T @ y0
h = predictor_corrector(A_FAC, B_FAC, C_FAC, x0, y0, s0, eta=.99, tol=1e-6)
fig, (a, b) = figure(width_mm=112, height_mm=54, ncols=2)
xlim, ylim = (-.4, 5.6), (-.4, 3.9)
A, rb = with_sign(RES_A, RES_B); V = polygon(A, rb); draw_region(a, V)
route = [(0, 0), (0, 3), (2, 3), (4, 2)]
path(a, np.array(route), color=YELLOW, lw=1.6, ms=3.2)
path(a, np.array([r['x'][:2] for r in h[:5]]), color=GREEN, lw=1.5, ms=3.2)
opt_point(a, (4, 2)); setup(a, xlim, ylim, range(0, 6), range(0, 4)); xlab(a, '$x_1$', '(a) 迭代点与顶点')
a.set_aspect('equal')
sp = [0, 15, 23, 26]
b.plot(range(4), sp, color=YELLOW, lw=1.6, marker='o', ms=3)
b.plot([r['t'] for r in h], [-C_FAC @ r['x'] for r in h], color=GREEN, lw=1.6, marker='o', ms=3)
b.axhline(26, color=RED, lw=1.1, ls='--')
b.text(1.25, 11.5, '单纯形法', fontsize=7.5); b.text(2.5, 22, '内点法', fontsize=7.5)
b.set_xlabel('换基次数或内点轮次\n(b) 利润', labelpad=1); b.set_ylim(-1, 28)
save(fig, OUT, 'figure', {'rounds': len(h) - 1, 'iterates': [r['x'].tolist() for r in h], 'objective': [float(-C_FAC @ r['x']) for r in h], 'gaps': [float(r['x'] @ r['s']) for r in h]})
print(len(h) - 1, [round(float(-C_FAC @ r['x']), 3) for r in h], [float(r['x'] @ r['s']) for r in h])
