from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：系数跳变时解有折角；系数在端点可积无界时解连续但端点斜率无穷。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .075, .985, .96, .26, .28)
a, b = axes
t = np.linspace(0, 2.5, 600)
x = np.where(t < 1, np.exp(-t), np.exp(-1)*np.exp(-3*(t-1)))
a.plot(t, x, color=BLUE, lw=MAIN)
a.plot([0], [1], 'o', ms=3.8, color=RED, mew=0, clip_on=False, zorder=5)
a.axvline(1, color=MUTED, lw=.7, ls=(0, (3, 2)))
a.text(.32, .24, '$a=-1$', color=MUTED, fontsize=7.5); a.text(1.45, .24, '$a=-3$', color=MUTED, fontsize=7.5)
a.set_xlim(0, 2.5); a.set_ylim(0, 1.08); a.set_xticks([0, 1, 2]); a.set_yticks([0, .5, 1]); a.set_yticklabels(['0', '0.5', '1']); label(a, '$t$', '$x$')
t = np.linspace(0, 2.5, 1600)
b.plot(t, np.exp(-t), color=YELLOW, lw=1.5)
b.plot(t, np.exp(-np.sqrt(t)), color=BLUE, lw=MAIN)
b.plot([0], [1], 'o', ms=3.8, color=RED, mew=0, clip_on=False, zorder=5)
b.text(.95, .62, '$\\mathrm{e}^{-t}$', color=YELLOW); b.text(.14, .32, '$\\mathrm{e}^{-\\sqrt{t}}$', color=BLUE)
b.set_xlim(0, 2.5); b.set_ylim(0, 1.08); b.set_xticks([0, 1, 2]); b.set_yticks([0, .5, 1]); b.set_yticklabels(['0', '0.5', '1']); label(b, '$t$', '$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'a(t)=-1 on [0,1), -3 on [1,2.5], x0=1', 'b': 'a(t)=-1/(2 sqrt t), x0=1'})
