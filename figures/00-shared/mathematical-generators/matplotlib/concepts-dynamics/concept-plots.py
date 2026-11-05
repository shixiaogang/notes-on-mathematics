"""Reproduce five analytic teaching figures; no sampled or experimental data.

Run with Python, NumPy and Matplotlib installed. All assets are relative to this
file, so no machine-specific runtime, font or dependency path is required.
"""
from pathlib import Path
import hashlib
import json
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Polygon
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
sys.path.insert(0, str(ROOT / 'figures/00-shared/mathematical-generators/matplotlib'))
from plot_style import configure, prepare_figure, style_record

configure()
CHAPTER_DIR = Path("tex/01-mathematical-preliminaries")
BLUE, RED, YELLOW = "#7998AD", "#D57B70", "#D6B35D"
INK, STROKE, GREY, GRID = "#222222", "#4C4D4F", "#747A80", "#C8CDCF"


def axes_style(ax, grid=True):
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(length=3)
    ax.set_axisbelow(True)
    if grid:
        ax.grid(axis="y")


def save(fig, name, width, height, chapter, question, formulas, data, sampling):
    prepare_figure(fig)
    outputs = {}
    for ext in ("pdf", "svg", "png"):
        file = asset_path(HERE, f"{name}.{ext}")
        fig.savefig(file, dpi=300, facecolor="white")
        outputs[ext] = {"file": str(file.relative_to(ROOT)),
                        "sha256": hashlib.sha256(file.read_bytes()).hexdigest()}
    source = CHAPTER_DIR / chapter
    record = {
        "figure": name, "date": "2026-10-06", "generator": "concept-plots.py",
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "purpose": question, "kind": "analytic teaching construction; not observed data",
        "source": {"file": str(source), "sha256": hashlib.sha256((ROOT / source).read_bytes()).hexdigest()},
        "formulas": formulas, "parameters_and_constructed_data": data,
        "sampling_and_processing": sampling, "size_mm": [width, height],
        "fonts": {"Chinese": "fonts/LXGWWenKai-Regular.ttf", "Western": "fonts/SourceSans3-Regular.otf",
                  "Mathematics": "Matplotlib STIX",
                  "mixed_text": "Western first with per-glyph fallback; Chinese first for Chinese/mathtext spans"},
        "palette": {"two_series": [BLUE, RED], "single_series": YELLOW,
                    "text": INK, "neutral": GREY},
        "style": style_record(),
        "style_helper_sha256": hashlib.sha256((ROOT / 'figures/00-shared/mathematical-generators/matplotlib/plot_style.py').read_bytes()).hexdigest(),
        "software": {"Matplotlib": matplotlib.__version__, "NumPy": np.__version__},
        "outputs": outputs,
        "validation": {"analytic": "Assertions in generator passed",
                       "visual": "See validation.json for inspected output hashes",
                       "scope": "No TeX compilation or embedded book-page inspection, at user request"},
    }
    (asset_path(HERE, f"{name}.json")).write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    plt.close(fig)


