from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Bernstein polynomials B_m f* (m=4,16,64) for f*=|x-1/2|, and the error curves of B_16 and of the best quadratic p*(x)=2(x-1/2)^2+1/16.
from math import lgamma
def B(m, x):
    j = np.arange(m+1); fj = np.abs(j/m-.5)
    lg = np.array([lgamma(m+1)-lgamma(i+1)-lgamma(m-i+1) for i in j])
    xx = np.clip(x, 1e-300, 1-1e-16)
    w = np.exp(lg[None, :]+j[None, :]*np.log(xx)[:, None]+(m-j)[None, :]*np.log1p(-xx)[:, None])
    return (w*fj).sum(1)
x = np.linspace(0, 1, 4001); fs = np.abs(x-.5)
for m in (2, 4, 16, 64): print(m, (B(m, x)-fs).max())
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.27, wspace=.27)
ax = axes[0]
ax.plot(x, B(4, x), color=GREEN, lw=1.2); ax.plot(x, B(16, x), color=YELLOW, lw=1.2); ax.plot(x, B(64, x), color=RED, lw=1.2); ax.plot(x, fs, color=BLUE, lw=1.4)
ax.text(.5, .23, r'$B_4$', ha='center'); ax.text(.5, .132, r'$B_{16}$', ha='center'); ax.annotate(r'$B_{64}$', xy=(.53, .056), xytext=(.72, .045), ha='left', va='center', arrowprops=dict(arrowstyle='-', color=MUTED, lw=.7)); ax.text(.92, .49, r'$f_*$', ha='right')
ax.set_xlim(0, 1); ax.set_ylim(-.02, .56); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '1/4', '1/2']); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
ax.axhline(0, color=MUTED, lw=.85)
ps = 2*(x-.5)**2+1/16
ax.plot(x, B(16, x)-fs, color=YELLOW, lw=1.4); ax.plot(x, ps-fs, color=GREEN, lw=1.4)
xa = np.array([0, .25, .5, .75, 1]); ea = 2*(xa-.5)**2+1/16-np.abs(xa-.5)
ax.plot(xa, ea, 'o', ms=3.2, color=GREEN, mew=0)
ax.text(.39, .092, r'$B_{16}-f_*$', ha='right'); ax.text(.625, -.05, r'$p^*-f_*$', ha='left')
ax.set_xlim(0, 1); ax.set_ylim(-.09, .125); ax.set_xticks([0, .25, .5, .75, 1]); ax.set_xticklabels(['0', '1/4', '1/2', '3/4', '1']); ax.set_yticks([-.0625, 0, .0625, .1]); ax.set_yticklabels(['-1/16', '0', '1/16', '0.1']); ax.set_xlabel('$x$', labelpad=0)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'B_m f(x)=sum f(j/m) C(m,j) x^j (1-x)^(m-j); p*(x)=2(x-1/2)^2+1/16'})
