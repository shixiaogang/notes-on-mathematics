from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def tag(fig, axes, y=.02):
    for ax, s in zip(axes, ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha='center', va='bottom')

# 频域乘 G(t xi) 等于空间与 G_t 卷积。B*G_t(x)=Phi((x+1/2)/s)-Phi((x-1/2)/s)，s=t/sqrt(2 pi)。
from math import erf
Phi = np.vectorize(lambda z: .5*(1+erf(z/np.sqrt(2))))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.06, right=.985, top=.96, bottom=.26, wspace=.19)
ax = axes[0]
xi = np.linspace(-6, 6, 2400); t = .5
ax.axhline(0, color=MUTED, lw=.85)
ax.plot(xi, np.exp(-np.pi*t**2*xi**2), color=MUTED, lw=.95, ls=(0, (3, 2)))
ax.plot(xi, np.sinc(xi), color=GREEN, lw=1.4)
ax.plot(xi, np.sinc(xi)*np.exp(-np.pi*t**2*xi**2), color=YELLOW, lw=1.4)
ax.set_xlim(-6, 6); ax.set_ylim(-.3, 1.12); ax.set_xticks([-6, -3, 0, 3, 6]); ax.set_yticks([0, .5, 1]); ax.set_xlabel(r'$\xi$', labelpad=0)
ax.text(2.55, .36, r'$G(t\xi)$', color=MUTED, ha='left', va='center')
ax = axes[1]
x = np.linspace(-1.1, 1.1, 1500)
ax.plot([-1.1, -.5, -.5, .5, .5, 1.1], [0, 0, 1, 1, 0, 0], color=BLUE, lw=1.4)
for t, c in ((.5, YELLOW), (.1, PURPLE)):
    s = t/np.sqrt(2*np.pi)
    ax.plot(x, Phi((x+.5)/s)-Phi((x-.5)/s), color=c, lw=1.3)
ax.text(.76, .24, '$t=0.5$', color=INK, ha='left', va='center')
ax.text(.53, .62, '$t=0.1$', color=INK, ha='left', va='center')
ax.set_xlim(-1.1, 1.1); ax.set_ylim(-.05, 1.12); ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$x$', labelpad=0)
tag(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'B^(xi)G(t xi), B*G_t via normal cdf, t=0.5,0.1'})
