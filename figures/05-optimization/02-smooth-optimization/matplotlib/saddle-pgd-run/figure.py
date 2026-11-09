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
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2); panel(fig,.09,.985,.97,.25,wspace=.27)
contour(a,(-.25,1.2),(-.12,1.08),levels=[.02,.08,.16,.25,.4,.6,.8]); minima(a,((1,0),)); saddle(a)
eg=.1; xi=np.array([.03,-.02]); Tw=19; Fth=.05; x=np.array([0.,1.]); P=[x]; v=[F(x)]; jumps=[]; c=[1]; grads=1; marks=[]
while True:
    g=G(x)
    if np.linalg.norm(g)>eg:
        x=x-.5*g; P.append(x); grads+=1; v.append(F(x)); c.append(grads); continue
    base=x.copy(); fb=F(base); jumps.append(len(P)-1); x=base+xi; P.append(x); v.append(F(x)); c.append(grads)
    for s in range(Tw): x=x-.5*G(x); P.append(x); grads+=1; v.append(F(x)); c.append(grads)
    marks.append((c[jumps[-1]],fb,c[-1]))
    if F(x)<=fb-Fth: grads+=1; continue
    break
P=np.array(P); print(grads, jumps)
j=jumps[0]
a.plot(P[:j+1,0],P[:j+1,1],'-o',color=GREEN,lw=1.3,ms=2.8,mew=0,zorder=4)
a.plot(P[j:j+2,0],P[j:j+2,1],'-',color=RED,lw=1.2,zorder=5)
a.plot(P[j+1:j+21,0],P[j+1:j+21,1],'-o',color=GREEN,lw=1.3,ms=2.8,mew=0,zorder=4)
a.text(.09,.09,'扰动',fontsize=7.5)
a.set_xlim(-.25,1.2); a.set_ylim(-.12,1.08); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0); a.set_xticks([0,.5,1]); a.set_yticks([0,.5,1])
b.plot(c,v,color=GREEN,lw=1.4)
for s,fb,e in marks:
    b.plot([s,e],[fb-Fth,fb-Fth],color=PURPLE,lw=1.1,ls=(0,(3,2))); b.axvline(s,color=RED,lw=.85,ls=(0,(1,2)))
b.text(7,.09,'门槛',fontsize=7.5,color=INK); b.text(27,.14,'第二次窗口',fontsize=7.5); b.text(6.5,.72,'第一次窗口',fontsize=7.5)
b.set_xlabel('累计梯度次数',labelpad=1); b.set_ylabel('$f$',labelpad=1); b.set_ylim(-.07,.8); b.set_xlim(0,grads)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'xi':[.03,-.02],'T_w':Tw,'F':Fth,'eps_g':eg})
