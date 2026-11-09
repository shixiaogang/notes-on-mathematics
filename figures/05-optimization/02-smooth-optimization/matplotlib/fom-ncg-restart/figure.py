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
# 弯谷 f(x)=x1^2/2+(9/2)(x2-0.1 x1^2)^2：c=0 时退化为贯穿例，极小点 (0,0)，该点 Hessian 为 diag(1,9)。
c=0.1
def F(x): return .5*x[0]**2+4.5*(x[1]-c*x[0]**2)**2
def G(x):
    r=x[1]-c*x[0]**2
    return np.array([x[0]-18*c*x[0]*r, 9*r])
def Hs(x):
    r=x[1]-c*x[0]**2
    return np.array([[1-18*c*r+36*c*c*x[0]**2,-18*c*x[0]],[-18*c*x[0],9.]])
def wolfe(x,d,c1,c2,a1=1.0):
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
def ncg(rule,x0,c2=.4,restart=False,T=300,tol=1e-8):
    x=np.array(x0,float); g=G(x); d=-g; rec=[(np.linalg.norm(g),1.)]; P=[x.copy()]; D=[d.copy()]; N=1
    for t in range(T):
        a,k=wolfe(x,d,1e-4,c2); N+=k
        x=x+a*d; gn=G(x); y=gn-g
        b={'FR':(gn@gn)/(g@g),'PRP':(gn@y)/(g@g),'PRP+':max((gn@y)/(g@g),0)}[rule]
        if restart and abs(gn@g)>=.1*(gn@gn): b=0
        d=-gn+b*d
        if gn@d>=0: d=-gn
        g=gn; P.append(x.copy()); D.append(d.copy()); rec.append((np.linalg.norm(g),-(g@d)/np.linalg.norm(g)/np.linalg.norm(d)))
        if rec[-1][0]<tol: break
    return np.array(rec),np.array(P),D,N
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.095,.985,.97,.25,wspace=.3)
x0=[6,1]
R,_,_,N=ncg('FR',x0); Rr,_,_,Nr=ncg('FR',x0,restart=True); Rp,_,_,Np=ncg('PRP+',x0)
a.semilogy(R[:,0],color=YELLOW,lw=1.5); a.semilogy(Rr[:,0],color=PURPLE,lw=1.3); a.semilogy(Rp[:,0],color=GREEN,lw=1.6)
a.set_xlabel('$t$',labelpad=1); a.set_ylabel(r'$\Vert g^{(t)}\Vert_2$',labelpad=1); a.set_xlim(0,110); a.set_ylim(1e-8,100)
a.text(85,3e-3,'FR',fontsize=7.5,ha='center',color=INK); a.text(44,1e-1,'FR+重启',fontsize=7.5,color=INK) if 0 else None
a.text(68,3e-7,'FR 重启',fontsize=7.5,ha='left',color=INK) if 0 else None
a.annotate('FR 带重启',xy=(47,1e-7),xytext=(70,1e-6),fontsize=7.5,ha='center',arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=1))
a.text(9,3e-7,'PRP+',fontsize=7.5,color=INK,ha='left')
b.plot(R[1:45,1],color=YELLOW,lw=1.2); b.plot(Rp[1:25,1],color=GREEN,lw=1.3)
b.set_xlabel('$t$',labelpad=1); b.set_ylabel(r'$\cos\theta^{(t)}$',labelpad=1); b.set_ylim(0,1.02); b.set_xlim(0,44)
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
print(N,Nr,Np,len(R)-1,len(Rr)-1,len(Rp)-1, R[1:,1].min(), Rp[1:,1].min())
R9,_,_,N9=ncg('PRP+',[9,1]); R9r,_,_,N9r=ncg('PRP+',[9,1],restart=True); print(len(R9)-1,len(R9r)-1)
save(fig,HERE,'figure',{'PRP_plus_from_9_1':len(R9)-1,'PRP_plus_restart_from_9_1':len(R9r)-1,'x0':x0,'FR':[len(R)-1,N],'FR_restart':[len(Rr)-1,Nr],'PRP_plus':[len(Rp)-1,Np]})
