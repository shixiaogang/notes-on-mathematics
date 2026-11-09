from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# G(x)=x/2+1_{[1/2,inf)}(x)/4+F_C(x)/4 on [0,1]; ordinary derivative integrates to x/2.
def cantor(t):
    y, b = 0.0, .5
    for _ in range(45):
        t *= 3
        if t < 1: pass
        elif t < 2: return y + b
        else: y += b; t -= 2
        b /= 2
    return y
fig, ax = figure(width_mm=100, height_mm=58)
L = np.linspace(0, .5, 2400, endpoint=False); R = np.linspace(.5, 1, 2401)
FL = np.array([cantor(float(t)) for t in L]); FR = np.array([cantor(float(t)) for t in R])
GL = L/2 + FL/4; GR = R/2 + .25 + FR/4
ax.plot(L, GL, color=BLUE, lw=1.4); ax.plot(R, GR, color=BLUE, lw=1.4, label='G')
xx = np.array([0, 1]); ax.plot(xx, xx/2, color=GREEN, lw=1.4, ls=(0, (4, 2)))
ax.plot([.5, .5], [GL[-1], GR[0]], color=RED, lw=1.0, ls=(0, (1.6, 1.4)))
ax.plot([.5], [GR[0]], 'o', ms=4, color=BLUE, mew=0)
ax.plot([.5], [GL[-1]], 'o', ms=4, mfc='white', mec=BLUE, mew=1)
ax.annotate('', xy=(1.0, 1.0), xytext=(1.0, .5), arrowprops=dict(arrowstyle='<->', color=RED, lw=.85, shrinkA=0, shrinkB=0))
ax.text(1.015, .75, r'$G(1)-\int_0^1 G^\prime=\frac{1}{2}$', ha='left', va='center')
ax.text(.53, .5, r'$\frac{1}{4}$', ha='left', va='center')
ax.text(.27, .36, r'$G$', ha='center', va='center')
ax.text(.80, .24, r'$\int_0^x G^\prime=\frac{x}{2}$', ha='center', va='center')
ax.set_xlim(0, 1.0); ax.set_ylim(0, 1.05); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, .5, 1])
ax.set_xlabel(r'$x$')
fig.set_layout_engine(None); fig.subplots_adjust(left=.075, right=.70, top=.97, bottom=.18)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'G=x/2+1_[1/2,oo)/4+F_C/4, Cantor via ternary digits'})
