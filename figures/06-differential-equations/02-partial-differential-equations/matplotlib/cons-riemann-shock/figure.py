from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: Burgers Riemann problem (2,0): shock speed 1, characteristics absorbed, profile and space-time field.
fig, axs = figure(width_mm=112, height_mm=50, ncols=3)
ax=axs[0]; style(ax); tm=2
for x0 in np.arange(-2.5,-.01,.4):
    e=min(-x0,tm); ax.plot([x0,x0+2*e],[0,e],color=LINE,lw=.75)
for x0 in np.arange(.4,3.01,.4):
    e=min(x0,tm); ax.plot([x0,x0],[0,e],color=LINE,lw=.75)
ax.plot([0,2],[0,2],color=LINE,lw=2.2); ax.plot([-2.5,3],[0,0],color=RED,lw=2,clip_on=False)
ax.set_xlim(-2.5,3); ax.set_ylim(0,tm); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); ax.plot([-2,0,0,3],[2,2,0,0],color=RED,lw=1.4)
ax.plot([-2,1,1,3],[2,2,0,0],color=SHADES[1],lw=1.4); ax.plot([-2,2,2,3],[2,2,0,0],color=SHADES[3],lw=1.4)
ax.text(-.42,1.1,'$0$',color=RED); ax.text(.75,1.1,'$1$',color=SHADES[1]); ax.text(1.72,1.1,'$2$',color=SHADES[3])
ax.set_xlim(-2,3); ax.set_ylim(0,2.4); ax.set_ylabel('$u$'); sub(ax,'b','$x$')
ax=axs[2]; style(ax); x=np.linspace(-2,3,400); t=np.linspace(0,2,300); XX,TT=np.meshgrid(x,t)
ax.pcolormesh(XX,TT,np.where(XX<TT,2.0,0.0),cmap=FIELD,vmin=0,vmax=2,shading='auto',rasterized=True)
ax.plot([0,2],[0,2],color=LINE,lw=2.0); ax.set_xlim(-2,3); ax.set_ylim(0,2); ax.set_ylabel('$t$'); sub(ax,'c','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'u_l=2,u_r=0,s=1'})
