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
# 冻结记忆 p=g=0，一维确定性粒子：v+=omega v-phi x，x+=x+v+。稳定区：|omega|<1，0<phi<2+2omega
def tr(om,ph,N=45):
    x,v=1.,0.; o=[x]
    for t in range(N): v=om*v-ph*x; x=x+v; o.append(x)
    return o
fig,axes=figure(width_mm=112,height_mm=56,ncols=2); panel(fig,.085,.975,.96,.26,.3)
a=axes[0]; a.axhline(0,color=MUTED,lw=.7); a.plot(tr(1,1.5),color=YELLOW,lw=1.4); a.plot(tr(.7,1.5),color=GREEN,lw=1.6); a.set_xlim(0,45); a.set_ylim(-1.3,1.3); a.set_xticks([0,20,40]); a.set_yticks([-1,0,1]); a.set_xlabel('$t$',labelpad=1); a.set_ylabel('$x^{(t)}$',labelpad=1)
b=axes[1]; b.fill([-1,1,1,-1],[0,4,0,0],facecolor=BLUE_FILL,edgecolor=BLUE,lw=1); b.plot([1],[1.5],'o',ms=4.6,mfc=YELLOW,mec=YELLOW,clip_on=False,zorder=5); b.plot([.7],[1.5],'o',ms=4.6,color=GREEN,mew=0,zorder=5); b.set_xlim(-1.15,1.15); b.set_ylim(0,4.3); b.set_xticks([-1,0,1]); b.set_yticks([0,2,4]); b.set_xlabel(r'$\omega$',labelpad=1); b.set_ylabel(r'$\varphi$',labelpad=1)
tags(fig,axes); print(tr(.7,1.5)[-1],max(abs(np.array(tr(1,1.5)[20:])))); save(fig,HERE,'figure',{'traces':{'omega1':tr(1,1.5),'omega.7':tr(.7,1.5)}})
