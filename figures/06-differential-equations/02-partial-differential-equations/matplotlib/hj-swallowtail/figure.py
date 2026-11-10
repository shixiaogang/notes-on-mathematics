from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: at t=pi/2 the characteristic image of the initial data is multi-valued; lower envelope = Hopf-Lax.
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
t=np.pi/2; y=np.linspace(-np.pi,np.pi,6001)
x=y-t*np.sin(y); z=np.cos(y)+t*np.sin(y)**2/2; p=-np.sin(y)
gx=np.linspace(-np.pi,np.pi,1201); gu,gy=hopf_lax(gx,t,np.cos,np.linspace(-9,9,36001))
mask=np.abs(gx)>1e-3
ax=axs[0]; style(ax); ax.plot(x,z,color=YELLOW,lw=1.5)
ax.plot(gx,gu,color=BLUE,lw=1.5)
ax.plot([0],[np.pi/4],'o',ms=4.4,color=RED,zorder=6); ax.plot([0],[1],'o',ms=4.4,mfc='white',mec=RED,zorder=6)
ax.set_xlim(-1.2,1.2); ax.set_ylim(.3,1.1); ax.set_ylabel('$u$'); sub(ax,'a','$x$')
ax=axs[1]; style(ax); ax.plot(x,p,color=YELLOW,lw=1.5)
L=gx<0
ax.plot(gx[L],(gx[L]-gy[L])/t,color=BLUE,lw=1.5); ax.plot(gx[~L],(gx[~L]-gy[~L])/t,color=BLUE,lw=1.5)
ax.plot([0,0],[-1,1],color=LINE,lw=1.5,ls='--')
ax.set_xlim(-1.2,1.2); ax.set_ylim(-1.2,1.2); ax.set_ylabel('$p$'); sub(ax,'b','$x$')
xc=np.arccos(2/np.pi)-t*np.sin(np.arccos(2/np.pi))
save(fig,HERE,'figure',{'formula':'t=pi/2; x=y-t sin y; u(0)=pi/4; third branch 1','fold_x':float(xc)})
print('fold at',xc)
