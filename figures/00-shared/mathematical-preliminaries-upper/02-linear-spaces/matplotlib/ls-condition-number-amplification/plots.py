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


matrices=[np.array([[1.,.2],[.2,1.]]),np.array([[1.,.85],[.85,1.]])]
eps=.1;t=np.linspace(0,2*np.pi,501);circle=np.vstack([np.cos(t),np.sin(t)])
fig,axs=plt.subplots(2,2,figsize=(169/25.4,112/25.4),layout='constrained')
info=[]
for j,(A,color,fill) in enumerate(zip(matrices,[BLUE,GREEN],[BLUE_FILL,GREEN_FILL])):
 top,bottom=axs[:,j];s=np.linalg.svd(A,compute_uv=False);image=A@circle;invimage=np.linalg.solve(A,eps*circle)
 axes(top,2.05,[-1,0,1]);axes(bottom,.76,[-.5,0,.5])
 top.plot(*circle,color=MUTED,ls='--',lw=.7);top.fill(*image,facecolor=fill,edgecolor=color,lw=1.2)
 bottom.fill(*invimage,facecolor=fill,edgecolor=color,lw=1.2)
 bottom.plot(*(eps*circle),color=MUTED,ls='--',lw=.7)
 top.set_title(r'$A_'+str(j+1)+r'B_2$');bottom.set_title(r'$A_'+str(j+1)+r'^{-1}(\varepsilon B_2)$')
 # The weak singular direction becomes the longest axis of the inverse image.
 q=np.array([1.,-1.])/np.sqrt(2);arrow(bottom,q*eps/s[-1],color)
 info.append({'matrix':A.tolist(),'singular_values':s.tolist(),'condition_number':float(s[0]/s[-1]),'inverse_error_max_semiaxis':float(eps/s[-1])})
save(fig,{'epsilon':eps,'cases':info,'top':'unit circle and its forward image A B2','bottom':'epsilon circle and its inverse image A^{-1}(epsilon B2)','scope':'Coordinate scale is shared within each row; the bottom row has its own enlarged scale. Forward anisotropy and inverse amplification are different displayed operations.'})
