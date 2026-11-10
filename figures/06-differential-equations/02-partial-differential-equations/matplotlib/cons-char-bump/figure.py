from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: straight characteristics of Burgers with the bump datum, their envelope and the first crossing.
fig, ax = figure(width_mm=100, height_mm=62); style(ax)
tm=3.2
for x0 in np.arange(-3,7.01,.3):
    ax.plot([x0,x0+bump(x0)*tm],[0,tm],color=LINE,lw=.7)
s=np.linspace(.12,4.5,1500); te=-1/dbump(s); xe=s+bump(s)*te; k=te<=tm
ax.plot(xe[k],te[k],color=RED,lw=1.5)
ax.plot([-3,7],[0,0],color=RED,lw=2,clip_on=False)
ax.plot([XSTAR],[TSTAR],'o',ms=4.5,color=RED,zorder=5)
ax.annotate('$(\\sqrt{3},\\,8\\sqrt{3}/9)$',xy=(XSTAR,TSTAR),xytext=(-1.6,2.1),color=INK,bbox=dict(fc='white',ec='none',pad=1.2),arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7))
ax.set_xlim(-3,7); ax.set_ylim(0,tm); ax.set_xlabel('$x$'); ax.set_ylabel('$t$')
save(fig, HERE(__file__), 'figure', {'formula':'x=x0+t/(1+x0^2); envelope t=-1/u0prime(x0)'})
