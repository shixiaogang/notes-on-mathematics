from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：f=e^t 被权 e^{-zt} 压低：z=2 可积，z=1 恰为常数，z=0.5 仍增长。
fig, ax = figure(width_mm=92, height_mm=46)
panel(fig, .08, .975, .95, .18)
t = np.linspace(0, 5, 400)
ax.plot(t, np.exp(t), color=YELLOW, lw=1.5)
ax.plot(t, np.exp(.5*t), color=RED, lw=1.3, ls=(0, (4, 2)))
ax.plot(t, np.ones_like(t), color=PURPLE, lw=1.2)
ax.fill_between(t, 0, np.exp(-t), color=BLUE_FILL, lw=0)
ax.plot(t, np.exp(-t), color=BLUE, lw=MAIN)
ax.text(2.28, 8.6, '$f=\\mathrm{e}^{t}$', color=YELLOW); ax.text(4.0, 4.7, '$z=0.5$', color=RED); ax.text(3.9, 1.3, '$z=1$', color=PURPLE); ax.annotate('$z=2$', xy=(.75, .47), xytext=(1.2, 2.6), color=BLUE, arrowprops=dict(arrowstyle='-', color=MUTED, lw=.6, shrinkA=1, shrinkB=1))
ax.set_xlim(0, 5); ax.set_ylim(0, 12); ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, 4, 8, 12]); label(ax, '$t$', '')
save(fig, HERE, 'figure', {'curves': 'e^{t}, e^{(1-z)t} for z=0.5,1,2'})
