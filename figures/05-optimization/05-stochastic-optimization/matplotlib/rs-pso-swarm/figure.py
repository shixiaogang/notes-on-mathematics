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
# 二维 Rastrigin 上的粒子群，24 粒子，同步更新，omega=0.7298，c1=c2=1.496，vmax=2，种子 4
rng=np.random.default_rng(4); N=24; x=rng.uniform(-5,5,(N,2)); v=rng.uniform(-1,1,(N,2)); F=lambda z:rastrigin(z[:,0],z[:,1]); p=x.copy(); fp=F(p); S={}
for g in range(61):
    S[g]=(x.copy(),p[np.argmin(fp)].copy())
    G=p[np.argmin(fp)]; v=.7298*v+1.496*rng.random((N,2))*(p-x)+1.496*rng.random((N,2))*(G-x); v=np.clip(v,-2,2); x=x+v; fx=F(x); m=fx<fp; p[m]=x[m]; fp[m]=fx[m]
fig,axes=figure(width_mm=112,height_mm=52,ncols=3); panel(fig,.07,.99,.97,.26,.16)
g_=np.linspace(-5,5,600); X,Y=np.meshgrid(g_,g_); Z=rastrigin(X,Y)
for a,k in zip(axes,(0,8,60)):
    a.contour(X,Y,Z,levels=[30],colors=[BLUE],linewidths=.45); xs,G=S[k]; a.plot(xs[:,0],xs[:,1],'o',ms=2.9,color=GREEN,mew=0,zorder=5); a.plot([0],[0],'o',ms=4,color=RED,mew=0,zorder=4)
    a.plot([G[0]],[G[1]],'o',ms=4.4,mfc='none',mec=INK,mew=.8,zorder=6)
    a.set_aspect('equal'); a.set_xlim(-5,5); a.set_ylim(-5,5); a.set_xticks([-4,0,4]); a.set_yticks([-4,0,4]); a.set_xlabel('$x_1$',labelpad=1)
axes[0].set_ylabel('$x_2$',labelpad=0); tags(fig,axes); print(fp.min(),p[np.argmin(fp)],np.abs(v).max(),x.std(0))
save(fig,HERE,'figure',{'seed':4,'N':24,'omega':.7298,'c':1.496,'vmax':2,'snapshots':[0,8,60],'best':float(fp.min())})
