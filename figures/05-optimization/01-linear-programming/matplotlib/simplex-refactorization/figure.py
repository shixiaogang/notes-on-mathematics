from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Random column exchanges on a basis of order 120 (seed 7); residual of x_B from updated inverse, with and without refactorization.
m=120;rng=np.random.default_rng(7);T=300
def fresh(): return rng.normal(size=(m,m))+6*np.eye(m)
A0=fresh();cols=[rng.normal(size=m) for _ in range(T)];pos=rng.integers(0,m,size=T)
b=rng.normal(size=m)
def run(period,small):
    B=A0.copy();Inv=np.linalg.inv(B);res=[]
    for t in range(T):
        a=cols[t];u=Inv@a
        mag=np.abs(u)
        if small:
            ok=np.where(mag>1e-4)[0];r=int(ok[np.argmin(mag[ok])])   # smallest admissible pivot
        else:
            r=int(np.argmax(mag))
        E=Inv-np.outer(u,Inv[r])/u[r];E[r]=Inv[r]/u[r];Inv=E
        B[:,r]=a
        if period and (t+1)%period==0: Inv=np.linalg.inv(B)
        x=Inv@b;res.append(np.linalg.norm(B@x-b)/np.linalg.norm(b))
    return np.array(res)
a=run(0,True);c=run(40,True);g=run(0,False)
fig,ax=figure(width_mm=100,height_mm=52)
X=range(1,T+1)
ax.semilogy(X,a,color=YELLOW,lw=1.6)
ax.semilogy(X,c,color=PURPLE,lw=1.2)
ax.semilogy(X,g,color=GREEN,lw=1.4)
ax.set_xlabel('换基次数 t',labelpad=1);ax.set_ylabel('相对残差',labelpad=1);ax.set_xlim(0,T)
save(fig,Path(__file__).resolve().parent,'figure',{'m':m,'T':T,'seed':7,'small_pivot_final':float(a[-1]),'small_refactor_max':float(c.max()),'large_pivot_final':float(g[-1])})
print(a[[20,50,100,200,299]],c.max(),g[[50,299]])
