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
fig,(a,b)=figure(width_mm=112,height_mm=54,ncols=2); panel(fig,.115,.985,.97,.26,wspace=.27)
s=np.linspace(0,2,400)
a.plot(s,.25*(s*s-1)**2-.25,color=BLUE,lw=1.4); a.plot(s,-.5*s*s,color=GREEN,lw=1.3); a.plot(s,-.5*s*s+s**3,color=PURPLE,lw=1.2,ls=(0,(3,2)))
a.axhline(0,color=MUTED,lw=.8,ls=(0,(1,2))); a.axvline(1,color=STROKE,lw=.85)
a.plot([1/3],[16/81-.25],'o',color=GREEN,ms=4,mew=0,zorder=6); a.plot([1],[-.25],'o',color=RED,ms=4.5,mew=0,zorder=6); a.plot([2**.5],[0],'o',mfc='white',mec=RED,ms=4.5,mew=1,zorder=6)
a.text(.38,-.11,'$\\alpha=1/3$',fontsize=7.5); a.text(1.47,.1,'$\\sqrt{2}$',fontsize=7.5); a.text(1.03,.28,'盒外',fontsize=7.5,color=INK)
a.text(1.05,-.6,'二次模型',fontsize=7.5); a.text(1.74,.28,'目标',fontsize=7.5); a.text(.08,.33,'三次上界',fontsize=7.5)
a.set_xlim(0,2); a.set_ylim(-.75,.55); a.set_xlabel('$\\alpha$',labelpad=1); a.set_ylabel('$f(\\alpha,0)-f(0,0)$',labelpad=1)
x0=.2; t=np.linspace(-1,1,400); h=lambda u:.25*((x0+u)**2-1)**2-.25*(x0**2-1)**2
b.plot(t[t>=0],h(t[t>=0]),color=GREEN,lw=1.5); b.plot(t[t<=0],h(t[t<=0]),color=YELLOW,lw=1.6)
b.axhline(0,color=MUTED,lw=.8,ls=(0,(1,2))); b.axvline(0,color=MUTED,lw=.8,ls=(0,(1,2)))
b.plot([0],[0],'o',color=INK,ms=3.5,mew=0,zorder=6); b.plot([-.2],[h(-.2)],'o',mfc='white',mec=RED,ms=4.5,mew=1,zorder=6)
b.text(.16,-.2,'$+e_1$',fontsize=7.5); b.text(-.72,.03,'$-e_1$',fontsize=7.5); b.text(-.2,.058,'鞍点',fontsize=7.5,ha='center')
b.set_xlabel('$\\alpha$',labelpad=1); b.set_ylabel('目标变化量',labelpad=1); b.set_ylim(-.27,.1)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'M':6,'gamma':1,'x0':'(0.2,0) in (b)'})
