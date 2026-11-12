"""Versions of y->K(y,A), A=[0,1/8], triangle model.
(a) density version (blue), one-point change at y=1/2 (red), change on [1/4,1/2] to Unif(0,1) giving 1/8 (yellow).
(b) integrands K(y,A) f_Y(y): the yellow change adds int_{1/4}^{1/2} (1/8)2(1-y)dy = 5/128 (light red)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
from matplotlib.colors import LinearSegmentedColormap
HERE = Path(__file__).resolve().parent
fig, (a, b) = figure(width_mm=104, height_mm=46, ncols=2)
y = np.linspace(0, 0.98, 800)
K = tri_kernel(y, 0, 0.125)
for ax, fac in ((a, np.ones_like(y)), (b, 2*(1 - y))):
    ax.plot(y, K*fac, color=BLUE, lw=1.4)
seg = np.linspace(0.25, 0.5, 100)
a.plot(seg, np.full_like(seg, 0.125), color=YELLOW, lw=1.8)
a.scatter([0.5], [1.0], s=16, color=RED, zorder=4)
a.text(0.53, 0.95, '$K\'(1/2,A)=1$', fontsize=7.5)
a.set_xlim(0, 1); a.set_ylim(0, 1.08); a.set_xticks([0, 0.125, 0.25, 0.5, 1]); a.set_xticklabels(['0', '', '0.25', '0.5', '1'])
a.set_yticks([0, 0.125, 0.5, 1]); a.set_yticklabels(['0', '1/8', '0.5', '1'])
a.set_xlabel('$y$', labelpad=1); a.set_ylabel('$K(y,A)$')
b.fill_between(seg, 0, 0.125*2*(1 - seg), color=RED_FILL, lw=0)
b.plot(seg, 0.125*2*(1 - seg), color=YELLOW, lw=1.8)
b.plot(y, 0.12*(1 - y)*2 + 0, color='none')
b.text(0.52, 0.15, '$5/128$', fontsize=7.5)
b.set_xlim(0, 1); b.set_ylim(0, 0.27); b.set_xticks([0, 0.25, 0.5, 1]); b.set_yticks([0, 0.1, 0.2])
b.set_xlabel('$y$', labelpad=1); b.set_ylabel('$K(y,A)\\,f_Y(y)$')

extra = np.trapezoid(0.125*2*(1 - seg), seg) if hasattr(np, 'trapezoid') else np.trapz(0.125*2*(1 - seg), seg)
tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'A': '[0,1/8]', 'extra_mass_numeric': float(extra), 'extra_mass_exact': '5/128'})
