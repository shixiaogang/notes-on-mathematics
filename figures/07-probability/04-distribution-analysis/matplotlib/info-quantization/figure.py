from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# X ~ N(0,1), cells [k D,(k+1) D). (a) density and cell masses for D = 1/2 (bars, height p_k/D).
# (b) exact H(X_D) (green points) and h(X) - ln D (blue line) versus D (log axis);
#     inset-free: the difference H(X_D)+ln D - h(X) is listed in the json facts.
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.28, top=.95, wspace=.3)
h = .5*math.log(2*math.pi*math.e)
def cells(D):
    ks = np.arange(-int(12/D)-1, int(12/D)+1)
    return ks, Phi((ks+1)*D) - Phi(ks*D)
D = .5; ks, p = cells(D)
a.bar(ks*D, p/D, width=D, align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.6)
x = np.linspace(-3.5, 3.5, 600); a.plot(x, np.exp(-x*x/2)/math.sqrt(2*math.pi), color=BLUE, lw=1.4)
a.set_xlim(-3.5, 3.5); a.set_ylim(0, .45); axlab(a, '$x$', '密度')
lab(a, 1.35, .3, r'$\Delta=\frac{1}{2}$', GREEN)
Ds = 2.0**np.arange(-6, 2.01, .25)
Hq = np.array([H(cells(d)[1]) for d in Ds])
b.plot(Ds, h - np.log(Ds), color=BLUE, lw=1.3)
pts = 2.0**np.arange(-6, 2)
b.plot(pts, [H(cells(d)[1]) for d in pts], 'o', color=GREEN, ms=3.2, mew=0)
b.set_xscale('log', base=2); b.minorticks_off()
b.set_xticks([1/64, 1/16, 1/4, 1, 4]); b.set_xticklabels(['$2^{-6}$', '$2^{-4}$', '$2^{-2}$', '$1$', '$4$'])
lab(b, 1/14, 4.9, r'$h(X)-\ln\Delta$', BLUE)
lab(b, 1/5.5, 1.5, r'$H(X_{\Delta})$', GREEN)
b.set_ylim(0, 6); axlab(b, r'$\Delta$', 'nat')
tags(fig, (a, b))
facts = {'h': h, 'gap': {str(d): float(H(cells(d)[1]) + math.log(d) - h) for d in (2, 1, .5, .25, .1, 1/64)}}
save(fig, HERE, 'figure', facts)
