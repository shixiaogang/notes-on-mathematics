from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: rejection sampling of Beta(2,2) from Unif(0,1) with M = 1/4 (acceptance 2/3), stopped after at most T trials
# and returning the last candidate if all fail. Output density (1-(1/3)^T) 6x(1-x) + (1/3)^T 3(1-2x)^2.
x = np.linspace(0, 1, 400)
fig, A = figure(width_mm=72, height_mm=50)
style(A)
pi = 6*x*(1-x); r = 3*(1-2*x)**2
for T, col, ls in ((1, YELLOW, '-'), (2, PURPLE, '-'), (4, PURPLE, '--')):
    A.plot(x, (1-(1/3)**T)*pi+(1/3)**T*r, color=col, lw=1.2, ls=ls)
A.plot(x, pi, color=BLUE, lw=1.4)
A.text(.83, 1.06, '$T=1$', fontsize=7.5, color=INK)
xx = .06; A.annotate('$T=2$', (xx, (8/9)*6*xx*(1-xx)+(1/9)*3*(1-2*xx)**2), (.1, 1.25), fontsize=7.5, color=INK,
           arrowprops=dict(arrowstyle='-', color=LINE, lw=.6))
A.set_xlim(0, 1); A.set_ylim(0, 1.7); A.set_yticks([0, .5, 1, 1.5]); A.set_ylabel('密度'); A.set_xlabel('$x$')
save(fig, HERE(__file__), 'figure', {'weights_of_r': {T: (1/3)**T for T in (1, 2, 4)}})
