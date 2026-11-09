from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import simplex
from fractions import Fraction as F
A4=[[1,2,1,0,0,0,0],[2,1,0,1,0,0,0],[0,1,0,0,1,0,0],[1,1,0,0,0,-1,1]]; b4=[8,10,3,2]
M=10**6
st,tr,_=simplex(A4,b4,[-4,-5,0,0,0,0,M],[3,4,5,7])
xlim, ylim = (-.5, 6.4), (-.5, 4.6)
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
Aa=np.vstack([RES_A,[[-1.,-1.]]]); ba=np.concatenate([RES_B,[-2.]])
A,b=with_sign(Aa,ba); V=polygon(A,b)
ax=axs[0]; draw_region(ax,V); draw_line(ax,[1,1],2,xlim,ylim,lw=1.4)
contours(ax,PROFIT,[26],xlim,ylim)
r=[(float(t['x'][0]),float(t['x'][1])) for t in tr]; path(ax,r,color=GREEN); opt_point(ax,r[-1])
setup(ax,xlim,ylim,range(0,7),range(0,5),label='(a)')
# finite penalty: min 2x1+3x2 on the same constraints, artificial cost M.
Ms=[F(k,8) for k in range(0,33)]
av=[]
for m in Ms:
    st,t,_=simplex(A4,b4,[2,3,0,0,0,0,m],[3,4,5,7],'bland')
    av.append(float(t[-1]['x'][6]))
ax=axs[1]; X=[float(m) for m in Ms]
ax.axvspan(0,2,facecolor=RED_FILL,edgecolor='none',zorder=0)
ax.plot([v for v in X if v<2],[w for v,w in zip(X,av) if v<2],color=GREEN,lw=1.4,zorder=3)
ax.plot([v for v in X if v>2],[w for v,w in zip(X,av) if v>2],color=GREEN,lw=1.4,zorder=3)
ax.plot([2,2],[0,2],color=MUTED,lw=.85,ls=':',zorder=2)
ax.plot([2],[0],'o',color=RED,ms=4.5,zorder=5)
ax.text(2.1,.2,'$M=2$',fontsize=7.5,color=INK)
ax.set_xlim(0,4); ax.set_ylim(-.2,2.5); ax.set_xticks(range(0,5)); ax.set_yticks([0,1,2])
ax.set_xlabel('$M$\n(b)',labelpad=1); ax.set_ylabel('$v(M)$',labelpad=1)
save(fig,Path(__file__).resolve().parent,'figure',{'bigM_path':r,'finite_M':'min 2x1+3x2+Ma; threshold 2','a_values':av})
