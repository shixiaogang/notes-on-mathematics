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
    t=np.arange(7);return t,.8**t,.3**t

def build_figure(t,a,b):
    fig,axes=plt.subplots(1,2,figsize=np.array(SIZE_MM)/25.4,sharex=True,sharey=True)
    fig.subplots_adjust(left=.12,right=.97,bottom=.23,top=.82,wspace=.22)
    for ax,second,title in zip(axes,[b,a],['不同衰减率','相同衰减率']):
        ax.plot(t,a,'-',color=style.BLUE,lw=1.1)
        ax.plot(t,second,'--',color=style.GREEN,marker='o',mfc='white',mec=style.GREEN,ms=3)
        ax.set(title=title,xlabel=r'系统时间 $t$',xlim=(-.1,6.2),ylim=(-.04,1.08))
        ax.set_xticks([0,2,4,6]);ax.set_yticks([0,.5,1]);ax.grid(axis='y')
    axes[0].set_ylabel(r'无输入读数 $y_t$')
    axes[0].text(2.1,.78,r'$\mathbf{x}_0=(1,0)^\top$',color=style.INK,fontsize=7.5)
    axes[0].text(2.6,.2,r'$\mathbf{x}_0=(0,1)^\top$',color=style.INK,fontsize=7.5)
    style.note(axes[1].text(1.3,.73,'两条读数重合',color=style.MUTED))
    return fig

def main():
    t,a,b=load_data();fig=build_figure(t,a,b)
    save(fig,np.column_stack([t,a,b,a]),{'C':[[1,1]],'initial_states':[[1,0],[0,1]],'input':'zero','noise':'none','left_A':[[.8,0],[0,.3]],'right_A':[[.8,0],[0,.8]],'formula':'left y=0.8^t or 0.3^t; right both y=0.8^t','steps':6,'csv_columns':'t,y_left_x0_10,y_left_x0_01,y_right_both'},'相同当前读数不等于不可观测')
if __name__=='__main__':main()
