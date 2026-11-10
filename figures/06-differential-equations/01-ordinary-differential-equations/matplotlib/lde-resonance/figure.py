from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：x''+x=cos(wt)，零初值：w=2 有界，w=1.2 拍频，w=1 线性增长。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .075, .985, .96, .25, .25)
a, b = axes
t = np.linspace(0, 40, 2400)
for w, col, lw in ((1.2, BLUE, 1.2), (2., YELLOW, 1.2)):
    a.plot(t, (np.cos(w*t)-np.cos(t))/(1-w*w), color=col, lw=lw)
a.axhline(0, color=GRID, lw=.5, zorder=0); a.text(30, 5.1, '$\\omega=1.2$', color=BLUE); a.text(30.5, -4.4, '$\\omega=2$', color=YELLOW)
a.set_xlim(0, 40); a.set_ylim(-6, 6.4); a.set_xticks([0, 20, 40]); a.set_yticks([-5, 0, 5]); label(a, '$t$', '$x$')
b.plot(t, t*np.sin(t)/2, color=BLUE, lw=1.2); b.plot(t, t/2, color=PURPLE, lw=1, ls=(0, (4, 2))); b.plot(t, -t/2, color=PURPLE, lw=1, ls=(0, (4, 2)))
b.axhline(0, color=GRID, lw=.5, zorder=0); b.text(4, 15, '$\\pm t/2$', color=PURPLE)
b.set_xlim(0, 40); b.set_ylim(-21, 21); b.set_xticks([0, 20, 40]); b.set_yticks([-20, 0, 20]); label(b, '$t$', '')
tags(fig, axes)
save(fig, HERE, 'figure', {'formula off': '(cos wt-cos t)/(1-w^2)', 'formula on': 't sin t/2'})
