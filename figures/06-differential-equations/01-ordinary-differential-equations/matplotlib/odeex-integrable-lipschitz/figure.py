from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Lipschitz coefficients in time and Picard iterates of x'=x/(2 sqrt t).
from math import factorial
fig,axes=figure(width_mm=112,height_mm=50,ncols=2)
panel(fig,.07,.965,.965,.25,.22)
ax=axes[0]; t=np.linspace(.005,.25,500); ax.fill_between(t,0,1/(2*np.sqrt(t)),fc=BLUE_FILL,ec='none',zorder=1); t=np.linspace(.005,.5,500); ax.plot(t,1/(2*np.sqrt(t)),color=BLUE,lw=1.5,zorder=3); ax.plot(t,2/t,color=RED,lw=1.5,zorder=3)
ax.vlines(.25,0,1,color=MUTED,lw=.8,ls=':'); ax.set_xlim(0,.5); ax.set_ylim(0,14); ax.set_xticks([0,.25,.5]); ax.set_xticklabels(['0','1/4','1/2']); ax.set_yticks([0,5,10]); ax.set_xlabel('t',labelpad=1)
ax.text(.075,12,'2/t',color=RED,fontsize=7.5,ha='left',va='center'); ax.text(.3,1.65,'$1/(2\\sqrt{t})$',color=BLUE,fontsize=7.5,ha='left',va='center')
ax=axes[1]; t=np.linspace(0,.25,500); r=np.sqrt(t); S=0*t; lastk={}
for k in range(0,4):
    S=S+r**k/factorial(k); ax.plot(t,S,color=GREEN,lw=1.15,zorder=3); ax.text(.2525,S[-1]+(-.022 if k==2 else 0)+(.02 if k==3 else 0),f'k={k}',fontsize=7.5,va='center'); lastk[k]=float(S[-1])
ax.plot(t,np.exp(r),color=BLUE,lw=1.6,zorder=4); dot(ax,0,1); ax.text(.17,1.68,'$\\mathrm{e}^{\\sqrt{t}}$',color=BLUE,fontsize=8,ha='right',va='center')
ax.set_xlim(0,.295); ax.set_ylim(.95,1.8); ax.set_xticks([0,.125,.25]); ax.set_xticklabels(['0','1/8','1/4']); ax.set_yticks([1,1.5]); ax.set_xlabel('t',labelpad=1)
tags(fig,axes)
save(fig,HERE,'figure',{'values_at_1_4':lastk,'exact':float(np.exp(.5))})
