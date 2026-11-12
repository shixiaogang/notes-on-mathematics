from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# mu uniform on {0}x[0,1] (blue); nu = half uniform on {-1}x[0,1] + half on {1}x[0,1] (yellow).
# Map T_n: on each strip of length 1/n, first half -> left segment, second half -> right segment, stretched by 2.
# Cost of T_n: 1 + 1/(12 n^2) (horizontal move 1, vertical displacement uniform on an interval of length 1/(2n)).
# (a) T_2, (b) T_4, (c) optimal coupling: every point split half-left, half-right horizontally, cost 1.
def Tn(t, n):
    k = np.floor(t*n); r = t-k/n
    left = r < 1/(2*n)
    y = np.where(left, k/n+2*r, k/n+2*(r-1/(2*n)))
    return np.where(left, -1., 1.), y
def cost(n, N=400000):
    t = (np.arange(N)+.5)/N; x, y = Tn(t, n); return float(np.mean(x**2+(y-t)**2))
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, left=.03, right=.99, top=.97, bottom=.2, wspace=.15)
for ax, n in zip(axs, (2, 4, None)):
    ax.plot([0, 0], [0, 1], color=BLUE, lw=2)
    ax.plot([-1, -1], [0, 1], color=YELLOW, lw=2); ax.plot([1, 1], [0, 1], color=YELLOW, lw=2)
    ts = (np.arange(16)+.5)/16
    if n:
        xx, yy = Tn(ts, n)
        for t, x, y in zip(ts, xx, yy):
            ax.annotate('', xy=(x*.94, y), xytext=(0, t), arrowprops=dict(arrowstyle='->', color=STROKE, lw=.55, shrinkA=0, shrinkB=0))
    else:
        for t in ts[::2]:
            for x in (-1, 1):
                ax.annotate('', xy=(x*.94, t), xytext=(0, t), arrowprops=dict(arrowstyle='->', color=STROKE, lw=.55, shrinkA=0, shrinkB=0))
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-.05, 1.05); ax.axis('off')
tags(fig, axs)
save(fig, HERE, 'figure', {'cost_T2': cost(2), 'cost_T4': cost(4), 'formula': '1+1/(12 n^2)', 'exact_T2': 1+1/48, 'exact_T4': 1+1/192})