def amplitude_phase():
    n = np.arange(8)
    x = np.cos(2 * np.pi * n / 8)
    z = np.roll(x, 2)
    xf, zf = np.fft.fft(x), np.fft.fft(z)
    nonzero = np.array([1, 7])
    assert np.allclose(np.abs(xf), np.abs(zf))
    assert np.allclose(np.abs(xf[nonzero]), [4, 4])
    assert np.allclose(np.delete(xf, nonzero), 0)
    assert np.allclose(np.angle(zf[nonzero]), [-np.pi / 2, np.pi / 2])
    fig = plt.figure(figsize=(169 / 25.4, 84 / 25.4))
    gs = fig.add_gridspec(2, 2, left=.075, right=.975, bottom=.16, top=.91,
                          hspace=.63, wspace=.26)
    time_ax = fig.add_subplot(gs[0, :])
    mag_ax = fig.add_subplot(gs[1, 0])
    phase_ax = fig.add_subplot(gs[1, 1])
    for ax in (time_ax, mag_ax, phase_ax):
        axes_style(ax)
    time_ax.plot(n, x, "o-", color=BLUE, ms=3.4, label="原序列 x")
    time_ax.plot(n, z, "s--", color=RED, ms=3.2, label="右移两格 z")
    time_ax.set(xlim=(-.2, 7.2), ylim=(-1.25, 1.65), xticks=n,
                yticks=[-1, 0, 1], xlabel="离散位置 n", ylabel="信号值")
    time_ax.legend(loc="upper right", ncols=2, handlelength=1.8)
    time_ax.set_title("离散波形", pad=4)
    for offset, values, color, label in [(-.14, xf, BLUE, "x"), (.14, zf, RED, "z")]:
        mag_ax.bar(n + offset, np.abs(values), width=.25, color=color, label=label)
    mag_ax.set(xlim=(-.45, 7.45), ylim=(0, 4.9), xticks=n, yticks=[0, 2, 4],
               xlabel="频率索引 k", ylabel="系数幅度")
    mag_ax.set_title("幅度", pad=4)
    mag_ax.legend(loc="upper center", ncols=2)
    phase_ax.scatter(nonzero - .1, np.angle(xf[nonzero]), marker="o", s=24, color=BLUE, label="x")
    phase_ax.scatter(nonzero + .1, np.angle(zf[nonzero]), marker="s", s=22, color=RED, label="z")
    phase_ax.set(xlim=(-.45, 7.45), ylim=(-2.15, 2.15), xticks=n,
                 yticks=[-np.pi / 2, 0, np.pi / 2],
                 yticklabels=[r"$-\pi/2$", "0", r"$\pi/2$"],
                 xlabel="频率索引 k", ylabel="相位（弧度）")
    phase_ax.set_title("非零系数相位", pad=4)
    phase_ax.legend(loc="upper left", ncols=2)
    save(fig, "amplitude-phase", 169, 84, "03-graphs-and-signals/01-signal-representation-and-processing.tex",
         "Why can equal Fourier magnitudes describe different sequences?",
         {"sequence": "x[n]=cos(2*pi*n/8)", "shift": "z[n]=x[(n-2) mod 8]",
          "DFT": "X[k]=sum_(n=0)^7 x[n]*exp(-2*pi*i*k*n/8)"},
         {"N": 8, "shift": 2, "x": x.tolist(), "z": z.tolist(), "nonzero_frequencies": nonzero.tolist(),
          "magnitudes": [4, 4], "original_phases": [0, 0], "shifted_phases": [-np.pi / 2, np.pi / 2]},
         "All eight discrete samples and frequencies. Lines join samples for guidance, not interpolation. Zero-coefficient phases are undefined and omitted.")


def transient_growth():
    k = np.arange(15)
    norms = []
    fig, ax = plt.subplots(figsize=(112 / 25.4, 64 / 25.4))
    fig.subplots_adjust(left=.14, right=.97, bottom=.22, top=.95)
    axes_style(ax)
    for coupling, color, marker in [(0, BLUE, "o"), (4, RED, "s")]:
        states = np.column_stack((coupling * k * 2. ** (1 - k), 2. ** (-k)))
        values = np.linalg.norm(states, axis=1)
        norms.append(values)
        assert np.allclose(states[0], [0, 1])
        assert np.allclose(states[1], [coupling, .5])
        ax.plot(k, values, marker=marker, ms=3.1, color=color,
                ls="-" if coupling == 0 else "--", label=f"K = {coupling}")
    assert norms[1][1] > 4 and norms[1][-1] < .01
    ax.axhline(1, color=GREY, ls=":", lw=.6)
    ax.set(xlim=(-.2, 14.2), ylim=(0, 4.6), xticks=[0, 2, 4, 6, 8, 10, 12, 14],
           yticks=[0, 1, 2, 3, 4], xlabel="步数 k", ylabel="状态范数")
    ax.legend(loc="upper right", ncols=2)
    save(fig, "transient-growth", 112, 64, "05-dynamical-systems-control-decision-and-games/01-action-and-state.tex",
         "How can identical stable eigenvalues allow different finite-time gains?",
         {"matrix": "A=[[1/2,K],[0,1/2]]", "initial_state": "x_0=(0,1)",
          "state": "x_k=(K*k*2^(1-k),2^(-k))", "ordinate": "Euclidean norm of x_k"},
         {"K": [0, 4], "k": k.tolist(), "norm_K0": norms[0].tolist(), "norm_K4": norms[1].tolist()},
         "All integer states k=0,...,14; no continuous trajectory is inferred. Dotted horizontal line is the initial norm 1.")


