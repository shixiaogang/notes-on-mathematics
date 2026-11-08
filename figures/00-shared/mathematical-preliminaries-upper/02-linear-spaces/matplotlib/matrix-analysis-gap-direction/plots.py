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

gamma=np.logspace(-3,0,81);eps=.02
delta=eps**2/(np.hypot(gamma/2,eps)+gamma/2);theta=.5*np.degrees(np.arctan2(2*eps,gamma))
fig,axs=plt.subplots(1,2,figsize=(112/25.4,58/25.4),layout='constrained')
axs[0].semilogx(gamma,delta,color=BLUE);axs[0].axhline(eps,color=MUTED,ls='--',lw=.7)
axs[0].set(xlim=(1e-3,1),ylim=(0,.022),xlabel=r'$\gamma$',ylabel=r'$\Delta\lambda_{\max}$',yticks=[0,.01,.02])
axs[1].semilogx(gamma,theta,color=GREEN);axs[1].set(xlim=(1e-3,1),ylim=(0,49),xlabel=r'$\gamma$',ylabel=r'$\theta$（度）',yticks=[0,15,30,45])
for ax in axs:ax.grid(False)
prepare_figure(fig)
for ext in ['pdf','png','svg']:fig.savefig(OUT/('figure.'+ext),dpi=300)
(OUT/'data-and-sources.json').write_text(json.dumps(dict(epsilon=eps,gamma=gamma.tolist(),eigenvalue_increment=delta.tolist(),angle_degrees=theta.tolist(),formula='delta=sqrt((gamma/2)^2+eps^2)-gamma/2; theta=atan2(2eps,gamma)/2',style=style_record(),width_mm=112,height_mm=58,reference_width_mm=112,scale=1,source='plots.py'),ensure_ascii=False,indent=2)+'\n')
plt.close(fig)
