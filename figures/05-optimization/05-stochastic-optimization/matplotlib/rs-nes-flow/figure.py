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
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# J(m,s)=m^2+s^2，高斯搜索分布 N(m,s^2)。欧氏梯度流 (m',s')=-(2m,2s) 与自然梯度流 (m',s')=-(2m s^2, s^3)
fig,ax=figure(width_mm=88,height_mm=64)
g=np.linspace(-.3,2.6,300); h=np.linspace(0,1.9,300); X,Y=np.meshgrid(g,h); ax.contour(X,Y,X**2+Y**2,levels=[.25,1,2.25,4,5.5],colors=[BLUE],linewidths=.7)
def flow(v,x0,dt=.002,N=9000):
    x=np.array(x0,float); p=[x.copy()]
    for i in range(N): x=x+dt*v(x); p.append(x.copy())
    return np.array(p)
E=flow(lambda x:-np.array([2*x[0],2*x[1]]),(2,1.5)); Nf=flow(lambda x:-np.array([2*x[0]*x[1]**2,x[1]**3]),(2,1.5),N=40000)
ax.plot(E[:,0],E[:,1],color=YELLOW,lw=1.6); ax.plot(Nf[:,0],Nf[:,1],color=GREEN,lw=1.6); ax.plot([2],[1.5],'o',ms=4,mfc='white',mec=INK,mew=.9,zorder=6); ax.plot([0],[0],'o',ms=5,color=RED,mew=0,zorder=6,clip_on=False)
ax.text(.95,1.06,'自然梯度',fontsize=7.5,ha='right',va='bottom'); ax.text(1.3,.72,'欧氏梯度',fontsize=7.5,ha='left',va='top')
ax.set_xlim(-.3,2.6); ax.set_ylim(0,1.9); ax.set_aspect('equal'); ax.set_xticks([0,1,2]); ax.set_yticks([0,1]); ax.set_xlabel('$m$',labelpad=1); ax.set_ylabel(r'$\sigma$',labelpad=1)
print(Nf[-1],Nf[::10000]); save(fig,HERE,'figure',{'J':'m^2+s^2','start':[2,1.5]})
