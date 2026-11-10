from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：三个二阶方程同一初值 x(0)=1,x'(0)=0：实根、重根、复根。
fig, ax = figure(width_mm=92, height_mm=50)
panel(fig, .095, .975, .96, .16)
t = np.linspace(0, 7, 700)
ax.axhline(0, color=GRID, lw=.6, zorder=0)
ax.plot(t, 2*np.exp(-t)-np.exp(-2*t), color=BLUE, lw=MAIN)
ax.plot(t, (1+t)*np.exp(-t), color=YELLOW, lw=1.6)
ax.plot(t, np.exp(-t)*(np.cos(2*t)+.5*np.sin(2*t)), color=PURPLE, lw=1.4)
ax.plot([0], [1], 'o', ms=3.8, color=RED, mew=0, clip_on=False, zorder=5)
ax.text(1.28, .86, '$-1,-1$', color=YELLOW); ax.text(.98, .18, '$-1,-2$', color=BLUE)
ax.text(1.85, -.3, '$-1\\pm 2\\mathrm{i}$', color=PURPLE)
ax.set_xlim(0, 7); ax.set_ylim(-.4, 1.08); ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '0.5', '1']); label(ax, '$t$', '$x$')
save(fig, HERE, 'figure', {'p1': 'z^2+3z+2', 'p2': 'z^2+2z+1', 'p3': 'z^2+2z+5', 'init': [1, 0]})
