from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"tr-common"))
from tr_core import *
HERE = Path(__file__).resolve().parent
# 沿 x1 的切片：(a) 在 (0,0)，模型 p-p^2/2；(b) 在 (2,2)，模型 7p+5.5p^2。
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax = axs[0]; p = np.linspace(-2.6, 1.6, 400)
ax.plot(p, p**4/4 - p**2/2 + p, color=BLUE, lw=1.4)
ax.plot(p, p - p**2/2, color=GREEN, lw=1.4)
ax.axvspan(-1, 1, facecolor=BLUE_FILL, edgecolor='none', zorder=0)
ax.plot([0], [0], 'o', color=INK, ms=4, mew=0)
ax.set_ylim(-5.5, 3.2); ax.set_xlim(-2.6, 1.6); ax.set_xlabel('$p_1$', labelpad=1)
ax.text(-2.5, 2.3, '$f$', color=BLUE); ax.text(-2.1, -5.1, '$m$', color=GREEN)
ax = axs[1]; p = np.linspace(-2.6, 1.0, 400)
F = lambda p: (2+p)**4/4 - (2+p)**2/2 + (2+p) - 4
M = lambda p: 7*p + 5.5*p**2
ax.plot(p, F(p), color=BLUE, lw=1.4); ax.plot(p, M(p), color=GREEN, lw=1.4)
ax.axvspan(-.7, .7, facecolor=BLUE_FILL, edgecolor='none', zorder=0)
ax.plot([0], [0], 'o', color=INK, ms=4, mew=0); ax.set_xlim(-2.6, 1.0); ax.set_ylim(-4, 12)
ax.set_xlabel('$p_1$', labelpad=1)
ax.text(.42, 9.8, '$f$', color=BLUE); ax.text(-2.55, 7.2, '$m$', color=GREEN)
panels(fig, .07, .985, .98, .26, .22); tags(fig, axs)
save(fig, HERE, 'figure', {'f': 'x1^4/4-x1^2/2+x1 (x2 part omitted), slices at x1=0 and x1=2'})
