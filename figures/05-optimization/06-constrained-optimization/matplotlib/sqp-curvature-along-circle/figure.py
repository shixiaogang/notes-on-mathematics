from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
# (a) at x*=(1,1): along the circle f=-2cos(s/sqrt2); QP models along tangent with L-curvature and f-curvature.
# (b) at x=(1.4,.2) on the circle with nu=.5: same comparison, arc length s from the point.
fig,axes=figure(width_mm=112,height_mm=56,ncols=2); panels(fig,.1,.99,.98,.215,.3); a,b=axes
s=np.linspace(-1.6,1.6,300)
a.plot(s,-2*np.cos(s/np.sqrt(2)),color=BLUE,lw=1.4); a.plot(s,-2+.5*s**2,color=GREEN,lw=1.4); a.plot(s,-2+0*s,color=YELLOW,lw=1.6,ls=(0,(4,2)))
dot(a,(0,-2)); a.text(1.62,-1.75,'$\\nabla^2\\mathcal{L}$',color=GREEN,fontsize=8,ha='right'); a.text(-1.6,-1.9,'$\\nabla^2 f$',color=MUTED,fontsize=8); a.text(0,-1.2,'圆上的目标',color=BLUE,fontsize=8,ha='center')
setup(a,(-1.7,1.7),(-2.2,-.7),xt=(-1,0,1),yt=(-2,-1.5,-1),xl='$s$',yl='目标值',equal=False)
x=np.array([1.4,.2]); r=np.sqrt(2); t0=np.arctan2(x[1],x[0]); tang=np.array([-x[1],x[0]])/r
s=np.linspace(-.3,2.6,300); pts=r*np.c_[np.cos(t0+s/r),np.sin(t0+s/r)]
b.plot(s,-pts.sum(1),color=BLUE,lw=1.4); g=cg(x)@tang
b.plot(s,-1.6+g*s+.5*s**2,color=GREEN,lw=1.4); b.plot(s,-1.6+g*s,color=YELLOW,lw=1.6,ls=(0,(4,2)))
sm=-g; dot(b,(0,-1.6),GREEN); dot(b,(sm,-1.6+g*sm+.5*sm**2),GREEN,ms=4); dot(b,(np.pi/4*r-t0*r,-2.))
b.text(2.55,-3.25,'$\\nabla^2 f$',color=MUTED,fontsize=8,ha='right',va='top'); b.text(2.0,-1.74,'$\\nabla^2\\mathcal{L}$',color=GREEN,fontsize=8,ha='right'); b.text(1.2,-2.2,'圆上的目标',color=BLUE,fontsize=8,ha='left')
setup(b,(-.35,2.65),(-3.5,-1.3),xt=(0,1,2),yt=(-3,-2),xl='$s$',yl='目标值',equal=False)
tags(fig,axes)
save(fig,HERE,'figure',{'slope_b':float(g),'sm':float(sm)})
