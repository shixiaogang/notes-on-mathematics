from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Delayed approximations y_N for x'=-x+g(t), x(0)=0, g=1 on [0,1), 0 after.
fig,ax=figure(width_mm=92,height_mm=50)
panel(fig,.11,.97,.97,.16)
d=2.; g=lambda s:(s<1.)*1.
n=4000; t=np.linspace(0,d,n+1); dt=t[1]-t[0]
def delay(N):
    lag=int(round(n/N)); y=np.zeros(n+1); F=np.zeros(n+1)
    # F[i]=int_0^{t_i} f(s,y(s)) ds by the left rectangle rule, y[i]=F[i-lag]
    for i in range(n):
        y[i+1]=F[i+1-lag] if i+1>=lag else 0.
        F[i+1]=F[i]+dt*(-y[i]+g(t[i]))
    return y
for N,c,ls in ((4,YELLOW,'-'),(16,GREEN,'-')):
    ax.plot(t,delay(N),color=c,lw=1.3,ls=ls,zorder=3)
x=np.where(t<=1,1-np.exp(-t),(1-np.exp(-1))*np.exp(-(t-1))); ax.plot(t,x,color=BLUE,lw=1.6,zorder=4); dot(ax,0,0)
ax.text(.42,.08,'N=4',color=YELLOW,fontsize=7.5,ha='left',va='bottom'); ax.text(.32,.40,'N=16',color=GREEN,fontsize=7.5,ha='right',va='bottom')
ax.text(.7,.60,'x(t)',color=BLUE,fontsize=7.5,ha='right',va='bottom')
ax.set_xlim(0,2); ax.set_ylim(-.02,1.0); ax.set_xticks([0,.5,1,1.5,2]); ax.set_yticks([0,.5]); ax.set_xlabel('t',labelpad=1); ax.set_ylabel('x',labelpad=1)
save(fig,HERE,'figure',{'delta':2,'N':[4,16]})
