"""Exact analytic sensitivity example. No stochastic or measured data.
Local generator replaces the old multi-topic export path, preserving samples.
"""
from pathlib import Path
import sys,json
import numpy as np
import matplotlib.pyplot as plt
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,GREEN
configure();OUT=Path(__file__).parent
eps=np.logspace(-4,-1,121);coeff=1e-4/(np.sqrt(2)*eps);response=np.full_like(eps,5e-5)
fig,ax=plt.subplots(figsize=(112/25.4,75/25.4));fig.subplots_adjust(left=.17,right=.97,bottom=.18,top=.95)
ax.loglog(eps,coeff,color=BLUE,label='系数相对变化');ax.loglog(eps,response,color=GREEN,ls='--',label='响应相对扰动');ax.set(xlim=(1e-4,1e-1),ylim=(1e-5,1),xlabel=r'$\varepsilon$',ylabel='相对变化');ax.legend();ax.grid(False,which='both');prepare_figure(fig)
for ext in ['pdf','png','svg']:fig.savefig(OUT/('figure.'+ext),dpi=300)
(OUT/'data-and-sources.json').write_text(json.dumps({'eta':1e-4,'epsilon':eps.tolist(),'coefficient_change':coeff.tolist(),'response_change':response.tolist(),'formula':'|eta|/(sqrt(2)*epsilon); |eta|/2','style':style_record(),'width_mm':112,'height_mm':75},ensure_ascii=False,indent=2)+'\n')
