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
    t=np.arange(9);K=np.array([.3,1.6,2.]);return t,K,np.array([(0.8-k)**t for k in K])

def build_figure(t,K,x):
    fig,ax=plt.subplots(figsize=np.array(SIZE_MM)/25.4)
    fig.subplots_adjust(left=.13,right=.97,bottom=.22,top=.75)
    for k,curve,c,ls,m in zip(K,x,[style.BLUE,style.GREEN,style.RED],['-','--','-.'],['o','s','^']):
        ax.plot(t,curve,color=c,ls=ls,marker=m,ms=3,label=rf'$K={k:g},\ 0.8-K={.8-k:g}$')
    ax.set(xlabel=r'系统时间 $t$',ylabel=r'状态 $x_t$',xlim=(-.1,8.2),ylim=(-4.1,4.7))
    ax.set_xticks([0,2,4,6,8]);ax.set_yticks([-4,-2,0,2,4]);ax.axhline(0,color=style.STROKE,lw=.6);ax.grid(axis='y')
    ax.legend(loc='lower left',bbox_to_anchor=(-.025,1.02),ncol=1,fontsize=7.5,labelspacing=.15,handlelength=1.8)
    return fig

def main():
    t,K,x=load_data();fig=build_figure(t,K,x)
    save(fig,np.column_stack([t,x.T]),{'dynamics':'x[t+1]=0.8 x[t]+u[t]','feedback':'u[t]=-K x[t]','initial_state':1,'K':K.tolist(),'closed_loop_modes':(.8-K).tolist(),'formula':'x[t]=(0.8-K)^t','noise':'none','input_constraints':'none','steps':8,'csv_columns':'t,x_K_0p3,x_K_1p6,x_K_2'},'反馈增益增大不保证稳定')
if __name__=='__main__':main()
