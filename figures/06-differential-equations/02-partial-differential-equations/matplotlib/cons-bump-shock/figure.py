from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/cons-common'))
from cons_common import *
# Target: the bump datum after breaking: curved shock absorbs characteristics, profile develops a decaying front.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
T,Xs,UL,UR=bump_shock(12.0)
ax=axs[0]; style(ax); tm=6
for x0 in np.arange(-3,8.01,.3):
    u=bump(x0); tt=np.linspace(0,tm,3000); X=x0+u*tt; gam=np.interp(tt,T,Xs,left=np.nan)
    d=X-gam; idx=np.where(np.diff(np.sign(d[~np.isnan(d)])))[0]
    off=np.where(~np.isnan(d))[0][0]
    if len(idx): e=tt[idx[0]+off]
    else: e=tm
    ax.plot([x0,x0+u*e],[0,e],color=LINE,lw=.7)
k=T<=tm; ax.plot(Xs[k],T[k],color=LINE,lw=2.2); ax.plot([XSTAR],[TSTAR],'o',ms=4.5,color=RED,zorder=5)
ax.plot([-3,8],[0,0],color=RED,lw=2,clip_on=False); ax.set_xlim(-3,8); ax.set_ylim(0,tm); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); x=np.linspace(-4,11,6000); ax.plot(x,bump(x),color=RED,lw=1.4)
for t,c,lab,tx,ty in ((TSTAR,SHADES[0],'$T^{*}$',2.1,.97),(3,SHADES[1],'$3$',3.25,.72),(6,SHADES[2],'$6$',5.3,.62),(12,SHADES[3],'$12$',7.7,.54)):
    u=bump_profile(x,t,T,Xs); g=np.interp(t,T,Xs); j=np.searchsorted(x,g)
    xx=np.r_[x[:j],g,g,x[j:]]; uu=np.r_[u[:j],bump_profile(np.array([g-1e-9]),t,T,Xs),bump_profile(np.array([g+1e-9]),t,T,Xs),u[j:]]
    ax.plot(xx,uu,color=c,lw=1.4); ax.text(tx,ty,lab,color=c)
ax.text(-3.2,.42,'$t=0$',color=RED)
ax.set_xlim(-4,11); ax.set_ylim(0,1.12); ax.set_ylabel('$u$'); sub(ax,'b','$x$')
save(fig, HERE(__file__), 'figure', {'formula':'bump shock path by RK4', 's12':float(Xs[-1])})
