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
PURPOSE = "Show why discounted occupancy depends on the initial state and differs from an invariant distribution."

def build_figure():
    gamma = np.linspace(0,.999,1000)
    d0, d1 = 1/(1+gamma), gamma/(1+gamma)
    fig, ax = plt.subplots(figsize=(107/25.4, HEIGHT/25.4))
    fig.subplots_adjust(left=.16, right=.97, bottom=.24, top=.95)
    ax.plot(gamma,d0,color=s.BLUE)
    ax.plot(gamma,d1,color=s.GREEN,ls='--')
    ax.axhline(.5,color=s.MUTED,lw=.7,ls=':')
    ax.scatter([1],[.5],facecolors='white',edgecolors=s.STROKE,s=18,zorder=5)
    ax.text(.13,.9,r'状态 $s_0$',color=s.INK)
    ax.text(.08,.27,r'状态 $s_1$',color=s.INK)
    s.note(ax.text(.08,.54,'平稳分布的质量均为 1/2',fontsize=7.5,color=s.MUTED))
    ax.set(xlim=(0,1.025),ylim=(0,1.02),xticks=[0,.2,.4,.6,.8,1],yticks=[0,.25,.5,.75,1],xlabel=r'折扣因子 $\gamma$',ylabel=r'归一化占用质量 $d_\pi(s)$')
    return fig, {"states":["s0","s1"],"actions_per_state":1,"transition_matrix":[[0,1],[1,0]],"initial_distribution":[1,0],"gamma_domain":"[0,1)","d_pi(s0)":"(1-gamma)*sum_{j>=0}gamma**(2*j)=1/(1+gamma)","d_pi(s1)":"(1-gamma)*sum_{j>=0}gamma**(2*j+1)=gamma/(1+gamma)","invariant_distribution":[.5,.5],"sampling":"1000 equally spaced gamma points from 0 to 0.999; open endpoint at gamma=1 is a limit only","note":"The state distribution alternates and does not converge from this initial state, although an invariant distribution exists."}

if __name__ == '__main__':
    save_figure(*build_figure())
