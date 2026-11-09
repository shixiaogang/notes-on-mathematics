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
def tag(fig, ax, s, y=None, d=.15):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, (p.y0-d) if y is None else y, s, ha='center', va='top')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
# 邻近束方法与次梯度法，f(x)=max_i(a_i^T x+b_i)（同 ns-smoothing-budget）。
import math,itertools
th_=2*np.pi*np.arange(7)/7;Aa=np.c_[np.cos(th_),np.sin(th_)];bb_=np.array([0,.3,-.2,.5,.1,-.4,.2]);m=7
f=lambda x:np.max(Aa@x+bb_)
def orc(x):
    i=int(np.argmax(Aa@x+bb_));return f(x),Aa[i]
best=1e9;bx=None
for i,j,k in itertools.combinations(range(m),3):
    M=np.c_[Aa[[i,j,k]],-np.ones(3)]
    if abs(np.linalg.det(M))<1e-10: continue
    s=np.linalg.solve(M,-bb_[[i,j,k]])
    if abs(f(s[:2])-s[2])<1e-9 and s[2]<best: best=s[2];bx=s[:2]
fs=best
def proj(v):
    u=np.sort(v)[::-1];c=np.cumsum(u)-1;k=np.nonzero(u>c/np.arange(1,len(v)+1))[0][-1];return np.maximum(v-c[k]/(k+1),0)
def qp(C,G,ctr,tau):
    n=len(C);Hm=tau*G@G.T;Lp=np.linalg.norm(Hm,2)+1e-12;l=np.ones(n)/n;y=l.copy();th=1.
    for it in range(3000):
        ln=proj(y+(C-Hm@y)/Lp);thn=(1+math.sqrt(1+4*th*th))/2;y=ln+(th-1)/thn*(ln-l);l=ln;th=thn
    return ctr-tau*G.T@l
tau=2.;beta=.5
pts=[np.array([3.,2.])];v,g=orc(pts[0]);V=[v];Gs=[g];ctr=pts[0].copy();fc=v;path=[(ctr.copy(),True)];calls=[fc]
for k in range(40):
    G=np.array(Gs);Y=np.array(pts);Vv=np.array(V);C=Vv+((ctr-Y)*G).sum(1)
    y=qp(C,G,ctr,tau);mv=np.max(Vv+((y-Y)*G).sum(1));delta=fc-mv
    if delta<1e-9: break
    vn,gn=orc(y);pts.append(y);V.append(vn);Gs.append(gn)
    ser=fc-vn>=beta*delta;path.append((y.copy(),bool(ser)))
    if ser: ctr=y.copy();fc=vn
    calls.append(fc)
print('rounds',len(calls),'serious',sum(s for _,s in path),'final gap',fc-fs)
x=np.array([3.,2.]);b=f(x);Sb=[b]
for t in range(800):
    v,g=orc(x);x=x-math.sqrt(13)/math.sqrt(t+1)*g;b=min(b,f(x));Sb.append(b)
print('sub end',Sb[40]-fs,Sb[-1]-fs)
fig,(A,B)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.07,.97,.98,.24,wspace=.2)
XX,YY=np.meshgrid(np.linspace(-1.5,3.6,500),np.linspace(-1.8,2.6,500));Z=(XX[...,None]*Aa[:,0][None,None]+YY[...,None]*Aa[:,1][None,None]+bb_).max(-1)
A.contour(XX,YY,Z,levels=[.5,1,1.5,2,2.8,3.5],colors=[BLUE],linewidths=.7)
sp=np.array([p for p,s in path if s]);np_=np.array([p for p,s in path if not s])
A.plot(sp[:,0],sp[:,1],'-o',color=GREEN,lw=1.2,ms=3.3,mew=0,zorder=5)
if len(np_):A.plot(np_[:,0],np_[:,1],'o',ms=3.2,mfc='white',mec=GREEN,mew=.75,zorder=4,ls='none')
opt(A,bx[0],bx[1])
A.set_xlim(-1.5,3.6);A.set_ylim(-1.8,2.6);A.set_aspect('equal');A.set_xticks([-1,0,1,2,3]);A.set_yticks([-1,0,1,2]);A.set_xlabel('$x_1$',labelpad=1);A.set_ylabel('$x_2$',labelpad=0)
tt=np.arange(len(calls));B.semilogy(tt,np.maximum(np.array(calls)-fs,1e-10),'-o',color=GREEN,lw=1.3,ms=2.6,mew=0);tt2=np.arange(len(Sb));B.semilogy(tt2,np.array(Sb)-fs,color=YELLOW,lw=1.4)
B.set_xlim(0,max(40,len(calls)));B.set_ylim(1e-10,6);B.set_yticks([1e-8,1e-4,1]);B.set_xlabel('读取次数',labelpad=1)
fig.canvas.draw();tag(fig,A,'(a)',y=.055);tag(fig,B,'(b)',y=.055)
save(fig,HERE,'figure',{'tau':tau,'beta':beta,'rounds':len(calls),'serious':int(sum(s for _,s in path))})
