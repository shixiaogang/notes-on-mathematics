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
x=np.array([0.,1.]); P=[x]; typ=[]; eg=.1; eH=.6**.5
for t in range(40):
    g=G(x); lm=3*x[0]**2-1
    if np.linalg.norm(g)>eg: x=x-.5*g; typ.append('G')
    elif min(lm,1)<-eH: x=x+2*abs(lm)/6*np.array([1.,0]); typ.append('N')
    else: break
    P.append(x)
P=np.array(P); 
a.plot(P[:5,0],P[:5,1],'-o',color=GREEN,lw=1.3,ms=3,mew=0,zorder=4)
a.plot(P[5:,0],P[5:,1],'-o',color=GREEN,lw=1.3,ms=3,mew=0,zorder=4)
a.annotate('',xy=P[5],xytext=P[4],arrowprops=dict(arrowstyle='-|>',color=RED,lw=1.3,mutation_scale=7,shrinkA=1,shrinkB=1),zorder=5)
Q=[np.array([0.,1.])]
for t in range(10): Q.append(Q[-1]-.5*G(Q[-1]))
Q=np.array(Q); a.plot(Q[:,0]-.0,Q[:,1],color=YELLOW,lw=2.8,zorder=3)
a.text(.17,.125,'负曲率步',fontsize=7.5)
a.set_xlim(-.25,1.2); a.set_ylim(-.12,1.08); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0); a.set_xticks([0,.5,1]); a.set_yticks([0,.5,1])
FP=[F(p) for p in P]; FQ=[F(p) for p in Q]
b.plot(FQ,'-',color=YELLOW,lw=1.7); b.plot(range(len(FP)),FP,'-o',color=GREEN,lw=1.3,ms=3,mew=0)
b.axhline(.25,color=MUTED,lw=.85,ls=(0,(3,2))); b.axvline(4,color=RED,lw=.85,ls=(0,(1,2)))
b.text(5.9,.28,'$f=1/4$',fontsize=7.5); b.text(4.2,.68,'第 4 轮',fontsize=7.5)
b.set_xlabel('$t$',labelpad=1); b.set_ylabel('$f(x^{(t)})$',labelpad=1); b.set_xlim(0,10); b.set_ylim(-.03,.8)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'x0':[0,1],'alpha':.5,'eps_g':.1,'eps_H':'sqrt(0.6)','M':6})
