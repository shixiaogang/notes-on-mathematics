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


b1=np.array([2.,0.]);b2=np.array([1.,1.5]);B=np.column_stack([b1,b2]);G=B.T@B
fig,axs=plt.subplots(1,2,figsize=(112/25.4,55/25.4),layout='constrained',gridspec_kw={'width_ratios':[1.3,1]})
a,b=axs;a.set(xlim=(-.15,2.4),ylim=(-.35,1.9),aspect='equal');a.axis('off');b.axis('off')
arrow(a,b1,BLUE);arrow(a,b2,GREEN)
a.plot([1,1],[0,1.5],ls='--',color=MUTED,lw=.75)
a.plot([.9,.9,1],[0,.1,.1],color=MUTED,lw=.75)
a.text(2.05,-.09,r'$b_1$',color=BLUE);a.text(1.02,1.55,r'$b_2$',color=GREEN)
a.plot(1,0,'o',color=YELLOW,ms=3)
a.text(1,-.22,r'$p$',color=YELLOW,ha='center')
b.set(xlim=(0,3.5),ylim=(0,3.5),aspect='equal')
b.text(.05,1.8,r'$G=$',ha='left',va='center')
for x,side in [(1.1,1),(3.35,-1)]:
 b.plot([x+.12*side,x,x,x+.12*side],[2.75,2.75,.85,.85],color=INK,lw=.8)
for i in range(2):
 for j in range(2):
  col=BLUE if i==j==0 else GREEN if i==j==1 else YELLOW
  b.text(1.65+j*1.0,2.3-i*1.0,f'{G[i,j]:g}',ha='center',va='center',color=col)
fig.text(.52,.52,r'$\longrightarrow$',ha='center',va='center',color=MUTED)
save(fig,{'vectors':[b1.tolist(),b2.tolist()],'projection_b2_on_b1':[1,0],'gram':G.tolist(),'formula':'G=B.T@B; G11=4, G12=G21=2, G22=3.25','scope':'Left geometry supplies the entries of the right Gram table.'})
