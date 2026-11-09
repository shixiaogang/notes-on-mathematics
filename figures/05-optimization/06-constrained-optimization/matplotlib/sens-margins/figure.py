from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Branch with active set {1}: lam1=(3-tau)/2, x1=(tau+1)/2, x2=(tau-1)/2 continued outside its window.
fig, ax = figure(width_mm=100, height_mm=54)
T = np.linspace(0, 4, 201)
ax.axvspan(1, 3, facecolor=GREEN_FILL, edgecolor='none', zorder=0)
ax.axhline(0, color=STROKE, lw=.75, zorder=1)
L = (3-T)/2; X1 = (T+1)/2; X2 = (T-1)/2
ax.plot(T, X1, color=BLUE, lw=1.3, zorder=3); ax.plot(T, X2, color=BLUE, lw=1.3, ls='--', zorder=3); ax.plot(T, L, color=PURPLE, lw=1.3, zorder=3)
ax.plot(T[T < 1], X2[T < 1], color=RED, lw=1.8, ls='--', zorder=4); ax.plot(T[T > 3], L[T > 3], color=RED, lw=1.8, zorder=4)
ax.plot([1], [0], 'o', color=INK, ms=3.2, zorder=6); ax.plot([3], [0], 'o', color=INK, ms=3.2, zorder=6)
ax.axvline(2, color=MUTED, lw=.85, ls=':', zorder=1)
for y, c in [(1.5, BLUE), (.5, BLUE)]: ax.plot([2], [y], 'o', color=c, ms=3.2, zorder=6)
ax.plot([2], [.5], 'o', color=PURPLE, ms=3.2, zorder=6, mfc=PURPLE, mec=BLUE, mew=.7)
ax.text(3.45, 2.32, '$x_1$', fontsize=8, color=BLUE)
ax.text(3.5, 1.43, '$x_2$', fontsize=8, color=BLUE)
ax.text(.28, 1.46, r'$\lambda_1$', fontsize=8, color=PURPLE)
clean(ax, (0, 4), (-.75, 2.7), xlabel=r'$\tau$', ylabel='分支上的值')
ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, 1, 2])
save(fig, Path(__file__).resolve().parent, 'figure', {'branch': 'active set {1}'})
