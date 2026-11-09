from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Basic variables along the entering direction: x_B(alpha)=x_B-alpha*u.
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
data = [([8,10,3],[2,1,1],['$x_3$','$x_4$','$x_5$'],[3.0],(0,6),(-2,11),'(a)',[(1.6,5.9),(4.6,6.0),(1.3,2.15)]),
        ([2,3,3],[-2,3,1],['$x_1$','$x_4$','$x_2$'],[1.0],(0,3.6),(-2,10),'(b)',[(2.9,8.5),(1.4,-1.5),(2.5,1.3)])]
for ax,(xb,u,names,ast,xl,yl,lab,pos) in zip(axs,data):
    t=np.linspace(xl[0],xl[1],100)
    ax.axhline(0,color=EDGE,lw=.85,zorder=1)
    cols=[BLUE,PURPLE,GREEN] 
    for v,w,n,c in zip(xb,u,names,cols):
        y=v-t*w; ax.plot(t,y,color=c,lw=1.4)
    for n,(px,py) in zip(names,pos): ax.text(px,py,n,fontsize=8,color=INK)
    a=ast[0]; ax.axvline(a,color=MUTED,lw=.85,ls=':')
    ax.plot([a],[0],'o',color=RED,ms=5,zorder=6)
    ax.text(a+.06*xl[1],.45,f'$\\alpha={a:g}$',fontsize=7.5,color=INK)
    ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_xlabel('$\\alpha$\n'+lab,labelpad=1)
    ax.set_ylabel('基变量取值',labelpad=1)
save(fig, Path(__file__).resolve().parent, 'figure', {'round0':'xB=(8,10,3),u=(2,1,1)','round2':'xB=(2,3,3),u=(-2,3,1)'})
