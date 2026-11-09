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
# 双谷链精确计算：同一预算 B 下的降温安排，P(前 B 次内到过全局最小)
f=np.array([3,1,3,5,2,0,2.])
def step(d,T,absorb=5):
    up=.5*np.minimum(1,np.exp(-(f[1:]-f[:-1])/T)); dn=.5*np.minimum(1,np.exp(-(f[:-1]-f[1:])/T))
    out=np.zeros(7); out[1:]+=d[:-1]*up; out[:-1]+=d[1:]*dn
    stay=np.ones(7); stay[:-1]-=up; stay[1:]-=dn; o=out+d*stay
    return o
def log_(t,B): return 4/np.log(t+2)
def geo(t,B): return 4*(.1/4)**(t/max(B-1,1))
def stair(t,B): return [4,2,1,.5,.25][min(4,int(5*t/B))]
def fix(t,B): return 1.0
Bs=np.unique(np.round(np.logspace(1,4,28)).astype(int))
def hit(fn,B):
    d=np.zeros(7); d[1]=1; got=0
    for t in range(B):
        d=step(d,fn(t,B)); got+=d[5]; d[5]=0
    return got
def end(fn,B):
    d=np.zeros(7); d[1]=1
    for t in range(B): d=step(d,fn(t,B))
    return d[5]
fig,axes=figure(width_mm=112,height_mm=58,ncols=2); panel(fig,.095,.965,.96,.25,.3)
a=axes[0]; B0=2000; tt=np.arange(B0)
a.plot(tt,[log_(t,B0) for t in tt],color=PURPLE,lw=1.4); a.plot(tt,[geo(t,B0) for t in tt],color=GREEN,lw=1.4); a.plot(tt,[stair(t,B0) for t in tt],color=YELLOW,lw=1.4); a.plot(tt,[1 for t in tt],color=MUTED,lw=1.2,ls=(0,(4,2)))
a.set_yscale('log'); a.set_xlim(0,2000); a.set_ylim(.08,6); a.set_xticks([0,1000,2000]); a.set_yticks([.1,1]); a.set_yticklabels(['0.1','1']); a.minorticks_off(); a.set_xlabel('$t$',labelpad=1); a.set_ylabel('$T$',labelpad=1)
a.text(1130,1.4,'对数',fontsize=7.5,va='center'); a.text(1200,.16,'几何',fontsize=7.5); a.text(1820,.32,'分段',fontsize=7.5,ha='center',va='bottom')
a.text(70,.8,'固定',fontsize=7.5,va='top')
b=axes[1]; R={}
for name,fn,c,ls in (('log',log_,PURPLE,'-'),('geo',geo,GREEN,'-'),('stair',stair,YELLOW,'-'),('fixed',fix,MUTED,(0,(4,2)))):
    h=[hit(fn,int(B)) for B in Bs]; b.plot(Bs,h,color=c,lw=1.5,ls=ls); R[name]=dict(hit=h[-1],end=end(fn,10000))
print(R)
b.set_xscale('log'); b.set_xlim(10,1e4); b.set_ylim(0,1.02); b.set_xticks([10,100,1000,10000]); b.minorticks_off(); b.set_yticks([0,.5,1]); b.set_yticklabels(['0','0.5','1']); b.set_xlabel('预算 B',labelpad=1); b.set_ylabel('到过全局最小的概率',labelpad=1)
tags(fig,axes); save(fig,HERE,'figure',{'budgets':Bs.tolist(),'result_at_1e4':R})
