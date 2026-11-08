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

# (a) f=x^2, V=(1,4), preimage (-2,-1)U(1,2). (b) f=x (x<1), x+1 (x>=1), V=(1.5,2.5), preimage [1,1.5).
fig,axes=figure(width_mm=112,height_mm=56,ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.06,right=.985,top=.96,bottom=.225,wspace=.16)
a,b=axes
x=np.linspace(-2.5,2.5,400); a.plot(x,x**2,color=BLUE,lw=1.4)
a.plot([-2.5,2.5],[0,0],color="none")
a.plot([-2.5,-2.5],[1,4],color=GREEN,lw=2.6,solid_capstyle="butt",clip_on=False,zorder=5); hollow(a,-2.5,1,GREEN); hollow(a,-2.5,4,GREEN)
for l,r in ((-2,-1),(1,2)):
    a.plot([l,r],[0,0],color=YELLOW,lw=2.6,solid_capstyle="butt",clip_on=False,zorder=5); hollow(a,l,0,YELLOW); hollow(a,r,0,YELLOW)
    for t in (l,r): a.plot([t,t],[0,t*t],color=MUTED,lw=.85,ls=(0,(2,1.5)))
a.plot([-2.5,2],[1,1],color=MUTED,lw=.85,ls=(0,(2,1.5))); a.plot([-2.5,2],[4,4],color=MUTED,lw=.85,ls=(0,(2,1.5)))
a.text(-2.32,2.5,"$V$",color=INK,va="center"); a.set_xlim(-2.5,2.5); a.set_ylim(0,6.2); a.set_xticks([-2,-1,0,1,2]); a.set_yticks([0,1,4]); a.text(1.72,5.3,"$f$",color=INK)
g1=np.linspace(-.5,1,200); g2=np.linspace(1,3,200)
b.plot(g1,g1,color=BLUE,lw=1.4); b.plot(g2,g2+1,color=BLUE,lw=1.4); hollow(b,1,1,BLUE); solid(b,1,2,BLUE)
b.plot([-.5,-.5],[1.5,2.5],color=GREEN,lw=2.6,solid_capstyle="butt",clip_on=False,zorder=5); hollow(b,-.5,1.5,GREEN); hollow(b,-.5,2.5,GREEN)
b.plot([1,1.5],[-.5,-.5],color=RED,lw=2.6,solid_capstyle="butt",clip_on=False,zorder=5); solid(b,1,-.5,RED); hollow(b,1.5,-.5,RED)
for y,xr in ((1.5,1),(2.5,1.5)): b.plot([-.5,xr],[y,y],color=MUTED,lw=.85,ls=(0,(2,1.5)))
b.plot([1,1],[-.5,2],color=MUTED,lw=.85,ls=(0,(2,1.5))); b.plot([1.5,1.5],[-.5,2.5],color=MUTED,lw=.85,ls=(0,(2,1.5)))
b.text(-.36,2,"$V$",color=INK,va="center"); b.set_xlim(-.5,3); b.set_ylim(-.5,4.2); b.set_xticks([0,1,1.5,2,3]); b.set_xticklabels(["0","1","1.5","2","3"]); b.set_yticks([1,1.5,2,2.5,4]); b.set_yticklabels(["1","1.5","2","2.5","4"])
label(fig,axes,("(a)","(b)"))
save(fig,Path(__file__).resolve().parent,"figure",{"formula":"x^2 on [-2.5,2.5]; piecewise x, x+1 with jump at 1"})
