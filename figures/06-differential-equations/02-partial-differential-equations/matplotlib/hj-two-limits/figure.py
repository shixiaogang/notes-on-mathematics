from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: separate eps->0 from mesh refinement. (a) fixed eps=.1, central differences/explicit Euler on periodic grid, sup-norm
# error at t=pi/2 against u_eps (exact) and against the limit u (Hopf-Lax). (b) |u_eps-u| at x=0 versus eps, reference 2 ln2 eps.
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
t_end=np.pi/2; ys=np.linspace(-20,20,160001); eps=.1
Ns=[20,40,80,160,320,640]; E1=[];E2=[];H=[]
for N in Ns:
    h=2*np.pi/N; x=-np.pi+h*np.arange(N); tau0=min(.4*h*h/eps,.4*h); n=int(np.ceil(t_end/tau0)); tau=t_end/n
    u=np.cos(x)
    for _ in range(n):
        ux=(np.roll(u,-1)-np.roll(u,1))/(2*h); uxx=(np.roll(u,-1)-2*u+np.roll(u,1))/h/h
        u=u+tau*(-.5*ux*ux+eps*uxx)
    ue=cole_hopf(x,t_end,eps,np.cos,ys); uh,_=hopf_lax(x,t_end,np.cos,ys)
    E1.append(np.abs(u-ue).max()); E2.append(np.abs(u-uh).max()); H.append(h)
print(list(zip(Ns,E1,E2)))
ax=axs[0]; style(ax); ax.loglog(H,E1,'-o',ms=3.4,color=GREEN,lw=1.4); ax.loglog(H,E2,'-o',ms=3.4,color=RED,lw=1.4)
H=np.array(H); ax.loglog(H,E1[-1]*(H/H[-1])**2,color=PURPLE,lw=1,ls='--'); ax.set_ylabel('最大误差'); sub(ax,'a','$h$')
ax=axs[1]; style(ax); es=np.array([.4,.2,.1,.05,.02,.01,.005]); D=[]
for e in es:
    D.append(float(np.pi/4-cole_hopf(np.array([0.]),t_end,e,np.cos,ys)[0]))
print(list(zip(es,D,2*np.log(2)*es)))
ax.loglog(es,D,'-o',ms=3.4,color=RED,lw=1.4); ax.loglog(es,2*np.log(2)*es,color=PURPLE,lw=1,ls='--'); ax.set_ylabel('$|u_\\varepsilon-u|$'); sub(ax,'b','$\\varepsilon$')
save(fig,HERE,'figure',{'formula':'central differences; eps=.1; t=pi/2','Ns':Ns,'E1':[float(v) for v in E1],'E2':[float(v) for v in E2]})
