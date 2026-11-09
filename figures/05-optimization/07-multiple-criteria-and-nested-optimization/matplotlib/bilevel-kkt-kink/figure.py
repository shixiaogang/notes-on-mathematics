from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
# inner: min .5(y1-2)^2+.5(y2-1)^2 s.t. y1+y2<=tau; outer F=.5(y1-2)^2+.5(y2-2)^2.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax=axs[0]
for t,ls in [(2,'-'),(3,'--')]:
    yy=np.linspace(-.3,3,10); ax.plot(yy,t-yy,color=ACTIVE,lw=1.5,ls=ls)
Y1,Y2=np.meshgrid(np.linspace(0,3,200),np.linspace(-.3,2.6,200))
ax.contour(Y1,Y2,.5*(Y1-2)**2+.5*(Y2-1)**2,levels=[.125,.5,1.125],colors=BLUE,linewidths=.6)
ts=np.linspace(1.2,3,40); ax.plot((1+ts)/2,(ts-1)/2,color=GREEN,lw=1.5)
ax.plot([1.5],[.5],'o',color=GREEN,ms=4,zorder=6)
ax.plot([2],[1],'o',color=RED,ms=4,zorder=6)
ax.plot([2],[2],'o',mfc='white',mec=INK,mew=.9,ms=4,zorder=6)
ax.text(2.1,2.08,'外层目标点',fontsize=7.5,color=INK)
ax.text(.1,2.1,r'$\tau=2$',fontsize=7.5,color=ACTIVE); ax.text(.78,2.42,r'$\tau=3$',fontsize=7.5,color=ACTIVE)
clean(ax,(0,3),(-.3,2.6),'$y_1$','$y_2$'); tag(ax,'(a)',-.27)
ax=axs[1]
T=np.linspace(1.2,4,300)
P=lambda t: np.where(t<3,.125*(t-3)**2+.125*(t-5)**2,.5)
ax.plot(T,P(T),color=BLUE,lw=1.5)
t=np.linspace(1.5,2.5,5); ax.plot(t,P(np.array(2.))+(-1)*(t-2),color=GREEN,lw=1.2)
ax.plot([2],[P(np.array(2.))],'o',color=GREEN,ms=4,zorder=6)
ax.plot([3],[.5],'o',color=RED,ms=4,zorder=6)
ax.axvline(3,color=MUTED,lw=.85,ls=':')
ax.text(2.25,1.15,'斜率 -1',color=GREEN,fontsize=7.5)
ax.text(3.1,.62,'斜率 0',color=BLUE,fontsize=7.5); ax.text(2.0,.5,'左斜率 -1/2',color=BLUE,fontsize=7.5,ha='left',va='top')
clean(ax,(1.2,4),(.2,3.0),r'$\tau$',r'$\Phi(\tau)$'); tag(ax,'(b)',-.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'kink':3})
