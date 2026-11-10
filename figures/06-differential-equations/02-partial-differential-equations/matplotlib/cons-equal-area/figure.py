from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: equal-area rule cuts the multi-valued graph: hand-checkable ramp at t=2, numerically tracked bump at t=3.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax=axs[0]; style(ax)
sc=1.5; ax.fill([1,sc,sc],[0,0,sc-1],color=BLUE_FILL,lw=0); ax.fill([sc,2,sc],[sc-1,1,1],color=BLUE_FILL,lw=0)
ax.plot([-.5,2],[1,1],color=BLUE,lw=1.4); ax.plot([1,3],[0,0],color=BLUE,lw=1.4,clip_on=False)
ax.plot([1,2],[0,1],color=RED,lw=1.5,ls='--'); ax.plot([sc,sc],[0,1],color=LINE,lw=2)
ax.text(1.27,.07,'$1/8$',ha='center'); ax.text(1.69,.89,'$1/8$',ha='center')
ax.set_xlim(-.5,3); ax.set_ylim(0,1.15); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); t=3.0
T,Xs,UL,UR=bump_shock(3.0); g=Xs[-1]; ul,ur=UL[-1],UR[-1]
s=GRID0; X=s+t*bump(s); neg=1+t*dbump(s)<0; il,ir=branches(t)
xl=np.interp(g,X[:il+1],s[:il+1]); xr=np.interp(g,X[ir:],s[ir:])
mid=np.linspace(xl,xr,1500)
xm=mid+t*bump(mid); um=bump(mid)
ax.fill(np.r_[xm,g],np.r_[um,ul],color=BLUE_FILL,lw=0)
m=(s>=xl)&(s<=xr)
ax.plot(np.where(s<xl,X,np.nan),np.where(s<xl,bump(s),np.nan),color=BLUE,lw=1.4)
ax.plot(np.where(s>xr,X,np.nan),np.where(s>xr,bump(s),np.nan),color=BLUE,lw=1.4)
ax.plot(xm,um,color=RED,lw=1.5,ls='--'); ax.plot([g,g],[ur,ul],color=LINE,lw=2)
ax.set_xlim(-3,7); ax.set_ylim(0,1.15); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'equal area cut; bump shock by RK4 on s=(u-+u+)/2', 'g_at_t3':float(g)})
