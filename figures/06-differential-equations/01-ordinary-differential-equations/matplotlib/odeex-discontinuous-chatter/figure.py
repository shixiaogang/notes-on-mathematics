from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# f=-1 for x>=0, f=+1 for x<0. No solution from x(0)=0; Euler polygons chatter.
fig,axes=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.075,.97,.965,.25,.2)
f=lambda t,x:-1. if x>=0 else 1.
ax=axes[0]; ax.set_xlim(0,2); ax.set_ylim(-1.1,1.1); field(ax,f,nt=15,nx=10)
ax.plot([0,1,2],[1,0,0],color=BLUE,lw=1.5,zorder=4); ax.plot([0,1],[-1,0],color=BLUE,lw=1.5,zorder=4); ax.lines[-1].set_ls('-')
dot(ax,0,0); ax.set_xticks([0,1,2]); ax.set_yticks([-1,0,1]); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x$',labelpad=1)
ax=axes[1]
for h,c,ls in ((.25,YELLOW,'-'),(.0625,GREEN,'-')):
    n=int(round(1/h)); ints=[0]
    for k in range(n): ints.append(ints[-1]+(-1 if ints[-1]>=0 else 1))
    ax.plot(np.arange(n+1)*h,np.array(ints)*h,color=c,lw=1.25,ls=ls,marker='o',ms=2.3,mew=0)
ax.axhline(0,color=STROKE,lw=1.,zorder=1); dot(ax,0,0)
ax.text(.98,.022,'折线的极限',color=INK,fontsize=7.5,ha='right',va='bottom')
ax.text(.27,-.235,'$h=1/4$',color=INK,fontsize=7.5,ha='left',va='center'); ax.text(.62,-.1,'$h=1/16$',color=INK,fontsize=7.5,ha='left',va='center')
ax.set_xlim(0,1); ax.set_ylim(-.3,.1); ax.set_xticks([0,.5,1]); ax.set_yticks([-.25,0]); ax.set_xlabel('$t$',labelpad=1)
tags(fig,axes)
save(fig,HERE,'figure',{'steps':[.25,.0625]})
