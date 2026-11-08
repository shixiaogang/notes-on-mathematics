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


A=np.array([[1.,1.],[0.,1.]])
U,s,Vt=np.linalg.svd(A);v=Vt[0];v=v if v[0]>0 else -v;w=A@v
t=np.linspace(0,2*np.pi,501);circle=np.vstack([np.cos(t),np.sin(t)]);ellipse=A@circle
fig,axs=plt.subplots(1,2,figsize=(169/25.4,64/25.4),layout='constrained')
for ax in axs:axes(ax,1.9,[-1,0,1])
axs[0].fill(*circle,facecolor=BLUE_FILL,edgecolor=BLUE,lw=1.2)
axs[1].fill(*ellipse,facecolor=GREEN_FILL,edgecolor=GREEN,lw=1.2)
arrow(axs[0],v,BLUE);arrow(axs[1],w,GREEN)
axs[0].plot(*v,'o',color=BLUE,ms=3);axs[1].plot(*w,'o',color=GREEN,ms=3)
axs[0].text(v[0]+.1,v[1]+.06,r'$x_*$',color=BLUE)
axs[1].text(w[0]+.1,w[1]+.06,r'$Ax_*$',color=GREEN)
axs[0].set_title(r'$B_2$');axs[1].set_title(r'$AB_2$')
assert np.isclose(s[0],(1+np.sqrt(5))/2)
save(fig,{'matrix':A.tolist(),'maximizing_unit_direction':v.tolist(),'image':w.tolist(),'singular_values':s.tolist(),'spectral_norm':'(1+sqrt(5))/2','scope':'Same shear matrix as the immediately preceding example; both panels have the same Euclidean coordinate scale.'})
