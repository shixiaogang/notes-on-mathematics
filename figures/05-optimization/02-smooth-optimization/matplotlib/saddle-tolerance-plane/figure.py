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
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2); panel(fig,.105,.985,.97,.25,wspace=.28)
eg=.1; eH=.6**.5
a.fill_between([-eH,2.1],0,eg,color=GREEN_FILL,lw=0); a.plot([-eH,-eH],[0,eg],color=STROKE,lw=1.2); a.plot([-eH,2.1],[eg,eg],color=STROKE,lw=1.2)
a.fill_between([-1.25,-eH],0,eg,color=RED_FILL,lw=0)
x=np.array([0.,1.]); P=[x]
for t in range(40):
    g=G(x); lm=3*x[0]**2-1
    if np.linalg.norm(g)>eg: x=x-.5*g
    elif min(lm,1)<-eH: x=x+2*abs(lm)/6*np.array([1.,0])
    else: break
    P.append(x)
ll=[min(3*p[0]**2-1,1.) for p in P]; gg=[np.linalg.norm(G(p)) for p in P]
a.plot(ll,gg,'-o',color=GREEN,lw=1.2,ms=3,mew=0,zorder=5); print(list(zip(np.round(ll,3),np.round(gg,3))))
a.set_yscale('log'); a.set_ylim(.02,1.3); a.set_xlim(-1.25,1.25); a.set_xlabel('$\\lambda_{\\min}(H)$',labelpad=1); a.set_ylabel('$\\Vert g\\Vert_2$',labelpad=1); a.axhline(eg,color=STROKE,lw=0)
a.text(.3,.042,'验收区',fontsize=7.5); a.text(-1.2,.03,'鞍点附近',fontsize=7.5)
X,Y=np.meshgrid(np.linspace(-1.35,1.35,1200),np.linspace(-.3,.3,600))
gn=np.sqrt((X**3-X)**2+Y**2); lm=np.minimum(3*X*X-1,1.)
ok1=gn<=eg; ok2=ok1&(lm>=-eH)
b.contourf(X,Y,ok1.astype(float),levels=[.5,2],colors=[RED_FILL]); b.contourf(X,Y,ok2.astype(float),levels=[.5,2],colors=[GREEN_FILL])
b.contour(X,Y,ok1.astype(float),levels=[.5],colors=[STROKE],linewidths=.85)
minima(b); saddle(b); b.set_xlabel('$x_1$',labelpad=1); b.set_ylabel('$x_2$',labelpad=0); b.set_ylim(-.3,.3); b.set_xticks([-1,0,1]); b.set_yticks([-.2,0,.2])
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'eps_g':eg,'eps_H':eH})
