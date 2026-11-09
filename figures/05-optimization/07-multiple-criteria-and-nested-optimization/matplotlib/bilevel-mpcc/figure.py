from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# (a) a>=0,b>=0,ab=0. (b) inner min .5(y-x)^2 s.t. y>=0; graph y=max(x,0), outer F=.5(x+1)^2+.5(y-1)^2.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax=axs[0]
ax.plot([0,2.2],[0,0],color=ACTIVE,lw=2,clip_on=False); ax.plot([0,0],[0,2.2],color=ACTIVE,lw=2,clip_on=False)
ax.annotate('',xy=(1.2,.72),xytext=(1.2,0),arrowprops=dict(arrowstyle='-|>',color=RED,lw=1.1,shrinkA=0,shrinkB=0))
ax.plot([1.2],[0],'o',color=GREEN,ms=4,zorder=6,clip_on=False)
ax.plot([0],[0],'o',color=RED,mfc=RED_FILL,mec=RED,mew=.9,ms=4.4,zorder=6,clip_on=False)
ax.text(1.32,.52,'离开可行集',color=RED,fontsize=7.5); ax.text(.1,1.55,'$a=0$',fontsize=7.5,color=ACTIVE); ax.text(1.6,.1,'$b=0$',fontsize=7.5,color=ACTIVE)
clean(ax,(-.1,2.3),(-.1,2.3),'$a$','$b$'); ax.set_xticks([0,1,2]); ax.set_yticks([0,1,2]); tag(ax,'(a)',-.27)
ax=axs[1]
X,Y=np.meshgrid(np.linspace(-2.2,1.5,200),np.linspace(-.6,2,200))
ax.contour(X,Y,.5*(X+1)**2+.5*(Y-1)**2,levels=[.125,.5,1.,1.5,2.2],colors=BLUE,linewidths=.6)
ax.plot([-2.2,0],[0,0],color=ACTIVE,lw=1.8); ax.plot([0,1.5],[0,1.5],color=ACTIVE,lw=1.8)
ax.plot([-1],[0],'o',color=RED,ms=4.2,zorder=6)
ax.plot([-1],[1],'o',mfc='white',mec=BLUE,mew=.9,ms=4,zorder=6)
ax.text(1.0,.5,'$y=x$',color=INK,fontsize=7.5); ax.text(-2.05,-.42,'$y=0$',color=INK,fontsize=7.5)
clean(ax,(-2.2,1.5),(-.6,2),'$x$','$y$'); tag(ax,'(b)',-.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'F':'.5(x+1)^2+.5(y-1)^2'})
