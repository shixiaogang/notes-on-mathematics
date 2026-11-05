# -*- coding: utf-8 -*-
"""Analytic phase-plane figure: maximum braking and viability."""
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
    d=np.linspace(0,.55,401);v=-np.sqrt(4*d)
    t=np.linspace(0,.5,201);vel=-1+2*t
    return d,v,t,vel,.3-t+t*t,.1-t+t*t
def validate_data(d,v,t,vel,safe,unsafe):
    assert np.allclose(v*v,4*d)
    assert abs(safe[-1]-.05)<1e-12 and abs(unsafe[-1]+.15)<1e-12
    assert np.allclose(vel,-1+2*t)
def build_figure(d,v,t,vel,safe,unsafe):
    fig,ax=plt.subplots(figsize=np.array(SIZE_MM)/25.4)
    fig.subplots_adjust(left=.15,right=.97,bottom=.24,top=.94)
    ax.axvspan(-.185,0,color=st.RED_FILL,zorder=0)
    ax.fill_between(d,-1.55,v,color=st.RED_FILL,zorder=0)
    ax.fill_between(d,v,.22,color=st.GREEN_FILL,zorder=0)
    ax.plot(d,v,color=st.STROKE,lw=1.1)
    ax.axvline(0,color=st.STROKE,lw=.75)
    ax.axhline(0,color=st.GRID,lw=.6)
    ax.plot(safe,vel,color=st.BLUE,lw=1.1)
    ax.plot(unsafe,vel,color=st.RED,lw=1.1,ls='--')
    ax.scatter([.3,.1],[-1,-1],color=[st.BLUE,st.RED],s=19,zorder=4)
    ax.scatter([safe[-1],unsafe[-1]],[0,0],facecolor='white',edgecolor=[st.BLUE,st.RED],s=23,zorder=4)
    for path,color in [(safe,st.BLUE),(unsafe,st.RED)]:
        ax.annotate('',xy=(path[94],vel[94]),xytext=(path[76],vel[76]),
                    arrowprops={'arrowstyle':'-|>','color':color,'lw':.9,'mutation_scale':8})
    ax.annotate(r'$(0.3,-1)$',xy=(.3,-1),xytext=(.35,-.91),ha='left',va='center',fontsize=8,
                arrowprops={'arrowstyle':'-','lw':.6,'color':st.MUTED})
    ax.annotate(r'$(0.1,-1)$',xy=(.1,-1),xytext=(-.17,-1.24),ha='left',va='center',fontsize=8,
                arrowprops={'arrowstyle':'-','lw':.6,'color':st.MUTED})
    ax.text(.32,-.38,'可以制动',ha='center',va='center')
    ax.text(.365,-1.40,'位置允许，制动不足',ha='center',va='center',fontsize=7.5)
    ax.text(-.09,.10,'已越界',ha='center',va='center',fontsize=7.5)
    ax.text(.34,-1.12,r'$v=-\sqrt{4d}$',ha='left',va='center')
    ax.set(xlim=(-.185,.55),ylim=(-1.55,.22),xlabel=r'余距 $d=p-p_{\min}$',ylabel=r'速度 $v$')
    ax.set_xticks([-.15,0,.15,.3,.45]);ax.set_yticks([-1.5,-1,-.5,0])
    return fig
def save_figure(fig,d,v,t,vel,safe,unsafe):
    st.prepare_figure(fig)
    fig.savefig(OUT/'figure.pdf');fig.savefig(OUT/'figure.svg');fig.savefig(OUT/'figure.png',dpi=400)
    np.savetxt(OUT/'boundary.csv',np.column_stack([d,v]),delimiter=',',header='distance_d,min_viable_velocity',comments='')
    np.savetxt(OUT/'trajectories.csv',np.column_stack([t,vel,safe,unsafe]),delimiter=',',header='time,velocity,safe_start_distance,unsafe_start_distance',comments='')
    meta={'title':'位置安全与最大制动可行域','created':'2026-10-17','method':'Matplotlib analytic teaching model',
      'physical_size_mm':SIZE_MM,'latex_width_mm':107,'inclusion_scale':1,'main_font_pt':8,'note_font_pt':7.5,'png_dpi':400,
      'parameters':{'dynamics':'d_dot=v; v_dot=u','input_constraint':'abs(u)<=2','maximum_braking':2,'state_constraint':'d>=0 only; no upper position bound','boundary':'v=-sqrt(4d) for d>=0, v<0','initial_states':[[.3,-1],[.1,-1]],'plotted_control':'u(t)=2 until stopping at t=.5','trajectories':'d(t)=d0-t+t*t; v(t)=-1+2*t','first_crossing_unsafe':'(1-sqrt(.6))/2','stopping_distances':[.05,-.15],'units':'dimensionless teaching model'},
      'data_gate':{'data':'analytic evaluations','filtering':'none','missing':'none','randomness':'none','sampling':'uniform grids; exact equation, no fitted smoothing'},
      'font_versions':json.loads((ROOT/'figures/00-shared/academic-drawing/font-manifest.json').read_text()),
      'font_license_files':['fonts/licenses/SourceHanSans-OFL.txt','fonts/licenses/LXGWWenKai-OFL.txt','fonts/licenses/FiraMath-font-license.txt','fonts/licenses/STIX-OFL.txt'],
      'style':st.style_record(),'software':{'python':sys.version.split()[0],'numpy':np.__version__,'matplotlib':mpl.__version__},
      'hashes':{f:hashlib.sha256((OUT/f).read_bytes()).hexdigest() for f in ['source.py','figure.pdf','figure.svg','figure.png','boundary.csv','trajectories.csv']},
      'validation':'Analytic boundary and endpoints checked; not identified with arbitrary high-order CBF feasible set.',
      'review':'Independent export reviewed by writer; final book-page review pending root build.'}
    (OUT/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
    data=load_data();validate_data(*data);fig=build_figure(*data);save_figure(fig,*data)
