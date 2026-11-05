# -*- coding: utf-8 -*-
"""Analytic stationary OU and probability-flow marginal/covariance comparison."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
import plot_style as st
st.configure()
import matplotlib as mpl
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent
SIZE_MM=(107,68)
def load_data():
    x=np.linspace(-3.5,3.5,401);t=np.linspace(0,3,401)
    return x,np.exp(-x*x/2)/np.sqrt(2*np.pi),t,np.exp(-t),np.ones_like(t)
def validate_data(x,p,t,cov_sde,cov_ode):
    assert np.all(np.isfinite(p)) and np.all(p>0)
    assert p[200]==np.max(p) and np.isclose(cov_sde[0],1)
    assert np.all(np.diff(cov_sde)<0) and np.all(cov_ode==1)
def build_figure(x,p,t,cov_sde,cov_ode):
    fig,axes=plt.subplots(1,2,figsize=np.array(SIZE_MM)/25.4)
    fig.subplots_adjust(left=.13,right=.97,bottom=.24,top=.77,wspace=.60)
    ax=axes[0]
    ax.plot(x,p,color=st.BLUE,lw=1.1,label='OU扩散')
    ax.plot(x,p,color=st.GREEN,lw=1.1,ls='--',label='概率流ODE')
    ax.set(xlim=(-3.5,3.5),ylim=(0,.43),xlabel=r'状态 $x$',ylabel=r'密度 $p_t(x)$')
    ax.set_xticks([-3,0,3]);ax.set_yticks([0,.2,.4])
    ax.set_title('所有时刻的共同边缘',pad=7)
    ax.text(.5,.08,r'$\mathcal{N}(0,1)$',transform=ax.transAxes,ha='center')
    ax=axes[1]
    ax.plot(t,cov_sde,color=st.BLUE,lw=1.1)
    ax.plot(t,cov_ode,color=st.GREEN,lw=1.1,ls='--')
    ax.set(xlim=(0,3),ylim=(0,1.08),xlabel=r'时差 $t$',ylabel=r'$\operatorname{Cov}(X_0,X_t)$')
    ax.set_xticks([0,1,2,3]);ax.set_yticks([0,.5,1]);ax.set_title('不同的跨时依赖',pad=7)
    ax.text(1.8,.27,r'$\mathrm{e}^{-t}$',color=st.INK)
    ax.text(2.3,.88,r'$1$',color=st.INK)
    fig.legend(*axes[0].get_legend_handles_labels(),loc='upper center',ncol=2,bbox_to_anchor=(.51,1),columnspacing=1.4,handlelength=2.2)
    return fig
def save_figure(fig,x,p,t,cov_sde,cov_ode):
    st.prepare_figure(fig)
    fig.savefig(OUT/'figure.pdf');fig.savefig(OUT/'figure.svg');fig.savefig(OUT/'figure.png',dpi=400)
    np.savetxt(OUT/'data.csv',np.column_stack([x,p,t,cov_sde,cov_ode]),delimiter=',',header='state,common_density,time_lag,covariance_ou,covariance_flow',comments='')
    parameters={'origin':'analytic dimensionless teaching model, not empirical data','sde':'dX=-X dt+sqrt(2) dW','initial':'X0~N(0,1), independent of driving Brownian W; stationary','density':'p_t(x)=exp(-x*x/2)/sqrt(2*pi) for all t','score':'-x','diffusion_covariance':2,'probability_flow':'v=-x-(2/2)*(-x)=0; X_t=X_0','cross_time_covariance':{'sde':'exp(-t)','ode':'1'},'domains':{'density_x':[-3.5,3.5],'time_lag':[0,3]},'uniform_evaluation_points':401}
    meta={'title':'相同边缘密度与不同跨时依赖','created':'2026-10-17','method':'Matplotlib analytic teaching figure',
      'physical_size_mm':SIZE_MM,'latex_width_mm':107,'inclusion_scale':1,'main_font_pt':8,'note_font_pt':7.5,'png_dpi':400,'parameters':parameters,
      'data_gate':{'filtering':'none','missing_values':'none','random_sampling':'none','density_fitting':'none; exact Gaussian formula','aggregation':'none'},
      'font_versions':json.loads((ROOT/'figures/00-shared/academic-drawing/font-manifest.json').read_text()),
      'font_license_files':['fonts/licenses/SourceHanSans-OFL.txt','fonts/licenses/LXGWWenKai-OFL.txt','fonts/licenses/FiraMath-font-license.txt','fonts/licenses/STIX-OFL.txt'],
      'style':st.style_record(),'software':{'python':sys.version.split()[0],'numpy':np.__version__,'matplotlib':mpl.__version__},
      'hashes':{f:hashlib.sha256((OUT/f).read_bytes()).hexdigest() for f in ['source.py','data.csv','figure.pdf','figure.svg','figure.png']},
      'validation':'Same analytic marginal for both processes; exact covariance formulas differ.',
      'review':'Independent export reviewed by writer; final book-page review pending root build.'}
    (OUT/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
    data=load_data();validate_data(*data);fig=build_figure(*data);save_figure(fig,*data)
