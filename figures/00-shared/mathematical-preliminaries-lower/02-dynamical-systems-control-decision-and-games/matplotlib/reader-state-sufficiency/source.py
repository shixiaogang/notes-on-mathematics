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
    A=np.array([[.8,.1],[.1,.9]])
    states=[]
    for wall in [2.,-2.]:
        z=np.empty((16,2)); z[0]=[0.,wall]
        for t in range(15): z[t+1]=A@z[t]+[.4,0.]
        states.append(z)
    return np.arange(16),states

def build_figure(t, states):
    fig,ax=plt.subplots(figsize=np.array(SIZE_MM)/25.4)
    fig.subplots_adjust(left=.145,right=.97,bottom=.22,top=.95)
    for z,color,ls,marker,label in zip(states,[style.BLUE,style.GREEN],['-','--'],['o','s'],[r'$h_0=2$',r'$h_0=-2$']):
        ax.plot(t,z[:,0],color=color,ls=ls,marker=marker,ms=3,markevery=2,label=label)
    ax.set(xlabel=r'系统时间 $t$',ylabel=r'房间温差 $x_t$',xlim=(-.2,15.3),ylim=(-.1,3.4))
    ax.set_xticks([0,5,10,15]);ax.set_yticks([0,1,2,3]);ax.legend(loc='upper left')
    style.note(ax.annotate(r'同一 $x_0=0$',xy=(0,0),xytext=(2.7,.35),arrowprops={'arrowstyle':'->','color':style.STROKE,'lw':.6},color=style.MUTED))
    ax.grid(axis='y')
    return fig

def main():
    t,z=load_data(); assert z[0][0,0]==z[1][0,0] and not np.isclose(z[0][1,0],z[1][1,0])
    fig=build_figure(t,z)
    save(fig,np.column_stack([t,z[0],z[1]]),{'A':[[.8,.1],[.1,.9]],'constant_input':[.4,0.], 'initial_states':[[0,2],[0,-2]],'steps':15,'formula':'z[t+1]=A z[t]+(0.4,0); z=(room x,wall h)', 'csv_columns':'t,x_wall_positive,h_wall_positive,x_wall_negative,h_wall_negative'},'室温单坐标不足以确定未来')
if __name__=='__main__': main()
