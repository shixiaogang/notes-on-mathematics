from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Length-penalized assignment between the inner point c3 = 0.5936 (ideal length 1.328 bit) and the outer point
# c4 = 2.5936 (ideal length 3.299 bit) of the 4-level Lloyd-Max quantizer for Laplace(0,1), lambda = 0.5.
# Dashed: (x-c_j)^2 (lambda = 0), threshold 1.5936; solid: (x-c_j)^2 + lambda*l_j, threshold 1.5936 + 0.4928*lambda.
lm = lloyd([-1.5, -.5, .5, 1.5], 400)[-1]; c3, c4 = lm[1][2], lm[1][3]
p3 = mass(0, lm[0][2]); p4 = mass(lm[0][2], math.inf); l3, l4 = -math.log2(p3), -math.log2(p4)
lam = .5; t0 = (c3+c4)/2; t1 = t0 + lam*(l4-l3)/(2*(c4-c3))
x = np.linspace(0, 3.6, 500)
fig, ax = figure(width_mm=92, height_mm=52)
panel(fig, left=.1, right=.97, bottom=.17, top=.97)
ax.plot(x, (x-c3)**2, color=BLUE, lw=1.0, ls=DASH); ax.plot(x, (x-c4)**2, color=YELLOW, lw=1.2, ls=DASH)
ax.plot(x, (x-c3)**2+lam*l3, color=BLUE, lw=1.4); ax.plot(x, (x-c4)**2+lam*l4, color=YELLOW, lw=1.6)
ax.axvline(t0, color=STROKE, lw=.85, ls=DOT); ax.axvline(t1, color=RED, lw=.95)
dot(ax, c3, 0, color=BLUE); dot(ax, c4, 0, color=YELLOW)
lab(ax, c3, .25, '$c_3$', BLUE, ha='center'); lab(ax, c4+.08, .25, '$c_4$', YELLOW)
lab(ax, t0-.05, 4.3, '$1.594$', MUTED, ha='right'); lab(ax, t1+.05, 4.3, '$1.840$', RED)
ax.set_xlim(0, 3.6); ax.set_ylim(0, 4.8); ax.set_xlabel('$x$', labelpad=1)
save(fig, HERE, 'figure', {'c3': float(c3), 'c4': float(c4), 'p3': p3, 'p4': p4, 'l3': l3, 'l4': l4, 't0': float(t0), 't1': float(t1),
     'slope': float((l4-l3)/(2*(c4-c3)))})
