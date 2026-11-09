from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import simplex
A4=[[1,2,1,0,0,0,0],[2,1,0,1,0,0,0],[0,1,0,0,1,0,0],[1,1,0,0,0,-1,1]]; b4=[8,10,3,7]
st,p1,_=simplex(A4,b4,[0]*6+[1],[3,4,5,7])
xlim, ylim = (-.5, 7.6), (-.5, 7.6)
fig, ax = figure(width_mm=90, height_mm=66)
A,b=with_sign(RES_A,RES_B); V=polygon(A,b)
draw_region(ax,V)
draw_line(ax,[1,1],7,xlim,ylim,lw=1.4,color=RED)
draw_line(ax,[1,1],6,xlim,ylim,lw=.85,color=MUTED,ls=':')
r=[(float(t['x'][0]),float(t['x'][1])) for t in p1]; path(ax,r,color=GREEN)
for t,off in zip(p1,[(.12,.14),(.14,.14),(.16,.08)]):
    x=(float(t['x'][0]),float(t['x'][1]))
    ax.text(x[0]+off[0],x[1]+off[1],f"$v={t['f']}$",fontsize=7.5,color=INK,zorder=9)
ax.text(.45,6.72,'$x_1+x_2=7$',fontsize=7.5,color=INK)
ax.text(.42,5.72,'$x_1+x_2=6$',fontsize=7.5,color=MUTED)
setup(ax,xlim,ylim,range(0,8),range(0,8))
save(fig,Path(__file__).resolve().parent,'figure',{'phase1':r,'residual':[str(t['f']) for t in p1]})
