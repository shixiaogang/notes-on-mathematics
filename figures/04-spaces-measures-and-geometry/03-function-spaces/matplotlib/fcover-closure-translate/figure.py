from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# (a) g_n=sqrt((x-1/2)^2+1/n^2), n=2,4,10 收敛到 |x-1/2|；(b) 平移族 phi(x-3n)，phi=max(0,1-|x|)。
fig, axes = figure(width_mm=112, height_mm=44, ncols=2)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.055, right=.985, top=.96, bottom=.27, wspace=.17)
a,b=axes
x=np.linspace(0,1,1001)
for n,lw in [(2,1.1),(4,1.1),(10,1.1)]: a.plot(x,np.sqrt((x-.5)**2+1/n**2),color=BLUE,lw=lw)
a.plot(x,np.abs(x-.5),color=RED,lw=1.4)
a.set_xlim(0,1); a.set_ylim(0,.8); a.set_xticks([0,.5,1]); a.set_xticklabels(['0','1/2','1']); a.set_yticks([0,.5])
a.text(.5,.535,'$g_2$',color=BLUE,ha='center',va='bottom'); a.text(.5,.265,'$g_4$',color=BLUE,ha='center',va='bottom'); a.text(.62,.02,'|x-1/2|',color=RED,ha='left',va='bottom')
x=np.linspace(-1.5,11.2,3001)
for n in range(4): b.plot(x,np.maximum(0,1-np.abs(x-3*n)),color=BLUE,lw=1.4)
b.plot(x,0*x,color=BLUE,lw=.85)
b.set_xlim(-1.5,11.4); b.set_ylim(0,1.25); b.set_xticks([0,3,6,9]); b.set_yticks([0,1])
for n in range(4): b.text(3*n,1.04,fr'$\varphi_{n}$',ha='center',va='bottom')
b.text(10.9,.1,r'$\cdots$',ha='center',va='bottom')
for ax,s_ in zip(axes,['(a)','(b)']):
    q=ax.get_position(); fig.text((q.x0+q.x1)/2,.03,s_,ha='center',va='bottom')
save(fig,Path(__file__).resolve().parent,'figure',{'formula':'g_n=sqrt((x-1/2)^2+1/n^2), n=2,4,10; phi(x-3n), phi=max(0,1-|x|)'})
