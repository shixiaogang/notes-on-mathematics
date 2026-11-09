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



fig=plt.figure(figsize=(169/25.4,67/25.4));axs=[fig.add_axes([x,.11,.44,.78]) for x in [.035,.525]]
for ax in axs:ax.set(xlim=(-2.6,3.0),ylim=(-1.25,2.35),aspect='equal');ax.axis('off')
a,b=axs
# Both origins have the same page baseline. Right panel uses explicit oblique
# projection e1=(1,0), e2=(.65,.4), e3=(0,1), not a 3D plotting box.
a.plot([-2.3,2.7],[0,0],color=BLUE,lw=1.3);a.plot([0,0],[-.9,1.95],color=RED,lw=1.3)
arrow(a,(2,1),INK);a.plot([2,2],[1,0],color=MUTED,ls='--',lw=.8);a.plot(2,0,'o',color=BLUE,ms=4)
a.text(2.1,1.05,r'$v$');a.text(2,-.3,r'$T(v)$',color=BLUE,ha='center')
a.text(-2.25,.15,r'$\operatorname{im}T$',color=BLUE);a.text(.12,1.9,r'$\ker T$',color=RED)
plane=np.array([[-2.145,-.52],[.455,-.52],[2.145,.52],[-.455,.52]])
b.add_patch(Polygon(plane,closed=True,facecolor=BLUE_FILL,edgecolor=BLUE,lw=1.2))
b.plot([0,0],[-.9,1.95],color=RED,lw=1.3)
b.plot([1.65,1.65],[1.4,.4],color=MUTED,ls='--',lw=.8)
b.plot(1.65,1.4,'o',color=INK,ms=4);b.plot(1.65,.4,'o',color=BLUE,ms=4)
b.text(1.8,1.45,r'$p$');b.text(1.8,.15,r'$T(p)$',color=BLUE)
b.text(-1.9,-.85,r'$\operatorname{im}T$',color=BLUE);b.text(.12,1.9,r'$\ker T$',color=RED)
for x,label in [(.255,'(a)'),(.745,'(b)')]:fig.text(x,.94,label,ha='center',va='center')
save(fig,{'panel_a':{'map':'T(x,y)=(x,0)','sample':[2,1],'image':[2,0],'kernel_dimension':1,'image_dimension':1},'panel_b':{'map':'T(x,y,z)=(x,y)','sample':[1,1,1],'image':[1,1],'kernel_dimension':1,'image_dimension':2,'projection_basis':[[1,0],[.65,.4],[0,1]]},'layout':'Shared physical frame, origin baseline and panel-title baseline; plane schematic uses explicit oblique projection.'})
