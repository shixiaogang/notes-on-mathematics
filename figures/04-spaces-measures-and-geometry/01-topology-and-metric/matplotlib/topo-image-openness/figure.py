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

# (a) x^2 maps (-1,1) to [0,1). (b) projection of (1,3)x(1,2) is (1,3). (c) x1 x2=1 projects to R\{0}.
fig,axes=figure(width_mm=112,height_mm=48,ncols=3)
fig.set_layout_engine(None); fig.subplots_adjust(left=.05,right=.985,top=.96,bottom=.25,wspace=.24)
a,b,c=axes
x=np.linspace(-1.3,1.3,300); a.plot(x,x**2,color=BLUE,lw=1.4)
a.plot([-1,1],[-.25,-.25],color=GREEN,lw=2.6,solid_capstyle="butt",clip_on=False,zorder=5); hollow(a,-1,-.25,GREEN); hollow(a,1,-.25,GREEN)
a.plot([-1.3,-1.3],[0,1],color=RED,lw=2.6,solid_capstyle="butt",clip_on=False,zorder=5); solid(a,-1.3,0,RED); hollow(a,-1.3,1,RED)
a.set_xlim(-1.3,1.3); a.set_ylim(-.25,1.7); a.set_xticks([-1,0,1]); a.set_yticks([0,1])
b.fill([1,3,3,1],[1,1,2,2],facecolor=BLUE_FILL,edgecolor=BLUE,lw=1.1,ls=(0,(2,1.5)))
b.plot([1,3],[0,0],color=GREEN,lw=2.6,solid_capstyle="butt",clip_on=False,zorder=5); hollow(b,1,0,GREEN); hollow(b,3,0,GREEN)
for t in (1,3): b.plot([t,t],[0,1],color=MUTED,lw=.85,ls=(0,(2,1.5)))
b.set_xlim(0,4); b.set_ylim(0,3); b.set_xticks([1,3]); b.set_yticks([1,2])
for s in (np.linspace(.32,3.2,200),np.linspace(-3.2,-.32,200)): c.plot(s,1/s,color=BLUE,lw=1.4)
c.axhline(0,color=GREEN,lw=2.6,zorder=4); hollow(c,0,0,RED); c.axvline(0,color=MUTED,lw=.85)
c.set_xlim(-3.2,3.2); c.set_ylim(-3.2,3.2); c.set_xticks([-2,0,2]); c.set_yticks([-2,0,2])
label(fig,axes)
save(fig,Path(__file__).resolve().parent,"figure",{"formula":"x^2; rectangle projection; hyperbola x1 x2=1"})
