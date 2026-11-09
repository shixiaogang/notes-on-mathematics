from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# min -p*x1-x2 on triangle tau=2. S(1)=hypotenuse; V(p)=-2*max(p,1).
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
ax = axs[0]
triangle(ax, 2)
for a in (.6, 1.3): ax.plot([0, a], [a, 0], color=BLUE, lw=.7, ls='--', zorder=2)
ax.plot([2, 0], [0, 2], color=RED, lw=2.2, zorder=5)
ax.plot([2], [0], 'o', color=RED, ms=4.4, zorder=6); ax.plot([0], [2], 'o', color=RED, ms=4.4, zorder=6)
ax.text(2.05, .13, r'$p>1$', fontsize=7.5, ha='left')
ax.text(.1, 2.08, r'$p<1$', fontsize=7.5, ha='left')
ax.text(1.14, 1.2, r'$p=1$', fontsize=7.5, color=RED)
ax.set_aspect('equal'); clean(ax, (-.15, 2.8), (-.15, 2.5), xlabel='$x_1$', ylabel='$x_2$', sub='(a)')
ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
ax = axs[1]
P = np.linspace(0, 2, 201); ax.plot(P, -2*np.maximum(P, 1), color=BLUE, lw=1.4)
opt_point(ax, (1, -2))
ax.text(.42, -1.86, '斜率 0', fontsize=7.5, ha='center'); ax.text(1.62, -2.85, '斜率 -2', fontsize=7.5, ha='left')
clean(ax, (0, 2), (-4.3, -1.3), xlabel='$p$', sub='(b)', ylabel='$V(p)$')
ax.set_xticks([0, 1, 2]); ax.set_yticks([-4, -3, -2])
save(fig, Path(__file__).resolve().parent, 'figure', {'V': '-2*max(p,1)'})
