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

# x_n=(-1)^n/n; bands eps=.3 (from n=4) and eps=.12 (from n=9).
fig,ax=figure(width_mm=100,height_mm=50)
n=np.arange(1,19); x=(-1.0)**n/n
ax.axhspan(-.3,.3,color=GREEN_FILL,lw=0,zorder=0); ax.axhspan(-.12,.12,color=YELLOW_FILL,lw=0,zorder=1)
ax.axhline(0,color=MUTED,lw=.85,zorder=2)
ax.vlines(n,0,x,color=BLUE,lw=.85,zorder=3); ax.plot(n,x,"o",ms=3.6,color=BLUE,mew=0,zorder=4)
for N,e in ((4,.3),(9,.12)): ax.plot([N,N],[-1.05,e],color=MUTED,lw=.85,ls=(0,(2,1.5)),zorder=3)
ax.text(4.15,-.92,"$n=4$",color=INK); ax.text(9.15,-.92,"$n=9$",color=INK)
ax.set_xlim(0,18.8); ax.set_ylim(-1.05,.75); ax.set_xticks([1,5,10,15]); ax.set_yticks([-1,-.3,-.12,.12,.3,.5]); ax.set_yticklabels(["-1","-0.3","","","0.3","0.5"])
ax.text(18.6,.31,"$\\varepsilon=0.3$",ha="right",va="bottom",color=INK); ax.text(18.6,.125,"$\\varepsilon=0.12$",ha="right",va="bottom",color=INK)
ax.set_xlabel("$n$"); ax.set_ylabel("$x_n$")
save(fig,Path(__file__).resolve().parent,"figure",{"formula":"x_n=(-1)^n/n, n=1..18; bands 0.3 and 0.12"})
