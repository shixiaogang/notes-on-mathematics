"""Discrete state X in {0,1}, P(X=1)=0.2; reading Y|X=0 ~ N(20,1), Y|X=1 ~ N(23,1).
(a) f_Y = 0.8 phi(y-20)+0.2 phi(y-23) and its two weighted parts; (b) P(X=1|Y=y); red point y=22 (0.528)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = "#4C4D4F"
def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha="center", va="top")

phi = lambda z: np.exp(-z**2/2)/np.sqrt(2*np.pi)
y = np.linspace(16.5, 26.5, 500)
c0 = 0.8*phi(y-20); c1 = 0.2*phi(y-23); f = c0 + c1
fig, (a, b) = figure(width_mm=108, height_mm=44, ncols=2)
a.plot(y, c0, color=YELLOW, lw=1.3, ls='--'); a.plot(y, c1, color=PURPLE, lw=1.3, ls='--')
a.plot(y, f, color=BLUE, lw=1.5)
a.text(20, 0.335, '$0.8\\,f_{Y\\mid X}(y\\mid 0)$', ha='center', fontsize=7.5)
a.text(24.0, 0.095, '$0.2\\,f_{Y\\mid X}(y\\mid 1)$', ha='left', fontsize=7.5)
a.set_ylim(0, 0.38); a.set_xlim(16.5, 26.5); a.set_xticks([17, 20, 23, 26]); a.set_xlabel('$y$', labelpad=1)
a.set_ylabel('$f_Y(y)$')
post = c1/f
b.plot(y, post, color=BLUE, lw=1.5)
b.axhline(0.2, color=STROKE, lw=0.85, ls='--')
p22 = 0.2*phi(-1)/(0.2*phi(-1)+0.8*phi(2))
b.scatter([22], [p22], s=18, color=RED, zorder=4)
b.text(22.3, p22 - 0.03, f'$({22},\\,{p22:.3f})$', fontsize=7.5, va='top')
b.text(26.3, 0.23, '$0.2$', ha='right', fontsize=7.5, color=MUTED)
b.set_xlim(16.5, 26.5); b.set_xticks([17, 20, 23, 26]); b.set_ylim(0, 1.03); b.set_xlabel('$y$', labelpad=1)
b.set_ylabel(r'$\mathrm{P}(X=1\mid Y=y)$')
tag(a, '(a)', y=-0.28); tag(b, '(b)', y=-0.28)
save(fig, Path(__file__).resolve().parent, 'figure', {'p1': 0.2, 'means': [20, 23], 'sd': 1, 'post_at_22': float(p22)})
