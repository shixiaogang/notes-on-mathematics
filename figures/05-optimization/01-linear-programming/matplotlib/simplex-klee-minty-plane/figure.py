from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import simplex,klee_minty
a,b,c,B=klee_minty(2); st,tr,_=simplex(a,b,c,B)
fig,ax=figure(width_mm=78,height_mm=62)
xlim,ylim=(-.5,7.2),(-1.2,27.5)
V=np.array([[0,0],[5,0],[5,5],[0,25]],float);ax.fill(V[:,0],V[:,1],facecolor=BLUE_FILL,edgecolor=BLUE,lw=1,zorder=1)
r=[(float(t['x'][0]),float(t['x'][1])) for t in tr];path(ax,r,color=GREEN);opt_point(ax,r[-1])
for t,p,off in zip(tr,r,[(.15,1.),(.2,.6),(.2,.6),(.2,-.2)]):
    ax.text(p[0]+off[0],p[1]+off[1],f"$z={-t['f']}$",fontsize=7.5,color=INK,zorder=9)
setup(ax,xlim,ylim,range(0,7),range(0,26,5))
save(fig,Path(__file__).resolve().parent,'figure',{'path':r})
