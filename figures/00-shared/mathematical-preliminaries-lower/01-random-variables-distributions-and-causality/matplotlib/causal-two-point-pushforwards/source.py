"""Exact five probability panels for one declared two-point teaching model.
No random sampling, data filtering, smoothing, or model-generated quantitative art.
"""
from pathlib import Path
from fractions import Fraction
import sys,json,hashlib,os
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file())
D=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
import plot_style as style
style.configure()
sys.path.insert(0,str(ROOT/'figures/00-shared/mathematical-generators/matplotlib/redraw-reproduction'))
import instrument_export  # Record real artist data and measured glyph bounds.
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

def load_data():
    return json.loads((D/'probability-data.json').read_text())

def validate_data(data):
    for row in data['panels']:
        q=[Fraction(x) for x in row['probabilities']]
        assert sum(q)==1 and all(x>=0 for x in q)
        if 'mean' in row:
            assert sum(Fraction(x)*p for x,p in zip(row['states'],q))==row['mean']
    prior=list(map(Fraction,data['fact']['prior']))
    likelihood=list(map(Fraction,data['fact']['likelihood']))
    evidence=sum(p*l for p,l in zip(prior,likelihood))
    assert evidence==Fraction(data['fact']['evidence_probability'])
    posterior=[p*l/evidence for p,l in zip(prior,likelihood)]
    panels={row['id']:row for row in data['panels']}
    for key in ['prior-top','prior-bottom','population-bottom']:
        assert list(map(Fraction,panels[key]['probabilities']))==prior
    for key in ['posterior-top','counterfactual-top']:
        assert list(map(Fraction,panels[key]['probabilities']))==posterior
    for key in ['counterfactual-top','population-bottom']:
        assert list(map(int,panels[key]['states']))==data['action_outcomes']
    return data

def build_figure(data):
    fig=plt.figure(figsize=(169/25.4,81/25.4))
    positions={'prior-top':[.07,.62,.15,.25], 'posterior-top':[.345,.62,.15,.25],
      'counterfactual-top':[.795,.62,.15,.25], 'prior-bottom':[.345,.15,.15,.25],
      'population-bottom':[.795,.15,.15,.25]}
    titles={'prior-top':'背景先验','posterior-top':'给定事实的后验',
      'counterfactual-top':'条件反事实','prior-bottom':'沿用背景先验','population-bottom':'总体干预'}
    for row in data['panels']:
        key=row['id']; ax=fig.add_axes(positions[key])
        probs=[float(Fraction(x)) for x in row['probabilities']]
        ax.bar([0,1],probs,width=.46,color=[style.BLUE_FILL,style.GREEN_FILL],
          edgecolor=[style.BLUE,style.GREEN],linewidth=.8)
        ax.set_ylim(0,1);ax.set_xlim(-.6,1.6)
        ax.set_xticks([0,1], [r'$u_{\mathrm{L}}$',r'$u_{\mathrm{H}}$'] if 'prior' in key or 'posterior' in key else ['2','6'])
        ax.set_yticks([0,.5,1]);ax.tick_params(length=2,labelsize=8)
        if key!='prior-top':ax.set_yticklabels([])
        else:ax.set_ylabel('概率',fontsize=8,labelpad=2)
        ax.set_title(titles[key],fontsize=8,pad=6,color=style.INK)
        for x,p,raw in zip([0,1],probs,row['probabilities']):
            ax.text(x,p+.045,r'$\frac{'+raw.split('/')[0]+'}{'+raw.split('/')[1]+'}$',ha='center',va='bottom',fontsize=8)
        if 'mean' in row:
            style.note(ax.text(.5,-.39,f"均值 {row['mean']}",transform=ax.transAxes,ha='center',va='top',fontsize=7.5))
    overlay=fig.add_axes([0,0,1,1],frameon=False);overlay.set_xlim(0,1);overlay.set_ylim(0,1);overlay.axis('off')
    arrow=dict(arrowstyle='-|>',mutation_scale=8,lw=.7,color=style.STROKE)
    overlay.annotate('',xy=(.335,.745),xytext=(.23,.745),arrowprops=arrow)
    overlay.text(.272,.80,'条件化 $S=1$',ha='center',va='center',fontsize=8)
    # A second branch reuses the prior, rather than conditioning on the evidence.
    overlay.annotate('',xy=(.335,.275),xytext=(.23,.61),arrowprops=dict(**arrow,connectionstyle='angle,angleA=-90,angleB=180,rad=4'))
    overlay.text(.272,.46,'沿用先验',ha='center',va='center',fontsize=8)
    for y in [.745,.275]:
        overlay.annotate('',xy=(.575,y),xytext=(.51,y),arrowprops=arrow)
        overlay.annotate('',xy=(.78,y),xytext=(.716,y),arrowprops=arrow)
    box=FancyBboxPatch((.585,.175),.12,.64,boxstyle='round,pad=0.008,rounding_size=0.004',
      facecolor='white',edgecolor=style.BLUE,linewidth=.7)
    overlay.add_patch(box)
    overlay.text(.645,.55,'同一行动映射\n$F_{M,Y}^{a}$',ha='center',va='center',fontsize=8,linespacing=1.7)
    overlay.text(.645,.41,r'$u_{\mathrm{L}}\mapsto 2$'+'\n'+r'$u_{\mathrm{H}}\mapsto 6$',ha='center',va='center',fontsize=8,linespacing=1.7)
    return fig

def save_figure(fig,data):
    out=D
    if os.environ.get('ACADEMIC_PROOF_DIR'):
        out=Path(os.environ['ACADEMIC_PROOF_DIR'])/D.relative_to(ROOT/'figures')
    out.mkdir(parents=True,exist_ok=True)
    style.prepare_figure(fig)
    for suffix in ['pdf','svg','png']:
        kwargs={'dpi':300}
        if suffix=='pdf':kwargs['metadata']={'CreationDate':None,'ModDate':None}
        fig.savefig(out/('figure.'+suffix),**kwargs)
    report={'date':'2026-10-11','scientific_source':'ex:causal-two-point-background-posterior',
      'route':'Matplotlib; exact probabilities and a few qualitative arrows; newly designed vector figure',
      'input_file':'probability-data.json','input_sha256':hashlib.sha256((D/'probability-data.json').read_bytes()).hexdigest(),
      'filtering':None,'sampling':None,'uncertainty':None,'y_limits_common':[0,1],'zero_baseline':True,
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'physical_size_mm':[169,81],'intended_body_width_mm':169,'label_size_pt':{'main':8,'note':7.5},
      'style':style.style_record(),'status':'rendered; independent scientific and actual-size review pending'}
    (out/'render-20261011.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
    data=validate_data(load_data()); fig=build_figure(data);save_figure(fig,data);plt.close(fig)
