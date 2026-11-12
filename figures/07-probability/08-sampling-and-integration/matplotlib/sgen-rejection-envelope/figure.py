from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
# Target: rejection sampling of p~(x) = x(1-x) on [0,1] (Z = 1/6, normalized Beta(2,2)) from q = Unif(0,1), M = 1/4.
# (a) 400 candidates plotted at (Y, V M q(Y)); accepted (green) below p~, rejected (red) above; seed 2.
#     Hand-worked trials: (y, v) = (0.9, 0.5) rejected, (0.37, 0.80) accepted.
# (b) histogram of the accepted points of 6000 candidates against 6x(1-x).
rng = np.random.default_rng(2)
Y, V = rng.random(400), rng.random(400)
H = V/4; acc = H <= Y*(1-Y)
x = np.linspace(0, 1, 300)
fig, (A, B) = figure(width_mm=112, height_mm=50, ncols=2)
style(A); style(B)
A.fill_between(x, 0, x*(1-x), color=BLUE_FILL, lw=0)
A.plot(x, x*(1-x), color=BLUE, lw=1.4)
A.plot([0, 1], [.25, .25], color=PURPLE, lw=1.1)
A.plot(Y[acc], H[acc], 'o', ms=1.6, color=GREEN, mec='none')
A.plot(Y[~acc], H[~acc], 'o', ms=1.6, color=RED, mec='none')
for (y, v) in ((.9, .5), (.37, .8)):
    A.plot([y], [v/4], 'o', ms=4.2, mfc='white', mec=INK, mew=.9, zorder=6)
A.text(.62, .262, '$Mq(x)=1/4$', fontsize=7.5, color=INK)
A.text(.40, .085, r'$\widetilde{p}(x)$', fontsize=7.5, color=INK)
A.set_xlim(0, 1); A.set_ylim(0, .3); A.set_xticks([0, .37, .9]); A.set_xticklabels(['0', '0.37', '0.9']); A.set_yticks([0, .1, .2, .25]); A.set_yticklabels(['0', '0.1', '0.2', '0.25'])
sub(A, 'a', '$y$')
Y2, V2 = rng.random(6000), rng.random(6000)
keep = Y2[V2/4 <= Y2*(1-Y2)]
B.hist(keep, bins=np.linspace(0, 1, 21), density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
B.plot(x, 6*x*(1-x), color=BLUE, lw=1.4)
B.set_xlim(0, 1); B.set_ylim(0, 1.7); B.set_yticks([0, .5, 1, 1.5])
B.set_ylabel('密度'); sub(B, 'b', '$x$')
save(fig, HERE(__file__), 'figure', {'acc_rate_a': float(acc.mean()), 'acc_rate_b': len(keep)/6000, 'theory': 2/3})
print(acc.mean(), len(keep)/6000)
