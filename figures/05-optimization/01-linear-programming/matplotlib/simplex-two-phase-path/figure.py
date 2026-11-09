from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import simplex
A4=[[1,2,1,0,0,0,0],[2,1,0,1,0,0,0],[0,1,0,0,1,0,0],[1,1,0,0,0,-1,1]]; b4=[8,10,3,2]
st,p1,_=simplex(A4,b4,[0]*6+[1],[3,4,5,7])
B=p1[-1]['B']; st,p2,_=simplex([r[:6] for r in A4],b4,[-4,-5,0,0,0,0],B)
xlim, ylim = (-.5, 6.4), (-.5, 4.6)
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
Aa=np.vstack([RES_A,[[-1.,-1.]]]); ba=np.concatenate([RES_B,[-2.]])
A,b=with_sign(Aa,ba); V=polygon(A,b)
def pts(tr): return [(float(r['x'][0]),float(r['x'][1])) for r in tr]
axs[0].fill(V[:,0],V[:,1],facecolor=BLUE_FILL,edgecolor=BLUE,lw=1.0,zorder=1)
axs[1].fill(V[:,0],V[:,1],facecolor=BLUE_FILL,edgecolor=BLUE,lw=1.0,zorder=1)
for ax,lab in zip(axs,['(a)','(b)']):
    draw_line(ax,[1,1],2,xlim,ylim,lw=1.4)
    setup(ax,xlim,ylim,range(0,7),range(0,5),label=lab)
axs[0].fill([0,2,0],[0,0,2],facecolor=RED_FILL,edgecolor='none',zorder=1)
path(axs[0],pts(p1),color=GREEN)
axs[0].text(.05,-.42,'',fontsize=7.5)
axs[0].text(.1,.16,'$v=2$',fontsize=7.5,color=INK); axs[0].text(2.1,.16,'$v=0$',fontsize=7.5,color=INK)
contours(axs[1],PROFIT,[8,26],xlim,ylim)
r=pts(p2); path(axs[1],r,color=GREEN); opt_point(axs[1],r[-1])
save(fig,Path(__file__).resolve().parent,'figure',{'phase1':pts(p1),'phase2':pts(p2)})
