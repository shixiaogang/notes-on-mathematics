from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: doubling of variables: Phi(x,y)=u(x)-v(y)-(x-y)^2/eps^2 for a kinked u and v. Max moves to the diagonal.
fig, axs = figure(width_mm=112, height_mm=50, ncols=3, width_ratios=[1.15,1,1])
xs=np.linspace(0,1,701)
u=lambda x:.75-1.3*np.abs(x-.42)
v=lambda x:.2+.9*np.abs(x-.62)
ax=axs[0]; style(ax); ax.plot(xs,u(xs),color=BLUE,lw=1.4); ax.plot(xs,v(xs),color=YELLOW,lw=1.6)
i=np.argmax(u(xs)-v(xs)); ax.plot([xs[i]]*2,[v(xs[i]),u(xs[i])],color=RED,lw=1.4)
ax.set_xlim(0,1); ax.set_ylim(-.1,.95); ax.set_xticks([0,.5,1]); sub(ax,'a','$x$')
for ax,e,l in zip(axs[1:],(.6,.12),'bc'):
    style(ax); X,Y=np.meshgrid(xs,xs); P=u(X)-v(Y)-(X-Y)**2/e**2
    vm=P.max()
    ax.imshow(np.maximum(P,0),origin='lower',extent=[0,1,0,1],cmap=FIELD,vmin=0,vmax=vm,aspect='equal',interpolation='bilinear')
    ax.plot([0,1],[0,1],color=LINE,lw=.85,ls='--')
    j=np.unravel_index(P.argmax(),P.shape); ax.plot([xs[j[1]]],[xs[j[0]]],'o',ms=4.2,color=GREEN,mec='white',mew=.5)
    print(e,xs[j[1]],xs[j[0]],P.max())
    ax.set_xticks([0,.5,1]); ax.set_yticks([0,.5,1]); sub(ax,l,'$x$'); ax.set_ylabel('$y$',labelpad=1)
save(fig,HERE,'figure',{'formula':'Phi=u(x)-v(y)-(x-y)^2/eps^2, eps=.6,.12'})
