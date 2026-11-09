from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    H=fig.get_figheight()*25.4
    if len(fig.axes)>1: bottom=15.5/H
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tag(fig, ax, s, y=None):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, 1.0/(fig.get_figheight()*25.4), s, ha='center', va='bottom')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
def dot(ax, x, y, c=GREEN, ms=4.2, z=6, m='o'): ax.plot([x],[y],m,ms=ms,color=c,mew=0,zorder=z)
def hollow(ax, x, y, c=BLUE, ms=4.4, z=7): ax.plot([x],[y],'o',ms=ms,mfc='white',mec=c,mew=1.0,zorder=z)

# 固定 nu=-3/4，L=(x1^2+4x2^2)/2+nu(x1+x2-1)，mu=1；x_tilde=(0.8,0.15)。
nu=-.75
def L(a,b): return .5*(a**2+4*b**2)+nu*(a+b-1)
xt=(.8,.15);g=(xt[0]+nu,4*xt[1]+nu);Lt=L(*xt);q=L(.75,.1875);cert=Lt-(g[0]**2+g[1]**2)/2
fig,(A,B)=figure(width_mm=112,height_mm=54,ncols=2,gridspec_kw={'width_ratios':[1.05,1]})
panel(fig,.085,.985,.97,.2,wspace=.12)
x=np.linspace(.55,1.0,300);y=np.linspace(.05,.33,300);X,Y=np.meshgrid(x,y)
A.contour(X,Y,L(X,Y),levels=q+np.array([.0015,.0041,.01,.02]),colors=BLUE,linewidths=.8)
dot(A,.75,.1875,PURPLE,ms=4.8,m='s');dot(A,*xt,GREEN,ms=4.8)
A.annotate('',xy=(xt[0]-.5*g[0],xt[1]-.5*g[1]),xytext=xt,arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=1.0,shrinkA=0,shrinkB=0))
A.text(.715,.2,r'$x(\nu)$',ha='right',fontsize=8);A.text(.815,.135,r'$\tilde{x}$',fontsize=8,va='top')
A.set_xlim(.55,1.0);A.set_ylim(.05,.33);A.set_xticks([.6,.7,.8,.9,1.0]);A.set_yticks([.1,.2,.3]);A.set_xlabel('$x_1$',labelpad=1);A.set_ylabel('$x_2$',labelpad=1)
B.set_xlim(0,1);B.set_ylim(.387,.409);B.axis('off')
B.plot([.3,.3],[.387,.409],color=STROKE,lw=.95)
items=[(cert,PURPLE,'认证下界 '+f'{cert:.4f}',-.0002),(q,PURPLE,'$q(\\nu)$ '+f'{q:.4f}',-.0006),(.4,RED,'$f^\\star$ 0.4000',0),(Lt,RED,'未修正的内层值 '+f'{Lt:.4f}',.0004),(13/32,GREEN,'$f(\\hat{x})$ '+f'{13/32:.5f}',.0003)]
for v,c,s,dy in items:
    B.plot([.3],[v],'o',ms=4.6,color=c,mew=0,zorder=5); B.text(.37,v+dy,s,va='center',fontsize=7.5)
for a_,s in zip((A,B),('(a)','(b)')):tag(fig,a_,s)
save(fig,HERE,'figure',{'cert':cert,'q':q,'L_tilde':Lt,'f_hat':13/32})
