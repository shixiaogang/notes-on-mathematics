"""Log-variance coordinate tau=ln sigma^2, displacement Delta. Blue: D(P_tau||P_{tau+Delta})=(Delta+e^{-Delta}-1)/2;
yellow: reverse direction (e^{Delta}-Delta-1)/2; purple dashed: quadratic Delta^2/4 = (1/2) G Delta^2 with G=1/2."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, ax = figure(width_mm=84, height_mm=50)
d = np.linspace(-2, 2, 400)
fwd = 0.5*(d+np.exp(-d)-1); rev = 0.5*(np.exp(d)-d-1); quad = d*d/4
ax.plot(d, rev, color=YELLOW, lw=1.6); ax.plot(d, fwd, color=BLUE, lw=1.4)
ax.plot(d, quad, color=PURPLE, lw=1.1, ls='--')
ax.set_xlim(-2, 2); ax.set_ylim(0, 1.6)
ax.set_xlabel(r'$\Delta$', labelpad=1); ax.set_ylabel('KL', labelpad=1)
ax.text(1.62, 0.78, r'$\frac{\Delta^{2}}{4}$', color=PURPLE)
save(fig, HERE, 'figure', {'fwd_0.5': 0.5*(0.5+np.exp(-0.5)-1), 'rev_0.5': 0.5*(np.exp(0.5)-1.5), 'quad_0.5': 0.0625,
                            'fwd_2': 0.5*(2+np.exp(-2)-1), 'rev_2': 0.5*(np.exp(2)-3)})
