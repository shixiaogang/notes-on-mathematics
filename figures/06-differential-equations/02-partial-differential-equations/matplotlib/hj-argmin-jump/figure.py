from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: objective F(y)=cos y+(x-y)^2/(2t), t=pi/2, for x=0,.3, and the minimiser y*(x), which jumps at x=0.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
t=np.pi/2; Y=np.linspace(-np.pi,np.pi,1201)
ax=axs[0]; style(ax)
F=lambda x,y:np.cos(y)+(x-y)**2/(2*t)
for x0,c in ((0,BLUE),(.3,YELLOW)):
    ax.plot(Y,F(x0,Y),color=c,lw=1.5); i=np.argmin(F(x0,Y)); 
    if x0==0: ax.plot([-np.pi/2,np.pi/2],[np.pi/4]*2,'o',ms=4.4,color=RED,zorder=6)
    else: ax.plot([Y[i]],[F(x0,Y)[i]],'o',ms=4.4,color=RED,zorder=6); print('x=.3 min',Y[i],F(x0,Y)[i])
ax.set_xlim(-np.pi,np.pi); ax.set_ylim(.4,3.2); ax.set_xticks([-3,-2,-1,0,1,2,3]); ax.set_ylabel('$F(y)$'); sub(ax,'a','$y$')
ax=axs[1]; style(ax); x=np.linspace(-1.6,1.6,1601); _,ystar=hopf_lax(x,t,np.cos,np.linspace(-9,9,72001))
ax.plot(x[x<0],ystar[x<0],color=BLUE,lw=1.5); ax.plot(x[x>0],ystar[x>0],color=BLUE,lw=1.5); ax.plot([0,0],[-np.pi/2,np.pi/2],color=LINE,lw=1.2,ls='--')
ax.plot([0,0],[-np.pi/2,np.pi/2],'o',ms=4.2,color=RED,zorder=6)
ax.set_xlim(-1.6,1.6); ax.set_ylabel('$y^{*}(x)$'); sub(ax,'b','$x$')
save(fig,HERE,'figure',{'formula':'F=cos y+(x-y)^2/(2t), t=pi/2'})
