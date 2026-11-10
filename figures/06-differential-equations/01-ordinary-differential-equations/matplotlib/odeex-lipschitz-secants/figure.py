from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Cones of slope L around a base point for x^2, 2sqrt|x|, |x|.
fig,axes=figure(width_mm=112,height_mm=46,ncols=3)
panel(fig,.05,.99,.965,.27,.2)
def draw(ax,f,x0,L,lo,hi,yl,tagx):
    xs=np.linspace(lo,hi,800); y0=f(x0)
    ax.fill_between(xs,y0-L*abs(xs-x0),y0+L*abs(xs-x0),fc=PURPLE_FILL,ec='none',zorder=1)
    ax.plot(xs,f(xs),color=BLUE,lw=1.4,zorder=3)
    dot(ax,x0,y0); ax.set_xlim(lo,hi); ax.set_ylim(*yl); ax.set_xlabel('$x$',labelpad=1)
draw(axes[0],lambda x:x**2,1.,4.,0.,2.,(-1,5),None); axes[0].set_xticks([0,1,2]); axes[0].set_yticks([0,2,4])
draw(axes[1],lambda x:2*np.sqrt(abs(x)),0.,4.,-.8,.8,(-.6,2.),None); axes[1].set_xticks([-.5,0,.5]); axes[1].set_yticks([0,1,2])
xs=np.linspace(-.25,.25,300); axes[1].plot(xs,2*np.sqrt(abs(xs)),color=RED,lw=1.8,zorder=4)
draw(axes[2],np.abs,0.,1.,-1.,1.,(-1.05,1.05),None); axes[2].set_xticks([-1,0,1]); axes[2].set_yticks([-1,0,1])
axes[1].text(.1,1.72,'越出',color=RED,fontsize=7.5,ha='left',va='center')
tags(fig,axes)
save(fig,HERE,'figure',{'L':[4,4,1]})
