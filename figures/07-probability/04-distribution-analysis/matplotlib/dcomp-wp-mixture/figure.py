from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcomp-common"))
from common import *
# mu=delta_0, nu_eps=(1-eps)delta_0+eps delta_1 on R. W_p(mu,nu_eps)=eps^{1/p} (only eps mass moves distance 1);
# any integral probability metric is linear: d_F(mu,nu_eps)=eps d_F(delta_0,delta_1). p=1 (blue), 2 (yellow), 4 (purple).
fig, ax = figure(width_mm=80, height_mm=52)
e = np.linspace(0, 1, 500)
for pp, c, y in ((1, BLUE, .5), (2, YELLOW, .75), (4, PURPLE, .9)):
    ax.plot(e, e**(1/pp), color=c, lw=1.4 if c != YELLOW else 1.6)
lab(ax, .62, .5, '$W_1=\\varepsilon$', BLUE, ha='left')
lab(ax, .3, .66, '$W_2=\\sqrt{\\varepsilon}$', YELLOW, ha='left')
lab(ax, .1, .86, '$W_4$', PURPLE, ha='left')
ax.set_xlim(0, 1); ax.set_ylim(0, 1.05); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$\varepsilon$', None)
save(fig, HERE, 'figure', {'W2(eps=0.04)': .2})
