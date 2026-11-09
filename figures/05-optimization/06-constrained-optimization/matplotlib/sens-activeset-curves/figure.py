from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Solution, multipliers, and V'(tau) as exact piecewise functions.
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
T = np.linspace(.001, 4.5, 901); R = [budget(t) for t in T]
X = np.array([r[0] for r in R]); L = np.array([r[1] for r in R])
dV = np.gradient([value(t) for t in T], T)
for ax in axs:
    ax.axvline(1, color=MUTED, lw=.85, ls=':'); ax.axvline(3, color=MUTED, lw=.85, ls=':'); ax.set_xticks([0, 1, 2, 3, 4])
ax = axs[0]; ax.plot(T, X[:, 0], color=GREEN, lw=1.4); ax.plot(T, X[:, 1], color=GREEN, lw=1.4, ls='--')
ax.text(.2, 1.55, '$x_1$', fontsize=8, color=GREEN); ax.text(3.45, .72, '$x_2$', fontsize=8, color=GREEN)
clean(ax, (0, 4.5), (-.1, 2.3), xlabel=r'$\tau$', sub='(a)'); ax.set_yticks([0, 1, 2])
ax = axs[1]; ax.plot(T, L[:, 0], color=PURPLE, lw=1.4); ax.plot(T, L[:, 2], color=PURPLE, lw=1.4, ls='--')
ax.text(1.5, 1.1, r'$\lambda_1$', fontsize=8, color=PURPLE); ax.text(.08, .43, r'$\lambda_3$', fontsize=8, color=PURPLE)
clean(ax, (0, 4.5), (-.1, 2.3), xlabel=r'$\tau$', sub='(b)'); ax.set_yticks([0, 1, 2])
ax = axs[2]; ax.plot(T[2:-2], dV[2:-2], color=BLUE, lw=1.4)
ax.text(1.5, -.25, r"$V'(\tau)$", fontsize=8, color=BLUE)
clean(ax, (0, 4.5), (-2.2, .2), xlabel=r'$\tau$', sub='(c)'); ax.set_yticks([-2, -1, 0])
save(fig, Path(__file__).resolve().parent, 'figure', {'note': 'budget quadratic, exact active-set solution'})
