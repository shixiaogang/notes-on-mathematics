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
rng=np.random.default_rng(11)
L=2.; a0=1/L; r=.05; F0=.05; delta=.1
def steps(n,gam,N=3000):
    z=rng.standard_normal((N,n)) if n<=500 else None
    if z is not None:
        u=z/np.linalg.norm(z,axis=1,keepdims=True); c1=u[:,0]; rest=1-c1**2
    else:
        # 大维数时直接抽第一分量与其余平方和
        z1=rng.standard_normal(N); chi=rng.chisquare(n-1,N); c1=z1/np.sqrt(z1*z1+chi); rest=1-c1**2
    R=r*rng.random(N)**(1/n); c=(R*c1)**2; s=(R**2)*rest
    t=0; out=np.full(N,-1); t_max=200000
    # 其余方向取特征值 1，因子 (1-alpha)
    T=np.arange(0,4000)
    lg=np.log(1+a0*gam)
    for i in range(N):
        tt=0
        # 解 f(t)<=-F
        val=lambda u:.5*s[i]*(1-a0)**(2*u)-.5*gam*c[i]*(1+a0*gam)**(2*u)
        lo=int(np.log((2*F0+1e-30)/(gam*c[i]))/(2*lg)); lo=max(lo,0)
        while val(lo)>-F0: lo+=1
        while lo>0 and val(lo-1)<=-F0: lo-=1
        out[i]=lo
    return out
bound=lambda n,g:(L/g)*np.log(4*n*(L*r*r+2*F0)/(np.pi*g*r*r*delta**2))
fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2); panel(fig,.08,.985,.97,.25,wspace=.27)
ns=np.array([2,5,10,30,100,300,1000,3000,10000,30000,100000])
m=[];q=[]
for n in ns:
    o=steps(int(n),1.); m.append(np.median(o)); q.append(np.quantile(o,.9))
a.semilogx(ns,m,'-o',color=GREEN,lw=1.3,ms=2.8,mew=0); a.semilogx(ns,q,color=GREEN,lw=1.1,ls=(0,(3,2)),marker='o',ms=2.8,mew=0); a.semilogx(ns,bound(ns,1.),color=PURPLE,lw=1.1,ls=(0,(3,2)))
a.text(5e2,bound(5e2,1.)*1.04+.3,'定理的上界',fontsize=7.5,ha='right'); a.text(2.2,3.5,'中位数',fontsize=7.5); a.set_xlabel('$n$',labelpad=1); a.set_ylabel('$T$',labelpad=1); a.set_ylim(0,max(bound(ns,1.))*1.1)
print('n',list(zip(ns,m,q)),[round(bound(n,1.),1) for n in ns])
gs=np.logspace(-2,0,9); mg=[np.median(steps(10,float(g))) for g in gs]
b.loglog(gs,mg,'-o',color=GREEN,lw=1.3,ms=2.8,mew=0); b.loglog(gs,bound(10,gs),color=PURPLE,lw=1.1,ls=(0,(3,2)))
b.text(.06,1.2e3,'定理的上界',fontsize=7.5); b.text(.012,160,'中位数',fontsize=7.5)
b.set_xlabel('$\\gamma$',labelpad=1); b.set_ylabel('$T$',labelpad=1); print(list(zip(np.round(gs,3),mg)))
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'L':L,'r':r,'F':F0,'delta':delta,'seed':11,'gamma_vs_n':1})
