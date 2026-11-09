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
def trs(g,lam,D):
    # 精确求解 min g.p+p.diag(lam).p/2, |p|<=D（二维对角情形）
    q=int(np.argmin(lam)); lmin=lam[q]; o=1-q
    if lmin>0 and np.linalg.norm(g/lam)<=D: return -g/lam
    if abs(g[q])<1e-14:
        mu=max(-lmin,0.); pp=np.zeros(2)
        if lam[o]+mu>0: pp[o]=-g[o]/(lam[o]+mu)
        if np.linalg.norm(pp)<=D:
            pp[q]=np.sqrt(D*D-pp[o]**2); return pp
    lo=max(0.,-lmin)+1e-14; hi=lo+1
    while np.linalg.norm(g/(lam+hi))>D: hi*=2
    for _ in range(200):
        m=.5*(lo+hi)
        if np.linalg.norm(g/(lam+m))>D: lo=m
        else: hi=m
    return -g/(lam+hi)
def tcg(g,lam,D):
    # 截断共轭梯度，二维对角 B
    z=np.zeros(2); r=g.copy(); d=-r
    if np.linalg.norm(r)<1e-12: return z
    for j in range(5):
        Bd=lam*d; c=d@Bd
        if c<=0:
            a,b,cc=d@d,2*z@d,z@z-D*D; tau=(-b+np.sqrt(b*b-4*a*cc))/(2*a); return z+tau*d
        al=r@r/c; zn=z+al*d
        if np.linalg.norm(zn)>=D:
            a,b,cc=d@d,2*z@d,z@z-D*D; tau=(-b+np.sqrt(b*b-4*a*cc))/(2*a); return z+tau*d
        rn=r+al*Bd
        if np.linalg.norm(rn)<1e-10: return zn
        be=rn@rn/(r@r); d=-rn+be*d; z,r=zn,rn
    return z
def tr_run(x0,D0,solve,T=40,tol=1e-9):
    x=np.array(x0,float); D=D0; P=[x.copy()]; rec=[]
    for t in range(T):
        g=G(x); lam=np.array([3*x[0]**2-1,1.])
        if np.linalg.norm(g)<tol and lam.min()>=-1e-9: break
        if np.linalg.norm(g)<tol and solve is tcg: break
        p=solve(g,lam,D); pred=-(g@p+.5*(lam*p*p).sum())
        if pred<=1e-15: break
        ared=F(x)-F(x+p); rho=ared/pred; acc=rho>=.25
        rec.append((t,x.copy(),D,p.copy(),pred,ared,rho,acc))
        if acc: x=x+p
        if rho<.25: D=D/2
        elif rho>=.75 and abs(np.linalg.norm(p)-D)<1e-9: D=min(2*D,2.)
        P.append(x.copy())
    return np.array(P),rec
def mod_run(x0,T=40,tol=1e-9):
    x=np.array(x0,float); P=[x.copy()]
    for t in range(T):
        g=G(x); lam=np.array([3*x[0]**2-1,1.])
        if np.linalg.norm(g)<tol: break
        d=-g/np.maximum(np.abs(lam),1e-3); al=1.
        while F(x+al*d)>F(x)+1e-4*al*(g@d): al*=.5
        x=x+al*d; P.append(x.copy())
    return np.array(P)
x0=np.array([.01,.0625]); g=G(x0); lam=np.array([3*x0[0]**2-1,1.]); D=.5
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2); panel(fig,.08,.985,.97,.25,wspace=.27)
X,Y=np.meshgrid(np.linspace(-.72,.72,500),np.linspace(-.72,.72,500))
Z=g[0]*X+g[1]*Y+.5*(lam[0]*X*X+lam[1]*Y*Y)
th=np.linspace(0,2*np.pi,300); a.fill(D*np.cos(th),D*np.sin(th),color=BLUE_FILL,lw=0); a.plot(D*np.cos(th),D*np.sin(th),color=BLUE,lw=.95)
a.contour(X,Y,Z,levels=[-.2,-.12,-.05,-.01,.01,.05,.12,.2],colors=[BLUE],linewidths=.65)
p=trs(g,lam,D); d=-g/np.maximum(np.abs(lam),1e-3)
A=dict(arrowstyle='-|>',lw=1.3,mutation_scale=7,shrinkA=0,shrinkB=0)
a.annotate('',xy=p,xytext=(0,0),arrowprops=dict(color=GREEN,**A),zorder=6); a.annotate('',xy=d,xytext=(0,0),arrowprops=dict(color=YELLOW,**A),zorder=6)
a.plot([p[0]],[p[1]],'o',ms=4.5,color=RED,mew=0,zorder=7); a.plot([0],[0],'o',ms=3,color=INK,mew=0,zorder=7)
a.text(.06,.11,'信赖域步',fontsize=7.5); a.text(-.34,-.2,'修正步',fontsize=7.5)
a.set_aspect('equal'); a.set_xlim(-.72,.72); a.set_ylim(-.72,.72); a.set_xlabel('$p_1$',labelpad=1); a.set_ylabel('$p_2$',labelpad=0); a.set_xticks([-.5,0,.5]); a.set_yticks([-.5,0,.5])
P,rec=tr_run(x0,D,trs); Q=mod_run(x0); print(len(P),len(Q)); print(P[:6]); print(Q[:10]); print([ (r[2],round(r[6],3),r[7]) for r in rec][:8])
b.semilogy(range(len(P)),[F(x)+1e-17 for x in P],'-o',color=GREEN,lw=1.3,ms=2.8,mew=0); b.semilogy(range(len(Q)),[F(x)+1e-17 for x in Q],'-o',color=YELLOW,lw=1.6,ms=2.8,mew=0)
b.text(4,.6e-5,'信赖域',fontsize=7.5); b.text(9.3,.08,'修正 Newton',fontsize=7.5)
b.set_ylim(1e-16,1); b.set_xlabel('$t$',labelpad=1); b.set_ylabel('$f(x^{(t)})$',labelpad=1); b.set_xlim(0,16)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'x0':[.01,.0625],'Delta':.5,'modified':'|lambda| spectral with Armijo'})
