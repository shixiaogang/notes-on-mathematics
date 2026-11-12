from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Fair coin, S_n ~ Bin(n,1/2), n = 10, 40, 160 (exact masses).
# (a) centred count S_n - n/2: spread grows like sqrt(n)/2;
# (b) centred proportion S_n/n - 1/2: spread shrinks like 1/(2 sqrt(n)).
NS = (10, 40, 160); COLS = (YELLOW, PURPLE, BLUE)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.97, bottom=.28, wspace=.3)
facts = {}
for n, c in zip(NS, COLS):
    pm = binpmf(n); k = np.arange(n+1)
    a.plot(k-n/2, pm, '-o', color=c, lw=1.0, ms=2.0, mew=0)
    b.plot(k/n-.5, pm*n, '-o', color=c, lw=1.0, ms=2.0, mew=0)
    facts[str(n)] = {'sd_count': (n/4)**.5, 'sd_mean': (1/(4*n))**.5}
lab(a, 1.2, .245, '$n=10$', YELLOW, ha='left'); lab(a, 3.6, .118, '$n=40$', PURPLE, ha='left'); lab(a, 6.5, .052, '$n=160$', BLUE, ha='left')
lab(b, .1, 2.6, '$n=10$', YELLOW, ha='left'); lab(b, .085, 4.6, '$n=40$', PURPLE, ha='left'); lab(b, .06, 9.0, '$n=160$', BLUE, ha='left')
a.set_xlim(-20, 20); a.set_ylim(0, .27); a.set_xticks([-20, -10, 0, 10, 20])
b.set_xlim(-.5, .5); b.set_ylim(0, 10.5); b.set_xticks([-.5, -.25, 0, .25, .5])
axlab(a, '$S_n-n/2$', '质量'); axlab(b, r'$\bar{X}_n-1/2$', '质量 / 格点间距')
tags(fig, (a, b))
save(fig, HERE, 'figure', facts)
