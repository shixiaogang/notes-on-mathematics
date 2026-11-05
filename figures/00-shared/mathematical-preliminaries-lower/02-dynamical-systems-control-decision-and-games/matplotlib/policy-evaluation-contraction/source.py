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

HEIGHT = 58
PURPOSE = "Distinguish fixed-policy value iteration from execution and show geometric error decay."

def build_figure():
    k = np.arange(0, 41)
    gamma, value = .9, 10.
    v = value * (1 - gamma ** k)
    err = value * gamma ** k
    fig, axes = plt.subplots(1, 2, figsize=(107/25.4, HEIGHT/25.4))
    fig.subplots_adjust(left=.105, right=.98, bottom=.24, top=.88, wspace=.46)
    a, b = axes
    a.plot(k, v, color=s.BLUE, marker='o', markevery=5, markersize=2.5)
    a.axhline(value, color=s.MUTED, ls='--', lw=.7)
    a.text(8, 10.25, r'$V^pi=10$', fontsize=8)
    a.set(xlim=(0,40), ylim=(0,11.5), xticks=[0,20,40], yticks=[0,5,10], xlabel=r'迭代次数 $k$', ylabel=r'价值 $V^{(k)}$')
    b.semilogy(k, err, color=s.GREEN, marker='s', markevery=5, markersize=2.4)
    b.set(xlim=(0,40), ylim=(.1,15), xticks=[0,20,40], yticks=[.1,1,10], xlabel=r'迭代次数 $k$', ylabel=r'误差 $|V^{(k)}-V^pi|$')
    b.set_yticklabels(['0.1','1','10'])
    b.minorticks_off()
    return fig, {"states":1,"stationary_expected_stage_cost":1,"gamma":gamma,"V0":0,"Vpi":value,"iteration":"V[k+1]=1+0.9 V[k]","V[k]":"10*(1-0.9**k)","absolute_error":"10*0.9**k","k":"integers 0..40 inclusive","right_axis":"logarithmic y scale"}

if __name__ == '__main__':
    save_figure(*build_figure())
