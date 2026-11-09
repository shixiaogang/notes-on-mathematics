from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Coordinates along the first Newton direction of the running example, sigma=0.3.
r = path_following(A_RUN, B_RUN, C_RUN, X0_RUN, Y0_RUN, S0_RUN, sigma=.3, eta=.9, tol=1e-3, maxit=1)[0]
al = np.linspace(0, 1.15, 200)
fig, ax = figure(width_mm=92, height_mm=52)
for i in range(3):
    ax.plot(al, r['x'][i] + al * r['dx'][i], color=GREEN, lw=1.3, ls=['-', '--', ':'][i])
    ax.plot(al, r['s'][i] + al * r['ds'][i], color=PURPLE, lw=1.3, ls=['-', '--', ':'][i])
ax.axhline(0, color='#4C4D4F', lw=2)
ax.plot([r['amax']], [0], 'o', color=RED, ms=4.5, zorder=7)
ax.axvline(r['alpha'], color=MUTED, lw=.85)
ax.plot([r['alpha']], [r['s'][0] + r['alpha'] * r['ds'][0]], 'o', color=GREEN, ms=4, zorder=7)
ax.text(r['alpha'] - .015, 2.72, '$\\alpha=0.9\\,\\alpha_{\\max}$', fontsize=7.5, ha='right')
ax.text(r['amax'], -.3, '$\\alpha_{\\max}$', fontsize=7.5, ha='center')
ax.text(.03, .57, '$x_1,x_2,x_3$', fontsize=7.5); ax.text(.03, 1.23, '$s_1$', fontsize=7.5); ax.text(.04, 2.08, '$s_2$', fontsize=7.5); ax.text(.04, 3.0, '$s_3$', fontsize=7.5)
ax.set_xlim(0, 1.15); ax.set_ylim(-.4, 3.3); ax.set_xlabel('$\\alpha$', labelpad=1); ax.set_ylabel('坐标值', labelpad=1)
save(fig, OUT, 'figure', {'alpha_max': r['amax'], 'alpha': r['alpha']})
