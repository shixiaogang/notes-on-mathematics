from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Limit of the undamped Riemannian Newton iteration (Rayleigh quotient iteration) for each start point.
from matplotlib.colors import ListedColormap
fig,ax=figure(width_mm=62,height_mm=58)
D=Disk(28,24,N=700); P=D.P.copy(); d=np.array([1.,2,4])
for _ in range(40):
    q=(P*P*d).sum(-1,keepdims=True)
    den=d-q; den[np.abs(den)<1e-13]=1e-13
    P=P/den; P/=np.linalg.norm(P,axis=-1,keepdims=True)
lab=np.ma.array(np.abs(P).argmax(-1),mask=D.mask)
for i in range(3): print(i,float((lab==i).sum())/float((~D.mask).sum()))
ax.imshow(lab,origin='lower',extent=(-1,1,-1,1),cmap=ListedColormap([BLUE_FILL,YELLOW_FILL,PURPLE_FILL]),vmin=0,vmax=2,interpolation='nearest')
th=np.linspace(0,2*np.pi,400); ax.plot(np.cos(th),np.sin(th),color=BLUE,lw=1.1)
e=np.eye(3)
ax.plot(*D.xy(e[0]),'o',ms=4.6,color=RED); ax.plot(*D.xy(e[1]),'o',ms=4.6,mfc='white',mec=PURPLE,mew=1.1); ax.plot(*D.xy(e[2]),'s',ms=4.2,mfc='white',mec=GRAY,mew=1.1)
ax.plot(*D.xy(X0),'o',ms=4.2,color=GREEN)
for p,t,dx,dy in [(e[0],r'$\mathbf{e}_1$',-.04,-.17),(e[1],r'$\mathbf{e}_2$',.1,-.07),(e[2],r'$\mathbf{e}_3$',.12,-.02),(X0,r'$\mathbf{x}^{(0)}$',.06,.1)]:
    a,b=D.xy(p); ax.text(a+dx,b+dy,t,ha='center',va='center',fontsize=8)
ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.05,1.05); ax.set_ylim(-1.05,1.05)
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'x+ = normalize((A-qI)^{-1}x), 40 steps, label = largest component of limit'})
