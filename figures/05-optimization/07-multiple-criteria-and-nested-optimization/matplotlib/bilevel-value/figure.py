from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"bilevel-common"))
from bilevel_core import *
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
ax=axs[0]
x=np.linspace(-1,1,200)
ax.plot(x,-x,color=MUTED,lw=1,ls='--'); ax.plot(x,x,color=MUTED,lw=1,ls='--')
ax.plot(x,-np.abs(x),color=BLUE,lw=1.6)
ax.plot([0],[0],'o',color=RED,mfc=RED_FILL,mec=RED,mew=.9,ms=4.4,zorder=6)
ax.text(0,-.8,r'$V(x)=-|x|$',color=BLUE,fontsize=7.5,ha='center')
ax.text(.28,.08,r'$g(x,y_-(x))$',color=MUTED,fontsize=7.5); ax.text(-.92,.08,r'$g(x,y_+(x))$',color=MUTED,fontsize=7.5)
clean(ax,(-1,1),(-1.1,1.1),'$x$',None); tag(ax,'(a)',-.27)
ax=axs[1]
x=np.linspace(0,5,300); eps=.1
w=np.sqrt(2*eps/(1+x)); ys=ystar(x)
ax.fill_between(x,ys-w,ys+w,facecolor=BLUE_FILL,edgecolor=BLUE,lw=.6)
ax.plot(x,ys,color=ACTIVE,lw=1.5)
ax.axhline(1,color=MUTED,lw=.85,ls='--')
u1=(6.2-np.sqrt(6.2**2-36))/2-1; u2=(6.2+np.sqrt(6.2**2-36))/2-1
print(u1,u2)
ax.plot([u1,u2],[1,1],color=RED,lw=2.2,zorder=5)
ax.plot([2],[1],'o',color=RED,ms=4.2,zorder=6)
ax.text(2.15,1.1,'松弛后的解',fontsize=7.5,color=RED); ax.text(.5,2.55,r'$y^*(x)$',color=ACTIVE)
clean(ax,(0,5),(0,3.5),'$x$','$y$'); tag(ax,'(b)',-.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'eps':eps})
