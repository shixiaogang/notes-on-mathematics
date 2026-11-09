from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"simplex-common"))
from lp_plot import *

# Degenerate variant b=(8,7,3): three lines through (2,3); (b) raises b2 by 0.6 (exaggerated).
xlim, ylim = (-.4, 4.6), (-.4, 4.4)
fig, axs = figure(width_mm=112, height_mm=56, ncols=2)
for ax,b2,lab in zip(axs,[7.,7.6],['(a)','(b)']):
    B=np.array([8.,b2,3.]); A,b=with_sign(RES_A,B); V=polygon(A,b)
    draw_region(ax,V)
    for a,v in zip(RES_A,B): draw_line(ax,a,v,xlim,ylim,lw=1.2)
    setup(ax,xlim,ylim,range(0,5),range(0,5),label=lab)
ax=axs[0]; ax.plot([2],[3],'o',color=RED,ms=5,zorder=8)
ax.text(2.2,3.72,'$(1,4,2)$',fontsize=7.5,color=INK)
ax.text(2.2,3.36,'$(1,5,2)$',fontsize=7.5,color=INK)
ax.text(.55,2.5,'$(3,1,2)$',fontsize=7.5,color=INK)
ax.annotate('',xy=(2,3.04),xytext=(1.3,2.75),arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7),zorder=3)
ax=axs[1]; p=np.array([2.,3.]); q=np.linalg.solve(RES_A[:2],[8.,7.6])
path(ax,[(0,3),p,q],color=GREEN); opt_point(ax,q)
ax.text(1.42,2.62,'$(2,3)$',fontsize=7.5,color=INK); ax.text(2.32,2.3,'$(2.4,2.8)$',ha='right',fontsize=7.5,color=INK)
save(fig,Path(__file__).resolve().parent,'figure',{'vertex':[2,3],'perturbed_b2':7.6,'split_vertex':q.tolist()})
