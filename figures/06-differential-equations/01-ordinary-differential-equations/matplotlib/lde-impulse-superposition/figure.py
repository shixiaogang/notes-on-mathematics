from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：dx/dt=-x+g，g=1+cos t，把输入切成宽 0.5 的矩形，各段脉冲响应叠加后接近精确解。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, .075, .985, .96, .24, .26)
a, b = axes
g = lambda s: 1+np.cos(s)
d = .5
Sj = np.arange(0, 6, d)
s = np.linspace(0, 6, 400)
a.bar(Sj, g(Sj), width=d, align='edge', color=GREEN_FILL, edgecolor=GREEN, lw=.6)
a.plot(s, g(s), color=RED, lw=1.4)
a.set_xlim(0, 6); a.set_ylim(0, 2.2); a.set_xticks([0, 2, 4, 6]); a.set_yticks([0, 1, 2]); label(a, '$s$', '$g$')
t = np.linspace(0, 6, 1200)
tot = np.zeros_like(t)
for sj in Sj:
    # 高度 g(s_j)、宽度 d 的矩形输入的精确响应
    r = np.where(t < sj, 0., np.where(t < sj+d, g(sj)*(1-np.exp(-(t-sj))), g(sj)*(1-np.exp(-d))*np.exp(-(t-sj-d))))
    tot += r
    m = t >= sj
    b.plot(t[m], r[m], color=YELLOW, lw=.85)
ex = 1+(np.cos(t)+np.sin(t))/2-1.5*np.exp(-t)
b.plot(t, tot, color=GREEN, lw=1.2)
b.plot(t, ex, color=BLUE, lw=MAIN)
b.set_xlim(0, 6); b.set_ylim(0, 1.75); b.set_xticks([0, 2, 4, 6]); b.set_yticks([0, .5, 1, 1.5]); b.set_yticklabels(['0', '0.5', '1', '1.5']); label(b, '$t$', '$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'g': '1+cos t', 'd': d, 'exact': '1+(cos t+sin t)/2-1.5 e^-t'})
