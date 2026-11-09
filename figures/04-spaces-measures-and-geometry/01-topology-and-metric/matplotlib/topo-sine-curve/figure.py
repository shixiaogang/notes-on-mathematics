from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def hollow(ax,x,y,c=INK,z=6): ax.plot([x],[y],"o",ms=3.6,mfc="white",mec=c,mew=.8,zorder=z,clip_on=False)
def solid(ax,x,y,c=INK,z=6): ax.plot([x],[y],"o",ms=3.6,color=c,mew=0,zorder=z,clip_on=False)
def label(fig,axes,names=("(a)","(b)","(c)")):
    for ax,s in zip(axes,names):
        p=ax.get_position(); fig.text((p.x0+p.x1)/2,.025,s,ha="center",va="bottom")

# G={(x,sin(1/x)):0<x<=1}, J={0}x[-1,1]; marks x^+=2/(5pi), x^-=2/(7pi).
fig,axes=figure(width_mm=112,height_mm=50,ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.06,right=.985,top=.96,bottom=.235,wspace=.16)
a,b=axes
th=np.concatenate([np.linspace(1,40,4000),np.linspace(40,400,40000)]); xs=1/th
for ax,lim in ((a,1.03),(b,.16)):
    ax.plot(xs,np.sin(th),color=BLUE,lw=.9 if ax is a else 1.2); ax.plot([0,0],[-1,1],color=RED,lw=2.2,solid_capstyle="butt",zorder=5)
    ax.set_xlim(-.012*lim/.16 if ax is b else -.03,lim); ax.set_ylim(-1.2,1.2); ax.set_yticks([-1,0,1])
a.set_xticks([0,.5,1]); b.set_xticks([0,.05,.1,.15])
xp,xm=2/(5*np.pi),2/(7*np.pi)
solid(b,xp,1,GREEN); solid(b,xm,-1,YELLOW); b.text(xp+.004,1.04,"$x^+$",color=INK,va="bottom"); b.text(xm+.004,-1.04,"$x^-$",color=INK,va="top")
label(fig,axes,("(a)","(b)"))
save(fig,Path(__file__).resolve().parent,"figure",{"formula":"sin(1/x); x+=2/(5pi), x-=2/(7pi)"})
