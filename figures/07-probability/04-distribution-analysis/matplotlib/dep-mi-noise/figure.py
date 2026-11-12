"""(a) I(X; X^2 + sigma Z) for X ~ Unif(-1,1), Z ~ N(0,1) independent, computed as h(Y) - 0.5 ln(2 pi e sigma^2)
by quadrature; purple dashed reference ln(1/sigma) + c with c matched at sigma = 0.01.
(b) Bivariate Gaussian I = -0.5 ln(1 - rho^2) (nat); red dot rho = 0.5, 0.144."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

S = np.logspace(-2.3, 0, 22)
I = np.array([parabola_mi(s, 20000) for s in S])
fig, axs = figure(width_mm=110, height_mm=46, ncols=2)
ax = axs[0]
ax.plot(S, I, color=BLUE, lw=1.4)
c = I[0]-math.log(1/S[0])
ax.plot(S, np.log(1/S)+c, color=PURPLE, lw=.9, ls='--')
for s in (.1, .2):
    v = parabola_mi(s, 20000); ax.plot([s], [v], 'o', color=RED, ms=3)
ax.set_xscale('log'); ax.invert_xaxis()
ax.set_xlabel('$\\sigma$', labelpad=0); ax.set_ylabel('互信息（nat）', labelpad=1)
ax.set_ylim(0, 4.6)
ax.set_box_aspect(.8)
tag(ax, '(a)', y=-.3)
ax = axs[1]
r = np.linspace(0, .995, 400)
ax.plot(r, gauss_mi(r), color=BLUE, lw=1.4)
ax.plot([.5], [gauss_mi(.5)], 'o', color=RED, ms=3)
ax.set_xlim(0, 1); ax.set_ylim(0, 2.6); ax.set_xticks([0, .5, 1])
ax.set_xlabel('$\\rho$', labelpad=0)
ax.set_box_aspect(.8)
tag(ax, '(b)', y=-.3)
save(fig, HERE, 'figure', {'sigma': S.tolist(), 'MI': I.tolist(), 'MI_sigma_0.1': parabola_mi(.1, 20000), 'MI_sigma_0.2': parabola_mi(.2, 20000), 'offset_c': c})
