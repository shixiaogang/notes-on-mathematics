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
fig,(a,b)=figure(width_mm=112,height_mm=54,ncols=2); panel(fig,.09,.985,.97,.26,wspace=.27)
contour(a,(-.25,1.2),(-.12,1.08),levels=[.02,.08,.16,.25,.4,.6,.8]); minima(a,((1,0),)); saddle(a)
for s,c,lw in ((.2,GREEN,1.2),(.02,GREEN,1.2),(.002,GREEN,1.2),(0.,YELLOW,1.7)):
    x=np.array([s,1.]); P=[x]
    for t in range(40): x=x-.5*G(x); P.append(x)
    P=np.array(P); a.plot(P[:,0],P[:,1],'-',color=c,lw=lw,zorder=4); a.plot(P[:,0],P[:,1],'o',color=c,ms=2,mew=0,zorder=4)
a.text(.26,.98,'$0.2$',fontsize=7.5); a.text(.075,.72,'$0.02$',fontsize=7.5)
a.set_xlim(-.25,1.2); a.set_ylim(-.12,1.08); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0); a.set_xticks([0,.5,1]); a.set_yticks([0,.5,1])
x=np.array([1e-3,1.]); P=[x]
for t in range(34): x=x-.5*G(x); P.append(x)
P=np.array(P); T=np.arange(len(P))
b.semilogy(T,np.abs(P[:,0]),color=RED,lw=1.4); b.semilogy(T,np.abs(P[:,1]),color=BLUE,lw=1.4)
b.semilogy(T[:18],1e-3*1.5**T[:18],color=MUTED,lw=.85,ls=(0,(3,2)))
b.text(21,.008*2.1,'$\\vert x_1^{(t)}\\vert$',fontsize=7.5); b.text(14,2.2e-6,'$\\vert x_2^{(t)}\\vert$',fontsize=7.5); b.text(4,3e-2,'$10^{-3}\\cdot 1.5^t$',fontsize=7.5)
b.set_ylim(1e-9,4); b.set_xlim(0,34); b.set_xlabel('$t$',labelpad=1); tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'alpha':.5,'x0':'(s,1)'})
