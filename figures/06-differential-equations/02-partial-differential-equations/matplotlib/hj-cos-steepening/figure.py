from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: classical solution for t<1 from characteristics: u and p=u_x for t=0,.5,.9; slope at 0 is -cos0/(1-t).
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
y=np.linspace(-np.pi,np.pi,4001)
for t,col in zip((0,.5,.9),(SHADES[0],SHADES[2],SHADES[3])):
    x=y-t*np.sin(y); u=np.cos(y)+t*np.sin(y)**2/2; p=-np.sin(y)
    axs[0].plot(x,u,color=col,lw=1.4); axs[1].plot(x,p,color=col,lw=1.4)
for ax,l,yl in zip(axs,'ab',('$u(x,t)$',r'$\partial_x u(x,t)$')):
    style(ax); ax.set_xlim(-np.pi,np.pi); ax.set_xticks([-3,-2,-1,0,1,2,3]); ax.set_ylabel(yl); sub(ax,l,'$x$')
save(fig,HERE,'figure',{'formula':'x=y-t sin y,u=cos y+t sin^2 y/2,p=-sin y; t=0,.5,.9'})
