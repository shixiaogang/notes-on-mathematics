from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: y u_xx + u_yy = 0 changes type across y=0; characteristic curves x -+ (2/3)(-y)^{3/2} = const in y<0.
fig, ax = figure(width_mm=84, height_mm=52); style(ax)
ax.fill_between([-1.5,1.5],0,.75,color=BLUE_FILL,lw=0)
s=np.linspace(0,1,120)
for c in np.arange(-2.2,2.3,.4):
    ax.plot(c+2/3*s**1.5,-s,color=LINE,lw=.8); ax.plot(c-2/3*s**1.5,-s,color=LINE,lw=.8)
ax.plot([-1.5,1.5],[0,0],color=RED,lw=1.6)
ax.text(0,.38,'椭圆型',ha='center',va='center'); ax.text(1.46,.09,'退化',ha='right',va='center',color=MUTED,fontsize=7.5)
ax.set_xlim(-1.5,1.5); ax.set_ylim(-1,.75); ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.text(-1.42,-.9,'双曲型',va='center',backgroundcolor='white')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'characteristics x -+ (2/3)(-y)^(3/2)=c, y<0'})
