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

t=np.linspace(-1,1,401)
fig,axs=plt.subplots(1,2,figsize=(112/25.4,58/25.4),layout='constrained')
axs[0].plot(t,t,color=BLUE);axs[0].plot(t,-t,color=GREEN,ls='--')
axs[0].text(.7,.55,'$t$',color=BLUE);axs[0].text(.7,-.6,'$-t$',color=GREEN)
axs[1].plot(t,np.abs(t),color=BLUE);axs[1].text(.48,.7,'$|t|$',color=BLUE)
for a in axs:
 a.set(xlim=(-1.05,1.05),ylim=(-1.05,1.1),xlabel='$t$',ylabel=r'$\lambda$',xticks=[-1,0,1],yticks=[-1,0,1]);a.grid(False)
 a.axhline(0,color=MUTED,lw=.5);a.axvline(0,color=MUTED,lw=.5)
data=dict(matrix='diag(t,-t)',domain=[-1,1],samples=401,sorted_max='abs(t)',unsorted=['t','-t'])

prepare_figure(fig)
for ext in ['pdf','png','svg']:fig.savefig(OUT/(Path(__file__).stem+'.'+ext),dpi=300)
(OUT/(Path(__file__).stem+'.json')).write_text(json.dumps(dict(style=style_record(),data=data,width_mm=112,height_mm=58,reference_width_mm=112,scale=1,final_label_pt=8),ensure_ascii=False,indent=2)+'\n')
plt.close(fig)
