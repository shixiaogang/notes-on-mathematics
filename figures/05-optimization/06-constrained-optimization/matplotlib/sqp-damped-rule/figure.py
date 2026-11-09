from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# sTr as a function of sTy with sTBs=.25 (the example), damping factor c=.2.
sBs=.25; v=np.linspace(-.5,.5,400); c=.2
def rr(u):
    th=1. if u>=c*sBs else (1-c)*sBs/(sBs-u); return th*u+(1-th)*sBs
fig,ax=figure(width_mm=86,height_mm=52); panels(fig,.14,.985,.98,.16,0)
ax.plot(v,v,color=YELLOW,lw=1.6,ls=(0,(4,2))); ax.plot(v,[rr(u) for u in v],color=GREEN,lw=1.4)
ax.axhline(0,color=MUTED,lw=.85); ax.axvline(c*sBs,color=MUTED,lw=.85,ls=':')
ax.plot([-.25],[-.25],'o',color=RED,ms=4.4,mew=0); ax.plot([-.25],[rr(-.25)],'o',color=GREEN,ms=4.4,mew=0)
ax.text(-.24,.085,'$\\mathbf{s}^{T}\\mathbf{r}$',color=GREEN,fontsize=8,ha='left'); ax.text(-.22,-.285,'$\\mathbf{s}^{T}\\mathbf{y}$',color=RED,fontsize=8,ha='left',va='center')
ax.text(c*sBs+.01,-.42,'$0.2\\,\\mathbf{s}^{T}\\mathbf{B}\\mathbf{s}$',fontsize=7.5,color=MUTED)
ax.set_xlim(-.5,.5); ax.set_ylim(-.5,.5); ax.set_xticks([-.4,-.2,0,.2,.4]); ax.set_yticks([-.4,-.2,0,.2,.4]); ax.set_xlabel('$\\mathbf{s}^{T}\\mathbf{y}$',labelpad=1); ax.set_ylabel('$\\mathbf{s}^{T}\\mathbf{r}$',labelpad=1)
save(fig,HERE,'figure',{'sBs':sBs,'c':c,'r_at_-.25':rr(-.25)})
