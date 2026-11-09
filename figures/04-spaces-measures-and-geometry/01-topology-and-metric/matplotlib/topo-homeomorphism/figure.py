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

# (a) h(x)=x/(1-|x|). (b) radial map among circle r=.75, ellipse (1.4,1.0), square half-side 1.6, ray at 35 deg.
fig,axes=figure(width_mm=112,height_mm=58,ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.06,right=.985,top=.97,bottom=.2,wspace=.14)
a,b=axes
x=np.linspace(-.857,.857,500); a.plot(x,x/(1-np.abs(x)),color=BLUE,lw=1.4)
for s in (-1,1): a.axvline(s,color=MUTED,lw=.85,ls=(0,(2,1.5)))
pts=[-.75,-.5,.5,.75]
for t in pts:
    y=t/(1-abs(t)); solid(a,t,y,BLUE); a.plot([t,t],[0,y],color=MUTED,lw=.85,ls=(0,(2,1.5))); a.plot([-1.1,t],[y,y],color=MUTED,lw=.85,ls=(0,(2,1.5)))
a.axhline(0,color=MUTED,lw=.85); a.set_xlim(-1.1,1.1); a.set_ylim(-6,6); a.set_xticks([-1,-.75,-.5,0,.5,.75,1]); a.set_xticklabels(["-1","","-1/2","0","1/2","3/4","1"]); a.set_yticks([-3,-1,1,3])
t=np.linspace(0,2*np.pi,400); b.plot(.75*np.cos(t),.75*np.sin(t),color=BLUE,lw=1.4); b.plot(1.4*np.cos(t),np.sin(t),color=GREEN,lw=1.4)
b.plot([-1.6,1.6,1.6,-1.6,-1.6],[-1.6,-1.6,1.6,1.6,-1.6],color=YELLOW,lw=1.4)
th=np.deg2rad(35); u=np.array([np.cos(th),np.sin(th)]); e=1/np.sqrt((u[0]/1.4)**2+u[1]**2); s=1.6/max(abs(u))
b.plot([0,s*u[0]],[0,s*u[1]],color=MUTED,lw=.85); solid(b,0,0,INK)
for r,col in ((.75,BLUE),(e,GREEN),(s,YELLOW)): solid(b,r*u[0],r*u[1],col)
b.set_aspect("equal"); b.set_xlim(-1.75,1.75); b.set_ylim(-1.75,1.75); b.axis("off")
label(fig,axes,("(a)","(b)"))
save(fig,Path(__file__).resolve().parent,"figure",{"formula":"h=x/(1-|x|); radial projection along ray at 35 degrees"})
