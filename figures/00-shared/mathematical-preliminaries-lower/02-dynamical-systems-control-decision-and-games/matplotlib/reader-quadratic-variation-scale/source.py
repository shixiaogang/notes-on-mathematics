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
    n=2.**np.arange(11)
    return n,np.ones_like(n),np.sqrt(2/n),1/n

def build_figure(n,mean,rms,smooth):
    fig,ax=plt.subplots(figsize=np.array(SIZE_MM)/25.4)
    fig.subplots_adjust(left=.15,right=.97,bottom=.24,top=.88)
    ax.loglog(n,mean,'-',color=style.BLUE,marker='o',ms=2.5)
    ax.loglog(n,rms,'--',color=style.GREEN,marker='s',ms=2.5)
    ax.loglog(n,smooth,':',color=style.PURPLE,marker='^',ms=2.5)
    ax.text(28,1.14,'Brownian平方和均值',color=style.INK,va='bottom')
    ax.annotate('Brownian均方根偏差',xy=(256,np.sqrt(2/256)),xytext=(40,.37),color=style.INK,va='bottom',arrowprops={'arrowstyle':'-','color':style.STROKE,'lw':.6})
    ax.annotate('光滑路径平方和',xy=(128,1/128),xytext=(4,.0025),color=style.INK,va='bottom',arrowprops={'arrowstyle':'-','color':style.STROKE,'lw':.6})
    ax.set(xlabel=r'等分区间数 $n$',ylabel='平方增量累计量',xlim=(1,1600),ylim=(6e-4,2))
    ax.set_xticks([1,16,256,1024],labels=['1','16','256','1024']);ax.grid(which='major')
    return fig

def main():
    n,mean,rms,smooth=load_data();assert np.allclose(rms*rms,2/n)
    fig=build_figure(n,mean,rms,smooth)
    save(fig,np.column_stack([n,mean,rms,smooth]),{'time_interval':[0,1],'n':[int(x) for x in n], 'Brownian_mean':'E[sum_i (Delta W_i)^2]=1','Brownian_rms_deviation':'||sum_i (Delta W_i)^2 -1||_L2=sqrt(2/n)','smooth_path':'a(t)=t; sum_i (Delta a_i)^2=1/n','statistical_note':'exact moments, no Brownian paths sampled; RMS deviation is neither confidence band nor mean trajectory','csv_columns':'n,Brownian_square_sum_mean,Brownian_square_sum_RMS_deviation,smooth_square_sum'},'Brownian平方增量累计不随网格缩小而消失')
if __name__=='__main__':main()
