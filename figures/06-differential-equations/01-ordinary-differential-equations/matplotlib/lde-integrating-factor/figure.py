from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：dx/dt=-2tx+2t，积分因子 e^{t^2} 把解族变成上下平移的曲线。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .075, .985, .96, .25, .28)
a, b = axes
t = np.linspace(0, 1.5, 300)
X0 = (-1, 0, 1, 2, 3)
for x0 in X0:
    a.plot(t, 1+(x0-1)*np.exp(-t**2), color=BLUE, lw=MAIN)
    a.plot([0], [x0], 'o', ms=3.6, color=RED, mew=0, clip_on=False, zorder=5)
    b.plot(t, x0+np.exp(t**2)-1, color=BLUE, lw=MAIN)
    b.plot([0], [x0], 'o', ms=3.6, color=RED, mew=0, clip_on=False, zorder=5)
a.set_xlim(0, 1.5); a.set_ylim(-1.2, 3.2); label(a, '$t$', '$x$'); a.set_xticks([0, .5, 1, 1.5]); a.set_xticklabels(['0', '0.5', '1', '1.5'])
b.set_xlim(0, 1.5); b.set_ylim(-1.2, 12.5); label(b, '$t$', '$y=\\mathrm{e}^{t^2}x$'); b.set_xticks([0, .5, 1, 1.5]); b.set_xticklabels(['0', '0.5', '1', '1.5'])
tc = 1.25
base = np.exp(tc**2)-1
for x0 in (-1, 1):
    b.annotate('', xy=(tc, x0+1+base), xytext=(tc, x0+base), arrowprops=dict(arrowstyle='<|-|>', color=STROKE, lw=.8, mutation_scale=5, shrinkA=0, shrinkB=0), zorder=4)
tags(fig, axes)
save(fig, HERE, 'figure', {'formula': 'x=1+(x0-1)e^{-t^2}, y=x0+e^{t^2}-1'})
