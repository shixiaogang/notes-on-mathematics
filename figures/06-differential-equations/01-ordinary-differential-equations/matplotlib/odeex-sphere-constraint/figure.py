from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Ambient ODE y''=-|y'|^2 y on R^3. Tangent start stays on the sphere; a non-tangent start leaves.
fig,axes=figure(width_mm=112,height_mm=52,ncols=2,gridspec_kw={'width_ratios':[1,1.35]})
panel(fig,.02,.975,.965,.24,.2)
def F(t,z):
    y,v=z[:3],z[3:]; return np.concatenate((v,-np.dot(v,v)*y))
z0=np.array([1,0,0,0,1,0.]); T=3.
t,Z=rk4(F,0.,z0,T,6000); c=np.sum(Z[:,:3]**2,axis=1)-1
z1=np.array([1,0,0,.25,1,0.]); t1,Z1=rk4(F,0.,z1,T,6000); c1=np.sum(Z1[:,:3]**2,axis=1)-1
d1=np.sum(Z1[:,:3]*Z1[:,3:],axis=1)
# view: orthographic, camera direction e
az,el=np.radians(25),np.radians(20)
e=np.array([np.cos(el)*np.cos(az),np.cos(el)*np.sin(az),np.sin(el)])
r=np.cross([0,0,1.],e); r/=np.linalg.norm(r); u=np.cross(e,r)
P=lambda y:(y@r,y@u)
ax=axes[0]; th=np.linspace(0,2*np.pi,400); ax.plot(np.cos(th),np.sin(th),color=STROKE,lw=.85,zorder=1)
s=np.linspace(0,2*np.pi,500); C=np.stack((np.cos(s),np.sin(s),0*s),1); vis=C@e>=0
X,Y=P(C); ax.plot(np.where(vis,X,np.nan),np.where(vis,Y,np.nan),color=BLUE,lw=1.5,zorder=3); ax.plot(np.where(~vis,X,np.nan),np.where(~vis,Y,np.nan),color=BLUE,lw=.95,ls=(0,(2,2)),zorder=2)
p=np.array([1,0,0.]); v=np.array([0,1,0.]); px,py=P(p); vx,vy=P(.55*v)
ax.annotate('',xy=(px+vx,py+vy),xytext=(px,py),arrowprops=dict(arrowstyle='-|>,head_width=.16,head_length=.28',color=PURPLE,lw=1.,shrinkA=0,shrinkB=0),zorder=5); dot(ax,px,py)
ax.text(px+vx+.04,py+vy+.12,'v',color=PURPLE,fontsize=8,ha='center'); ax.text(px-.04,py-.14,'p',fontsize=8,ha='center',va='top')
ax.set_xlim(-1.08,1.08); ax.set_ylim(-1.08,1.08); ax.set_aspect('equal'); ax.axis('off')
ax=axes[1]; ax.plot(t1,c1,color=RED,lw=1.5,zorder=3); ax.plot(t,c,color=BLUE,lw=1.6,zorder=4); dot(ax,0,0)
ax.text(1.6,.012,'切向初速度',color=BLUE,fontsize=7.5,ha='left',va='bottom')
ax.text(3.,.27,'非切向初速度',color=RED,fontsize=7.5,ha='right',va='center')
ax.set_xlim(0,3); ax.set_xticks([0,1,2,3]); ax.set_xlabel('t',labelpad=1); ax.set_ylabel('‖y‖² − 1',labelpad=1)
tags(fig,axes)
r=save(fig,HERE,'figure',{'max|c| tangent':float(np.max(abs(c))),'c1 range':[float(c1.min()),float(c1.max())]})
print(r['facts'])
