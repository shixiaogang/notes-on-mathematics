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



A=np.array([[2.,.5],[.5,1.]]);G=A.T@A;lam,V=np.linalg.eigh(G);order=np.argsort(lam)[::-1];lam=lam[order];V=V[:,order]
for i in range(2):
 if V[1,i]<0:V[:,i]*=-1
sigma=np.sqrt(lam);U=A@V/sigma
th=np.linspace(0,2*np.pi,501);circle=np.vstack([np.cos(th),np.sin(th)])
fig=plt.figure(figsize=(169/25.4,57/25.4))
axs=[fig.add_axes([x/169,7/57,44/169,44/57]) for x in [10,62,114]]
for ax,limit in zip(axs,[2.1,1.25,2.5]):ax.set(xlim=(-limit,limit),ylim=(-limit,limit),aspect='equal');ax.axis('off')
axs[0].plot(*(V@np.diag(np.sqrt(2/lam))@circle),color=BLUE,lw=1.2);axs[0].plot(0,0,'o',color=INK,ms=2.5)
axs[1].plot(*circle,color=MUTED,lw=.85)
for i,color in enumerate([BLUE,GREEN]):
 arrow(axs[1],V[:,i],color)
 q=(.65,-.05) if i==0 else (-.55,.6);axs[1].text(*q,rf'$v_{i+1}$',color=color)
axs[2].plot(*circle,color=MUTED,lw=.85);axs[2].plot(*(A@circle),color=BLUE,lw=1.2)
for i,color in enumerate([BLUE,GREEN]):
 tip=sigma[i]*U[:,i];arrow(axs[2],tip,color)
 labelpos=(1.3,1.55) if i==0 else (-1.35,1.55)
 axs[2].text(*labelpos,rf'$\sigma_{i+1}u_{i+1}$',color=color,fontsize=8)
for x,label in [(32,'(a)'),(84,'(b)'),(136,'(c)')]:fig.text(x/169,54/57,label,ha='center',va='center')
for x in [58,110]:fig.text(x/169,29/57,r'$\rightarrow$',ha='center',va='center',color=INK)
assert np.allclose(A,U@np.diag(sigma)@V.T)
save(fig,{'matrix':A.tolist(),'Gram':G.tolist(),'eigenvalues':lam.tolist(),'singular_values':sigma.tolist(),'right_singular_vectors':V.tolist(),'left_singular_vectors':U.tolist(),'panel_a':'x.T A.T A x=2','panel_b':'unit circle and Gram eigendirections','panel_c':'unit circle, its image A B2, and images sigma_i*u_i','layout':'Three44mm square diagram frames separated by8mm; shared origin and title baselines; numerical matrices and long formulas moved to caption.'})
