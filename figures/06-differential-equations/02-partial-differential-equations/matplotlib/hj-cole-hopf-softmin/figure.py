from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: the Cole-Hopf integrand exp(-(F-Fmin)/(2 eps)) concentrates at the minimisers of F as eps falls (x=0,t=pi/2).
fig, axs = figure(width_mm=112, height_mm=46, ncols=2)
t=np.pi/2; Y=np.linspace(-np.pi,np.pi,1601); F=np.cos(Y)+Y**2/(2*t)
ax=axs[0]; style(ax); ax.plot(Y,F,color=BLUE,lw=1.4); ax.plot([-np.pi/2,np.pi/2],[np.pi/4]*2,'o',ms=4.4,color=RED,zorder=6); ax.set_xlim(-np.pi,np.pi); ax.set_ylim(.5,3.3); ax.set_xticks([-3,-2,-1,0,1,2,3]); ax.set_ylabel('$F(y)$'); sub(ax,'a','$y$')
ax=axs[1]; style(ax)
for e,c in ((.3,PURPLE),(.1,YELLOW),(.02,GREEN)): ax.plot(Y,np.exp(-(F-F.min())/(2*e)),color=c,lw=1.4)
ax.set_xlim(-np.pi,np.pi); ax.set_ylim(0,1.08); ax.set_xticks([-3,-2,-1,0,1,2,3]); ax.set_ylabel('$\\mathrm{e}^{-(F-\\min F)/(2\\varepsilon)}$'); sub(ax,'b','$y$')
save(fig,HERE,'figure',{'formula':'exp(-(F-min)/(2e)), e=.3,.1,.02'})
