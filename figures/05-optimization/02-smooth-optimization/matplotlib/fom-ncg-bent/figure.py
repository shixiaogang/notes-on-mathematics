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
fig,(a,b)=figure(width_mm=112,height_mm=58,ncols=2,gridspec_kw={'width_ratios':[1.15,1]})
panel(fig,.07,.985,.97,.25,wspace=.3)
X,Y=np.meshgrid(np.linspace(-3,7,700),np.linspace(-1.2,4.8,500))
a.contour(X,Y,.5*X**2+4.5*(Y-c*X**2)**2,levels=[.5,2,5,10,18,30],colors=[BLUE],linewidths=.65)
R,P,D,N=ncg('FR',[6,1]); R2,P2,D2,N2=ncg('PRP+',[6,1])
path(a,P[:18],YELLOW,ms=2.6); path(a,P2[:18],GREEN,ms=2.6); opt(a)
a.set_xlim(-3,7); a.set_ylim(-1.2,4.8); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0); a.set_xticks([-2,0,2,4,6]); a.set_yticks([0,2,4])
# 近精确线搜索下相邻方向在当前 Hessian 下的夹角余弦
_,Pc,Dc,_=ncg('PRP',[6,1],c2=1e-6,tol=1e-6)
m=[]
for t in range(min(10,len(Dc)-1)):
    A=Hs(Pc[t+1]); u,v=Dc[t],Dc[t+1]
    if A[0,0]<=0 or np.linalg.det(A)<=0:
        m.append(abs(u@A@v)/np.linalg.norm(u)/np.linalg.norm(v)/np.linalg.norm(A,2))
    else: m.append(abs(u@A@v)/np.sqrt((u@A@u)*(v@A@v)))
b.bar(range(1,len(m)+1),m,.62,color=GREEN); b.axvline(2.5,color=MUTED,lw=.7,ls=':'); b.set_xlabel('$t$',labelpad=1); b.set_ylabel('残余共轭度',labelpad=1); b.set_xlim(.3,10.7); b.set_xticks([2,4,6,8,10]); b.set_ylim(0,max(m)*1.2)
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
print(N,N2,len(P),len(P2),[round(x,3) for x in m])
save(fig,HERE,'figure',{'c':c,'x0':[6,1],'FR_iters':len(P)-1,'PRP_plus_iters':len(P2)-1,'FR_fg':N,'PRP_plus_fg':N2})
