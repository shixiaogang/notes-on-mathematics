"""Exact analytic teaching figure aligned with current volume-two text."""
from pathlib import Path
import sys,json,argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Arc
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
NAME=OUT.name
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,GREEN,RED,YELLOW,INK,MUTED,BLUE_FILL,GREEN_FILL,RED_FILL
configure()
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--only',default=NAME,choices=[NAME]);parser.parse_args()

def axes(ax,limit,ticks):
 ax.set(xlim=(-limit,limit),ylim=(-limit,limit),xticks=ticks,yticks=ticks,aspect='equal')
 ax.grid(False)

def arrow(ax,end,color):
 ax.annotate('',xy=end,xytext=(0,0),arrowprops={'arrowstyle':'->','color':color,'lw':1.2,'shrinkA':0,'shrinkB':0})

def save(fig,facts):
 prepare_figure(fig)
 for ext in ('pdf','svg','png'):fig.savefig(OUT/(NAME+'.'+ext),dpi=300)
 (OUT/'sources.json').write_text(json.dumps({'kind':'exact analytic teaching construction, no empirical data','facts':facts,'style':style_record(),'width_mm':fig.get_figwidth()*25.4,'height_mm':fig.get_figheight()*25.4,'exports':['PDF vector','SVG glyph paths','PNG 300 dpi']},ensure_ascii=False,indent=2)+'\n')
 plt.close(fig)


z=np.array([2.,-1.]);B=np.array([[1,0],[0,1],[-1,0],[0,-1]])
fig,axs=plt.subplots(1,2,figsize=(112/25.4,58/25.4),layout='constrained')
for ax in axs:
 axes(ax,1.55,[-1,0,1]);ax.add_patch(Polygon(B,closed=True,facecolor=BLUE_FILL,edgecolor=BLUE,lw=1.2))
 ax.set_xlabel(r'$r_1$');ax.set_ylabel(r'$r_2$');ax.text(-.6,-.65,r'$B$',color=BLUE)
xx=np.linspace(-1.55,1.55,401)
for c in [.5,1.25]:axs[0].plot(xx,2*xx-c,color=MUTED,ls='--',lw=.7)
arrow(axs[0],z*.55,GREEN);axs[0].text(1.12,-.7,r'$z$',color=GREEN)
axs[1].plot(xx,2*xx-2,color=RED,lw=1.2);axs[1].plot(1,0,'o',color=RED,ms=4)
axs[1].text(.8,.23,r'$r_*$',color=RED)
save(fig,{'unit_ball':'abs(r1)+abs(r2)<=1','reading_direction':z.tolist(),'support_levels_before_contact':[.5,1.25],'support_level_at_contact':2,'maximizer':[1,0],'dual_norm':2,'formula':'max_{||r||1<=1} z.T r = ||z||infinity = 2','scope':'Parallel level lines move in direction z until the last contact at r*; coordinates and scale agree in both panels.'})
