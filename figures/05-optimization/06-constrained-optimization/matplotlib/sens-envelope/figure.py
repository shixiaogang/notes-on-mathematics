from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# f(x,theta)=.5(x1-2-theta)^2+.5(x2-1)^2 on the triangle tau=2. Branch x=(1.5+theta/2,.5-theta/2), v=(1+theta)^2/4.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax = axs[0]
triangle(ax, 2, (1,))
Th = [-.6, 0, .6]
for th in Th:
    c = np.array([2+th, 1.])
    ax.plot(*c, marker='x', color=BLUE, ms=4.2, mew=1.1, ls='none', zorder=6)
circles(ax, radii=(np.sqrt(.5),), lw=.8)
xa, xb = budget(2, (1.4, 1))[0], budget(2, (2.6, 1))[0]
ax.plot([xa[0], xb[0]], [xa[1], xb[1]], color=GREEN, lw=2.0, zorder=6)
opt_point(ax, (1.5, .5))
ax.annotate('', xy=(2, 1), xytext=(1.5, .5), arrowprops=dict(arrowstyle='-|>', color=INK, lw=1.0, mutation_scale=7, shrinkA=0, shrinkB=2), zorder=9)
ax.annotate('', xy=(1.5+.42, .5-.42), xytext=(1.5, .5), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.1, mutation_scale=7, shrinkA=0, shrinkB=0), zorder=9)
ax.text(1.03, .26, r"$x'(\theta)$", fontsize=7.5, color=GREEN, va='top')
ax.text(1.85, .6, r'$-\nabla_{x}f$', fontsize=7.5)
ax.annotate('', xy=(2.62, 1.2), xytext=(1.4, 1.2), arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=.85, mutation_scale=6))
ax.text(2.0, 1.27, r'$c(\theta)$', fontsize=7.5, color=BLUE, ha='center')
ax.set_aspect('equal'); clean(ax, (-.15, 3.05), (-.15, 2.25), xlabel='$x_1$', ylabel='$x_2$', sub='(a)')
ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1, 2])
ax = axs[1]
T = np.linspace(-1, 1, 201)
for th in (-.5, 0, .5):
    x = np.array([1.5+th/2, .5-th/2])
    ax.plot(T, .5*(x[0]-2-T)**2+.5*(x[1]-1)**2, color=YELLOW, lw=1.1, zorder=2)
    ax.plot([th], [(1+th)**2/4], 'o', color=GREEN, ms=3.4, zorder=5)
ax.plot(T, (1+T)**2/4, color=BLUE, lw=1.5, zorder=4)
ax.text(.25, .19, r'$v(\theta)$', fontsize=8, color=BLUE)
clean(ax, (-1, 1), (0, 1.3), xlabel=r'$\theta$', sub='(b)', ylabel='目标值')
ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_yticks([0, .5, 1])
save(fig, Path(__file__).resolve().parent, 'figure', {'v': '(1+theta)^2/4'})
