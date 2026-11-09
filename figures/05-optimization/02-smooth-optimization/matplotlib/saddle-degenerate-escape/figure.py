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
fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2); panel(fig,.11,.985,.97,.25,wspace=.28)
def run(y0,kind,N):
    y=y0; o=[y]
    for t in range(N):
        y=y+.5*(y if kind=='s' else y**3); o.append(y)
        if abs(y)>=.5: break
    return np.array(o)
y0=.01; S=run(y0,'s',100); D=run(y0,'d',20000)
a.loglog(np.arange(len(S))+1,S,color=GREEN,lw=1.5); a.loglog(np.arange(len(D))+1,D,color=YELLOW,lw=1.8)
a.axhline(.5,color=MUTED,lw=.85,ls=(0,(3,2))); a.text(1.3,.56,'离开阈值',fontsize=7.5); a.text(14,.018,'退化',fontsize=7.5); a.text(3,.06,'严格',fontsize=7.5)
a.set_ylim(.008,1); a.set_xlim(1,2e4); a.set_xlabel('$t+1$',labelpad=1); a.set_ylabel('$\\vert y^{(t)}\\vert$',labelpad=1)
ys=np.logspace(-3,-.5,14); s=[len(run(v,'s',500))-1 for v in ys]; d=[len(run(v,'d',3000000))-1 for v in ys]
b.loglog(ys,s,'-o',color=GREEN,lw=1.3,ms=2.8,mew=0); b.loglog(ys,d,'-o',color=YELLOW,lw=1.7,ms=2.8,mew=0)
b.text(.02,.7*18,'严格',fontsize=7.5); b.text(.012,1.2e4,'退化',fontsize=7.5)
b.set_xlabel('$\\vert y^{(0)}\\vert$',labelpad=1); b.set_ylabel('离开所需轮数',labelpad=1)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'strict':'-y^2/2','degenerate':'-y^4/4','alpha':.5})
print(s[:3],d[:3])
