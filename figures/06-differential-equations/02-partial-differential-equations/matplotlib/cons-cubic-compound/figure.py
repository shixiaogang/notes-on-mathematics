from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: non-convex flux F=u^3/3 with (u_l,u_r)=(1,-1): upper concave envelope gives a shock joined to a fan; checked by upwind scheme.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax=axs[0]; style(ax); u=np.linspace(-1,1,400); ax.plot(u,u**3/3,color=BLUE,lw=1.4)
a=-.5; ax.plot([a,1],[a**3/3,1/3],color=LINE,lw=2)
ug=np.linspace(-1,a,100); ax.plot(ug,ug**3/3,color=LINE,lw=2)
ax.plot([-1,a,1],[-1/3,a**3/3,1/3],'o',ms=4,color=RED,zorder=5)
ax.text(-.46,-.135,'$a=-1/2$',va='bottom',ha='left')
ax.set_xlim(-1.08,1.08); ax.set_ylim(-.42,.42); ax.set_ylabel('$F(u)$'); sub(ax,'a','$u$')
ax=axs[1]; style(ax); ax.axhline(0,color=MUTED,lw=.7)
x=np.linspace(-.6,1.6,1200); s=.25
ex=np.where(x<s,1.0,np.where(x<1,-np.sqrt(np.maximum(x,0)),-1.0))
h=2e-3; xg=np.arange(-1,2+h/2,h); un=np.where(xg<0,1.0,-1.0); tau=.45*h; n=int(1/tau); tau=1/n
for _ in range(n):
    # Godunov flux: F'=u^2>=0, so the exact Riemann flux is the left value
    v=un.copy(); v[1:]-=tau/h*(un[1:]**3-un[:-1]**3)/3; un=v
ax.plot(np.r_[x[x<s],s,s,x[x>=s]],np.r_[ex[x<s],1,-.5,ex[x>=s]],color=BLUE,lw=1.5)
k=np.arange(0,len(xg),30); ax.plot(xg[k],un[k],'o',ms=1.5,color=GREEN,zorder=5)
ax.set_xlim(-.6,1.6); ax.set_ylim(-1.25,1.25); ax.set_ylabel('$u(x,1)$'); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'F=u^3/3; shock 1 to -1/2 at s=1/4, fan -sqrt(x/t) on 1/4<x/t<1; upwind h=2e-3'})
