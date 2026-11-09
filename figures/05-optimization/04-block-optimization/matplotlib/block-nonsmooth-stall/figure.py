from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# F(u,v)=2|u-v|+|u+v-2|: origin is coordinatewise minimal, global min at (1,1).
F = lambda u, v: 2*abs(u-v)+abs(u+v-2)
fig, (a, b) = figure(width_mm=112, height_mm=60, ncols=2)
panel(fig, .105, .985, .97, .23, wspace=.27)
U, V = np.meshgrid(np.linspace(-1, 2.4, 700), np.linspace(-1, 2.4, 700))
a.contour(U, V, F(U, V), levels=[.5, 1, 2, 3, 4, 5], colors=[BLUE], linewidths=.65)
a.plot([-1, 2.4], [0, 0], color=MUTED, lw=.85, ls=(0, (3, 2))); a.plot([0, 0], [-1, 2.4], color=MUTED, lw=.85, ls=(0, (3, 2)))
a.annotate('', xy=(.82, .82), xytext=(.05, .05), arrowprops=dict(arrowstyle='-|>', color=PURPLE, lw=1.2, shrinkA=0, shrinkB=0))
a.plot([0], [0], 'o', ms=4.5, color=GREEN, mew=0, zorder=5); opt(a, 1, 1)
a.text(.08, -.28, '原点', fontsize=7.5, color=INK); a.text(1.12, 1.14, '$(1,1)$', fontsize=7.5, color=INK, bbox=dict(fc='white', ec='none', pad=.6))
a.set_xlabel('$u$', labelpad=1); a.set_ylabel('$v$', labelpad=1); a.set_aspect('equal'); a.set_xlim(-1, 2.4); a.set_ylim(-1, 2.4)
t = np.linspace(-1, 2, 300)
b.plot(t, F(t, 0*t), color=BLUE, lw=1.4); b.plot(t, F(t, t), color=YELLOW, lw=1.6)
b.plot([0], [2], 'o', ms=4.5, color=GREEN, mew=0, zorder=5); opt(b, 1, 0)
b.text(-.42, 4.3, '$F(u,0)$', fontsize=7.5, color=INK); b.text(1.3, .25, '$F(s,s)$', fontsize=7.5, color=INK)
b.set_xlabel(r'$u,\ s$', labelpad=1); b.set_xlim(-1, 2); b.set_ylim(-.2, 5.5)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'formula': '2|u-v|+|u+v-2|'})
