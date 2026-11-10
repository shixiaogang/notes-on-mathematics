from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: viscous Burgers from the step (0,1), computed by a conservative explicit finite-difference scheme, approaches the fan.
fig, ax = figure(width_mm=92, height_mm=46); style(ax)
def solve(nu,t=1.0):
    h=min(nu/2,.01); x=np.arange(-3,3+h/2,h); u=(x>0)*1.0; tau=min(.2*h*h/nu,.2*h); n=int(round(t/tau)); tau=t/n
    for _ in range(n):
        F=u**2/2; v=u.copy()
        v[1:-1]+=-tau/(2*h)*(F[2:]-F[:-2])+nu*tau/h**2*(u[2:]-2*u[1:-1]+u[:-2]); u=v
    return x,u
xx=np.linspace(-.6,1.6,1000); ax.plot(xx,np.clip(xx,0,1),color=BLUE,lw=1.4)
ax.plot([-.6,.5,.5,1.6],[0,0,1,1],color=YELLOW,lw=1.5)
for nu,ls in ((.1,'-'),(.02,'--')):
    x,u=solve(nu); ax.plot(x,u,color=GREEN,lw=1.4,ls=ls)
ax.set_xlim(-.6,1.6); ax.set_ylim(0,1.12); ax.set_xlabel('$x$'); ax.set_ylabel('$u(x,1)$')
save(fig, HERE(__file__), 'figure', {'formula':'explicit conservative central scheme with viscosity; t=1'})
