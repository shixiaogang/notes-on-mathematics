from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: comparison and sup-norm stability, computed from Hopf-Lax for H=p^2/2 with u0=cos x, v0=cos x+.3+.3 sin 2x.
fig, axs = figure(width_mm=112, height_mm=48, ncols=3)
x=np.linspace(-np.pi,np.pi,601); ys=np.linspace(-12,12,24001)
a=lambda y:np.cos(y); b=lambda y:np.cos(y)+.3+.3*np.sin(2*y)
ax=axs[0]; style(ax); ax.plot(x,a(x),color=BLUE,lw=1.4); ax.plot(x,b(x),color=YELLOW,lw=1.6); ax.set_xlim(-np.pi,np.pi); ax.set_xticks([-3,0,3]); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); t=1.2; U,_=hopf_lax(x,t,a,ys); V,_=hopf_lax(x,t,b,ys); ax.plot(x,U,color=BLUE,lw=1.4); ax.plot(x,V,color=YELLOW,lw=1.6); ax.set_xlim(-np.pi,np.pi); ax.set_xticks([-3,0,3]); sub(ax,'b','$x$')
ax=axs[2]; style(ax); ts=np.linspace(.02,3,60); gmax=[];gmin=[]
for t in ts:
    U,_=hopf_lax(x,t,a,ys); V,_=hopf_lax(x,t,b,ys); gmax.append((V-U).max()); gmin.append((V-U).min())
ax.plot(ts,gmax,color=RED,lw=1.4); ax.plot(ts,gmin,color=GREEN,lw=1.4); ax.axhline(.6,color=MUTED,lw=.85,ls=':'); ax.set_xlim(0,3); ax.set_ylim(-.03,.66); ax.set_ylabel('$v-u$'); sub(ax,'c','$t$')
print('min gap',min(gmin),'max gap',max(gmax))
save(fig,HERE,'figure',{'formula':'Hopf-Lax with u0=cos,v0=cos+.3+.3 sin 2x; (b) t=1.2'})
