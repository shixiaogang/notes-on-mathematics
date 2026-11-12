from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# P=N(0,1), Q=N(delta,1), M=(P+Q)/2.
# (a) densities for delta=3 with the mixture M (purple, dashed).
# (b) KL(P||Q)=delta^2/2 (yellow) and JS(P,Q) by quadrature on [-12, delta+12] (blue); JS <= ln 2 (purple dashed).
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.98, top=.95, bottom=.26, wspace=.28)
ax = axs[0]
x = np.linspace(-3.5, 6.5, 1200); d0 = 3.
p, q = npdf(x), npdf(x, d0); m = (p+q)/2
ax.plot(x, p, color=BLUE, lw=1.4); ax.plot(x, q, color=YELLOW, lw=1.6)
ax.plot(x, m, color=PURPLE, lw=1.3, ls=DASH)
lab(ax, -1.9, .3, '$P$', BLUE, ha='center', fontsize=8)
lab(ax, 4.9, .3, '$Q$', YELLOW, ha='center', fontsize=8)
lab(ax, 1.5, .27, '$M$', PURPLE, ha='center', fontsize=8)
ax.set_xlim(-3.5, 6.5); ax.set_ylim(0, .45); ax.set_yticks([0, .2, .4])
axlab(ax, '$x$', '密度')


def js(d):
    t = np.linspace(-12, d+12, 40001)
    a, b = npdf(t), npdf(t, d); mm = (a+b)/2
    with np.errstate(divide='ignore', invalid='ignore'):
        ia = np.where(a > 0, a*np.log(a/mm), 0.); ib = np.where(b > 0, b*np.log(b/mm), 0.)
    return .5*np.trapezoid(ia, t)+.5*np.trapezoid(ib, t)


ds = np.linspace(0, 6, 121)
J = np.array([js(d) for d in ds])
ax = axs[1]
ax.plot(ds, ds**2/2, color=YELLOW, lw=1.6)
ax.plot(ds, J, color=BLUE, lw=1.4)
ax.axhline(math.log(2), color=PURPLE, lw=.9, ls=DASH)
lab(ax, 2.35, 1.55, r'$D_{\mathrm{KL}}(P\Vert Q)$', YELLOW, ha='right')
lab(ax, 4.4, .45, r'$D_{\mathrm{JS}}(P,Q)$', BLUE, ha='center')
lab(ax, 5.9, .76, r'$\ln 2$', PURPLE, ha='right')
ax.set_xlim(0, 6); ax.set_ylim(0, 2.0); ax.set_xticks([0, 2, 4, 6])
axlab(ax, r'$\Delta$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'JS(delta=1)': float(js(1.)), 'JS(delta=3)': float(js(3.)), 'JS(delta=6)': float(js(6.))})
