from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：单位面积窄脉冲的响应趋于脉冲响应 w(t)=e^-t-e^-2t，方程 x''+3x'+2x=g，零初值。
W = lambda t: np.where(t > 0, .5-np.exp(-t)+.5*np.exp(-2*t), 0.)
w_ = lambda t: np.where(t > 0, np.exp(-t)-np.exp(-2*t), 0.)
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .075, .985, .96, .26, .25)
a, b = axes
t = np.linspace(0, 6, 1200)
for e, col, lab, xy in ((1., YELLOW, '$\\varepsilon=1$', (1.05, .75)), (.5, PURPLE, '$\\varepsilon=0.5$', (.56, 1.75)), (.1, GREEN, '$\\varepsilon=0.1$', (.17, 9.7))):
    a.plot([0, 0, e, e, 2.4], [0, 1/e, 1/e, 0, 0], color=col, lw=1.3)
    a.text(*xy, lab, color=col)
    b.plot(t, (W(t)-W(t-e))/e, color=col, lw=1.2)
a.set_xlim(-.08, 2.4); a.set_ylim(0, 11); a.set_xticks([0, 1, 2]); a.set_yticks([0, 5, 10]); label(a, '$t$', '$g$')
b.plot(t, w_(t), color=BLUE, lw=MAIN); b.text(.95, .265, '$w$', color=BLUE)
b.set_xlim(0, 6); b.set_ylim(0, .3); b.set_xticks([0, 2, 4, 6]); b.set_yticks([0, .1, .2, .3]); b.set_yticklabels(['0', '0.1', '0.2', '0.3']); label(b, '$t$', '$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'w': 'e^-t-e^-2t', 'pulse response': '(W(t)-W(t-eps))/eps', 'eps': [1, .5, .1]})
