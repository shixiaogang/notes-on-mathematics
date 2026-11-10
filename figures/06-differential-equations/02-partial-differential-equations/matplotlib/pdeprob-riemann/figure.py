from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: two weak solutions of Burgers with u0=0 (x<0), 1 (x>0) and the small-viscosity limit.
fig, axs = figure(width_mm=112, height_mm=50, ncols=3)
kw=dict(color=LINE,lw=.85)
ax=axs[0]
for x0 in np.arange(-1.5,0,.3): ax.plot([x0,x0],[0,1],**kw)
for x0 in np.arange(0.15,1.6,.3): ax.plot([x0,x0+1],[0,1],**kw)
# characteristics leaving the shock
for t0 in (.2,.45,.7):
    ax.plot([t0/2,t0/2],[t0,1],**kw); ax.plot([t0/2,t0/2+1-t0],[t0,1],**kw)
ax.plot([0,.5],[0,1],color=LINE,lw=2.4); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]
for x0 in np.arange(-1.5,0,.3): ax.plot([x0,x0],[0,1],**kw)
for x0 in np.arange(0.15,1.6,.3): ax.plot([x0,x0+1],[0,1],**kw)
for s in np.linspace(0,1,7): ax.plot([0,s],[0,1],color=BLUE,lw=1.0)
sub(ax,'b','$x$')
for ax in axs[:2]: style(ax); ax.set_xlim(-1,1.5); ax.set_ylim(0,1); ax.set_yticks([0,.5,1])
ax=axs[2]; style(ax)
dx=.005; x=np.arange(-3,4,dx); 
def viscous(nu,T=1.0):
    u=(x>0).astype(float); dt=min(.4*dx**2/nu,.4*dx); n=int(np.ceil(T/dt)); dt=T/n
    for _ in range(n):
        F=.25*(u[1:]**2+u[:-1]**2)-nu*(u[1:]-u[:-1])/dx
        u[1:-1]-=dt/dx*(F[1:]-F[:-1])
    return u
ax.plot([-1,.5,.5,2],[0,0,1,1],color=YELLOW,lw=1.6)
ax.plot([-1,0,1,2],[0,0,1,1],color=BLUE,lw=1.4)
ax.plot(x,viscous(.02),color=GREEN,lw=1.4)
ax.set_xlim(-1,2); ax.set_ylim(-.05,1.1); ax.set_ylabel(r'$u(x,1)$'); sub(ax,'c','$x$')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'shock speed 1/2; fan x/t; conservative central FD, nu=.02, dx=.005'})
