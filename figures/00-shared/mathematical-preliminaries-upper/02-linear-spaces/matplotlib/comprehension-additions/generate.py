# coding: utf-8
"""Two linear-space analytic teaching charts. No sampled empirical or random data."""
from pathlib import Path
import sys
import numpy as np
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/01-mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, PURPLE, RED, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL
D=Path(__file__).resolve().parent


def conjugate_directions():
    fig,ax=figure(height_mm=46)
    x=np.linspace(-.6,4.7,360); y=np.linspace(-1.35,1.35,240)
    xx,yy=np.meshgrid(x,y)
    ax.contour(xx,yy,.5*(xx**2+4*yy**2),levels=[.5,2,4,8],colors=GRID,linewidths=.6)
    points=np.array([[4.,0.],[3.2,-.8],[0.,0.]])
    ax.plot(points[:,0],points[:,1],color=BLUE,marker='o',ms=3)
    for a,b,c in zip(points[:-1],points[1:],[BLUE,GREEN]):
        ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':c,'lw':1.1})
    ax.text(4.07,.12,r'$𝐱^{(0)}$');ax.text(3.25,-1.12,r'$𝐱^{(1)}$');ax.text(-.2,.15,r'$𝐱_* = 0$')
    ax.text(3.85,-.55,r'$𝐩$',color=BLUE);ax.text(1.6,-.67,r'$𝐪$',color=GREEN)
    ax.set(xlim=(-.6,4.7),ylim=(-1.35,1.35),xlabel=r'$x_1$',ylabel=r'$x_2$')
    ax.set_xticks([0,2,4]); ax.set_yticks([-1,0,1])
    save(fig,D,'linear-conjugate-directions',{'objective':'phi(x)=0.5*(x1^2+4*x2^2)','A':[[1,0],[0,4]],'p':[1,1],'q':[-4,1],'pTAq':0,'start':[4,0],'line_search_steps':[-.8,.8],'points':points.tolist(),'scope':'Conjugate line-search example, not the CG recurrence from this initial residual.'})


def jordan_accumulation():
    fig,ax=figure(height_mm=46)
    k=np.arange(21);a=.8**k;b=np.zeros_like(a);b[1:]=k[1:]*.8**(k[1:]-1)
    ax.plot(k,b,'o-',color=BLUE,ms=2.5,label=r'$x_1^{(k)}=k\,0.8^{k-1}$')
    ax.plot(k,a,'s--',color=GREEN,ms=2.2,label=r'$x_2^{(k)}=0.8^k$')
    ax.set(xlabel=r'$k$',ylabel='坐标值',xlim=(0,20),ylim=(0,2.25));ax.set_xticks([0,5,10,15,20]);ax.legend(loc='upper right')
    save(fig,D,'linear-jordan-accumulation',{'matrix':[[.8,1],[0,.8]],'initial':[0,1],'k_range':[0,20],'first_coordinate_at_k0':0,'first_coordinate_k_ge_1':'k*0.8**(k-1)','second_coordinate':'0.8**k','data':np.column_stack([k,b,a]).tolist()})


if __name__=='__main__':
    for draw in [conjugate_directions,jordan_accumulation]:
        draw()
    print('Generated two linear-space analytic charts.')
