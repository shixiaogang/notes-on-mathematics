from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.05):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='top')
# 贯穿例 f(x)=(x1^2-1)^2/4+x2^2/2，L=2 与 M=6 在 |x1|<=1 上成立，alpha=1/2。
def F(x): return .25*(x[0]**2-1)**2+.5*x[1]**2
def G(x): return np.array([x[0]**3-x[0],x[1]])
LEV=[.02,.08,.16,.25,.4,.65,1,1.5]
def contour(ax,xr,yr,levels=LEV):
    X,Y=np.meshgrid(np.linspace(*xr,700),np.linspace(*yr,500))
    ax.contour(X,Y,.25*(X**2-1)**2+.5*Y**2,levels=levels,colors=[BLUE],linewidths=.65)
def minima(ax,pts=((1,0),(-1,0))):
    for x,y in pts: ax.plot([x],[y],'o',ms=4.8,color=RED,mew=0,zorder=6)
def saddle(ax,x=0,y=0): ax.plot([x],[y],'o',mfc='white',mec=RED,ms=5,mew=1,zorder=7)
rng=np.random.default_rng(7)
def lanczos_vals(lam,b,K):
    n=len(lam); Q=np.zeros((n,K)); al=np.zeros(K); be=np.zeros(K); q=b/np.linalg.norm(b); out=[]
    for k in range(K):
        Q[:,k]=q; w=lam*q; al[k]=q@w
        w=w-Q[:,:k+1]@(Q[:,:k+1].T@w); w=w-Q[:,:k+1]@(Q[:,:k+1].T@w)
        T=np.diag(al[:k+1])
        if k>0: T=T+np.diag(be[:k],1)+np.diag(be[:k],-1)
        out.append(np.linalg.eigvalsh(T)[0])
        be[k]=np.linalg.norm(w)
        if be[k]<1e-13: out+= [out[-1]]*(K-k-1); break
        q=w/be[k]
    return np.array(out)
def power_vals(lam,b,K,c):
    v=b/np.linalg.norm(b); out=[]
    for k in range(K):
        out.append(v@(lam*v)); v=(c-lam)*v; v/=np.linalg.norm(v)
    return np.array(out)
n=400; K=120; c=2.0
fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2); panel(fig,.11,.985,.97,.24,wspace=.26)
for ax,lm2,s in ((a,.3,'(a)'),(b,-.17,'(b)')):
    lam=np.r_[-.2,lm2,rng.uniform(.5,2,n-2)]; z=rng.standard_normal(n)
    P=power_vals(lam,z,K,c); Q=lanczos_vals(lam,z,K)
    ax.semilogy(np.arange(1,K+1),P-lam[0]+1e-16,color=YELLOW,lw=1.5); ax.semilogy(np.arange(1,K+1),Q-lam[0]+1e-16,color=GREEN,lw=1.5)
    ax.set_ylim(1e-8,5); ax.set_xlim(1,K); ax.set_xlabel('Hessian 向量积次数',labelpad=1); tag(fig,ax,s)
a.set_ylabel('$R-\\lambda_{\\min}$',labelpad=1)
a.text(66,.09,'幂迭代',fontsize=7.5); a.text(44,1e-6,'Lanczos',fontsize=7.5)
b.text(70,.012,'幂迭代',fontsize=7.5); b.text(70,3e-6,'Lanczos',fontsize=7.5)
save(fig,HERE,'figure',{'n':n,'spectrum':'-0.2, second, uniform[.5,2]','seed':7,'c':c})
