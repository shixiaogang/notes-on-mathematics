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

k=np.arange(21);j=np.arange(8)
fig,axs=plt.subplots(1,2,figsize=(112/25.4,58/25.4),layout='constrained')
for q,col,offset in [(0.5,BLUE,-.18),(0.8,GREEN,.18)]:
 axs[0].bar(j+offset,q**(7-j),width=.34,color=col,label=f'$q={q}$')
 axs[1].plot(k,(1-q**k)/(1-q),color=col,label=f'$q={q}$')
 axs[1].axhline(1/(1-q),color=col,ls='--',lw=.6)
axs[0].set(xlabel='$j$',ylabel='对 $e_8$ 的贡献',xticks=[0,3,7],yticks=[0,.5,1]);axs[0].legend(loc='upper left',handlelength=1)
axs[1].set(xlabel='$k$',ylabel='$e_k$',xticks=[0,10,20],yticks=[0,2,5])
for a in axs:a.grid(False)
data=dict(recurrence='e(k+1)=q*e(k)+1; e(0)=0',q=[.5,.8],left_step=8,right_steps=k.tolist(),contribution='q**(7-j)',sum='(1-q**k)/(1-q)')

prepare_figure(fig)
for ext in ['pdf','png','svg']:fig.savefig(OUT/(Path(__file__).stem+'.'+ext),dpi=300)
(OUT/(Path(__file__).stem+'.json')).write_text(json.dumps(dict(style=style_record(),data=data,width_mm=112,height_mm=58,reference_width_mm=112,scale=1,final_label_pt=8),ensure_ascii=False,indent=2)+'\n')
plt.close(fig)
