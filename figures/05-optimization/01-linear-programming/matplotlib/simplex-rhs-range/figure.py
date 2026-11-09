from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import simplex
from fractions import Fraction as F
A5=[[1,2,1,0,0],[2,1,0,1,0],[0,1,0,0,1]];c=[-4,-5,0,0,0]
fig,axs=figure(width_mm=112,height_mm=58,ncols=2)
xlim,ylim=(-.4,6.4),(-.5,4.8)
ax=axs[0]; A,b=with_sign(RES_A,RES_B); V=polygon(A,b); draw_region(ax,V)
draw_line(ax,RES_A[1],10,xlim,ylim,lw=1.4); draw_line(ax,RES_A[2],3,xlim,ylim)
for v,ls in [(5,':'),(8,'-'),(9.5,':')]: draw_line(ax,RES_A[0],v,xlim,ylim,ls=ls,lw=1.0)
ax.plot([5,3.5],[0,3],color=GREEN,lw=1.8,zorder=5)
ax.plot([5,3.5],[0,3],'o',color=GREEN,ms=3.6,zorder=6); opt_point(ax,(4,2))
ax.text(.1,1.6,'$b_1=5$',fontsize=7.5,color=MUTED)
ax.text(5.15,.5,'$b_1=8$',fontsize=7.5,color=INK);ax.text(5.0,2.3,'$b_1=9.5$',fontsize=7.5,color=MUTED)
setup(ax,xlim,ylim,range(0,7),range(0,5),label='(a)')
ax=axs[1]; G=[F(k,4) for k in range(0,65)]
vals=[]
for g in G:
    st,t,_=simplex(A5,[g,10,3],c,[3,4,5]); vals.append(-float(t[-1]['f']))
X=[float(g) for g in G]
ax.axvspan(5,9.5,facecolor=GREEN_FILL,edgecolor='none',zorder=0)
ax.plot(X,vals,color=BLUE,lw=1.4,zorder=3); opt_point(ax,(8,26))
ax.text(7.2,28.4,'',fontsize=7.5); ax.set_xlim(0,16);ax.set_ylim(0,34);ax.set_xticks([0,5,8,9.5,14]);ax.set_xticklabels(['0','5','8','9.5','14'])
ax.set_xlabel('$b_1$\n(b)',labelpad=1);ax.set_ylabel('最优利润',labelpad=1)
kink=[]
save(fig,Path(__file__).resolve().parent,'figure',{'range':[5,9.5],'values':dict(zip([str(g) for g in G[::8]],vals[::8]))})
print(list(zip(X[::4],vals[::4])))