def cvar_reweighting():
    loss, nominal, reweighted = np.array([0, 2, 10]), np.array([.6, .3, .1]), np.array([0, .6, .4])
    alpha = .75
    assert np.isclose(reweighted.sum(), 1) and np.all(reweighted <= nominal / (1 - alpha))
    assert np.isclose(loss @ reweighted, 5.2)
    assert np.allclose(reweighted / nominal, [0, 2, 4])
    fig, ax = plt.subplots(figsize=(112 / 25.4, 64 / 25.4))
    fig.subplots_adjust(left=.14, right=.97, bottom=.23, top=.94)
    axes_style(ax)
    positions = np.arange(3)
    for offset, values, color, label in [(-.17, nominal, BLUE, "原概率 p"), (.17, reweighted, RED, "风险评价 q")]:
        bars = ax.bar(positions + offset, values, width=.29, color=color, label=label)
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, value + .023,
                    f"{value:g}", ha="center", va="bottom", fontsize=8.3)
    ax.set(xlim=(-.6, 2.6), ylim=(0, .85), xticks=positions, xticklabels=["0", "2", "10"],
           yticks=[0, .2, .4, .6, .8], xlabel="损失 L", ylabel="概率质量")
    ax.legend(loc="upper center", ncols=2)
    save(fig, "cvar-reweighting", 112, 64, "05-dynamical-systems-control-decision-and-games/03-policy-value-and-optimization.tex",
         "How does CVaR redistribute evaluation mass toward the adverse tail?",
         {"risk_envelope": "sum_i q_i=1, 0<=q_i<=p_i/(1-alpha)",
          "density_ratio": "zeta_i=q_i/p_i", "CVaR": "sum_i q_i*L_i=5.2"},
         {"loss": loss.tolist(), "p": nominal.tolist(), "q": reweighted.tolist(), "alpha": alpha,
          "density_ratio": [0, 2, 4], "CVaR": 5.2},
         "All three atoms of the exact teaching distribution. Equal category spacing does not represent equal loss intervals; bars start at zero. q is an evaluation measure, not a changed real distribution.")


def reachable_directions():
    A, B = np.array([[1, 1], [0, 1]]), np.array([0, 1])
    AB = A @ B
    corners = np.array([[u0, u0 + u1] for u0, u1 in [(-1, -1), (1, -1), (1, 1), (-1, 1)]])
    assert np.allclose(AB, [1, 1]) and np.linalg.matrix_rank(np.column_stack((B, AB))) == 2
    assert np.allclose(corners, [[-1, -2], [1, 0], [1, 2], [-1, 0]])
    fig, ax = plt.subplots(figsize=(112 / 25.4, 76 / 25.4))
    fig.subplots_adjust(left=.17, right=.95, bottom=.19, top=.88)
    axes_style(ax, grid=False)
    ax.axhline(0, color=GREY, lw=.6)
    ax.axvline(0, color=GREY, lw=.6)
    ax.add_patch(Polygon(corners, closed=True, facecolor="#F8E8E5", edgecolor=RED,
                         lw=1.1, label="两步可达集合"))
    ax.plot([0, 0], [-1, 1], color=BLUE, marker="o", ms=3.2, label="一步可达集合")
    for vector, color, label, text_xy in [(B, BLUE, "B", (-.18, 1.10)), (AB, RED, "AB", (1.06, 1.00))]:
        ax.annotate("", xy=vector, xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.1})
        ax.text(*text_xy, label, color=INK, fontsize=9)
    ax.scatter([0], [0], s=14, color=INK, zorder=4)
    ax.set(xlim=(-1.55, 1.55), ylim=(-2.35, 2.7), xticks=[-1, 0, 1], yticks=[-2, -1, 0, 1, 2],
           xlabel="状态分量 x₁", ylabel="状态分量 x₂", aspect="equal")
    ax.legend(loc="lower center", bbox_to_anchor=(.5, 1.01), ncols=2,
              columnspacing=.8, handlelength=1.4)
    save(fig, "reachable-directions", 112, 76, "05-dynamical-systems-control-decision-and-games/02-policy-realization-and-control.tex",
         "Why does a scalar input generate a two-dimensional reachable set after propagation?",
         {"state_model": "x_(t+1)=A*x_t+B*u_t, x_0=0", "one_step": "x_1=B*u_0",
          "two_steps": "x_2=A*B*u_0+B*u_1=(u_0,u_0+u_1)"},
         {"A": A.tolist(), "B": B.tolist(), "AB": AB.tolist(), "input_bounds": [-1, 1],
          "two_step_corners": corners.tolist()},
         "Exact line segment and polygon for -1<=u_0,u_1<=1. The rank theorem in the text uses unrestricted inputs; removing these bounds expands the two-step set to the full plane.")


