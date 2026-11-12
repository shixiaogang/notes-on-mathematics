from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: effect of an invalid envelope. p~(x) = x(1-x), q = Unif(0,1), M = 1/5 < sup p~ = 1/4.
# The accept rule min{1, p~/(Mq)} gives output density proportional to min{p~(x), 1/5}.
# (b) histogram of accepted points from 20000 candidates, seed 4, against the normalized min{p~, 1/5} (red) and 6x(1-x) (blue).
x = np.linspace(0, 1, 600)
pt = x*(1-x); cap = np.minimum(pt, .2)
xa = (1-np.sqrt(1-.8))/2; xb = 1-xa
Zc = np.trapezoid(cap, x)
fig, (A, B) = figure(width_mm=112, height_mm=50, ncols=2)
style(A); style(B)
A.fill_between(x, 0, cap, color=BLUE_FILL, lw=0)
A.fill_between(x, .2, np.maximum(pt, .2), color=RED_FILL, lw=0)
A.plot(x, pt, color=BLUE, lw=1.4)
A.plot([0, 1], [.2, .2], color=PURPLE, lw=1.1)
A.text(.03, .21, '$Mq=1/5$', fontsize=7.5, color=INK)
A.set_xlim(0, 1); A.set_ylim(0, .28); A.set_xticks([0, xa, xb, 1]); A.set_xticklabels(['0', '0.276', '0.724', '1']); A.set_yticks([0, .1, .2, .25])
A.set_yticklabels(['0', '0.1', '0.2', '0.25'])
sub(A, 'a', '$x$')
rng = np.random.default_rng(4)
Y, V = rng.random(20000), rng.random(20000)
keep = Y[V <= np.minimum(1, Y*(1-Y)/.2)]
B.hist(keep, bins=np.linspace(0, 1, 21), density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
B.plot(x, 6*pt, color=BLUE, lw=1.4)
B.plot(x, cap/Zc, color=RED, lw=1.1)
B.set_xlim(0, 1); B.set_ylim(0, 1.7); B.set_yticks([0, .5, 1, 1.5])
B.set_ylabel('密度'); sub(B, 'b', '$x$')
save(fig, HERE(__file__), 'figure', {'xa': xa, 'xb': xb, 'Z_cap': Zc, 'acc': len(keep)/20000})
print(xa, xb, Zc, len(keep)/20000)
