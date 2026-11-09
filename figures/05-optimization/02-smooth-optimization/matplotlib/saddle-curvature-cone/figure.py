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
fig,(a,b)=figure(width_mm=112,height_mm=52,ncols=2); panel(fig,.02,.985,.97,.24,wspace=.2)
th=np.linspace(0,2*np.pi,721); R=-np.cos(2*th)
a.plot(np.cos(th),np.sin(th),color=BLUE,lw=1.1)
for s in (0,np.pi):
    t=np.linspace(s-np.pi/4,s+np.pi/4,200); a.plot(np.cos(t),np.sin(t),color=RED,lw=2.2,solid_capstyle='butt')
    t=np.linspace(s-np.pi/6,s+np.pi/6,100); a.fill_between(np.append(0,np.cos(t)) if 0 else np.cos(t),0,0)
    t=np.linspace(s-np.pi/6,s+np.pi/6,100); a.fill(np.r_[0,np.cos(t)],np.r_[0,np.sin(t)],color=RED_FILL,lw=0)
for th0 in (np.pi/4,3*np.pi/4,-np.pi/4,-3*np.pi/4): a.plot([0,np.cos(th0)],[0,np.sin(th0)],color=MUTED,lw=.85,ls=(0,(3,2)))
A=dict(arrowstyle='-|>',lw=1.2,mutation_scale=7,shrinkA=0,shrinkB=0)
a.annotate('',xy=(1,0),xytext=(0,0),arrowprops=dict(color=RED,**A)); a.text(1.05,.08,'$q_1$',fontsize=8)
a.plot([0],[0],'o',mfc='white',mec=RED,ms=4,mew=1,zorder=6); a.text(.62,.72,'$R=0$',fontsize=7.5,ha='left')
a.set_aspect('equal'); a.set_xlim(-1.3,1.45); a.set_ylim(-1.15,1.15); a.axis('off')
d=np.degrees(th-np.pi); ok=np.abs(d)<=90
b.plot(np.degrees(th)[:361]-90,-np.cos(2*np.radians(np.degrees(th)[:361]-90)),color=BLUE,lw=1.4)
b.axhline(0,color=MUTED,lw=.85,ls=(0,(3,2))); b.axhline(-.5,color=PURPLE,lw=.95,ls=(0,(3,2)))
b.fill_between([-45,45],[-1.2,-1.2],[1.2,1.2],color=RED_FILL,lw=0); b.set_ylim(-1.2,1.2); b.set_xlim(-90,90); b.set_xticks([-90,-45,0,45,90])
b.text(84,-.68,'$-\\gamma$',fontsize=7.5,color=INK,ha='right'); b.set_xlabel('夹角（度）',labelpad=1); b.set_ylabel('$R(v)$',labelpad=1)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'H':'diag(-1,1)','R':'-cos 2 theta'})
