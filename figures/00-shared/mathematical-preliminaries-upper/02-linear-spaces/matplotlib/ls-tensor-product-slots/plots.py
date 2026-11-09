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



U=np.array([1,2]);V=np.array([3,-1,2]);T=np.outer(U,V)
fig=plt.figure(figsize=(112/25.4,42/25.4));ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,112),ylim=(0,42));ax.axis('off')
def brackets(left,right,bottom,top):
 for x,d in [(left,1),(right,-1)]:ax.plot([x+1.2*d,x,x,x+1.2*d],[top,top,bottom,bottom],color=INK,lw=.9)
# No array grid; only the selected output row and column carry semantic marks.
ax.add_patch(Polygon([[71,8.5],[101,8.5],[101,17.5],[71,17.5]],closed=True,facecolor=BLUE_FILL,edgecolor='none'))
ax.add_patch(Polygon([[91,8],[101,8],[101,28],[91,28]],closed=True,facecolor='none',edgecolor=GREEN,lw=1.1))
brackets(6,18,8,28);brackets(28,58,12,24);brackets(69,103,6,30)
for i,val in enumerate(U):ax.text(12,23-10*i,str(val),ha='center',va='center',color=BLUE,fontsize=9)
for j,val in enumerate(V):ax.text(33+10*j,18,str(val),ha='center',va='center',color=GREEN,fontsize=9)
for i in range(2):
 for j in range(3):ax.text(76+10*j,23-10*i,str(T[i,j]),ha='center',va='center',color=INK,fontsize=9)
ax.text(23,18,r'$\otimes$',ha='center',va='center',fontsize=10)
ax.text(64,18,r'$=$',ha='center',va='center',fontsize=10)
for x,label in [(12,r'$u$'),(43,r'$v$'),(86,r'$u\otimes v$')]:ax.text(x,35,label,ha='center',va='center')
save(fig,{'u':U.tolist(),'v':V.tolist(),'tensor_product':T.tolist(),'highlighted_row':2,'highlighted_column':3,'row_relation':'row2=2*v','column_relation':'column3=2*u','layout':'No internal matrix grids; 9pt digits at native112mm; only u,v,u tensor v labels.'})
