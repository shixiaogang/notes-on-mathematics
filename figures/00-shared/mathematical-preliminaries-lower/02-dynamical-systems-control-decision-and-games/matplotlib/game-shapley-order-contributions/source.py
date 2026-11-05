"""Deterministic teaching figure. Run this file from any working directory."""
from pathlib import Path
import hashlib
import importlib.util
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT = next(p for p in Path(__file__).resolve().parents if (p / "build.sh").exists())
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("academic_style", ROOT / "figures/00-shared/academic-drawing/plot_style.py")
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)
s.configure()


def save_figure(fig, parameters):
    s.prepare_figure(fig)
    fig.savefig(HERE / "figure.pdf")
    fig.savefig(HERE / "figure.png", dpi=240)
    record = {
        "creation_date": "2026-10-17",
        "route": "matplotlib",
        "purpose": PURPOSE,
        "data_kind": "deterministic analytic teaching example; no experiment or random sampling",
        "analytic_parameters": parameters,
        "canvas_mm": [107, HEIGHT],
        "body_reference_width_mm": 107,
        "scaling": 1,
        "style_record": s.style_record(),
        "source": str(Path(__file__).relative_to(ROOT)),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "outputs": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in ["figure.pdf", "figure.png"]},
        "replay": "python3 " + str(Path(__file__).relative_to(ROOT)),
        "license": "Original analytic figure for this book; bundled font licenses in fonts/.",
        "visual_review": "pending actual output review"
    }
    (HERE / "generation.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    plt.close(fig)

from itertools import permutations
HEIGHT = 62
PURPOSE = "Connect Shapley coefficients to equal averaging over all joining orders in the existing three-player coalition example."

def build_figure():
    values={frozenset():0,frozenset([1]):1,frozenset([2]):1,frozenset([3]):0,frozenset([1,2]):3,frozenset([1,3]):2,frozenset([2,3]):2,frozenset([1,2,3]):4}
    orders=list(permutations([1,2,3]))
    contributions=[]
    for order in orders:
        prev=frozenset()
        row={}
        for player in order:
            nxt=prev|{player}
            row[player]=values[nxt]-values[prev]
            prev=nxt
        contributions.append([row[i] for i in [1,2,3]])
    data=np.array(contributions)
    assert np.all(data.sum(axis=1)==4)
    assert np.allclose(data.mean(axis=0),[5/3,5/3,2/3])
    fig, (ax,avg)=plt.subplots(1,2,figsize=(107/25.4,HEIGHT/25.4),gridspec_kw={'width_ratios':[1.4,1]})
    fig.subplots_adjust(left=.185,right=.98,bottom=.22,top=.85,wspace=.4)
    cols=[s.BLUE,s.GREEN,s.YELLOW]
    # Segment position follows actual joining order; segment color follows participant.
    for y,(order,row) in enumerate(zip(orders,contributions)):
        left=0
        for player in order:
            amount=row[player-1]
            ax.barh(y,amount,left=left,color=cols[player-1],height=.66)
            if amount:
                ax.text(left+amount/2,y,str(amount),ha='center',va='center',color=s.INK,fontsize=8)
            left+=amount
    ax.set(yticks=range(6),yticklabels=[r'$'+r'\to'.join(map(str,o))+'$' for o in orders],xticks=[0,2,4],xlim=(0,4.1),xlabel='联盟总价值')
    ax.invert_yaxis()
    ax.set_title('六种等权加入顺序',pad=7)
    ax.tick_params(axis='y',length=0)
    means=data.mean(axis=0)
    avg.bar([1,2,3],means,color=cols,width=.65)
    for x,y,label in zip([1,2,3],means,[r'$5/3$',r'$5/3$',r'$2/3$']):
        avg.text(x,y+.08,label,ha='center',va='bottom')
    avg.set(xticks=[1,2,3],xlim=(.4,3.6),ylim=(0,2.05),yticks=[0,1,2],xlabel='参与者',ylabel='平均边际贡献')
    avg.set_title('Shapley 分配',pad=7)
    return fig, {"players":[1,2,3],"coalition_values":{','.join(map(str,sorted(k))):v for k,v in values.items()},"orders":[list(o) for o in orders],"marginal_contributions_by_player":contributions,"probability_each_order":"1/6","shapley":["5/3","5/3","2/3"],"left_segment_order":"actual joining sequence, zero increments have zero width","colors":"participant1 blue; participant2 green; participant3 yellow","data_source":"Existing deterministic three-player teaching example in the owning chapter."}

if __name__ == '__main__':
    save_figure(*build_figure())
