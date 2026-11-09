from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Limited-memory Riemannian BFGS on the sphere with parallel transport; n=500, spectrum 1..100.
n=500; a=np.linspace(1,100,n); rng=np.random.default_rng(2)
xs=rng.normal(size=n); xs/=np.linalg.norm(xs)
def rg(x):
    Ax=a*x; return Ax-(x@Ax)*x
def par(x,y,v): return v-((x+y)@v)/(1+x@y)*(x+y)
def run(m,tol=1e-6,T=4000):
    x=xs.copy(); g=rg(x); S=[];Y=[]; h=[np.linalg.norm(g)]
    for t in range(T):
        qq=g.copy(); xi=[]
        for s,y in zip(reversed(S),reversed(Y)):
            r=1/(s@y); e=r*(s@qq); qq-=e*y; xi.append((r,e,s,y))
        gam=(S[-1]@Y[-1])/(Y[-1]@Y[-1]) if S else 1/np.linalg.norm(g)
        z=gam*qq
        for r,e,s,y in reversed(xi):
            z+=(e-r*(y@z))*s
        d=-z; d-=(x@d)*x
        al=1.; f0=.5*x@(a*x); gd=g@d
        while True:
            xn=retr(x,al*d)
            if .5*xn@(a*xn)<=f0+1e-4*al*gd or al<1e-10: break
            al/=2
        gn=rg(xn); sn=par(x,xn,al*d); yn=gn-par(x,xn,g)
        S=[par(x,xn,s) for s in S]; Y=[par(x,xn,y) for y in Y]
        if sn@yn>1e-10*np.sqrt(yn@yn*(sn@sn)):
            S.append(sn); Y.append(yn)
            if len(S)>m: S.pop(0); Y.pop(0)
        x,g=xn,gn; h.append(np.linalg.norm(g))
        if h[-1]<tol: break
    return np.array(h)
fig,axs=figure(width_mm=112,height_mm=48,ncols=2)
ms=[1,3,10,30]
cs=[YELLOW,PURPLE,BLUE,GREEN]
res={}
for m,c in zip(ms,cs):
    h=run(m,T=2000); res[m]=h; axs[0].semilogy(h,color=c,lw=1.4,label=f'$m={m}$'); print(m,len(h),h[-1])
axs[0].set_xlabel('迭代次数'+'\n(a)'); axs[0].set_ylabel(r'$\Vert\mathbf{g}^{(t)}\Vert_2$'); axs[0].legend(handlelength=1.6)
M=[1,2,3,5,10,20,30,50]; It=[]; Co=[]
for m in M:
    k=len(run(m,T=3000))-1; It.append(k); Co.append(k*(3+10*m)); print(m,k,k*(3+10*m))
ax=axs[1]
ax.loglog(M,It,'-o',color=GREEN,lw=1.5,ms=3.2,label='迭代数')
ax.loglog(M,Co,'-o',color=YELLOW,lw=1.5,ms=3.2,label='向量运算量')
ax.set_xlabel('历史长度'+'\n(b)'); ax.legend(handlelength=1.6)
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'L-RBFGS, n=500, spectrum 1..100, seed 2, parallel transport, tol 1e-6; vector cost model (3+10m) per iteration'})
