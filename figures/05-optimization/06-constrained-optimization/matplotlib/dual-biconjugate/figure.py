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
    H=fig.get_figheight()*25.4
    if len(fig.axes)>1: bottom=15.5/H
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tag(fig, ax, s, y=None):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, 1.0/(fig.get_figheight()*25.4), s, ha='center', va='bottom')
def opt(ax, x=0, y=0, ms=4.8, z=7): ax.plot([x],[y],'o',ms=ms,color=RED,mew=0,zorder=z)
def dot(ax, x, y, c=GREEN, ms=4.2, z=6, m='o'): ax.plot([x],[y],m,ms=ms,color=c,mew=0,zorder=z)
def hollow(ax, x, y, c=BLUE, ms=4.4, z=7): ax.plot([x],[y],'o',ms=ms,mfc='white',mec=c,mew=1.0,zorder=z)

# 开区间约束指标函数的双共轭；双井函数的双共轭由离散 Legendre 变换算出。
fig,(A,B,C)=figure(width_mm=112,height_mm=48,ncols=3)
panel(fig,.05,.985,.97,.25,wspace=.24)
def wall(ax,xx,c):
    ax.annotate('',xy=(xx,1.5),xytext=(xx,.14),arrowprops=dict(arrowstyle='-|>',color=c,lw=1.1,shrinkA=0,shrinkB=0,ls='--'))
A.plot([0,1],[0,0],color=BLUE,lw=1.6,zorder=3);hollow(A,0,0);hollow(A,1,0);wall(A,0,BLUE);wall(A,1,BLUE)
B.plot([0,1],[0,0],color=PURPLE,lw=1.6,zorder=3);dot(B,0,0,PURPLE,ms=4.6);dot(B,1,0,PURPLE,ms=4.6);wall(B,0,PURPLE);wall(B,1,PURPLE)
for ax in (A,B):
    ax.set_xlim(-.5,1.5);ax.set_ylim(-.25,1.75);ax.set_xticks([0,1]);ax.set_yticks([0,1]);ax.set_xlabel('$x$',labelpad=1)
x=np.linspace(-3,3,1201);f=(x**2-1)**2;ys=np.linspace(-60,60,2401)
fs=(ys[:,None]*x[None,:]-f[None,:]).max(1);fss=(x[:,None]*ys[None,:]-fs[None,:]).max(1)
m=abs(x)<=1.65
C.plot(x[m],f[m],color=BLUE,lw=1.5);C.plot(x[m],fss[m],color=PURPLE,lw=1.5,ls='--',zorder=4)
C.set_xlim(-1.65,1.65);C.set_ylim(-.15,2.8);C.set_xticks([-1,0,1]);C.set_yticks([0,1,2]);C.set_xlabel('$x$',labelpad=1)
for a_,s in zip((A,B,C),('(a)','(b)','(c)')):tag(fig,a_,s,y=.04)
save(fig,HERE,'figure',{'nonconvex':'(x^2-1)^2','biconjugate_max_on_[-1,1]':float(abs(fss[abs(x)<=1]).max())})
