from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"budget-common"))
from budget_fig import *
# (a) I = int_0^1 e^u du, sigma^2 = (e^2-1)/2-(e-1)^2, tolerance eps = 0.01.
#     Samples needed so that P(|I_n - I| > eps) <= delta: Chebyshev sigma^2/(delta eps^2), normal approx z^2 sigma^2/eps^2.
# (b) I = P(X > 4), X ~ Exp(1), per-sample variance I(1-I); 95% normal approximation.
#     absolute eps = 1e-3, relative 10%, mixed max(1e-3, 0.1 I), plotted against a generic tail probability I.
def zq(p):
    lo, hi = 0.0, 10.0
    for _ in range(80):
        m = (lo+hi)/2
        if Phi(m) < p: lo = m
        else: hi = m
    return (lo+hi)/2
s2 = (E*E-1)/2-(E-1)**2; eps = 0.01
d = np.logspace(-3, np.log10(0.3), 200)
ncheb = s2/(d*eps**2); nnorm = np.array([zq(1-x/2)**2 for x in d])*s2/eps**2
fig, axs = figure(width_mm=108, height_mm=52, ncols=2)
a1, a2 = axs
panel(fig, left=.1, right=.98, bottom=.3, top=.96, wspace=.38)
a1.plot(d, ncheb, color=PURPLE, lw=1.4); a1.plot(d, nnorm, color=BLUE, lw=1.4)
a1.set_xscale('log'); a1.set_yscale('log'); a1.set_xlim(1e-3, .3); a1.set_ylim(2e3, 5e6)
logticks(a1, [-3, -2, -1], 'x'); logticks(a1, [4, 5, 6])
z95 = zq(.975)
dot(a1, .05, s2/(.05*eps**2)); dot(a1, .05, z95**2*s2/eps**2)
lab(a1, .055, s2/(.05*eps**2)*1.35, 'Chebyshev', PURPLE)
lab(a1, .0013, 6.2e3, '正态近似', BLUE)
axlab(a1, r'$\delta$', '所需样本数')
I = np.logspace(-6, np.log10(.5), 300); z2 = z95**2
nabs = z2*I*(1-I)/1e-3**2; nrel = z2*(1-I)/(0.01*I); nmix = z2*I*(1-I)/np.maximum(1e-3, .1*I)**2
a2.plot(I, nmix, color=BLUE, lw=2.4, solid_capstyle='butt')
a2.plot(I, nabs, color=GREEN, lw=1.2, ls=DASH); a2.plot(I, nrel, color=YELLOW, lw=1.4, ls=DASH)
a2.set_xscale('log'); a2.set_yscale('log'); a2.set_xlim(1e-6, .5); a2.set_ylim(10, 1e9)
logticks(a2, [-6, -4, -2], 'x'); logticks(a2, [1, 3, 5, 7, 9])
It = math.exp(-4)
dot(a2, It, z2*It*(1-It)/1e-6); dot(a2, It, z2*(1-It)/(0.01*It))
a2.axvline(1e-2, color=STROKE, lw=.85, ls=DOT)
lab(a2, 2e-6, 2.5e8, '相对 10%', YELLOW)
lab(a2, 2e-6, 25, '绝对 0.001', GREEN)
lab(a2, 3e-4, 40, '混合', BLUE)
axlab(a2, r'$I$', '所需样本数')
tags(fig, axs)
save(fig, HERE, 'figure', {'sigma2': s2, 'eps': eps, 'cheb_n_delta05': s2/(.05*eps**2), 'normal_n_delta05': z95**2*s2/eps**2,
     'tail_I': It, 'n_abs_1e-3': z2*It*(1-It)/1e-6, 'n_rel_10pct': z2*(1-It)/(0.01*It), 'mixed_switch_I': 1e-2})
