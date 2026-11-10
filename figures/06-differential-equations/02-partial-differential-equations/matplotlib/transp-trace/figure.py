# Target: backward and forward tracing on (0,1) with v=1/2.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,axs=figure(112,52,ncols=3,sharey=True)
def base(a):
    a.fill_between([0,1],0,2,color=BLUE_FILL,lw=0)
    a.plot([0,1],[0,0],color=RED,lw=2.6,clip_on=False); a.plot([0,0],[0,2],color=RED,lw=2.6,clip_on=False)
    a.plot([1,1],[0,2],color=CHAR,lw=1.1,ls=(0,(3,2)),clip_on=False)
    a.set_xlim(0,1); a.set_ylim(0,2); a.set_xticks([0,.5,1])
a,b,c=axs
for A in axs: base(A)
def arrow(A,p,q,col,lw=1.3):
    A.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='-|>',color=col,lw=lw,shrinkA=0,shrinkB=0,mutation_scale=7))
arrow(a,(.8,1),(.3,0),CHAR); arrow(a,(.2,1),(0,.6),CHAR)
a.plot([.8,.2],[1,1],'o',color=BLUE,ms=4); a.plot([.3],[0],'o',color=RED,ms=4.5,clip_on=False); a.plot([0],[.6],'o',color=RED,ms=4.5,clip_on=False)
a.text(.83,1.06,'$P$'); a.text(.23,1.06,'$Q$'); a.text(.42,.06,'$(0.3,0)$',fontsize=7.5); a.text(.03,.48,'$(0,0.6)$',fontsize=7.5)
b.plot([.3,1],[0,1.4],color=BLUE,lw=1.5); b.plot([0,.7],[.6,2],color=BLUE,lw=1.5)
b.plot([.3],[0],'o',color=RED,ms=4.5,clip_on=False); b.plot([0],[.6],'o',color=RED,ms=4.5,clip_on=False)
b.text(.42,.1,'$R$'); b.text(.05,.42,'$S$')
c.plot([.3,.8],[0,1],color=YELLOW,lw=3)
c.plot([.8],[1],'o',color=BLUE,ms=4); c.plot([.3],[0],'o',color=RED,ms=4.5,clip_on=False); c.text(.83,1.06,'$P$')
c.text(.63,.42,'$f$',color=INK)
tail(a,'$x$','(a)','$t$'); tail(b,'$x$','(b)'); tail(c,'$x$','(c)')
save(fig,Path(__file__).resolve().parent,'figure',{'v':0.5,'P':[.8,1],'Q':[.2,1],'R':[.3,0],'S':[0,.6]})
