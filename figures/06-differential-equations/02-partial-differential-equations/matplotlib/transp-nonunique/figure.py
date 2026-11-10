# Target: non-Lipschitz velocity: branching v=2 sqrt|x| and merging v=-2 sgn(x) sqrt|x|.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,56,ncols=2,sharey=True)
t=np.linspace(0,2,500)
for x0 in (.25,.6,1.1,1.8): a.plot((np.sqrt(x0)+t)**2,t,color=CHAR,lw=.8)
for c in (0.0,.4,.8,1.2,1.6):
    tt=t[t>=c]; a.plot((tt-c)**2,tt,color=CHAR,lw=.8)
for x0 in (-.04,-.25,-.64,-1,-1.6):
    r=np.sqrt(-x0); tt=t[t<=r]; a.plot(-(r-tt)**2,tt,color=CHAR,lw=.8)
a.plot([0,0],[0,2],color=CHAR,lw=.8)
tt=np.linspace(1,2,100); a.plot((tt-1)**2,tt,color=BLUE,lw=1.7)
tt=np.linspace(0,1,100); a.plot(-(1-tt)**2,tt,color=YELLOW,lw=1.7,ls=(0,(3,2))); a.plot([0,0],[0,1],color=YELLOW,lw=1.7,ls=(0,(3,2)))
a.plot([-1,0],[0,0],color=RED,lw=3,clip_on=False); a.plot([1],[2],'o',color=BLUE,ms=4.5,clip_on=False); a.plot([0],[1],'o',color=INK,ms=3.5)
a.text(.9,1.72,'$P$',ha='right')
a.set_xlim(-2,3); a.set_ylim(0,2); tail(a,'$x$','(a)','$t$')
for x0 in (-3,-2,-1.3,-.7,-.3,.3,.7,1.3,2,3):
    r=np.sqrt(abs(x0)); tt=t[t<=r]; b.plot(np.sign(x0)*(r-tt)**2,tt,color=CHAR,lw=.8)
b.plot([-1,1],[0,0],color=RED,lw=3,clip_on=False); b.plot([0,0],[0,2],color=CHAR,lw=1.5)
for x0,c in ((1,YELLOW),(-1,YELLOW)):
    tt=np.linspace(0,1,100); b.plot(np.sign(x0)*(1-tt)**2,tt,color=c,lw=1.7,ls=(0,(3,2)))
b.plot([0],[1],'o',color=BLUE,ms=4.5); b.text(.12,1.05,'$(0,1)$',fontsize=7.5)
b.set_xlim(-3,3); tail(b,'$x$','(b)')
save(fig,Path(__file__).resolve().parent,'figure',{'a':'(sqrt x0+t)^2, branching at 0','b':'merging'})
