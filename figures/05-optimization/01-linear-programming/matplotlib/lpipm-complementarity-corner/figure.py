from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Complementarity corner xs=0 and its smooth hyperbolic perturbations xs=mu.
fig, ax = figure(width_mm=68, height_mm=56)
x = np.linspace(.01, 3, 800)
for mu, ls in [(1, '-'), (.3, '--'), (.05, ':')]:
    ax.plot(x, mu / x, color=BLUE, ls=ls, lw=1.4)
ax.plot([0, 3], [0, 0], color='#4C4D4F', lw=2.2, zorder=5, clip_on=False)
ax.plot([0, 0], [0, 3], color='#4C4D4F', lw=2.2, zorder=5, clip_on=False)
ax.text(1.55, .9, '$xs=1$', fontsize=7.5); ax.text(1.1, .46, '$xs=0.3$', fontsize=7.5); ax.text(.58, .15, '$xs=0.05$', fontsize=7.5)

ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.set_xlabel('$x_i$', labelpad=1); ax.set_ylabel('$s_i$', labelpad=1)
ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 1, 2, 3])
save(fig, OUT, 'figure', {'formula': 'x s = mu for mu in 1, .3, .05'})
