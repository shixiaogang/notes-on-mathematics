from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# (a) Unif(0,a), a = 1/2, 1, 2: h = ln a = -0.693, 0, 0.693 nat.
# (b) N(0,s^2), s = 1/2, 1, 2: h = 0.5 ln(2 pi e s^2) = 0.726, 1.419, 2.112 nat.
fig, (a, b) = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, bottom=.3, top=.95, wspace=.28)
cols = (YELLOW, BLUE, PURPLE)
facts = {}
for w, c in zip((.5, 1, 2), cols):
    a.plot([0, 0, w, w], [0, 1/w, 1/w, 0], color=c, lw=1.3)
    facts['unif_%g' % w] = math.log(w)
lab(a, .52, 1.95, r'$a=\frac{1}{2}$: $h=-\ln 2$', YELLOW)
lab(a, 1.04, 1.03, '$a=1$: $h=0$', BLUE)
lab(a, 1.15, .56, r'$a=2$: $h=\ln 2$', PURPLE)
a.set_xlim(-.1, 2.5); a.set_ylim(0, 2.25); axlab(a, '$x$', '密度')
x = np.linspace(-6, 6, 801)
for s, c in zip((.5, 1, 2), cols):
    b.plot(x, np.exp(-x*x/(2*s*s))/(s*math.sqrt(2*math.pi)), color=c, lw=1.3)
    facts['gauss_%g' % s] = .5*math.log(2*math.pi*math.e*s*s)
lab(b, .75, .72, r'$\sigma=\frac{1}{2}$: $h=%.3f$' % facts['gauss_0.5'], YELLOW)
lab(b, 1.2, .38, r'$\sigma=1$: $h=%.3f$' % facts['gauss_1'], BLUE)
lab(b, 1.7, .22, r'$\sigma=2$: $h=%.3f$' % facts['gauss_2'], PURPLE)
b.set_xlim(-6, 6); b.set_ylim(0, .85); axlab(b, '$x$', '密度')
tags(fig, (a, b))
save(fig, HERE, 'figure', facts)
