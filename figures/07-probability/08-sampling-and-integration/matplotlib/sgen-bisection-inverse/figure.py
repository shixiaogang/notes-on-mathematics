from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: numerical inversion of Gamma(2,1), F(x) = 1-(1+x)e^{-x}, by k = 5 bisection rounds on [0, 8].
# (a) midpoints 4, 2, 1, 1.5, 1.25 for u = 0.37; final bracket (1.25, 1.5], output 1.375, Q(0.37) = 1.2910.
# (b) exact CDF of the output (midpoint of the dyadic cell of width 0.25 containing Q(U); U > F(8) gives 7.875)
#     against F(x) and the band F(x - 0.125), F(x + 0.125).
F = lambda x: 1-(1+x)*np.exp(-x)
fig, (A, B) = figure(width_mm=112, height_mm=54, ncols=2)
style(A); style(B)
x = np.linspace(0, 6, 400)
A.plot(x, F(x), color=BLUE, lw=1.4)
A.axhline(.37, color=RED, lw=.9, xmin=0, xmax=1)
a, b = 0.0, 8.0; mids = []
for k in range(5):
    m = (a+b)/2; mids.append(m)
    if F(m) >= .37: b = m
    else: a = m
for i, m in enumerate(mids):
    if m > 6: continue
    A.plot([m, m], [0, F(m)], color=GREEN, lw=.8, ls='--')
    A.plot([m], [F(m)], 'o', ms=3.2, color=GREEN, zorder=5)
    pos = {0: (4.15, .84), 1: (2.15, .54), 2: (0.25, .18), 3: (1.95, .40), 4: (0.35, .52)}[i]
    A.annotate(f'$m_{i+1}$', (m, F(m)), pos, fontsize=7.5, color=INK,
               arrowprops=dict(arrowstyle='-', color=LINE, lw=.6, shrinkA=1, shrinkB=2))
A.text(4.4, .30, '$u=0.37$', fontsize=7.5, color=INK)
A.set_xlim(0, 6); A.set_ylim(0, 1.02); A.set_xticks([0, 1, 2, 4, 6]); A.set_yticks([0, .37, 1])
A.set_ylabel('$F(x)$'); sub(A, 'a', '$x$')
# exact output law
h = 0.25; cells = np.arange(0, 8, h); mass = F(cells+h)-F(cells); mass[-1] += 1-F(8.0)
vals = cells+h/2
xx = np.linspace(0, 6, 1200)
Ft = np.array([mass[vals <= t].sum() for t in xx])
B.plot(xx, F(xx-0.125)*(xx >= 0.125), color=PURPLE, lw=.85, ls='--')
B.plot(xx, F(xx+0.125), color=PURPLE, lw=.85, ls='--')
B.plot(xx, F(xx), color=BLUE, lw=1.4)
B.step(xx, Ft, where='post', color=GREEN, lw=1.1)
B.set_xlim(0, 4); B.set_ylim(0, 1.02); B.set_xticks([0, 1, 2, 3, 4]); B.set_yticks([0, .5, 1])
B.set_ylabel('分布函数'); sub(B, 'b', '$x$')
dev = max(abs(Ft-F(xx)))
save(fig, HERE(__file__), 'figure', {'mids': mids, 'final': [a, b], 'sup_cdf_error_on_grid': float(dev), 'tail_mass_beyond_8': float(1-F(8.0))})
print(mids, a, b, dev)
