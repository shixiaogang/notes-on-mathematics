from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# b=0；A: N(-0.1,0.1^2)；B: N(0.5,1)
b0=0.0; cand=[(-.1,.1,'候选 A',-.75,.75),(.5,1.,'候选 B',-3.,4.)]
fig,axs=figure(width_mm=112,height_mm=46,ncols=2)
for i,(ax,(m_,s_,nm,lo,hi)) in enumerate(zip(axs,cand)):
    v=np.linspace(lo,hi,500);p=np.exp(-.5*((v-m_)/s_)**2)/(s_*np.sqrt(2*np.pi))
    ax.fill_between(v[v<b0],0,p[v<b0],color=GREEN_FILL,lw=0)
    ax.plot(v,p,color=BLUE,lw=1.4);ax.axvline(b0,color=STROKE,lw=1.3)
    ax.text(b0,p.max()*1.08,'$b_t$',ha='center',va='bottom')
    ax.set_xlim(lo,hi);ax.set_ylim(0,p.max()*1.25);ax.set_yticks([])
    axes_style(ax,'$F(x)$',None);panel_label(ax,'(%s)'%'ab'[i],-.3)
FACTS={'A':[-.1,.1],'B':[.5,1.0],'b':0}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
