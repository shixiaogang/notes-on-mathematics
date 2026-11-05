"""Reproducible analytic teaching figure; no sampled experimental data."""
from pathlib import Path
import sys, json, hashlib
import numpy as np
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
import plot_style as style
style.configure()
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ft2font
OUT=Path(__file__).resolve().parent
SIZE_MM=(107,56)
def save(fig, data, parameters, purpose):
    style.prepare_figure(fig)
    fig.savefig(OUT/'figure.pdf')
    fig.savefig(OUT/'figure.png',dpi=220)
    np.savetxt(OUT/'data.csv',data,delimiter=',',header=parameters.pop('csv_columns'),comments='')
    font_versions={}
    for name in style.style_record()['font_sha256']:
        records=ft2font.FT2Font(str(ROOT/'fonts'/name)).get_sfnt()
        versions=[v.decode('utf-16-be',errors='replace') if k[0]==3 else v.decode('latin1',errors='replace') for k,v in records.items() if k[-1]==5]
        font_versions[name]=list(dict.fromkeys(versions))
    meta={
      'title':purpose,'created':'2026-10-17','source_type':'analytic teaching example, not empirical experiment',
      'generator':'source.py','generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'software':{'python':sys.version.split()[0],'numpy':np.__version__,'matplotlib':mpl.__version__},'font_versions':font_versions,'data_file':'data.csv','parameters':parameters,
      'data_gate':{'filtering':'none','missing_values':'none','outliers':'not applicable','random_sampling':'none','aggregation':'only explicitly given analytic moment formulas'},
      'physical_size_mm':SIZE_MM,'latex_width_mm':107,'scale_at_inclusion':1.0,
      'main_font_pt':8,'note_font_pt':7.5,'style_record':style.style_record(),
      'font_license_files':['fonts/licenses/SourceHanSans-OFL.txt','fonts/licenses/LXGWWenKai-OFL.txt','fonts/licenses/FiraMath-font-license.txt','fonts/licenses/STIX-OFL.txt'],
      'outputs':{name:hashlib.sha256((OUT/name).read_bytes()).hexdigest() for name in ['figure.pdf','figure.png','data.csv']},
      'review':{'independent_export':'recorded in reviews/vol2-add-figures-20261017/ch4-5-figures.json; not automatically certified','book_page':'delegated to root after final book build'}
    }
    (OUT/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    plt.close(fig)

def load_data():
    t=np.linspace(0,2*np.pi,501);q0,p0=.9,.7
    return t,np.column_stack([q0*np.cos(t)+p0*np.sin(t),p0*np.cos(t)-q0*np.sin(t)]),np.column_stack([q0*np.exp(-t),p0*np.exp(-t)])

def build_figure(t,h,g):
    fig,axes=plt.subplots(1,2,figsize=np.array(SIZE_MM)/25.4)
    fig.subplots_adjust(left=.09,right=.97,bottom=.22,top=.84,wspace=.34)
    theta=np.linspace(0,2*np.pi,361)
    for ax,traj,title,color in zip(axes,[h,g],['Hamilton演化','梯度下降'],[style.BLUE,style.GREEN]):
        for radius in [.4,.8,np.sqrt(1.3)]:
            ax.plot(radius*np.cos(theta),radius*np.sin(theta),color=style.GRID,lw=.6,ls=':')
        ax.plot(traj[:,0],traj[:,1],color=color)
        ax.scatter([.9],[.7],s=13,color=color,zorder=4)
        idx=48 if ax is axes[0] else 30
        ax.annotate('',xy=traj[idx+12],xytext=traj[idx],arrowprops={'arrowstyle':'->','color':color,'lw':1.1})
        ax.set(title=title,xlabel=r'位置 $q$',ylabel=r'动量 $p$',xlim=(-1.35,1.35),ylim=(-1.35,1.35),aspect='equal')
        ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.axhline(0,lw=.4,color=style.GRID);ax.axvline(0,lw=.4,color=style.GRID)
    return fig

def main():
    t,h,g=load_data();assert np.max(abs(np.sum(h*h,axis=1)-1.3))<1e-12
    fig=build_figure(t,h,g)
    save(fig,np.column_stack([t,h,g]),{'H':'(q^2+p^2)/2','initial_state':[.9,.7],'time_range':[0,float(2*np.pi)],'samples':501,'Hamilton':'qdot=p,pdot=-q; q=q0 cos(t)+p0 sin(t), p=p0 cos(t)-q0 sin(t)','gradient_descent':'qdot=-q,pdot=-p; (q,p)=exp(-t)(q0,p0)','level_radii':[.4,.8,float(np.sqrt(1.3))],'csv_columns':'t,q_hamilton,p_hamilton,q_gradient,p_gradient'},'Hamilton运动沿能量等值线而非下降方向')
if __name__=='__main__':main()
