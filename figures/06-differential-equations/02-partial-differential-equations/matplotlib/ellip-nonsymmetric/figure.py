from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# -u''+b u'=1, u(0)=u(1)=0.
fig, ax = figure(width_mm=86, height_mm=50)
panel(fig, left=.11, right=.97, top=.96, bottom=.17)
def sol(b): return X/b-(np.expm1(b*X)/np.expm1(b))/b
ax.plot(X, X*(1-X)/2, color=BLUE, lw=1.4)
ax.plot(X, sol(5), color=YELLOW, lw=1.5); ax.plot(X, sol(20), color=PURPLE, lw=1.4)
lab(ax, .22, .105, '$b=0$', BLUE, ha='right'); lab(ax, .78, .1, '$b=5$', YELLOW, ha='left'); lab(ax, .55, .04, '$b=20$', PURPLE, ha='left', va='bottom')
dot(ax, 0, 0, RED, 4); dot(ax, 1, 0, RED, 4)
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.003, .19); ax.set_xticks([0, 1]); ax.set_yticks([0, .1]); hat01(ax, yl='$u$')
save(fig, HERE, 'figure', {'u_b': 'x/b-(e^{bx}-1)/(b(e^b-1))'})
