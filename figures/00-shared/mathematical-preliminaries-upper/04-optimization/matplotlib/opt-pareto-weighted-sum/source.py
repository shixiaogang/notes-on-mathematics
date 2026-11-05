"""Three exact feasible loss vectors; no continuous feasible frontier is implied."""
from pathlib import Path
import sys,json
import numpy as np
import matplotlib.pyplot as plt
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,GREEN,PURPLE,MUTED,note
configure()
points=np.array([[0.,1.],[1.,0.],[.6,.6]])
assert not any(np.all(q<=p) and np.any(q<p) for i,p in enumerate(points) for j,q in enumerate(points) if i!=j)
fig,ax=plt.subplots(figsize=(112/25.4,77/25.4))
fig.subplots_adjust(left=.16,right=.98,bottom=.18,top=.97)
x=np.linspace(0,1,101)
ax.plot(x,1-x,color=GREEN,ls='--',lw=.6,label=r'$\alpha=1/2$ 的等值线')
ax.scatter(points[:2,0],points[:2,1],color=BLUE,s=28,zorder=3)
ax.scatter([.6],[.6],color=PURPLE,marker='^',s=32,zorder=3)
note(ax.annotate(r'$A=(0,1)$',(0,1),xytext=(10,-1),textcoords='offset points',va='center'))
note(ax.annotate(r'$B=(1,0)$',(1,0),xytext=(.70,.025),textcoords='data',ha='right',arrowprops={'arrowstyle':'-','color':MUTED,'lw':.6}))
note(ax.annotate(r'$C=(0.6,0.6)$',(.6,.6),xytext=(7,8),textcoords='offset points'))
ax.set(xlim=(-.08,1.12),ylim=(-.08,1.12),xlabel=r'第一目标损失 $f_1$',ylabel=r'第二目标损失 $f_2$',xticks=[0,.5,1],yticks=[0,.5,1],aspect='equal')
ax.legend(loc='lower left',bbox_to_anchor=(.02,.12))
prepare_figure(fig)
for ext in ['pdf','svg','png']:fig.savefig(HERE/('figure.'+ext),dpi=300)
(HERE/'scientific-input.json').write_text(json.dumps({'kind':'Exact finite teaching construction from chapter 4; no measurements, fitting or random inputs','loss_vectors':points.tolist(),'minimization':'both coordinates','support_line':{'alpha':.5,'weighted_value':.5,'equation':'f1+f2=1','meaning':'Auxiliary equal-value line; its intervening points are not feasible candidates'},'nonattainment_proof':'For any alpha in [0,1], min(alpha,1-alpha)<=1/2<3/5, while the third point has weighted loss 3/5','style':style_record()},ensure_ascii=False,indent=2)+'\n')
plt.close(fig)
