from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvm-common'))
from rvm_fig import *
# Constant density 1 on (0,1) and perturbations 1+q(x), with q orthogonal to 1,...,x^k:
# (a) q3 = 20x^3-30x^2+12x-1 keeps moments of order 1,2; (b) q5 keeps orders 1..4.
x = np.linspace(0, 1, 801)
q3 = 20*x**3-30*x**2+12*x-1
q5 = 252*x**5-630*x**4+560*x**3-210*x**2+30*x-1
def mom(f, k): return float(np.trapezoid(x**k*f, x))
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
panel(fig, left=.08, right=.98, bottom=.3, wspace=.25)
facts = {}
for ax, q, name in [(axes[0], q3, 'q3'), (axes[1], q5, 'q5')]:
    ax.plot(x, 1+0*x, color=BLUE, lw=1.4)
    ax.plot(x, 1+q, color=YELLOW, lw=1.6)
    ax.set_xlim(0, 1); ax.set_ylim(0, 2.2); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '0.5', '1']); ax.set_yticks([0, 1, 2])
    axlab(ax, '$x$')
    facts[name] = [[mom(1+0*x, k), mom(1+q, k)] for k in range(0, 7)]
tags(fig, axes)
save(fig, HERE, 'figure', facts)
for k, v in facts.items(): print(k, v)
