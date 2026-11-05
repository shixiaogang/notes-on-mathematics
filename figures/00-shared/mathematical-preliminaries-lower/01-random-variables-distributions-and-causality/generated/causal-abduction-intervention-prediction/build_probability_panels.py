"""Exact Matplotlib panels on the new, model-emptied schematic.

Every numeric geometry comes from probability-data.json. No source pixels are
erased or flattened: transparent plots are alpha-composited into blank slots.
"""
from pathlib import Path
import os,json
from fractions import Fraction
O=Path(__file__).resolve().parent
ROOT=next(p for p in O.parents if (p/'build.sh').exists())
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'build/figure-proofs/matplotlib-cache'))
import matplotlib
matplotlib.use('Agg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.font_manager import FontProperties
from PIL import Image

def read_data():
    d=json.loads((O/'probability-data.json').read_text())
    for p in d['panels']:
        p['values']=[float(Fraction(x)) for x in p['probabilities']]
        assert sum(Fraction(x) for x in p['probabilities'])==1
        assert all(0<=v<=1 for v in p['values'])
        if 'mean' in p:
            assert sum(float(s)*v for s,v in zip(p['states'],p['values']))==p['mean']
    return d

def draw_panel(d,p):
    w,h=d['plot_width_px'],d['plot_height_px']
    fig=Figure(figsize=(w/100,h/100),dpi=100,facecolor=(0,0,0,0))
    FigureCanvasAgg(fig)
    ax=fig.add_axes([0,0,1,1]);ax.patch.set_alpha(0)
    ax.set_xlim(0,w);ax.set_ylim(-2,h-2)
    bars=ax.bar(p['centers'],[d['shared_probability_height_px']*v for v in p['values']],
        width=56,color=p['colors'],edgecolor=p['colors'],linewidth=0)
    ax.plot([0,w],[0,0],color='#4C4D4F',linewidth=1.0,solid_capstyle='butt')
    ax.axis('off')
    # Actual font files are fixed for any chart labels. The numeric probability
    # labels deliberately live in the shared real-font overlay, not these plots.
    fonts={n:FontProperties(fname=str(ROOT/'fonts'/f)) for n,f in {
       'cn':'SourceHanSansSC-Normal.otf','note':'LXGWWenKai-Regular.ttf',
       'math':'FiraMath-Regular.otf'}.items()}
    assert all(Path(f.get_file()).is_file() for f in fonts.values())
    P=O/'panels';P.mkdir(exist_ok=True)
    matplotlib.rcParams['svg.fonttype']='path'
    matplotlib.rcParams['svg.hashsalt']='causal-exact-probability-panels'
    matplotlib.rcParams['pdf.fonttype']=42
    for fmt in ['png','svg','pdf']:
        metadata={'Date':None} if fmt=='svg' else ({'CreationDate':None,'ModDate':None} if fmt=='pdf' else None)
        fig.savefig(P/(p['id']+'.'+fmt),format=fmt,dpi=100,transparent=True,metadata=metadata)
    expected=[d['shared_probability_height_px']*v for v in p['values']]
    assert [b.get_height() for b in bars]==expected
    return {'panel':p['id'],'data':p['probabilities'],'bar_heights_px':expected,
      'origin':p['origin'],'zero_baseline':True,'scale_px_per_probability':d['shared_probability_height_px'],
      'numeric_labels':'../labels-source.json, actual Fira Math text overlay'}

def main():
    d=read_data();canvas=Image.open(O/'background.png').convert('RGBA');checks=[]
    for p in d['panels']:
        checks.append(draw_panel(d,p))
        panel=Image.open(O/'panels'/(p['id']+'.png')).convert('RGBA')
        assert panel.size==(d['plot_width_px'],d['plot_height_px'])
        canvas.alpha_composite(panel,tuple(p['origin']))
    canvas.save(O/'background-composed.png')
    (O/'panels'/'data-check.json').write_text(json.dumps({'matplotlib':matplotlib.__version__,
        'geometry_source':'probability-data.json','panels':checks,
        'modified_schematic_pixels':'Only alpha compositing of computed data artists into model-emptied slots.'},indent=2))

if __name__=='__main__':main()
