from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Basis stays optimal for profit p1 in [2.5,10] (p2=5).
xlim,ylim=(.6,7.4),(-.3,5.6)
fig,ax=figure(width_mm=90,height_mm=62)
A,b=with_sign(RES_A,RES_B);V=polygon(A,b);draw_region(ax,V)
o=np.array([4.,2.])
for p,c,ls,lw in [((4,5),BLUE,'--',1.1)]: draw_line(ax,p,p[0]*4+p[1]*2,xlim,ylim,color=c,ls=ls,lw=lw)
draw_line(ax,(2.5,5),20,xlim,ylim,lw=1.4);draw_line(ax,(10,5),50,xlim,ylim,lw=1.4)
for p,c,t,off in [((2.5,5),PURPLE,'$(2.5,5)$',(-.5,.13)),((4,5),BLUE,'$(4,5)$',(.08,.1)),((10,5),PURPLE,'$(10,5)$',(.08,-.02))]:
    e=o+.42*np.array(p)*(1 if p[0]<9 else .42*1.3)
    ax.annotate('',xy=e,xytext=o,arrowprops=dict(arrowstyle='-|>',color=c,lw=1.4,shrinkA=0,shrinkB=0,mutation_scale=9),zorder=6)
    ax.text(e[0]+off[0],e[1]+off[1],t,fontsize=7.5,color=INK,zorder=8)
opt_point(ax,o);ax.text(3.75,1.6,'$(4,2)$',fontsize=7.5,color=INK,ha='right')
setup(ax,xlim,ylim,range(1,8),range(0,6))
save(fig,Path(__file__).resolve().parent,'figure',{'range_p1':[2.5,10],'p2':5})
