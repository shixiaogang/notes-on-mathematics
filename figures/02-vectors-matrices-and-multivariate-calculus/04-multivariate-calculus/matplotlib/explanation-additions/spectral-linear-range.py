from pathlib import Path
import sys,json,os
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'build/refresh-v2-mpl'))
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,GREEN,RED,MUTED,BLUE_FILL
configure()
import numpy as np
import matplotlib.pyplot as plt
OUT=Path(__file__).parent

r=np.linspace(-1.5,1.5,401);theta=.5*np.arctan(2*r)
fig,ax=plt.subplots(figsize=(112/25.4,58/25.4),layout='constrained')
ax.plot(r,theta,color=BLUE,label='实际转角');ax.plot(r,r,color=GREEN,ls='--',label='一阶预测')
ax.set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),xlabel=r'$t/\gamma$',ylabel=r'$\theta$（弧度）',xticks=[-1.5,0,1.5],yticks=[-1.5,0,1.5]);ax.grid(False);ax.legend(loc='upper left')
ax.scatter([0],[0],s=14,color=MUTED,zorder=4)
data=dict(ratio=r.tolist(),actual_angle=theta.tolist(),first_order=r.tolist(),formula='theta=atan(2t/gamma)/2',gamma='any positive')

prepare_figure(fig)
for ext in ['pdf','png','svg']:fig.savefig(OUT/(Path(__file__).stem+'.'+ext),dpi=300)
(OUT/(Path(__file__).stem+'.json')).write_text(json.dumps(dict(style=style_record(),data=data,width_mm=112,height_mm=58,reference_width_mm=112,scale=1,final_label_pt=8),ensure_ascii=False,indent=2)+'\n')
plt.close(fig)
