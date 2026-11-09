from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, .015, s, ha='center', va='bottom')

# 相同梯度，不同误差。(a) 一元二次；(b) 拟合例 gamma=0.01。
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, .095, .985, .955, .21, .27)
a=axes[0]; x=np.linspace(-12,12,500)
a.plot(x,.005*x**2,color=BLUE,lw=1.4,label='_'); 
xs=x[np.abs(x)<=1.75]; a.plot(xs,.5*xs**2,color=BLUE,lw=1.4,ls=(0,(3,1.6)))
a.plot([10],[.5],'o',ms=4.4,color=GREEN,mew=0,zorder=5); a.plot([.1],[.005],'o',ms=4.4,color=GREEN,mew=0,zorder=5)
a.plot([0],[0],'o',ms=4.6,color=RED,mew=0,zorder=4) if 0 else None
a.text(9.6,.53,'$x=10$',ha='right',va='bottom'); a.annotate('$x=0.1$',xy=(.1,.005),xytext=(3.2,.2),fontsize=7.5,arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkA=1,shrinkB=2)); a.text(1.8,1.3,'$f_2$',ha='left',va='center'); a.text(-10.5,.68,'$f_1$',ha='left',va='center')
a.set_xlim(-12,12); a.set_ylim(-.08,1.6); a.set_xticks([-10,0,10]); a.set_yticks([0,.5,1,1.5]); a.set_yticklabels(['0','0.5','1','1.5']); a.set_xlabel('$x$',labelpad=1); a.set_ylabel('目标',labelpad=1)
b=axes[1]; g=.01; X,Y=np.meshgrid(np.linspace(-14,16,900),np.linspace(-14,16,900))
F=.5*(X+Y-2)**2+.5*g*(X**2+Y**2); fs=2*g/(2+g)
b.contour(X,Y,F-fs,levels=[.1,.5,1,2],colors=[BLUE],linewidths=.75)
xst=2/(2+g); b.plot([xst],[xst],'o',ms=4.8,color=RED,mew=0,zorder=5)
b.plot([11],[-9],'o',ms=4.4,color=GREEN,mew=0,zorder=5)
b.text(11.2,-7.6,r'$\hat{x}$',ha='left',va='bottom'); b.text(xst+1,xst+1,r'$x^*$',ha='left',va='bottom')
b.set_xlim(-14,16); b.set_ylim(-14,16); b.set_aspect('equal'); b.set_xticks([-10,0,10]); b.set_yticks([-10,0,10]); b.set_xlabel('$x_1$',labelpad=1); b.set_ylabel('$x_2$',labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'f1':'0.005 x^2','f2':'0.5 x^2','ridge_gamma':.01,'x_hat':[11,-9],'x_star':[xst,xst]})
