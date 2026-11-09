from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# Newton from (8,4,1)/9 versus backtracking gradient descent from the same start.
xs=np.array([8.,4,1])/9
def newton():
    x=xs.copy(); h=[]
    for t in range(6):
        g=grad3(x); h.append(np.linalg.norm(g))
        if h[-1]<1e-15: break
        q=x@A3@x; Q=tangent_basis(x); H=Q.T@(A3-q*np.eye(3))@Q; v=Q@np.linalg.solve(H,-Q.T@g); x=retr(x,v)
    return h
def gd(T=30):
    x=xs.copy(); h=[]
    for t in range(T):
        g=grad3(x); h.append(np.linalg.norm(g)); a=1.
        while f3(retr(x,-a*g))>f3(x)-.25*a*g@g: a/=2
        x=retr(x,-a*g)
    return h
fig,ax=figure(width_mm=88,height_mm=48)
h1=newton(); h2=gd(); print(h1)
ax.semilogy(range(len(h2)),h2,'-o',color=YELLOW,lw=1.4,ms=2.8,label='梯度下降')
ax.semilogy(range(len(h1)),h1,'-o',color=GREEN,lw=1.6,ms=3.4,label='Newton')
ax.set_xlabel('迭代次数'); ax.set_ylabel(r'$\Vert\mathbf{g}^{(t)}\Vert_2$'); ax.legend(handlelength=1.8); ax.set_ylim(1e-17,3)
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'Newton vs RGD, A=diag(1,2,4), x0=(8,4,1)/9'})
