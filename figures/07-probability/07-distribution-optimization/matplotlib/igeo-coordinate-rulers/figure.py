"""Local KL rulers for N(0,v) at v=0.5,1,2,4 with eps=0.01: intervals {(1/2) G d^2 <= eps}.
(a) variance coordinate v, G=1/(2v^2): half-length 2 v sqrt(eps)=0.2 v. (b) tau=ln v, G=1/2: half-length 2 sqrt(eps)=0.2."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, (a, b) = figure(width_mm=104, height_mm=44, nrows=2)
eps = 0.01; vs = np.array([0.5, 1, 2, 4])
for ax, xs, hl, lim, lab in ((a, vs, 2*vs*np.sqrt(eps), (0, 5), r'$v=\sigma^{2}$'),
                             (b, np.log(vs), np.full(4, 2*np.sqrt(eps)), (-1.2, 1.9), r'$\tau=\ln\sigma^{2}$')):
    for x0, h in zip(xs, hl):
        ax.plot([x0-h, x0+h], [0, 0], color=BLUE, lw=4.0, solid_capstyle='butt')
        ax.scatter([x0], [0], s=12, color=RED, zorder=5)
    ax.set_xlim(*lim); ax.set_ylim(-0.6, 0.6); ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.set_xlabel(lab, labelpad=1)
a.set_xticks([0, 0.5, 1, 2, 3, 4, 5])
b.set_xticks(np.log(vs)); b.set_xticklabels([r'$\ln\frac{1}{2}$', r'$0$', r'$\ln 2$', r'$\ln 4$'])
save(fig, HERE, 'figure', {'half_lengths_v': (2*vs*np.sqrt(eps)).tolist(), 'half_length_tau': 2*np.sqrt(eps)})
