from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
# Shampoo：单步拉平奇异值；重复读取与累积统计下的变换后奇异值。
rng=np.random.default_rng(21)
U,_=np.linalg.qr(rng.standard_normal((3,3))); V,_=np.linalg.qr(rng.standard_normal((3,3)))
s=np.array([6.,1.,.2]); G=U@np.diag(s)@V.T
def root(A,p):
    w,Q=np.linalg.eigh(A); return Q@np.diag(w**p)@Q.T
eps=1e-6
def step(L,R,G):
    L=L+G@G.T; R=R+G.T@G; return L,R,root(L,-.25)@G@root(R,-.25)
L=eps*np.eye(3);R=eps*np.eye(3)
L,R,Y=step(L,R,G)
sv1=np.linalg.svd(Y,compute_uv=False); print('single',sv1)
# 用同一个 G 重复 20 次：L=20 GG^T，方向奇异值变为 20^{-1/2}
hist=[];Ls=eps*np.eye(3);Rs=eps*np.eye(3)
for k in range(30):
    z=np.array([1.,.1 if k%5 else 1.,.05 if k%3 else .2])
    Gk=U@np.diag(z*s)@V.T + .02*rng.standard_normal((3,3))
    Ls,Rs,Yk=step(Ls,Rs,Gk); hist.append(np.linalg.svd(Yk,compute_uv=False))
hist=np.array(hist); print('hist',hist[[0,5,29]])
fig,(a,b)=figure(width_mm=112,height_mm=54,ncols=2)
panel(fig,.125,.965,.97,.26,wspace=.3)
t=np.arange(3); w=.36
a.bar(t-w/2,s,w,color=YELLOW); a.bar(t+w/2,sv1,w,color=GREEN)
a.set_xticks(t); a.set_xticklabels([r'$\sigma_1$',r'$\sigma_2$',r'$\sigma_3$']); a.set_ylabel('奇异值',labelpad=1)
for k,c in ((0,GREEN),(1,YELLOW),(2,PURPLE)): b.semilogy(np.arange(1,31),hist[:,k],color=c,lw=1.3)
b.set_xlabel('累积读取次数',labelpad=1); b.set_ylabel('变换后奇异值',labelpad=1); b.set_xlim(1,30)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'seed':21,'eps':eps})
