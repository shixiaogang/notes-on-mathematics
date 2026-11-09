from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')
def rastrigin(X, Y): return 20+X**2+Y**2-10*np.cos(2*np.pi*X)-10*np.cos(2*np.pi*Y)
# CMA-ES（标准默认参数，n=2，lambda=6）在 f=x^T A x/2，A=[[5,-4],[-4,5]] 上的协方差适应，种子固定
A=np.array([[5,-4],[-4,5.]]); F=lambda x:.5*np.einsum('...i,ij,...j',x,A,x)
def cma(m,s,lam,G,seed):
    rng=np.random.default_rng(seed); n=len(m); mu=lam//2; w=np.log(mu+.5)-np.log(np.arange(1,mu+1)); w/=w.sum(); me=1/(w**2).sum()
    cs=(me+2)/(n+me+5); ds=1+2*max(0,np.sqrt((me-1)/(n+1))-1)+cs; cc=(4+me/n)/(n+4+2*me/n); c1=2/((n+1.3)**2+me); cm=min(1-c1,2*(me-2+1/me)/((n+2)**2+me)); chi=np.sqrt(n)*(1-1/(4*n)+1/(21*n*n))
    C=np.eye(n); ps=np.zeros(n); pc=np.zeros(n); H=[(m.copy(),s,C.copy())]
    for g in range(G):
        d,B=np.linalg.eigh(C); d=np.sqrt(d); z=rng.standard_normal((lam,n)); y=(B*d)@z.T; y=y.T; x=m+s*y; o=np.argsort(F(x))[:mu]; yw=w@y[o]
        m=m+s*yw; ps=(1-cs)*ps+np.sqrt(cs*(2-cs)*me)*(B@((B.T@yw)/d)); hs=np.linalg.norm(ps)/np.sqrt(1-(1-cs)**(2*(g+1)))/chi<1.4+2/(n+1)
        pc=(1-cc)*pc+hs*np.sqrt(cc*(2-cc)*me)*yw; C=(1-c1-cm+c1*(1-hs)*cc*(2-cc))*C+c1*np.outer(pc,pc)+cm*(y[o].T*w)@y[o]; s=s*np.exp(cs/ds*(np.linalg.norm(ps)/chi-1)); H.append((m.copy(),s,C.copy()))
    return H
H=cma(np.array([5.,-1.]),1.,6,60,7)
th=np.linspace(0,2*np.pi,240); circ=np.c_[np.cos(th),np.sin(th)]
fig,axes=figure(width_mm=112,height_mm=62,ncols=2); panel(fig,.075,.985,.965,.235,.25)
a=axes[0]; g=np.linspace(-3,7,500); X,Y=np.meshgrid(g,g); a.contour(X,Y,.5*(5*X**2-8*X*Y+5*Y**2),levels=[2,8,20,40,70],colors=[BLUE],linewidths=.65)
gens=[0,2,4,7,11]; mp=np.array([h[0] for h in H[:12]]); a.plot(mp[:,0],mp[:,1],color=GREEN,lw=1.1)
for k in gens:
    m,s,C=H[k]; d,B=np.linalg.eigh(C); e=m+s*(B@(np.sqrt(d)*circ).T).T; a.plot(e[:,0],e[:,1],color=GREEN,lw=.85); a.plot([m[0]],[m[1]],'o',ms=2.6,color=GREEN,mew=0,zorder=5)
a.plot([0],[0],'o',ms=4.6,color=RED,mew=0,zorder=6); a.set_aspect('equal'); a.set_xlim(-3,7); a.set_ylim(-3,7); a.set_xticks([-2,2,6]); a.set_yticks([-2,2,6]); a.set_xlabel('$x_1$',labelpad=1); a.set_ylabel('$x_2$',labelpad=0)
b=axes[1]; R=[]
Ai=np.linalg.inv(A); Ai=Ai/np.sqrt(np.linalg.det(Ai))
for k,c,lw in ((0,YELLOW,1.1),(6,PURPLE,1.1),(40,GREEN,1.5)):
    C=H[k][2]; C=C/np.sqrt(np.linalg.det(C)); d,B=np.linalg.eigh(C); e=(B@(np.sqrt(d)*circ).T).T; b.plot(e[:,0],e[:,1],color=c,lw=lw); R.append((k,float(d[1]/d[0])))
d,B=np.linalg.eigh(Ai); e=(B@(np.sqrt(d)*circ).T).T; b.plot(e[:,0],e[:,1],color=RED,lw=.95,ls=(0,(3,2)))
b.set_aspect('equal'); b.set_xlim(-2,2); b.set_ylim(-2,2); b.set_xticks([-2,0,2]); b.set_yticks([-2,0,2]); b.set_xlabel('$z_1$',labelpad=1); b.set_ylabel('$z_2$',labelpad=0)
print(R,[float(F(h[0])) for h in H[::10]],H[40][2]/np.sqrt(np.linalg.det(H[40][2])),Ai)
tags(fig,axes); save(fig,HERE,'figure',{'A':A.tolist(),'seed':7,'lambda':6,'cond_C':R})
