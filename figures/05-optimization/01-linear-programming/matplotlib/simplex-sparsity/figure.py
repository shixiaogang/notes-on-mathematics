from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Tridiagonal basis matrix (order 40): nonzeros of the matrix, of its LU factors, and of its explicit inverse.
n=40
T=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
L=np.eye(n);U=T.copy()
for k in range(n-1):
    for i in range(k+1,n):
        L[i,k]=U[i,k]/U[k,k];U[i]=U[i]-L[i,k]*U[k]
LU=(np.abs(L-np.eye(n))>1e-12)|(np.abs(U)>1e-12)
Inv=np.abs(np.linalg.inv(T))>1e-12
fig,axs=figure(width_mm=112,height_mm=48,ncols=3)
counts=[int((T!=0).sum()),int(LU.sum()),int(Inv.sum())]
for ax,M,lab,cnt,col in zip(axs,[T!=0,LU,Inv],['(a)','(b)','(c)'],counts,[BLUE,GREEN,RED]):
    r,c=np.nonzero(M); ax.scatter(c,r,s=1.1,color=col,marker='s',linewidths=0)
    ax.set_xlim(-1,n);ax.set_ylim(n,-1);ax.set_aspect('equal');ax.set_xticks([]);ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(True); s.set_linewidth(.7)
    ax.set_xlabel(f'{cnt}\n{lab}',labelpad=2)
save(fig,Path(__file__).resolve().parent,'figure',{'n':n,'nonzeros':{'matrix':counts[0],'LU':counts[1],'inverse':counts[2]}})
