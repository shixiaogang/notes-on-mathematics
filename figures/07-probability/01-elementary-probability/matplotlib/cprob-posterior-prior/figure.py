"""Posterior probability of a defective item after alarms, as a function of the
prior defect rate pi. Detection probability 0.95, false-alarm probability 0.05;
the two tests are assumed to behave independently given the true state."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tidy(ax):
    for sp in ("left", "bottom"):
        ax.spines[sp].set_linewidth(0.95)

pi = np.logspace(-3, np.log10(0.5), 300)
s, f = 0.95, 0.05
one = s * pi / (s * pi + f * (1 - pi))
two = s**2 * pi / (s**2 * pi + f**2 * (1 - pi))
fig, ax = figure(width_mm=96, height_mm=52)
ax.plot(pi, pi, color=PURPLE, lw=1.0, ls=(0, (4, 2)), label='后验=先验')
ax.plot(pi, one, color=BLUE, lw=1.4, label='一次报警')
ax.plot(pi, two, color=YELLOW, lw=1.6, label='两次报警')
p0 = 0.02
o1 = s * p0 / (s * p0 + f * (1 - p0)); o2 = s**2 * p0 / (s**2 * p0 + f**2 * (1 - p0))
ax.plot([p0, p0], [o1, o2], 'o', color=RED, ms=4.5, zorder=4)
ax.axvline(p0, color='#4C4D4F', lw=0.85, ls=(0, (2, 2)))
ax.text(p0 * 1.12, o1 - 0.03, f'{o1:.3f}', fontsize=7.5, va='top')
ax.text(p0 * 1.12, o2 - 0.03, f'{o2:.3f}', fontsize=7.5, va='top')
ax.set_xscale('log'); ax.set_xlim(1e-3, 0.5); ax.set_ylim(0, 1.02)
ax.set_xticks([0.001, 0.01, 0.02, 0.1, 0.5]); ax.set_xticklabels(['0.001', '0.01', '0.02', '0.1', '0.5'])
ax.set_xlabel('先验次品率 π'); ax.set_ylabel('报警后的次品概率')
ax.text(0.16, 0.56, '一次报警', color=BLUE, fontsize=7.5, ha='left')
ax.text(0.0016, 0.62, '两次报警', color=YELLOW, fontsize=7.5, ha='left')
ax.text(0.2, 0.08, '后验=先验', color=PURPLE, fontsize=7.5, ha='center')
tidy(ax)
save(fig, Path(__file__).resolve().parent, 'figure', {'sensitivity': s, 'false_alarm': f, 'prior': p0, 'post1': o1, 'post2': o2})
print(o1, o2)
