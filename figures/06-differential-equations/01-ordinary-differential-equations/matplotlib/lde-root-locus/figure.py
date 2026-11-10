from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：z^2+2cz+1 的根随 c 移动，在 c=1 处相撞；差商 (e^{r1 t}-e^{r2 t})/(r1-r2) 趋于 t e^{-t}。
fig, axes = figure(width_mm=112, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [1, 1.25]})
panel(fig, .07, .985, .96, .24, .3)
a, b = axes
th = np.linspace(0, np.pi, 200)
a.plot(-np.sin(th), np.cos(th), color=BLUE, lw=MAIN)
a.plot([-2.8, -.33], [0, 0], color=BLUE, lw=MAIN)
a.axvline(0, color=MUTED, lw=.6); a.axhline(0, color=MUTED, lw=.6, zorder=0)
for c, col in ((0, YELLOW), (.6, PURPLE)):
    r = np.array([complex(-c, np.sqrt(1-c*c)), complex(-c, -np.sqrt(1-c*c))])
    a.plot(r.real, r.imag, 'o', ms=4, color=col, mew=0, zorder=5)
a.plot([-1], [0], 'o', ms=4.6, color=RED, mew=0, zorder=6)
c = 1.5
r = np.array([-c+np.sqrt(c*c-1), -c-np.sqrt(c*c-1)])
a.plot(r, [0, 0], 'o', ms=4, color=GREEN, mew=0, zorder=5)
a.text(.07, .98, '$c=0$', color=YELLOW); a.text(-1.6, .92, '$c=0.6$', color=PURPLE); a.text(-1.78, .13, '$c=1$', color=RED); a.text(-2.85, -.34, '$c=1.5$', color=GREEN)
a.set_aspect('equal'); a.set_xlim(-3, .75); a.set_ylim(-1.25, 1.25); a.set_xticks([-3, -2, -1, 0]); a.set_yticks([-1, 0, 1]); label(a, '$\\mathrm{Re}\\,z$', '$\\mathrm{Im}\\,z$')
t = np.linspace(0, 8, 500)
for e, col in ((1., YELLOW), (.4, PURPLE), (.1, GREEN)):
    b.plot(t, (np.exp(-t)-np.exp(-(1+e)*t))/e, color=col, lw=1.2)
b.plot(t, t*np.exp(-t), color=BLUE, lw=MAIN+.1)
b.text(1.9, .425, '$t\\mathrm{e}^{-t}$', color=BLUE)
b.set_xlim(0, 8); b.set_ylim(0, .48); b.set_xticks([0, 2, 4, 6, 8]); b.set_yticks([0, .2, .4]); b.set_yticklabels(['0', '0.2', '0.4']); label(b, '$t$', '')
tags(fig, axes)
save(fig, HERE, 'figure', {'poly': 'z^2+2cz+1', 'difference quotient': '(e^-t-e^-(1+eps)t)/eps', 'eps': [1, .4, .1]})
