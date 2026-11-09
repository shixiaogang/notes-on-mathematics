from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# g(x,y)=min{.5(y-1-x)^2-x, .5(y+1-x)^2+x}; local minimizers x+1 (x>-1), x-1 (x<1).
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
g = lambda x,y: np.minimum(.5*(y-1-x)**2-x, .5*(y+1-x)**2+x)
y = np.linspace(-2.1,2.1,500)
ax = axs[0]
for xv,ls,off in [(-.4,':',0),(0,'-',0),(.4,'--',0)]:
    ax.plot(y,g(xv,y),color=BLUE,lw=1.25,ls=ls)
for xv in (-.4,0,.4):
    gb,lb = (xv+1,xv-1) if xv>0 else (xv-1,xv+1)
    if xv==0:
        ax.plot([1,-1],[0,0],'o',color=RED,ms=4,zorder=6)
    else:
        ax.plot([gb],[g(xv,gb)],'o',color=RED,ms=4,zorder=6)
        ax.plot([lb],[g(xv,lb)],'o',mfc='white',mec=RED,mew=.9,ms=4,zorder=6)
ax.text(-1.72,-.05,'$x=-0.4$',fontsize=7.5,color=BLUE,va='top')
ax.text(.05,.68,'$x=0$',fontsize=7.5,color=BLUE)
ax.text(1.0,-.62,'$x=0.4$',fontsize=7.5,color=BLUE,va='top',ha='left')
clean(ax,(-2.1,2.1),(-.95,1.15),'$y$','$g(x,y)$'); tag(ax,'(a)',-.27)
ax = axs[1]
a = np.linspace(0,1.5,50); b=np.linspace(-1,0,50)
ax.plot(a,a+1,color=ACTIVE,lw=1.8); ax.plot(b,b+1,color=MUTED,lw=1.1,ls='--')
a2 = np.linspace(-1.5,0,50); b2=np.linspace(0,1,50)
ax.plot(a2,a2-1,color=ACTIVE,lw=1.8); ax.plot(b2,b2-1,color=MUTED,lw=1.1,ls='--')
ax.plot([0,0],[-1,1],color=MUTED,lw=.85,ls=':')
ax.text(.05,2.1,'$y_+(x)$',color=INK); ax.text(-1.4,-1.3,'$y_-(x)$',color=INK)
clean(ax,(-1.5,1.5),(-2.7,2.7),'$x$','$y$'); tag(ax,'(b)',-.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'g':'min of two parabolas'})
