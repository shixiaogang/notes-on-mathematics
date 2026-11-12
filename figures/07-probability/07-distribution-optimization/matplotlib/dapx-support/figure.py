from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# (a) target Exp(1) (blue), candidate N(1,1) (yellow); red fill: candidate mass on x<0 where the target density is 0,
#     Q(X<0)=Phi(-1)=0.1587, so D(Q||Pi)=+inf for every Gaussian candidate.
# (b) target standard Cauchy, candidate N(0,1): integrands of D(Pi||Q) (blue) and D(Q||Pi) (yellow).
#     pi ln(pi/q) -> 1/(2 pi) as |x|->inf, so D(Pi||Q)=+inf; the yellow integrand decays like a Gaussian.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.27, wspace=.28)
ax = axs[0]
x = np.linspace(-3, 5, 1601)
pe = np.where(x >= 0, np.exp(-np.clip(x, 0, None)), 0.)
q = npdf(x, 1, 1)
neg = x <= 0
ax.fill_between(x[neg], 0, q[neg], color=RED_FILL, lw=0)
ax.plot(x[neg], q[neg], color=RED, lw=1.6)
ax.plot(x[~neg], q[~neg], color=YELLOW, lw=1.6)
ax.plot(x[x >= 0], pe[x >= 0], color=BLUE, lw=1.4)
ax.plot([-3, 0], [0, 0], color=BLUE, lw=1.4)
ax.plot([0, 0], [0, 1], color=BLUE, lw=.85, ls=DOT)
lab(ax, .35, .9, r'$\pi$', BLUE)
lab(ax, 2.2, .3, r'$q$', YELLOW)
ax.annotate('', xy=(-.5, .06), xytext=(-1.6, .5), arrowprops=dict(arrowstyle='->', color=RED, lw=.85))
lab(ax, -2.9, .54, r'$Q(X<0)\approx0.159$', RED, fontsize=7)
ax.set_xlim(-3, 5); ax.set_ylim(0, 1.05)
axlab(ax, '$x$', None)
ax = axs[1]
x = np.linspace(-10, 10, 2001)
pc = 1/(np.pi*(1+x*x)); qn = npdf(x)
fw = pc*np.log(pc/qn)
rv = qn*(np.log(qn)-np.log(pc))
ax.plot(x, fw, color=BLUE, lw=1.4)
ax.plot(x, rv, color=YELLOW, lw=1.6)
ax.axhline(1/(2*np.pi), color=PURPLE, lw=.85, ls=DASH)
ax.axhline(0, color=STROKE, lw=.85)
lab(ax, 4.2, .2, r'$\pi\ln(\pi/q)$', BLUE)
lab(ax, 2.6, -.08, r'$q\ln(q/\pi)$', YELLOW)
lab(ax, -9.6, .172, r'$1/(2\pi)$', PURPLE, fontsize=7)
ax.set_xlim(-10, 10); ax.set_ylim(-.12, .26)
axlab(ax, '$x$', None)
tags(fig, axs)
from math import erf, sqrt
save(fig, HERE, 'figure', {'Q(X<0)': 0.5*(1+erf(-1/sqrt(2))), 'forward_integrand_limit': 1/(2*np.pi),
                           'reverse_KL_cauchy_gauss_numeric': float(np.sum(rv)*(x[1]-x[0]))})
