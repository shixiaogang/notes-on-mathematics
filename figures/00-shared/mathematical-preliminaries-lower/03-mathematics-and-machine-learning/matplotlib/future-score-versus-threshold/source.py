"""Reproduce an analytic teaching figure from the adjacent chapter; no samples."""
from pathlib import Path
import sys,json,hashlib
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file())
D=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
import plot_style as style
style.configure()
from fontTools.ttLib import TTFont
import numpy as np
import matplotlib.pyplot as plt
SPEC=json.loads((D/'parameters.json').read_text())

def build_figure():
    fig,axs=plt.subplots(1,2,figsize=(108/25.4,56/25.4))
    fig.subplots_adjust(left=.125,right=.94,bottom=.235,top=.87,wspace=.48)
    a,b=axs
    if SPEC['kind']=='infimum':
        x=np.linspace(0,5,501);ks=np.array([1,2,4,8,16,64,128])
        a.plot(x,np.exp(-x),color=style.BLUE)
        a.scatter(np.log(ks),1/ks,s=13,facecolor='white',edgecolor=style.BLUE,zorder=3)
        a.axhline(0,color=style.MUTED,ls=':',lw=.6)
        a.set(xlim=(-.15,5.1),ylim=(-.03,1.08),xlabel='$x$',ylabel='$f(x)$',title='目标下确界未达到')
        a.set_xticks([0,2,4]);a.set_yticks([0,.5,1])
        k=np.arange(1,129)
        b.plot(k,np.log(k),color=style.GREEN,label='$x_k=\\log k$')
        b.set(xlim=(1,128),ylim=(0,5.1),xlabel='$k$',ylabel='$x_k$',title='变量继续增大')
        b.set_xticks([1,64,128]);b.set_yticks([0,2,4])
        a.text(.47,.73,'$f(x)=e^{-x}$',transform=a.transAxes,fontsize=8)
        b.text(.12,.22,'$x_k=\\log k$',transform=b.transAxes,fontsize=8)
    elif SPEC['kind']=='threshold':
        eps=SPEC['epsilon'];x=np.linspace(-.2,.2,401)
        a.plot(x,x,color=style.BLUE)
        a.scatter([-eps,eps],[-eps,eps],s=16,color=[style.BLUE,style.GREEN],zorder=3)
        a.axhline(0,ls=':',color=style.MUTED,lw=.6);a.axvline(0,ls=':',color=style.MUTED,lw=.6)
        a.set(xlim=(-.2,.2),ylim=(-.2,.2),xlabel='$x$',ylabel='$s(x)$',title='连续评分')
        a.set_xticks([-.2,0,.2]);a.set_yticks([-.2,0,.2])
        a.text(.13,.77,'$s(x)=x$',transform=a.transAxes,fontsize=8)
        b.plot([-.2,0],[0,0],color=style.BLUE);b.plot([0,.2],[1,1],color=style.GREEN,ls='--')
        b.plot(0,0,'o',mfc='white',mec=style.STROKE,ms=4);b.plot(0,1,'o',color=style.STROKE,ms=4)
        b.scatter([-eps,eps],[0,1],s=16,color=[style.BLUE,style.GREEN],zorder=3)
        b.axvline(0,ls=':',color=style.MUTED,lw=.6)
        b.set(xlim=(-.2,.2),ylim=(-.18,1.22),xlabel='$x$',ylabel='$a(x)$',title='阈值决策')
        b.set_xticks([-.2,0,.2]);b.set_yticks([0,1])
    elif SPEC['kind']=='reweighting':
        x=np.linspace(-3,3,601);p=np.exp(-x*x/2)/np.sqrt(2*np.pi);q=np.exp(-(x-1)**2/2)/np.sqrt(2*np.pi)
        a.plot(x,p,color=style.BLUE,label='$p_{\\mathrm{s}}$')
        a.plot(x,q,color=style.GREEN,ls='--',label='$p_{\\mathrm{t}}$')
        a.set(xlim=(-3,3),ylim=(0,.47),xlabel='$x$',ylabel='概率密度',title='来源与目标')
        a.set_xticks([-3,0,3]);a.set_yticks([0,.2,.4]);a.legend(loc='upper left',handlelength=1.15,handletextpad=.35,borderaxespad=0)
        b.plot(x,np.exp(x-.5),color=style.BLUE)
        b.axhline(1,color=style.MUTED,ls=':',lw=.6)
        b.set(xlim=(-3,3),ylim=(0,13),xlabel='$x$',ylabel='$w(x)$',title='密度比权重')
        b.set_xticks([-3,0,3]);b.set_yticks([0,1,6,12])
        b.text(.06,.78,'$e^{x-1/2}$',transform=b.transAxes,fontsize=8)
    return fig

def main():
    fig=build_figure();style.prepare_figure(fig)
    for ext in ['pdf','png','svg']:
        kw={'dpi':220}
        if ext=='pdf':kw['metadata']={'CreationDate':None,'ModDate':None}
        fig.savefig(D/('figure.'+ext),**kw)
    record={'route':'Matplotlib analytic figure','parameters':SPEC,'source':'adjacent chapter equations, constructed teaching illustration; not empirical data','physical_size_mm':[108,56],'body_reference_width_mm':108,'scale':1,'style':style.style_record(),'font_licenses':['fonts/licenses/SourceHanSans-OFL.txt','fonts/licenses/LXGWWenKai-OFL.txt','fonts/licenses/FiraMath-font-license.txt','fonts/licenses/STIX-OFL.txt'],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'random_sampling':False,'font_versions':{p.name:TTFont(p)['name'].getDebugName(5) for p in [style.CN_FILE,style.NOTE_FILE,style.EN_FILE,style.STIX_FILE]},'standalone_review':'Root inspected actual PNG and independent agent checked analytic semantics; final book review is recorded separately.','status':'rendered; root will verify final book pages'}
    (D/'metadata.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');plt.close(fig)
if __name__=='__main__':main()
