from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# P=N(0,1), Q=Unif(-sqrt3,sqrt3); phi_P(w)=exp(-w^2/2), phi_Q(w)=sin(sqrt3 w)/(sqrt3 w).
# (a) |phi_P - phi_Q|^2 (blue) and Gaussian spectral weights exp(-sigma^2 w^2/2) for sigma=0.5,1,2
#     (normalised to 1 at w=0; purple, yellow, red dashed).
# (b) MMD_sigma(P,Q) = ( int |phi_P-phi_Q|^2 N(0,1/sigma^2)(dw) )^{1/2}, quadrature on [-60,60].
r3 = math.sqrt(3)
w = np.linspace(-60, 60, 240001)
with np.errstate(invalid='ignore', divide='ignore'):
    pq = np.where(w == 0, 1., np.sin(r3*w)/(r3*w))
d2 = (np.exp(-w*w/2)-pq)**2


def mmd(s):
    lam = np.exp(-(s*w)**2/2)*s/math.sqrt(2*math.pi)
    return math.sqrt(np.trapezoid(d2*lam, w))


fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.98, top=.95, bottom=.26, wspace=.32)
ax = axs[0]
m = (w >= 0) & (w <= 8)
ax.plot(w[m], d2[m]/d2[m].max(), color=BLUE, lw=1.4)
for s, c in ((.5, PURPLE), (1., YELLOW), (2., RED)):
    ax.plot(w[m], np.exp(-(s*w[m])**2/2), color=c, lw=1.1, ls=DASH)
lab(ax, 3.3, .95, r'$|\phi_P-\phi_Q|^2$', BLUE, ha='left')
ax.set_xlim(0, 8); ax.set_ylim(0, 1.08); ax.set_yticks([0, .5, 1])
axlab(ax, r'$\omega$', '相对大小')
ax = axs[1]
ss = np.linspace(.1, 5, 120)
M = np.array([mmd(s) for s in ss])
ax.plot(ss, M, color=BLUE, lw=1.4)
facts = {}
for s, c in ((.5, PURPLE), (1., YELLOW), (2., RED)):
    v = mmd(s); facts[str(s)] = v
    dot(ax, s, v, c, ms=4)
ax.set_xlim(0, 5); ax.set_ylim(0, M.max()*1.15)
axlab(ax, r'$\sigma$', r'$\mathrm{MMD}_{k_\sigma}(P,Q)$')
tags(fig, axs)
facts['d2max'] = float(d2[m].max()); facts['argmax'] = float(w[m][np.argmax(d2[m])])
save(fig, HERE, 'figure', facts)