def correlated_mass():
    independent = np.full((2, 2), .25)
    correlated = np.diag([.5, .5])
    payoff = np.diag([2, 2])
    assert np.allclose(independent.sum(0), correlated.sum(0))
    assert np.allclose(independent.sum(1), correlated.sum(1))
    assert np.isclose((independent * payoff).sum(), 1)
    assert np.isclose((correlated * payoff).sum(), 2)
    fig, axs = plt.subplots(1, 2, figsize=(112 / 25.4, 72 / 25.4))
    fig.subplots_adjust(left=.14, right=.96, top=.85, bottom=.33, wspace=.36)
    cmap = LinearSegmentedColormap.from_list("probability-yellow", ["#FFFFFF", YELLOW])
    for ax, matrix, title in zip(axs, [independent, correlated], ["独立随机化", "共同建议"]):
        image = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=.5, interpolation="nearest")
        ax.set(xticks=[0, 1], xticklabels=["L", "R"], yticks=[0, 1], yticklabels=["L", "R"],
               xlabel="参与方 2", title=title)
        ax.tick_params(length=0)
        ax.set_xticks([-.5, .5, 1.5], minor=True)
        ax.set_yticks([-.5, .5, 1.5], minor=True)
        ax.grid(which="minor", color=GRID, lw=.5)
        ax.tick_params(which="minor", length=0)
        for (i, j), value in np.ndenumerate(matrix):
            ax.text(j, i, f"{value:g}", ha="center", va="center", fontsize=9)
    axs[0].set_ylabel("参与方 1")
    cax = fig.add_axes([.29, .15, .5, .035])
    colorbar = fig.colorbar(image, cax=cax, orientation="horizontal", ticks=[0, .25, .5])
    colorbar.ax.tick_params(length=2.5, labelsize=8)
    colorbar.set_label("联合概率", fontsize=8.5, labelpad=1)
    save(fig, "correlated-mass", 112, 72, "05-dynamical-systems-control-decision-and-games/04-multi-agent-response-and-evolution.tex",
         "Why do the same individual action frequencies allow different coordination?",
         {"independent": "mu(a_1,a_2)=x(a_1)*y(a_2)=1/4",
          "correlated": "mu(L,L)=mu(R,R)=1/2; off-diagonal mass=0",
          "payoff": "2 for matching actions, 0 otherwise"},
         {"independent_joint_mass": independent.tolist(), "correlated_joint_mass": correlated.tolist(),
          "both_marginals": [.5, .5], "expected_payoffs": [1, 2], "color_range": [0, .5]},
         "Every atom of two exact joint distributions; identical [0,.5] color range on both panels. Sequential white-to-yellow color represents probability, not participant identity.")


if __name__ == "__main__":
    amplitude_phase()
    transient_growth()
    cvar_reweighting()
    reachable_directions()
    correlated_mass()
