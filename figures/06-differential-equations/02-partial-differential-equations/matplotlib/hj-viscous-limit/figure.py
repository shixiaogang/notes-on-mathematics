from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: exact viscous solutions (Cole-Hopf) at t=pi/2 for eps=.2,.05,.01 and the Hopf-Lax limit; (b) x-derivative.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
t=np.pi/2; x=np.linspace(-1.6,1.6,1601); ys=np.linspace(-14,14,56001)
U,_=hopf_lax(x,t,np.cos,ys)
ax0,ax1=axs; style(ax0); style(ax1)
for e,c in ((.2,PURPLE),(.05,YELLOW),(.01,GREEN)):
    V=cole_hopf(x,t,e,np.cos,ys); ax0.plot(x,V,color=c,lw=1.4); ax1.plot(x,np.gradient(V,x),color=c,lw=1.4)
    print(e,'u_eps(0)',V[800],'u0',U[800],'diff',V[800]-U[800],'-2e ln2',-2*e*np.log(2))
ax0.plot(x,U,color=BLUE,lw=1.5); L=x<0; ax1.plot(x[L],np.gradient(U,x)[L],color=BLUE,lw=1.5); ax1.plot(x[~L][1:],np.gradient(U,x)[~L][1:],color=BLUE,lw=1.5)
ax0.plot([0],[np.pi/4],'o',ms=4.2,color=RED,zorder=6)
ax0.set_xlim(-1.6,1.6); ax0.set_ylabel('$u$'); sub(ax0,'a','$x$')
ax1.set_xlim(-1.6,1.6); ax1.set_ylabel('$\\partial_x u$'); sub(ax1,'b','$x$')
save(fig,HERE,'figure',{'formula':'Cole-Hopf, t=pi/2, eps=.2,.05,.01'})
