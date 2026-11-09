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
# 三对角二次（光滑凸、无强凸余量）：f=(1/4)(x^T A x/2 - x1)，n=400，L=1，x0=0。
fig,(a,b)=figure(width_mm=112,height_mm=58,ncols=2)
panel(fig,.095,.985,.97,.25,wspace=.3)
n=400; def_A=lambda x:2*x-np.r_[0,x[:-1]]-np.r_[x[1:],0]
G=lambda x:.25*(def_A(x)-np.eye(1,n,0)[0])
F=lambda x:.25*(.5*x@def_A(x)-x[0])
xs=1-np.arange(1,n+1)/(n+1); fs=F(xs); R2=xs@xs
T=800; x=np.zeros(n); gd=[F(x)-fs]
for t in range(T): x=x-G(x); gd.append(F(x)-fs)
x=np.zeros(n); y=x.copy(); th=1.; nag=[F(x)-fs]
for t in range(T):
    xn=y-G(y); thn=(1+np.sqrt(1+4*th*th))/2
    y=xn+(th-1)/thn*(xn-x); x=xn; th=thn; nag.append(F(x)-fs)
gd=np.array(gd); nag=np.array(nag); t=np.arange(1,T+1)
a.loglog(t,gd[1:],color=YELLOW,lw=1.5); a.loglog(t,nag[1:],color=GREEN,lw=1.6)
a.loglog(t,R2/(2*t),color=YELLOW,lw=.9,ls=(0,(3,2))); a.loglog(t,2*R2/(t+1)**2,color=GREEN,lw=.9,ls=(0,(3,2)))
a.set_xlabel('$T$',labelpad=1); a.set_ylabel(r'$f-f^*$',labelpad=1); a.set_ylim(1e-3,1e3); a.set_xlim(1,800)
# (b) 贯穿例按凸情形的 theta 参数运行，L=9，势函数 E_t 单调而目标差振荡。
L=9.; x=X0.copy(); y=x.copy(); v=x.copy(); th=1.; thp=0.
gap=[f_ex(x)]; E=[.5*L*(x@x)]
for t in range(40):
    xn=y-H*y/L; thn=(1+np.sqrt(1+4*th*th))/2; vn=x+th*(xn-x)
    y=xn+(th-1)/thn*(xn-x); x=xn; v=vn
    gap.append(f_ex(x)); E.append(th*th*f_ex(x)+.5*L*(v@v)); thp=th; th=thn
gap=np.array(gap); E=np.array(E); tt=np.arange(41)
b.semilogy(tt,E,color=PURPLE,lw=1.2); b.semilogy(tt,gap,color=GREEN,lw=1.6)
b.set_xlabel('$t$',labelpad=1); b.set_xlim(0,40); b.set_ylim(1e-3,1e3)
b.text(14,70,'$E^{(t)}$',fontsize=7.5,color=INK); b.text(26,.12,'$f-f^*$',fontsize=7.5,color=INK)
tag(fig,a,'(a)',y=.05); tag(fig,b,'(b)',y=.05)
print('R2',R2,'up',int(np.sum(np.diff(gap)>0)),'E up',int(np.sum(np.diff(E)>1e-9)),E[:4],gap[:6])
save(fig,HERE,'figure',{'n':n,'L':1,'R2':float(R2),'E0':float(E[0])})
