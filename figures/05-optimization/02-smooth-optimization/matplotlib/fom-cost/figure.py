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
def tag(fig, ax, s, y=None, d=.085):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
# 贯穿例：f(x)=(x1^2+9 x2^2)/2，x0=(9,1)，mu=1，L=9，kappa=9。
H = np.array([1., 9.]); X0 = np.array([9., 1.])
def f_ex(x): return .5*(H*np.asarray(x)**2).sum(-1)
def contour_ex(ax, xr, yr, levels):
    X,Y = np.meshgrid(np.linspace(*xr,700), np.linspace(*yr,500))
    ax.contour(X,Y,.5*(X**2+9*Y**2),levels=levels,colors=[BLUE],linewidths=.65)
def path(ax, P, c, ms=3.2, lw=1.2, **k):
    P=np.asarray(P); ax.plot(P[:,0],P[:,1],'-o',color=c,lw=lw,ms=ms,mew=0,zorder=4,**k)
def opt(ax, x=0, y=0): ax.plot([x],[y],'o',ms=4.8,color=RED,mew=0,zorder=6)
# n=100：f=x^T diag(lam) x/2 + sum log cosh x_i，lam 在 [1,1000] 对数等距，mu=1，L=1001，x0 固定种子。
import math
n=100; lam=np.logspace(0,3,n); rng=np.random.default_rng(0); x0=rng.normal(size=n)*5
F=lambda x:.5*x@(lam*x)+np.sum(np.logaddexp(x,-x)-math.log(2)); G=lambda x:lam*x+np.tanh(x)
Lc=lam.max()+1; mu=1.; TOL=1e-6
def wolfe(x,d,c1,c2,a1):
    n=[0]
    def phi(a):
        n[0]+=1; return F(x+a*d),G(x+a*d)@d
    p0=F(x); d0=G(x)@d
    def zoom(lo,hi,plo):
        for _ in range(80):
            a=.5*(lo+hi); p,dp=phi(a)
            if p>p0+c1*a*d0 or p>=plo: hi=a
            else:
                if abs(dp)<=c2*abs(d0): return a
                if dp*(hi-lo)>=0: hi=lo
                lo=a; plo=p
        return lo
    ao,po,a=0,p0,a1
    for i in range(40):
        p,dp=phi(a)
        if p>p0+c1*a*d0 or (i>0 and p>=po): return zoom(ao,a,po),n[0]
        if abs(dp)<=c2*abs(d0): return a,n[0]
        if dp>=0: return zoom(a,ao,p),n[0]
        ao,po=a,p; a*=2
    return a,n[0]
def gd():
    x=x0.copy(); r=[np.linalg.norm(G(x))]
    while r[-1]>TOL: x=x-G(x)/Lc; r.append(np.linalg.norm(G(x)))
    return np.array(r),np.arange(1,len(r)+1)
def nag():
    q=np.sqrt(mu/Lc); b=(1-q)/(1+q); x=xm=x0.copy(); r=[np.linalg.norm(G(x))]
    while r[-1]>TOL:
        y=x+b*(x-xm); xm,x=x,y-G(y)/Lc; r.append(np.linalg.norm(G(x)))
    return np.array(r),np.arange(1,len(r)+1)
def hb():
    k=Lc/mu; b=((k**.5-1)/(k**.5+1))**2; a=4/(Lc**.5+mu**.5)**2; x=xm=x0.copy(); r=[np.linalg.norm(G(x))]
    while r[-1]>TOL: xm,x=x,x-a*G(x)+b*(x-xm); r.append(np.linalg.norm(G(x)))
    return np.array(r),np.arange(1,len(r)+1)
def prp():
    x=x0.copy(); g=G(x); d=-g; r=[np.linalg.norm(g)]; N=[1]; n=1; ag=1/np.linalg.norm(d)
    while r[-1]>TOL:
        a,k=wolfe(x,d,1e-4,.1,ag); n+=k; x=x+a*d; gn=G(x); s=g@d
        b=max(gn@(gn-g)/(g@g),0); d=-gn+b*d
        if gn@d>=0: d=-gn
        ag=a*s/(gn@d); g=gn; r.append(np.linalg.norm(g)); N.append(n)
    return np.array(r),np.array(N)
fig,(a,b)=figure(width_mm=112,height_mm=58,ncols=2,sharey=True)
panel(fig,.095,.985,.97,.25,wspace=.1)
Rg,Ng=gd(); Rn,Nn=nag(); Rh,Nh=hb(); Rp,Np=prp()
for r,N,c,l in ((Rg,Ng,YELLOW,1.5),(Rh,Nh,PURPLE,1.3),(Rn,Nn,GREEN,1.6),(Rp,Np,INK,1.3)):
    a.semilogy(r,color=c,lw=l); b.semilogy(N,r,color=c,lw=l)
a.set_xlim(0,1000); b.set_xlim(0,1000); a.set_xticks([0,250,500,750]); b.set_xticks([0,250,500,750]); a.set_ylim(1e-6,1e4); a.set_xlabel('迭代步数',labelpad=1); b.set_xlabel('梯度读取次数',labelpad=1); a.set_ylabel(r'$\Vert g\Vert_2$',labelpad=1)
a.text(600,1e2,'梯度下降',fontsize=7.5,color=INK,ha='left'); a.text(40,3e-5,'PRP+',fontsize=7.5,color=INK,ha='left'); a.text(575,3e-5,'Nesterov',fontsize=7.5,color=INK,ha='left'); a.annotate('重球',xy=(160,30),xytext=(330,800),fontsize=7.5,ha='center',arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1)); a.text(350,1e-1,'重球',fontsize=7.5,color=INK,ha='left') if 0 else None
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
print(len(Rg)-1,len(Rn)-1,len(Rh)-1,len(Rp)-1,Np[-1])
save(fig,HERE,'figure',{'n':n,'kappa':Lc/mu,'tol':TOL,'GD':len(Rg)-1,'NAG':len(Rn)-1,'HB':len(Rh)-1,'PRP_plus_iters':len(Rp)-1,'PRP_plus_grad':int(Np[-1])})
