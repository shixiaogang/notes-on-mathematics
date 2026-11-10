from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/hj-common"))
from hj_common import *
HERE = Path(__file__).resolve().parent
# Target: H(x,p)=c(x)|p|, c=1+a*x2 with a=.5, source at origin. Rays from RK4 on the characteristic system,
# level curves from the closed-form arrival time T=arccosh(1+a^2 r^2/(2 c c0))/a. Prints mismatch along rays.
fig, ax = figure(width_mm=92, height_mm=66)
style(ax)
a=.5
def c(x,y): return 1+a*y
def TT(x,y): return np.arccosh(1+a*a*(x*x+y*y)/(2*c(x,y)))/a
xs=np.linspace(-5,5,601); ys=np.linspace(-1.1,4.2,401); X,Y=np.meshgrid(xs,ys)
ax.contour(X,Y,TT(X,Y),levels=[.5,1,1.5,2,2.5,3],colors=[BLUE],linewidths=1.1)
def rhs(s):
    x,y,px,py=s; n=np.hypot(px,py); cc=c(x,y)
    return np.array([cc*px/n,cc*py/n,0.0,-a*n])
worst=0
for th in np.deg2rad(np.arange(-20,201,20)):
    s=np.array([0,0,np.cos(th),np.sin(th)],float); h=.01; tr=[s[:2].copy()]; t=0
    while t<3.2-1e-9:
        k1=rhs(s);k2=rhs(s+h/2*k1);k3=rhs(s+h/2*k2);k4=rhs(s+h*k3); s=s+h/6*(k1+2*k2+2*k3+k4); t+=h; tr.append(s[:2].copy())
    worst=max(worst,abs(TT(s[0],s[1])-t))
    tr=np.array(tr); ax.plot(tr[:,0],tr[:,1],color=LINE,lw=.85)
print('max |T(ray end)-t| =',worst)
ax.plot([0],[0],'o',ms=4.5,color=RED,zorder=6)
ax.set_xlim(-5,5); ax.set_ylim(-1.1,4.2); ax.set_xlabel('$x_1$'); ax.set_ylabel('$x_2$')
save(fig,HERE,'figure',{'formula':'c=1+.5 x2; T closed form; rays RK4 h=.01','max_mismatch':float(worst)})
