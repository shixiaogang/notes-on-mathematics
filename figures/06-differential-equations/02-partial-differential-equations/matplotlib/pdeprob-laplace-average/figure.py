from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: second difference compares a point with the average of its two neighbours.
fig, ax = figure(width_mm=96, height_mm=48)
style(ax)
u = lambda x: np.exp(-x**2)
X = np.linspace(-3,3,500); ax.plot(X,u(X),color=BLUE,lw=1.4)
h = .55
for x0 in (0.0,1.75):
    a,b = x0-h,x0+h; m=(u(a)+u(b))/2
    ax.plot([a,b],[u(a),u(b)],color=PURPLE,lw=.95,ls='--')
    ax.plot([a,b],[u(a),u(b)],'o',ms=3,color=PURPLE)
    ax.plot([x0],[m],'s',ms=3,color=PURPLE)
    ax.plot([x0],[u(x0)],'o',ms=3.8,color=RED)
    ax.annotate('',xy=(x0,m),xytext=(x0,u(x0)),arrowprops=dict(arrowstyle='-|>',color=RED,lw=.95,shrinkA=2,shrinkB=2,mutation_scale=7))
ax.text(.12,1.04,'高于邻点平均：下降',color=INK,va='center')
ax.text(1.95,.42,'低于邻点平均：上升',color=INK,va='center',ha='center')
ax.set_xlim(-3,3.1); ax.set_ylim(0,1.15); ax.set_xlabel('$x$'); ax.set_ylabel('$u$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'u=exp(-x^2); neighbours at x0 +- 0.55, x0 in {0,1.75}'})
