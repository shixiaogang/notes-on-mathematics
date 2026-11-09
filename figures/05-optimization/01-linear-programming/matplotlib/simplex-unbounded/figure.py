from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Unbounded example: max x1+x2, x1-x2<=2, -x1+x2<=1, x>=0.
xlim, ylim = (-.4, 6.6), (-.4, 6.2)
fig, ax = figure(width_mm=88, height_mm=62)
far=9
poly=np.array([[0,0],[2,0],[2+far,far],[far,1+far],[0,1]],float)
ax.fill(poly[:,0],poly[:,1],facecolor=BLUE_FILL,edgecolor=BLUE,lw=1.0,zorder=1)
contours(ax,np.array([1.,1.]),[2,6,10],xlim,ylim)
draw_line(ax,[1,-1],2,xlim,ylim); draw_line(ax,[-1,1],1,xlim,ylim)
path(ax,[(0,0),(2,0)],color=GREEN)
d=np.array([1.,1.]); s=np.array([2.,0.])
ax.annotate('',xy=s+4.2*d,xytext=s,arrowprops=dict(arrowstyle='-|>',color=RED,lw=1.6,mutation_scale=9,shrinkA=0,shrinkB=0),zorder=6)
ax.text(4.55,1.75,'$\\mathbf{d}=(1,1,0,0)$',fontsize=7.5,color=INK)
ax.text(2.55,.05,'$t=1$',fontsize=7.5,color=INK); ax.text(.1,.2,'$t=0$',fontsize=7.5,color=INK)
setup(ax,xlim,ylim,range(0,7),range(0,7))
save(fig, Path(__file__).resolve().parent,'figure',{'problem':'max x1+x2; x1-x2<=2; -x1+x2<=1; x>=0','ray':'(2,0)+a(1,1)'})
