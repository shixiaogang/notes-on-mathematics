from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/02-partial-differential-equations/matplotlib/pdeprob-common'))
from pdeprob_common import *
# Target: min(x,1-x) has u''=0 a.e. but fails the weak equation; a bump probe reads the kink.
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
X=np.linspace(0,1,4001)
r=(X-.5)/.4; phi=np.zeros_like(X); m=np.abs(r)<1; phi[m]=np.exp(1-1/(1-r[m]**2))
dphi=np.gradient(phi,X); up=np.where(X<.5,1.0,-1.0)
ax=axs[0]; style(ax); ax.plot(X,np.minimum(X,1-X),color=BLUE,lw=1.4); ax.plot(X,.4*phi,color=PURPLE,lw=1.4)
ax.plot([.5],[.5],'o',ms=3.8,color=RED)
ax.text(.2,.33,'$u$',color=BLUE,ha='right'); ax.text(.5,.3,r'$0.4\varphi$',color=PURPLE,ha='center',fontsize=7.5)
ax.set_ylim(0,.58); ax.set_xlim(0,1); ax.set_xticks([0,.5,1]); sub(ax,'a','$x$')
ax=axs[1]; style(ax); y=up*dphi; ax.fill_between(X,0,y,color=BLUE_FILL,lw=0); ax.plot(X,y,color=BLUE,lw=1.4)
ax.set_xlim(0,1); ax.set_xticks([0,.5,1]); ax.set_ylabel(r"$u'\varphi'$"); sub(ax,'b','$x$')
I=float(np.trapezoid(y,X))
save(fig, Path(__file__).resolve().parent, 'figure', {'formula':'phi=exp(1-1/(1-r^2)), r=(x-.5)/.4','integral_uprime_phiprime':I}); print(I)
