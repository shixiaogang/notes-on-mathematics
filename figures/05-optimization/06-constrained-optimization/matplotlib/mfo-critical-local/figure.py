from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Pullback f(normalize(x+v)) near the three stationary pairs of the running example.
fig, axs = figure(width_mm=112, height_mm=44, ncols=3, sharey=True)
e = np.eye(3)
u = np.linspace(-.9,.9,240)
V1,V2 = np.meshgrid(u,u)
for k,(ax,i,lab) in enumerate(zip(axs,(0,1,2),'abc')):
    idx=[j for j in range(3) if j!=i]
    v=np.zeros(V1.shape+(3,)); v[...,i]=1; v[...,idx[0]]=V1; v[...,idx[1]]=V2
    F=.5*(v[...,0]**2+2*v[...,1]**2+4*v[...,2]**2)/(v**2).sum(-1)
    ax.contour(V1,V2,F,levels=8,colors=BLUE,linewidths=.8)
    ax.plot(0,0,'o',ms=4.6,color=RED if i==0 else 'white',mec=RED if i==0 else GRAY,mew=1.1)
    ax.set_aspect('equal'); ax.set_xticks([-.5,0,.5]); ax.set_yticks([-.5,0,.5])
    ax.set_xlabel(f'$v_{idx[0]+1}$'+'\n'+f'({lab})')
    ax.set_ylabel(f'$v_{idx[1]+1}$')
    for s in ax.spines.values(): s.set_linewidth(.75)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'pullback contours at e1,e2,e3, normalization retraction, A=diag(1,2,4)'})
