from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# From (3,4), f=x1^2+x1x2+x2^2: the two possible exact coordinate updates and their mean decrease.
fig, (a, b) = figure(width_mm=112, height_mm=58, ncols=2)
panel(fig, .085, .985, .97, .25, wspace=.3)
contour_c(a, (-3.4, 4.4), (-2.8, 5), [6.75, 12, 37])
a.plot([3, -2], [4, 4], color=GREEN, lw=1.4, zorder=4); a.plot([3, 3], [4, -1.5], color=GREEN, lw=1.4, zorder=4)
a.plot([3, -2, 3], [4, 4, -1.5], 'o', color=GREEN, ms=4, mew=0, zorder=5); opt(a)
a.text(3.15, 4.2, '$(3,4)$', fontsize=7.5, color=INK); a.text(-3.2, 4.3, '$(-2,4)$', fontsize=7.5, color=INK); a.text(3.12, -2.3, r'$(3,-\frac{3}{2})$', fontsize=7.5, color=INK, ha='center')
a.set_xlabel('$x_1$', labelpad=1); a.set_ylabel('$x_2$', labelpad=1); a.set_aspect('equal'); a.set_xlim(-3.4, 4.4); a.set_ylim(-2.8, 5)
vals = [37, 12, 6.75, 9.375]; cols = [BLUE, GREEN, GREEN, PURPLE]
b.bar(range(4), vals, color=cols, width=.6)
for i, v in enumerate(vals): b.text(i, v+.9, f'{v:g}', fontsize=7.5, color=INK, ha='center')
b.set_xticks(range(4)); b.set_xticklabels(['当前', '选1', '选2', '平均']); b.set_ylabel('目标值', labelpad=1); b.set_ylim(0, 43)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'values': vals})
