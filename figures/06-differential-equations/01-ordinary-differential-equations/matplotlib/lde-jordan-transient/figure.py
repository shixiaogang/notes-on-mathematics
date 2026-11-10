from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：A=[[-1,10],[0,-1]]，x0=(0,1)：两个特征值都是 -1，x1=10 t e^-t 先升后降。
fig, ax = figure(width_mm=92, height_mm=48)
panel(fig, .08, .975, .96, .17)
t = np.linspace(0, 8, 500)
ax.plot(t, 10*t*np.exp(-t), color=BLUE, lw=MAIN)
ax.plot(t, np.exp(-t), color=YELLOW, lw=1.5)
ax.plot([0], [1], 'o', ms=3.8, color=RED, mew=0, clip_on=False, zorder=5)
ax.plot([1], [10/np.e], 'o', ms=3.8, color=RED, mew=0, zorder=5)
ax.annotate('$10/\\mathrm{e}\\approx 3.68$', xy=(1, 10/np.e), xytext=(1.9, 3.6), color=INK, arrowprops=dict(arrowstyle='-', color=MUTED, lw=.6, shrinkA=1, shrinkB=2))
ax.text(4.2, 1.15, '$x_1=10t\\mathrm{e}^{-t}$', color=BLUE); ax.text(1.05, .5, '$x_2=\\mathrm{e}^{-t}$', color=YELLOW)
ax.set_xlim(0, 8); ax.set_ylim(0, 4.1); ax.set_xticks([0, 2, 4, 6, 8]); ax.set_yticks([0, 1, 2, 3, 4]); label(ax, '$t$', '')
save(fig, HERE, 'figure', {'A': [[-1, 10], [0, -1]], 'x0': [0, 1], 'peak': [1, 10/np.e]})
