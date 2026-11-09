from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

from simplex_core import simplex
from fractions import Fraction as F
C=[[F(1,2),F(-11,2),F(-5,2),9,1,0,0],[F(1,2),F(-3,2),F(-1,2),1,0,1,0],[1,0,0,0,0,0,1]]
b=[0,0,1]; c=[-10,57,9,24,0,0,0]
st,d,_=simplex(C,b,c,[5,6,7],'dantzig',max_rounds=19)
st2,bl,_=simplex(C,b,c,[5,6,7],'bland')
fig,ax=figure(width_mm=100,height_mm=48)
ax.plot([t['t'] for t in d],[float(t['f']) for t in d],'-o',color=YELLOW,lw=1.6,ms=3,zorder=3)
ax.plot([t['t'] for t in bl],[float(t['f']) for t in bl],'-o',color=GREEN,lw=1.4,ms=3,zorder=4)
for k in (6,12,18): ax.axvline(k,color=MUTED,lw=.7,ls=':',zorder=1)
ax.plot([bl[-1]['t']],[float(bl[-1]['f'])],'o',color=RED,ms=5,zorder=6)
ax.text(10.5,.1,'Dantzig',fontsize=7.5,color=INK); ax.text(5.1,-.72,'Bland',fontsize=7.5,color=INK)
ax.set_xlim(-.3,18.6); ax.set_ylim(-1.2,.4); ax.set_xticks(range(0,19,3)); ax.set_yticks([-1,0])
ax.set_xlabel('换基次数 t',labelpad=1); ax.set_ylabel('目标值 f',labelpad=1)
save(fig,Path(__file__).resolve().parent,'figure',{'bland_pivots':len(bl)-1,'bland_optimum':str(bl[-1]['f']),'dantzig_period':6})
