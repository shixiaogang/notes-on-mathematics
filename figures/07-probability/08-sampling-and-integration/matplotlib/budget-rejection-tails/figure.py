from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# Target t_3 density p(x) = 2/(pi sqrt(3)) (1 + x^2/3)^{-2}.  Envelopes: q1 = N(0, 2^2), q2 = Cauchy(0, 1).
# (a) densities on a log scale; (b) ratios p/q: unbounded for the Gaussian (grows like e^{x^2/8} x^{-4}),
# bounded for the Cauchy with M = sup p/q computed on a grid.
x = np.linspace(0, 12, 4001)
p = 2/(math.pi*math.sqrt(3))*(1+x*x/3)**(-2); q1 = phi(x, 0, 2); q2 = 1/(math.pi*(1+x*x))
fig, axs = figure(width_mm=108, height_mm=52, ncols=2)
a1, a2 = axs
panel(fig, left=.11, right=.98, bottom=.3, top=.96, wspace=.38)
a1.plot(x, p, color=BLUE, lw=1.4); a1.plot(x, q1, color=YELLOW, lw=1.6); a1.plot(x, q2, color=PURPLE, lw=1.3)
a1.set_yscale('log'); a1.set_xlim(0, 12); a1.set_ylim(1e-8, 1); logticks(a1, [-8, -6, -4, -2, 0])
lab(a1, 7, 1.2e-4, r'$t_{3}$', BLUE); lab(a1, 5.2, 1e-7, r'$\mathcal{N}(0,2^{2})$', YELLOW); lab(a1, 8.5, 1e-2, 'Cauchy', PURPLE)
axlab(a1, r'$x$', '密度')
r1 = p/q1; r2 = p/q2; M2 = r2.max()
a2.plot(x, r1, color=YELLOW, lw=1.6); a2.plot(x, r2, color=PURPLE, lw=1.3)
a2.axhline(M2, color=RED, lw=.9, ls=DOT)
a2.set_yscale('log'); a2.set_xlim(0, 12); a2.set_ylim(1e-2, 1e4); logticks(a2, [-2, 0, 2, 4])
lab(a2, 7.5, 300, r'$p/q_{1}$', YELLOW); lab(a2, 8, .08, r'$p/q_{2}$', PURPLE); lab(a2, .3, M2*1.6, r'$M$', RED)
axlab(a2, r'$x$', '密度比')
tags(fig, axs)
save(fig, HERE, 'figure', {'M_cauchy': float(M2), 'argmax': float(x[r2.argmax()]), 'ratio_gauss_at_12': float(r1[-1])}); print(M2, x[r2.argmax()], r1[-1])
