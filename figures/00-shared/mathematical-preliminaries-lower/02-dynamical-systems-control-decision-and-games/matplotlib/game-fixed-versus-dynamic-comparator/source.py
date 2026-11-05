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

HEIGHT = 54
PURPOSE = "Show that zero external regret can coexist with a positive gap against a per-round clairvoyant comparator."

def build_figure():
    rounds=np.arange(0,13)
    cumulative_B=rounds//2
    cumulative_P=(rounds+1)//2
    best_fixed=np.minimum(cumulative_B,cumulative_P)
    clairvoyant=np.zeros_like(rounds)
    assert np.all(cumulative_B==best_fixed)
    fig,ax=plt.subplots(figsize=(107/25.4,HEIGHT/25.4))
    fig.subplots_adjust(left=.14,right=.97,bottom=.24,top=.96)
    ax.fill_between(rounds,clairvoyant,cumulative_B,color=s.BLUE_FILL)
    ax.plot(rounds,cumulative_B,color=s.BLUE,marker='o',markersize=2.7)
    ax.plot(rounds,clairvoyant,color=s.GREEN,ls='--',lw=1.1)
    ax.text(3.5,4.65,r'始终 $B$ = 最佳固定行动',color=s.INK)
    ax.text(6,.35,'逐轮先知',color=s.INK)
    ax.hlines([0,6],12,12.85,color=s.STROKE,lw=.6)
    ax.vlines(12.65,0,6,color=s.STROKE,lw=.75)
    s.note(ax.text(12.5,3,'差距 6',rotation=90,va='center',ha='right',color=s.MUTED))
    ax.set(xlim=(0,13.2),ylim=(-.2,6.45),xticks=[0,2,4,6,8,10,12],yticks=[0,2,4,6],xlabel=r'轮数 $K$',ylabel='累计损失')
    return fig,{"loss_vector_odd_rounds":[0,1],"loss_vector_even_rounds":[1,0],"actions":["B","P"],"actual_action":"B every round","K":"integers 0..12 inclusive","actual_cumulative_loss":"floor(K/2)","fixed_B_loss":"floor(K/2)","fixed_P_loss":"ceil(K/2)","best_fixed_cumulative_loss":"floor(K/2)","clairvoyant_rule":"choose B on odd rounds and P on even rounds after knowing the round loss","clairvoyant_cumulative_loss":0,"external_regret":0,"gap_to_clairvoyant_at_K12":6,"data_source":"Existing alternating-loss teaching example in the owning chapter; straight segments only connect discrete observations."}

if __name__ == '__main__':
    save_figure(*build_figure())
