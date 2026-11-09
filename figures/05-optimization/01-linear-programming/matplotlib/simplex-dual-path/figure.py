from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import dual_simplex
c=[-4,-5,0,0,0]
A5=[[1,2,1,0,0],[2,1,0,1,0],[0,1,0,0,1]]
st,tr=dual_simplex(A5,[13,2,4],c,[1,5,2])
A6=[[1,2,1,0,0,0],[2,1,0,1,0,0],[0,1,0,0,1,0],[1,1,0,0,0,1]]
st2,tr2=dual_simplex(A6,[8,10,3,3],c+[0],[1,5,2,6])
fig,axs=figure(width_mm=112,height_mm=62,ncols=2)
def pts(t): return [(float(r['x'][0]),float(r['x'][1])) for r in t]
xlim,ylim=(-4.3,3.6),(-.6,9.2)
ax=axs[0]; A,b=with_sign(RES_A,np.array([13.,2.,4.])); V=polygon(A,b); draw_region(ax,V)
for a,v in zip(RES_A,[13.,2.,4.]): draw_line(ax,a,v,xlim,ylim)
ax.axvline(0,color=EDGE,lw=.85,zorder=2)
r=pts(tr); path(ax,r,color=GREEN); opt_point(ax,r[-1])
for k,(p,off) in enumerate(zip(r,[(.25,.1),(.25,.1),(.2,.25)])): ax.text(p[0]+off[0],p[1]+off[1],f'$t={k}$',fontsize=7.5,color=INK,zorder=9)
setup(ax,xlim,ylim,range(-4,4,2),range(0,10,2),label='(a)')
xlim,ylim=(-3.2,5.4),(-.6,6.4)
ax=axs[1]; Aa=np.vstack([RES_A,[[1.,1.]]]); ba=np.concatenate([RES_B,[3.]]); A,b=with_sign(Aa,ba); V=polygon(A,b); draw_region(ax,V)
draw_line(ax,[1,1],3,xlim,ylim,lw=1.4); ax.axvline(0,color=EDGE,lw=.85,zorder=2)
draw_line(ax,RES_A[0],8,xlim,ylim); draw_line(ax,RES_A[1],10,xlim,ylim); draw_line(ax,RES_A[2],3,xlim,ylim)
r2=pts(tr2); path(ax,r2,color=GREEN); opt_point(ax,r2[-1])
for k,(p,off) in enumerate(zip(r2,[(.15,.18),(.22,.1),(-.95,-.62)])): ax.text(p[0]+off[0],p[1]+off[1],f'$t={k}$',fontsize=7.5,color=INK,zorder=9)
setup(ax,xlim,ylim,range(-2,6,2),range(0,7,2),label='(b)')
save(fig,Path(__file__).resolve().parent,'figure',{'rhs_change':r,'new_row':r2,'dual_values':[str(t['f']) for t in tr]})
