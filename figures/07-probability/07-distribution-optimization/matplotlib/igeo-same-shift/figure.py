"""Same mean shift 0.5 at two scales: (a) N(0,0.25) vs N(0.5,0.25), KL=0.5; (b) N(0,4) vs N(0.5,4), KL=1/32."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, axs = figure(width_mm=108, height_mm=46, ncols=2)
for ax, sd, lab in zip(axs, (0.5, 2.0), ('(a)', '(b)')):
    x = np.linspace(-6.5, 6.5, 800); v = sd*sd
    ax.fill_between(x, npdf(x, 0, v), color=BLUE_FILL, lw=0)
    ax.plot(x, npdf(x, 0, v), color=BLUE, lw=1.4)
    ax.plot(x, npdf(x, 0.5, v), color=YELLOW, lw=1.6)
    top = npdf(0, 0, v)
    ax.plot([0, 0.5], [-0.06*top]*2, color=RED, lw=2.0, solid_capstyle='butt')
    ax.plot([0, 0], [-0.09*top, -0.03*top], color=RED, lw=1.0); ax.plot([0.5, 0.5], [-0.09*top, -0.03*top], color=RED, lw=1.0)
    ax.set_ylim(-0.12*top, 1.12*top); ax.set_xlim(-6.5, 6.5)
    ax.set_xlabel(r'$x$', labelpad=1); ax.set_yticks([0, round(top, 2)])
    ax.text(0.97, 0.95, rf'$\sigma={sd:g}$', transform=ax.transAxes, ha='right', va='top')
    tag(ax, lab, y=-0.30)
save(fig, HERE, 'figure', {'kl_a': float(kl_gauss(0, .25, .5, .25)), 'kl_b': float(kl_gauss(0, 4, .5, 4))})
