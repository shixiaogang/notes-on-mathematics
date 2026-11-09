from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# min exp(x1 x2 x3 x4 x5)-(x1^3+x2^3+1)^2/2, h=(|x|^2-10, x2x3-5x4x5, x1^3+x2^3+1); x0=(-1.8,1.7,1.9,-.8,-.8), least-squares nu0.
x0=np.array([-1.8,1.7,1.9,-.8,-.8]); nu0=-np.linalg.lstsq(J5(x0).T,g5(x0),rcond=None)[0]
x,nu=x0.copy(),nu0.copy(); X=[x.copy()]
for t in range(10):
    p,nu=kkt_step(g5(x),HL5(x,nu),J5(x),h5(x)); x=x+p; X.append(x.copy())
xs=x.copy(); nus=nu.copy(); E=[np.linalg.norm(y-xs) for y in X]
rho=1.5*np.abs(nus).max()+1; phi=lambda y:f5(y)+rho*np.abs(h5(y)).sum()
x,nu=x0.copy(),nu0.copy(); B=np.eye(5); EB=[np.linalg.norm(x-xs)]; A=[]
for t in range(22):
    p,nun=kkt_step(g5(x),B,J5(x),h5(x)); D=g5(x)@p-rho*np.abs(h5(x)).sum(); al=1.
    while phi(x+al*p)>phi(x)+.1*al*D and al>1e-10: al*=.5
    xn=x+al*p; s=xn-x; y=g5(xn)+J5(xn).T@nun-(g5(x)+J5(x).T@nun)
    B,th=damped_bfgs(B,s,y); x=xn; nu=nun; EB.append(np.linalg.norm(x-xs)); A.append(al)
fig,ax=figure(width_mm=100,height_mm=54); panels(fig,.13,.99,.98,.155,0)
N=[i for i,e in enumerate(E) if e>1e-14]; M=[i for i,e in enumerate(EB) if e>1e-14]
ax.semilogy(N,[E[i] for i in N],color=GREEN,lw=1.4,marker='o',ms=3.2,mew=0,label='精确 Hessian')
ax.semilogy(M,[EB[i] for i in M],color=YELLOW,lw=1.6,marker='s',ms=3,mew=0,label='阻尼 BFGS')
ax.legend(loc='upper right',handlelength=1.6,borderaxespad=.2)
setup(ax,(-.5,22.5),(1e-15,3),xt=range(0,23,4),yt=[1e-14,1e-10,1e-6,1e-2],xl='$t$',yl='到解的距离',equal=False); ax.minorticks_off()
save(fig,HERE,'figure',{'exact':E,'bfgs':EB,'alpha':A,'rho':float(rho),'x_star':xs.tolist(),'nu_star':nus.tolist()})
