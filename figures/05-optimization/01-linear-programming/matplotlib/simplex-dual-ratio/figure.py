from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Dual ratio test after adding x1+x2<=3: s3=2-tau/3, s4=1-tau/3, s6=tau.
fig,ax=figure(width_mm=84,height_mm=46)
t=np.linspace(0,7.2,50)
ax.axhline(0,color=EDGE,lw=.85)
ax.plot(t,2-t/3,color=PURPLE,lw=1.4);ax.plot(t,1-t/3,color=BLUE,lw=1.4);ax.plot(t,t*.0+t,color=GREEN,lw=1.4)
ax.axvline(3,color=MUTED,lw=.85,ls=':')
ax.plot([3],[0],'o',color=RED,ms=5,zorder=5)
ax.text(.35,1.98,'$s_3$',fontsize=8,color=INK);ax.text(1.5,.72,'$s_4$',fontsize=8,color=INK);ax.text(2.0,2.42,'$s_6$',fontsize=8,color=INK)
ax.text(3.15,-.42,'$\\tau=3$',fontsize=7.5,color=INK)
ax.set_xlim(0,7.2);ax.set_ylim(-1.2,3.4);ax.set_xlabel('$\\tau$',labelpad=1);ax.set_ylabel('约化成本',labelpad=1)
save(fig,Path(__file__).resolve().parent,'figure',{'s3':'2-tau/3','s4':'1-tau/3','s6':'tau'})
