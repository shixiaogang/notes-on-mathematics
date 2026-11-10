from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: mollifying the step (0,1) with a ramp of width eps gives classical solutions x/(eps+t) converging to the fan.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
ax=axs[0]; style(ax); tm=2; e=.5
for x0 in np.arange(-1.2,-.01,.4): ax.plot([x0,x0],[0,tm],color=LINE,lw=.75)
for x0 in np.linspace(0,e,6): ax.plot([x0,x0+x0/e*tm],[0,tm],color=LINE,lw=.75)
for x0 in np.arange(e+.4,2.1,.4): ax.plot([x0,x0+tm],[0,tm],color=LINE,lw=.75)
ax.plot([-1.2,2.3],[0,0],color=RED,lw=2,clip_on=False); ax.set_xlim(-1.2,3); ax.set_ylim(0,tm); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); x=np.linspace(-.5,1.8,800)
for e,c,tx,ty,lab in ((.5,SHADES[1],1.0,.5,'$\\varepsilon=0.5$'),(.2,SHADES[2],.15,.5,'$\\varepsilon=0.2$')):
    ax.plot(x,np.clip(x/(e+1),0,1),color=c,lw=1.4)
ax.text(.86,.42,'$0.5$',color=SHADES[1],ha='left'); ax.text(.72,.73,'$0.2$',color=SHADES[2],ha='right')
ax.plot(x,np.clip(x/(.05+1),0,1),color=SHADES[2],lw=1.0,ls='--')
ax.plot(x,np.clip(x,0,1),color=SHADES[3],lw=1.6)
ax.set_xlim(-.5,1.8); ax.set_ylim(0,1.15); ax.set_ylabel('$u(x,1)$'); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'u=x/(eps+t), 0<=x<=eps+t'})
