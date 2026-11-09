from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
# 贯穿例：f_i(x)=a_i(x-b_i)^2/2，a=(1,2,3)，b=(-3,0,3)；f(x)=(x-1)^2+5，x*=1。
A = np.array([1., 2., 3.]); B = np.array([-3., 0., 3.])
def gi(x): return A*(x-B)
def panel(fig, left, right, top, bottom, wspace=.3, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.05):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='top')

al=.1;gam=1.;tau=al*gam;x0=.2
g=gi(x0); z=x0-al*g; S=lambda u:np.sign(u)*np.maximum(np.abs(u)-tau,0)
fig,ax=figure(width_mm=96,height_mm=56)
u=np.linspace(-.35,1.2,400)
ax.axhline(0,color=STROKE,lw=.7); ax.axvline(0,color=STROKE,lw=.7)
ax.plot(u,S(u),color=BLUE,lw=1.5)
ax.plot(z,S(z),'o',ms=4,mfc='white',mec=GREEN,mew=1.1,zorder=6)
for a_,b_,s in zip(z,S(z),['$i=1$','$i=2$','$i=3$']):
    ax.text(a_+(.0 if s!='$i=3$' else -.03),b_+.075,s,fontsize=7.5,ha='center' if s!='$i=3$' else 'right')
mz=z.mean(); ax.plot([mz],[S(mz)],'o',ms=5,color=GREEN,mew=0,zorder=6)
ax.plot([mz,mz],[S(mz),S(z).mean()],color=YELLOW,lw=1.5,zorder=4)
ax.plot([mz],[S(z).mean()],'s',ms=4.4,color=YELLOW,mew=0,zorder=6)
ax.text(mz+.03,S(z).mean()+.015,'三次更新的平均 0.327',fontsize=7.5,va='bottom',ha='left')
ax.text(mz+.03,S(mz)-.015,'精确更新 0.26',fontsize=7.5,va='top',ha='left')
ax.set_xlim(-.35,1.2); ax.set_ylim(-.3,1.08); ax.set_xlabel(r'$z=x-\alpha\hat{g}$',labelpad=1); ax.set_ylabel(r'$\mathrm{prox}_{\alpha h}(z)$',labelpad=1)
print(z,S(z),S(z).mean(),mz,S(mz))
save(fig,HERE,'figure',{'z':z.tolist(),'prox':S(z).tolist(),'mean':float(S(z).mean()),'exact':float(S(mz))})
