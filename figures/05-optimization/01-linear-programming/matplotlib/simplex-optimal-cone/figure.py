from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Optimality at (4,2): profit (4,5)=2*(1,2)+1*(2,1).
xlim, ylim = (1.6, 7.9), (.3, 8.0)
fig, ax = figure(width_mm=86, height_mm=64)
A, b = with_sign(RES_A, RES_B); V = polygon(A, b)
draw_region(ax, V)
contours(ax, PROFIT, [26], xlim, ylim)
draw_line(ax, RES_A[0], 8, xlim, ylim, lw=1.4); draw_line(ax, RES_A[1], 10, xlim, ylim, lw=1.4)
o=np.array([4.,2.]); n1=np.array([1.,2.]); n2=np.array([2.,1.]); p=PROFIT
Q=np.array([o,o+2*n1,o+p,o+n2]); ax.fill(Q[:,0],Q[:,1],facecolor=PURPLE_FILL,edgecolor='none',zorder=2)
def arr(a,b,c,lw=1.4): ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='-|>',color=c,lw=lw,shrinkA=0,shrinkB=0,mutation_scale=9),zorder=6)
arr(o,o+2*n1,PURPLE); arr(o,o+n2,PURPLE); arr(o,o+p,BLUE,1.5)
ax.plot([(o+2*n1)[0],(o+p)[0]],[(o+2*n1)[1],(o+p)[1]],color=PURPLE,lw=.85,ls=':',zorder=5)
ax.plot([(o+n2)[0],(o+p)[0]],[(o+n2)[1],(o+p)[1]],color=PURPLE,lw=.85,ls=':',zorder=5)
opt_point(ax,o)
ax.text(4.86,4.95,'$2\\,(1,2)$',fontsize=7.5,color=INK,ha='right')
ax.text(6.05,2.6,'$1\\,(2,1)$',fontsize=7.5,color=INK)
ax.text(7.86,7.15,'$\\mathbf{p}=(4,5)$',fontsize=8,color=INK,ha='right')
ax.text(3.72,1.62,'$(4,2)$',fontsize=7.5,color=INK,ha='right')
setup(ax,xlim,ylim,range(2,8),range(1,9))
save(fig, Path(__file__).resolve().parent,'figure',{'identity':'(4,5)=2*(1,2)+1*(2,1)'})
