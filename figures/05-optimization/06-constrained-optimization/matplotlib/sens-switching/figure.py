from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# min theta*x on {-1,1}. Branch values and the selected solution.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
T = np.linspace(-1.2, 1.2, 241)
ax = axs[0]
ax.plot(T, T, color=GREEN, lw=1.1, ls='--', dashes=(3, 1.6), zorder=2); ax.plot(T, -T, color=YELLOW, lw=1.3, ls='--', dashes=(3, 1.6), zorder=2)
ax.plot(T, -abs(T), color=RED, lw=1.6, zorder=3)
ax.text(.72, .42, '$x=1$', fontsize=7.5, color=GREEN); ax.text(-1.12, .36, '$x=-1$', fontsize=7.5, color=YELLOW)
ax.text(.4, -.92, r'$V(\theta)$', fontsize=8, color=RED)
clean(ax, (-1.2, 1.2), (-1.3, 1.3), xlabel=r'$\theta$', sub='(a)', ylabel='目标值'); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
ax = axs[1]
ax.plot([-1.2, 0], [1, 1], color=RED, lw=1.6); ax.plot([0, 1.2], [-1, -1], color=RED, lw=1.6)
ax.plot([0, 0], [1, -1], 'o', color=RED, ms=4.4)
clean(ax, (-1.2, 1.2), (-1.5, 1.5), xlabel=r'$\theta$', sub='(b)', ylabel=r'$\bm{S}(\theta)$'.replace(r'\bm{S}', 'S')); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
save(fig, Path(__file__).resolve().parent, 'figure', {'V': '-|theta|'})
