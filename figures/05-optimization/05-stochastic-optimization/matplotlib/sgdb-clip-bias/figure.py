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
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
# 裁剪的几何与偏差。
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2,gridspec_kw={'width_ratios':[1,1.15]})
panel(fig,.05,.965,.97,.25,wspace=.28)
from matplotlib.patches import Rectangle,Circle
a.add_patch(Rectangle((-1,-1),2,2,fc=YELLOW_FILL,ec=YELLOW,lw=1.1)); a.add_patch(Circle((0,0),1,fc=GREEN_FILL,ec=GREEN,lw=1.1))
ar=dict(arrowstyle='-|>',shrinkA=0,shrinkB=0,mutation_scale=7)
a.annotate('',xy=(3,4),xytext=(0,0),arrowprops=dict(color=BLUE,lw=1.2,**ar))
a.annotate('',xy=(1,1),xytext=(0,0),arrowprops=dict(color=YELLOW,lw=1.5,**ar))
a.annotate('',xy=(.6,.8),xytext=(0,0),arrowprops=dict(color=GREEN,lw=1.5,**ar))
a.text(3.1,3.75,'$(3,4)$',fontsize=7.5); a.text(1.1,1.08,'$(1,1)$',fontsize=7.5); a.text(-1.32,1.15,'$(0.6,0.8)$',fontsize=7.5)
a.set_aspect('equal'); a.set_xlim(-1.5,4.7); a.set_ylim(-1.5,4.6); a.axis('off')
a.plot([-1.4,4.6],[0,0],color=STROKE,lw=.6); a.plot([0,0],[-1.4,4.5],color=STROKE,lw=.6)
c=np.linspace(0,4,801)
def cl(v,c): return np.minimum(c,np.abs(v))*np.sign(v)
mean=.5*(cl(3.,c)+cl(-1.,c))
b.plot(c,mean,color=GREEN,lw=1.4); b.axhline(1,color=BLUE,lw=1,ls='--')
b.fill_between(c,mean,1,color=RED_FILL,lw=0)
b.set_xlabel('$c$',labelpad=1); b.set_ylabel('裁后均值',labelpad=1); b.set_xlim(0,4); b.set_ylim(-.1,1.15)
b.text(2.1,1.03,'未裁剪均值',fontsize=7.5)
b.text(1.0,.5,'条件偏差',fontsize=7.5)
print(mean[[100,200,400,600,800]])
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'reading':[3,4],'c':1,'two_point':[3,-1]})
