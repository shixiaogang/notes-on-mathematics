from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Cyclic exact coordinate minimisation of x1^2+c x1 x2+x2^2 from (3,4), c=1 (both orders) and c=1.8.
fig, (a, b) = figure(width_mm=112, height_mm=62, ncols=2)
panel(fig, .08, .985, .97, .22, wspace=.24)
contour_c(a, (-3.5, 4.5), (-3, 5), [.75, 3, 12, 22, 37])
P1 = cyclic((3, 4), 1, (0, 1), 6); P2 = cyclic((3, 4), 1, (1, 0), 6)
path(a, P2, YELLOW, lw=1.6); path(a, P1, GREEN); opt(a)
a.text(3.15, 4.25, '$x^{(0)}$', fontsize=8, color=INK); a.text(-3.2, 4.3, r'$1\to2$', fontsize=7.5, color=INK); a.text(3.2, -1.6, r'$2\to1$', fontsize=7.5, color=INK)
a.set_xlabel('$x_1$', labelpad=1); a.set_ylabel('$x_2$', labelpad=1); a.set_aspect('equal'); a.set_xlim(-3.5, 4.5); a.set_ylim(-3, 5)
contour_c(b, (-5.2, 5.2), (-5.2, 5.2), [.2, 1, 3, 8, 16, 30, 53], c=1.8)
P3 = cyclic((3, 4), 1.8, (0, 1), 24); path(b, P3, GREEN, ms=2.6, lw=1.1); opt(b)
b.text(3.15, 4.35, '$x^{(0)}$', fontsize=8, color=INK)
b.set_xlabel('$x_1$', labelpad=1); b.set_aspect('equal'); b.set_xlim(-5.2, 5.2); b.set_ylim(-5.2, 5.2)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'c_values': [1, 1.8], 'P1_first': P1[:5].tolist()})
