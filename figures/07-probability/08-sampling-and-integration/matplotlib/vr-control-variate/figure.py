from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# I = E[e^U], U ~ Unif(0,1), control h(U) = U with E h = 1/2.
# (a) f(u) = e^u, the fitted line I + beta*(u - 1/2), and the corrected integrand e^u - beta*(u-1/2); the four teaching
#     uniforms 0.37, 0.81, 0.06, 0.52 marked.  (b) Var(f - beta(h - 1/2)) = s2 - 2 beta c + beta^2/12 as a function of beta.
s2 = (E*E-1)/2 - (E-1)**2; c = 1 - (E-1)/2; bs = 12*c; I = E-1
u4 = np.array(U5[:4]); y4 = np.exp(u4)
sc = np.cov(u4, y4)[0, 1]; bh = sc/np.var(u4, ddof=1)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.26)
a, b = axs
u = np.linspace(0, 1, 300)
a.plot(u, np.exp(u), color=BLUE, lw=1.4)
a.plot(u, I + bs*(u-.5), color=PURPLE, lw=.9, ls=DASH)
a.plot(u, np.exp(u) - bs*(u-.5), color=GREEN, lw=1.4)
for ui in u4:
    dot(a, ui, math.exp(ui), color=BLUE, ms=3.4)
    dot(a, ui, math.exp(ui) - bs*(ui-.5), color=GREEN, ms=3.4)
a.set_xlim(0, 1); a.set_ylim(.8, 2.8); a.set_xticks([0, .5, 1]); a.set_yticks([1, 1.5, 2, 2.5])
lab(a, .62, 2.25, r'$\mathrm{e}^{u}$', BLUE); lab(a, .03, 2.0, r'$\mathrm{e}^{u}-\beta^{*}(u-\frac{1}{2})$', GREEN)
axlab(a, '$u$')
beta = np.linspace(-.3, 3.4, 300); V = s2 - 2*beta*c + beta**2/12
b.plot(beta, V, color=BLUE, lw=1.4)
dot(b, 0, s2, color=BLUE); lab(b, .1, s2+.012, '直接平均', BLUE)
dot(b, bs, s2 - c*c*12); lab(b, bs-.35, .03, r'$\beta^{*}\approx1.690$', RED)
dot(b, bh, s2 - 2*bh*c + bh**2/12, color=GREEN, ms=3.4)
b.set_xlim(-.3, 3.4); b.set_ylim(0, .3); b.set_xticks([0, 1, 2, 3]); b.set_yticks([0, .1, .2, .3])
axlab(b, r'$\beta$')
tags(fig, axs)
save(fig, HERE, 'figure', {'sigma2': s2, 'cov': c, 'beta_star': bs, 'min_var': s2-12*c*c, 'beta_hat_4': float(bh),
     'var_at_beta_hat': float(s2 - 2*bh*c + bh**2/12), 'plain_mean_4': float(y4.mean()),
     'cv_hat_4': float(y4.mean() - bh*(u4.mean()-.5)), 'cv_star_4': float(y4.mean() - bs*(u4.mean()-.5))})
