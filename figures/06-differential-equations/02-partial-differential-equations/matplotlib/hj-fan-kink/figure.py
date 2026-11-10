from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: H=p^2/2; convex kink u0=|x| opens a fan, concave kink u0=-|x| persists. Formulas from Hopf-Lax, checked numerically.
fig, axs = figure(width_mm=112, height_mm=92, nrows=2, ncols=2)
X=np.linspace(-2.5,2.5,1001); ys=np.linspace(-14,14,56001); xc=np.linspace(-2.5,2.5,101)
a=lambda x,t:np.where(np.abs(x)<=t,x*x/(2*t),np.abs(x)-t/2)
b=lambda x,t:-np.abs(x)-t/2
print('err a',np.abs(hopf_lax(xc,1.,np.abs,ys)[0]-a(xc,1.)).max(),'err b',np.abs(hopf_lax(xc,1.,lambda y:-np.abs(y),ys)[0]-b(xc,1.)).max())
ax=axs[0,0]; style(ax)
for y in np.arange(-2.5,-.01,.25): ax.plot([y,y-1.5],[0,1.5],color=BLUE,lw=.85)
for y in np.arange(.25,2.51,.25): ax.plot([y,y+1.5],[0,1.5],color=BLUE,lw=.85)
for s in np.linspace(-1,1,9): ax.plot([0,1.5*s],[0,1.5],color=GREEN,lw=.95)
ax.plot([0],[0],'o',ms=4.2,color=RED,zorder=6)
ax.set_xlim(-2.5,2.5); ax.set_ylim(0,1.5); ax.set_ylabel('$t$'); sub(ax,'a','$x$')
ax=axs[0,1]; style(ax); ax.plot(X,np.abs(X),color=RED,lw=1.3)
for t,c in ((.5,SHADES[1]),(1.5,SHADES[3])): ax.plot(X,a(X,t),color=c,lw=1.4)
ax.set_xlim(-2.5,2.5); ax.set_ylim(-.1,2.6); ax.set_ylabel('$u$'); sub(ax,'b','$x$')
ax=axs[1,0]; style(ax)
for y in np.arange(.25,2.51,.25):
    ax.plot([y,0],[0,y],color=BLUE,lw=.85); ax.plot([-y,0],[0,y],color=BLUE,lw=.85)
ax.plot([0,0],[0,2.5],color=LINE,lw=1.7); ax.plot([0],[0],'o',ms=4.2,color=RED,zorder=6)
ax.set_xlim(-2.5,2.5); ax.set_ylim(0,1.5); ax.set_ylabel('$t$'); sub(ax,'c','$x$')
ax=axs[1,1]; style(ax); ax.plot(X,-np.abs(X),color=RED,lw=1.3)
for t,c in ((.5,SHADES[1]),(1.5,SHADES[3])): ax.plot(X,b(X,t),color=c,lw=1.4)
ax.set_xlim(-2.5,2.5); ax.set_ylim(-3.4,.1); ax.set_ylabel('$u$'); sub(ax,'d','$x$')
save(fig,HERE,'figure',{'formula':'u0=|x|: x^2/(2t) in fan; u0=-|x|: -|x|-t/2'})
