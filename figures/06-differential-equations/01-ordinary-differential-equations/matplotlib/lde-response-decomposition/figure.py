from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：x''+3x'+2x=1, x(0)=1,x'(0)=0 的响应 = 零输入响应 + 零状态响应。
fig, ax = figure(width_mm=92, height_mm=48)
panel(fig, .095, .975, .96, .17)
t = np.linspace(0, 6, 500)
zi = 2*np.exp(-t)-np.exp(-2*t); zs = .5-np.exp(-t)+.5*np.exp(-2*t)
ax.plot(t, zi, color=YELLOW, lw=1.5); ax.plot(t, zs, color=PURPLE, lw=1.3); ax.plot(t, zi+zs, color=BLUE, lw=MAIN)
ax.plot([0], [1], 'o', ms=3.8, color=RED, mew=0, clip_on=False, zorder=5)
ax.axhline(.5, color=MUTED, lw=.6, ls=(0, (3, 2)))
ax.text(1.45, .88, '总响应', color=BLUE); ax.text(2.8, .19, '零输入', color=YELLOW); ax.text(3.8, .36, '零状态', color=PURPLE)
ax.set_xlim(0, 6); ax.set_ylim(0, 1.1); ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '0.5', '1']); label(ax, '$t$', '$x$')
save(fig, HERE, 'figure', {'zero-input': '2e^-t-e^-2t', 'zero-state': '1/2-e^-t+e^-2t/2'})
