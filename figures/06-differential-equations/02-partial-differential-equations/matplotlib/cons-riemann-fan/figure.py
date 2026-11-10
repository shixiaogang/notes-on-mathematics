from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: Burgers Riemann (0,1): characteristics leave an empty wedge; the fan fills it continuously.
fig, axs = figure(width_mm=112, height_mm=50, ncols=3)
tm=2
for ax,l in zip(axs[:2],'ab'):
    style(ax)
    for x0 in np.arange(-2.4,-.01,.4): ax.plot([x0,x0],[0,tm],color=LINE,lw=.75)
    ax.plot([0,0],[0,tm],color=LINE,lw=.75)
    for x0 in np.arange(0,2.41,.4): ax.plot([x0,x0+tm],[0,tm],color=LINE,lw=.75)
    ax.plot([-2.4,4],[0,0],color=RED,lw=2,clip_on=False); ax.set_xlim(-2.4,4); ax.set_xticks([-2,0,2,4]); ax.set_ylim(0,tm); sub(ax,l,'$x$')
axs[0].set_ylabel('$t$')
axs[0].fill([0,0,2],[0,2,2],color=RED_FILL,lw=0,zorder=0)
for k in np.linspace(0,1,7)[1:-1]: axs[1].plot([0,2*k],[0,2],color=BLUE,lw=.95)
ax=axs[2]; style(ax); x=np.linspace(-1,3.4,1000); ax.plot([-1,0,0,3.4],[0,0,1,1],color=RED,lw=1.4)
ax.plot(x,np.clip(x/1,0,1),color=SHADES[1],lw=1.4); ax.plot(x,np.clip(x/2,0,1),color=SHADES[3],lw=1.4)
ax.text(.05,.98,'$0$',color=RED,va='bottom'); ax.text(.68,.52,'$1$',color=SHADES[1]); ax.text(1.78,.74,'$2$',color=SHADES[3])
ax.set_xlim(-1,3.4); ax.set_ylim(0,1.25); ax.set_ylabel('$u$'); sub(ax,'c','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'x/t fan for u_l=0,u_r=1'})
