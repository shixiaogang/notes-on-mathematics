"""Two joint laws ranked differently by two measures (500 samples each, seed 719):
(a) standard bivariate Gaussian rho = 0.6: MI = 0.223 nat, dCor = 0.550;
(b) X ~ Unif(-1,1), Y = X^2 + 0.1 Z: MI = 1.03 nat, dCor = 0.461 (quadrature).
Also records HSIC with Gaussian kernels whose bandwidths equal each coordinate's standard deviation."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

rng = np.random.default_rng(SEED)
n = 500
z1 = rng.standard_normal(n); z2 = .6*z1+.8*rng.standard_normal(n)
x = rng.uniform(-1, 1, n); y = x**2+.1*rng.standard_normal(n)
miA, dcA = float(gauss_mi(.6)), float(gauss_dcor(.6))
miB, dcB = parabola_mi(.1, 20000), parabola_dcor(.1, 1200)
sdY = math.sqrt(4/45+.01)
hsA = float(gauss_hsic(.6, 1.0)); hsB = parabola_hsic(.1, 1/math.sqrt(3), sdY, 1200)
fig, axs = figure(width_mm=100, height_mm=48, ncols=2)
for ax, (u, v), lab, txt in [(axs[0], (z1, z2), '(a)', f'$I={miA:.3f}$, dCor$={dcA:.3f}$'),
                             (axs[1], (x, y), '(b)', f'$I={miB:.2f}$, dCor$={dcB:.3f}$')]:
    ax.scatter(u, v, s=1.2, color=GREEN, linewidths=0)
    ax.set_box_aspect(.85)
    ax.text(.5, 1.04, txt, transform=ax.transAxes, ha='center', va='bottom', fontsize=7.5, color=MUTED)
    ax.set_xlabel('$x$', labelpad=0); ax.set_ylabel('$y$', labelpad=0)
    gfmt(ax)
    tag(ax, lab, y=-.3)
axs[0].set_xlim(-3.3, 3.3); axs[0].set_ylim(-3.3, 3.3); axs[0].set_xticks([-3, 0, 3]); axs[0].set_yticks([-3, 0, 3])
axs[1].set_xlim(-1.05, 1.05); axs[1].set_ylim(-.35, 1.35); axs[1].set_xticks([-1, 0, 1]); axs[1].set_yticks([0, .5, 1])
save(fig, HERE, 'figure', {'seed': SEED, 'MI': [miA, miB], 'dCor': [dcA, dcB], 'HSIC_sd_bandwidth': [hsA, hsB]})
