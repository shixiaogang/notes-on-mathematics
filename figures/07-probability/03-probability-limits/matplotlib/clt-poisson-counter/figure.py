from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Two standardized binomial counts with mean 0 and variance 1, n = 100.
# (a) Bin(100,1/2): masses divided by the lattice spacing 1/sd, against phi;
# (b) Bin(100,1/100): standardized count is close to Poisson(1)-1, not bell-shaped.
n = 100
fig, (a, b) = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.11, right=.97, bottom=.28, wspace=.24)
x = np.linspace(-4, 4, 400)
facts = {}
for ax, p in ((a, .5), (b, .01)):
    pm = binpmf(n, p); sd = math.sqrt(n*p*(1-p)); z = (np.arange(n+1)-n*p)/sd
    m = (z > -4) & (z < 4.5)
    ax.vlines(z[m], 0, pm[m]*sd, color=GREEN, lw=1.6 if p < .1 else .9)
    ax.plot(x, phi(x), color=BLUE, lw=1.4)
    ax.set_xlim(-4, 4.5); ax.set_xticks([-4, -2, 0, 2, 4])
    facts['p=%g' % p] = {'sd': sd, 'P(S=0)': float(pm[0]), 'P(S=1)': float(pm[1])}
a.set_ylim(0, .45); b.set_ylim(0, .45)
axlab(a, '$z$', '质量 / 格点间距'); axlab(b, '$z$')
lab(b, -1.05, .38, r'$S=0$', GREEN, ha='right'); lab(b, .12, .425, r'$S=1$', GREEN, ha='left'); lab(b, 1.05, .2, r'$S=2$', GREEN, ha='left')
lab(b, -2.3, .1, r'$\varphi$', BLUE, ha='left'); lab(a, 1.5, .25, r'$\varphi$', BLUE, ha='left')
tags(fig, (a, b))
save(fig, HERE, 'figure', facts)
