from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Fix x2=4 in f=x1^2+x1x2+x2^2: conditional min at x1=-2 with value 12; global min 0.
fig, (a, b) = figure(width_mm=112, height_mm=58, ncols=2)
panel(fig, .085, .985, .97, .25, wspace=.27)
contour_c(a, (-5, 4.5), (-2.4, 5.4), [3, 12, 22, 37])
a.plot([-5, 4.5], [4, 4], color=MUTED, lw=.85, ls=(0, (3, 2)))
a.plot([3, -2], [4, 4], color=GREEN, lw=1.4, zorder=4); a.plot([3, -2], [4, 4], 'o', color=GREEN, ms=4, mew=0, zorder=5); opt(a)
a.text(2.2, 4.3, '$(3,4)$', fontsize=7.5, color=INK); a.text(-3.4, 4.3, '$(-2,4)$', fontsize=7.5, color=INK); a.text(.3, -.7, '$x^*$', fontsize=8, color=INK)
a.set_xlabel('$x_1$', labelpad=1); a.set_ylabel('$x_2$', labelpad=1); a.set_aspect('equal'); a.set_xlim(-5, 4.5); a.set_ylim(-2.4, 5.4)
z = np.linspace(-6, 4, 300); phi = z**2 + 4*z + 16
b.plot(z, phi, color=BLUE, lw=1.4); b.plot([3, -2], [37, 12], 'o', color=GREEN, ms=4, mew=0, zorder=5)
b.axhline(0, color=PURPLE, lw=.95, ls=(0, (3, 2)))
b.text(2.1, 39.5, '37', fontsize=7.5, color=INK); b.text(-2.5, 15, '12', fontsize=7.5, color=INK); b.text(-5.6, 2, '$f^*=0$', fontsize=7.5, color=INK)
b.set_xlabel('$z$', labelpad=1); b.set_ylabel(r'$\varphi(z)$', labelpad=5); b.set_xlim(-6, 4); b.set_ylim(-3, 46)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'formula': 'phi(z)=z^2+4z+16'})
