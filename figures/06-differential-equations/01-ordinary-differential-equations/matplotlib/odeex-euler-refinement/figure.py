from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Euler polygons on [0,1/4] for x'=x^2,x(0)=1, N=1,2,4,8.
fig,ax=figure(width_mm=88,height_mm=50)
panel(fig,.095,.97,.965,.17)
d=.25
styles={1:(YELLOW,(0,(4,2)),1.25),2:(PURPLE,(0,(2,1.5)),1.15),4:(GREEN,(0,(5,1.5,1,1.5)),1.2),8:(GREEN,'-',1.3)}
res={}
for N,(c,ls,lw) in styles.items():
    h=d/N; xs=[1.]
    for k in range(N): xs.append(xs[-1]+h*xs[-1]**2)
    t=[k*h for k in range(N+1)]; res[N]=xs[-1]
    ax.plot(t,xs,color=c,ls=ls,lw=lw,marker='o',ms=2.6,mew=0)
    ax.text(.2525,xs[-1]+{1:0,2:0,4:-.006,8:.006}[N],f'$N={N}$',color=INK,fontsize=7.5,va='center')
t=np.linspace(0,d,200); ax.plot(t,1/(1-t),color=BLUE,lw=1.6,zorder=5)
ax.text(.226,1.325,'$1/(1-t)$',color=BLUE,fontsize=7.5,ha='right',va='bottom')
dot(ax,0,1); ax.set_xlim(-.005,.285); ax.set_ylim(.98,1.36); ax.set_xticks([0,.0625,.125,.1875,.25]); ax.set_xticklabels(['0','1/16','1/8','3/16','1/4']); ax.set_xlabel('$t$',labelpad=1); ax.set_ylabel('$x$',labelpad=1)
save(fig,HERE,'figure',{'end_values':res,'exact':4/3})
