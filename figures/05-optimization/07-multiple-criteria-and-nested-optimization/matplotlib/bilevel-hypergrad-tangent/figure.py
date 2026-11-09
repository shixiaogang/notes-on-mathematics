from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
x = np.linspace(0,4,200)
ax = axs[0]
ax.plot(x,ystar(x),color=ACTIVE,lw=1.8)
t=np.linspace(0,2.4,10); ax.plot(t,1.5-.75*(t-1),color=GREEN,lw=1.2)
ax.plot([1],[1.5],'o',color=GREEN,ms=4,zorder=6)
ax.text(1.75,1.28,'斜率 -3/4',color=GREEN,fontsize=7.5); ax.text(.42,2.45,r'$y^*(x)$',color=ACTIVE)
clean(ax,(0,4),(0,3.2),'$x$','$y$'); tag(ax,'(a)',-.3)
ax = axs[1]
ax.plot(x,Phi(x),color=BLUE,lw=1.5)
t=np.linspace(0,2.1,10); ax.plot(t,.125-.375*(t-1),color=GREEN,lw=1.2)
ax.plot([0,3.2],[.125,.125],color=YELLOW,lw=1.5,ls='--')
ax.plot([1],[.125],'o',color=GREEN,ms=4,zorder=6); ax.plot([2],[0],'o',color=RED,ms=4,zorder=6,clip_on=False)
ax.text(1.15,.33,'斜率 -3/8',color=GREEN,fontsize=7.5); ax.text(2.25,.17,'固定 y 时斜率 0',color=YELLOW,fontsize=7.5)
ax.text(.32,1.25,r'$\Phi(x)$',color=BLUE)
clean(ax,(0,4),(0,1.5),'$x$',None); tag(ax,'(b)',-.3)
save(fig, Path(__file__).resolve().parent, 'figure', {'x':1})
