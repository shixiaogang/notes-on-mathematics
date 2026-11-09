from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# L=M=1, eps=1/2, m=4, eta=1/4；f=x^2/2-1/4。(a) 节点值与 Lipschitz 允许区域；(b) 刻度量化与代表 Iq。
L=1; f=lambda x:x**2/2-.25
nodes=np.arange(5)/4; fv=f(nodes)
levels=np.array([-.75,-.25,.25,.75])
q=[]
for y in fv:
    d=np.abs(levels-y); q.append(levels[np.where(d<=d.min()+1e-12)[0][0]])
q=np.array(q); print(q)
fig, axes = figure(width_mm=112, height_mm=52, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.97, bottom=.24, wspace=.2)
a,b=axes
x=np.linspace(0,1,801)
for j in range(4):
    u=np.linspace(nodes[j],nodes[j+1],200)
    up=np.minimum(fv[j]+L*(u-nodes[j]),fv[j+1]+L*(nodes[j+1]-u))
    lo=np.maximum(fv[j]-L*(u-nodes[j]),fv[j+1]-L*(nodes[j+1]-u))
    a.fill_between(u,lo,up,color=BLUE_FILL,lw=0)
a.plot(x,f(x),color=BLUE,lw=1.4)
a.plot(nodes,fv,'o',ms=3.8,color=BLUE,mew=0,zorder=4)
for v in nodes: a.plot([v,v],[-.95,.95],color=MUTED,lw=.85,ls=(0,(2,1.5)),zorder=0)
a.set_xlim(-.02,1.02); a.set_ylim(-.95,.95); a.set_xticks(nodes); a.set_xticklabels(['0','1/4','1/2','3/4','1']); a.set_yticks([-.5,0,.5]); a.set_yticklabels(['-1/2','0','1/2'])
for lv in levels: b.plot([-.02,1.02],[lv,lv],color=MUTED,lw=.85,ls=(0,(4,2)),zorder=0)
b.plot(x,f(x),color=BLUE,lw=1.4)
b.plot(nodes,q,color=GREEN,lw=1.4)
for v,y,yq in zip(nodes,fv,q):
    if abs(y-yq)>1e-9: b.plot([v,v],[y,yq],color=RED,lw=1.1,solid_capstyle='butt')
b.plot(nodes,q,'s',ms=3.6,color=GREEN,mew=0,zorder=4)
b.plot(nodes,fv,'o',ms=3.4,color=BLUE,mew=0,zorder=4)
b.set_xlim(-.02,1.02); b.set_ylim(-.95,.95); b.set_xticks(nodes); b.set_xticklabels(['0','1/4','1/2','3/4','1']); b.set_yticks(levels); b.set_yticklabels(['-3/4','-1/4','1/4','3/4'])
b.text(.1,-.18,'$f$',color=BLUE,ha='center',va='bottom'); b.text(.84,.3,'$Iq_f$',color=GREEN,ha='center',va='bottom')
for ax,s_ in zip(axes,['(a)','(b)']):
    q_=ax.get_position(); fig.text((q_.x0+q_.x1)/2,.03,s_,ha='center',va='bottom')
save(fig,Path(__file__).resolve().parent,'figure',{'formula':'f=x^2/2-1/4; L=M=1, m=4, eta=1/4, levels ±1/4, ±3/4; q=(-1/4,-1/4,-1/4,1/4,1/4)'})
