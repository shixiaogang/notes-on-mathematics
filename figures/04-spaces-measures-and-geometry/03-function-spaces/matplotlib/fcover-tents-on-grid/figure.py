from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# 第 4.10 章的鼓包 phi_n，支撑 [1/(n+1),1/n]；节点 j/8。n>=8 的鼓包在节点上全为零。
def tent(n,x):
    l,r=1/(n+1),1/n; c,w=(l+r)/2,(r-l)/2
    return np.maximum(0,1-np.abs(x-c)/w)
fig, axes = figure(width_mm=112, height_mm=46, ncols=2, width_ratios=[1.25,1])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.96, bottom=.26, wspace=.14)
a,b=axes
x=np.linspace(0,1,40001)
for n in range(1,8): a.plot(x,tent(n,x),color=BLUE,lw=1.4 if n<4 else 1.1)
for n in range(8,15): a.plot(x,tent(n,x),color=RED,lw=.85)
nodes=np.arange(9)/8
vals=np.array([max(tent(n,np.array([v]))[0] for n in range(1,8)) for v in nodes])
a.plot(nodes,vals,'o',ms=3.8,mfc=INK,mec='white',mew=.5,zorder=5,clip_on=False)
a.set_xlim(0,1.02); a.set_ylim(0,1.18); a.set_xticks(nodes); a.set_xticklabels(['0','','','','1/2','','','','1']); a.set_yticks([0,1])
x=np.linspace(0,.13,40001)
for n in range(8,15): b.plot(x,tent(n,x),color=RED,lw=1.1)
b.plot([0,1/8],[0,0],'o',ms=3.8,mfc=INK,mec='white',mew=.5,zorder=5,clip_on=False)
b.set_xlim(0,.13); b.set_ylim(0,1.18); b.set_xticks([0,1/8]); b.set_xticklabels(['0','1/8']); b.set_yticks([0,1])
b.text(.1181,1.04,r'$\varphi_8$',ha='center',va='bottom',color=INK)
b.text(.1056,1.04,r'$\varphi_9$',ha='center',va='bottom',color=INK)
for ax,s_ in zip(axes,['(a)','(b)']):
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,s_,ha='center',va='bottom')
save(fig,Path(__file__).resolve().parent,'figure',{'formula':'tents on [1/(n+1),1/n], n=1..14; nodes j/8'})
