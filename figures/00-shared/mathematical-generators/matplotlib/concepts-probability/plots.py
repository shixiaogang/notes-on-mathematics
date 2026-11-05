"""Five analytic teaching figures; no experiments and no LaTeX invocation.

Run with Python, NumPy and Matplotlib. Repository fonts are loaded relative to
this file. Analytic formulas, parameters, evaluated data and export dimensions
are written to sources.json beside the figures.
"""
from pathlib import Path
import hashlib
import json
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
sys.path.insert(0, str(ROOT / 'figures/00-shared/mathematical-generators/matplotlib'))
from plot_style import configure, prepare_figure, style_record
from plot_style import BLUE, RED, YELLOW, MUTED as GRAY, GRID, BLUE_FILL, RED_FILL

configure()
CHAPTERS = Path("tex/01-mathematical-preliminaries")
RECORDS = {}


def canvas(n=1, width=112, height=66):
    fig, axs = plt.subplots(1, n, figsize=(width / 25.4, height / 25.4),
                            layout="constrained")
    axs = np.atleast_1d(axs)
    for ax in axs:
        ax.set_axisbelow(True)
        ax.grid(axis="y", color=GRID, linewidth=0.5)
        ax.tick_params(length=3, width=0.6)
    return fig, axs


def save(fig, name, chapter, difficulty, formula, parameters, data, design):
    width, height = (np.asarray(fig.get_size_inches()) * 25.4).tolist()
    prepare_figure(fig)
    for ext in ("pdf", "svg", "png"):
        fig.savefig(asset_path(HERE, f"{name}.{ext}"), dpi=400)
    plt.close(fig)
    source = CHAPTERS / chapter
    RECORDS[name] = {
        "kind": "analytic teaching construction; not experimental data",
        "chapter": source.as_posix(),
        "source_sha256_at_generation": hashlib.sha256((ROOT / source).read_bytes()).hexdigest(),
        "difficulty": difficulty, "formula": formula, "parameters": parameters,
        "evaluated_data": data, "design_intent": design,
        "processing": "Direct deterministic evaluation; no random sampling, filtering or smoothing.",
        "physical_size_mm": [width, height], "png_dpi": 400, "style": style_record(),
        "outputs": [f"{name}.{ext}" for ext in ("pdf", "svg", "png")],
    }


# Rare spikes: the value graph has jumps, so disconnected pieces are drawn.
fig, (a, b) = canvas(2, 169, 65)
for n, color, linestyle in ((4, BLUE, "-"), (16, RED, "--")):
    a.plot([0, 1 / n], [n, n], color=color, linestyle=linestyle,
           label=f"$n={n}$")
    a.plot([1 / n, 1], [0, 0], color=color, linestyle=linestyle)
    a.fill_between([0, 1 / n], 0, n, color=BLUE_FILL if n == 4 else RED_FILL)
    a.plot(1 / n, n, "o", color=color, markersize=3.3)
    a.plot(1 / n, 0, "o", markerfacecolor="white", markeredgecolor=color,
           markersize=3.3, zorder=5)
a.set(xlabel="$u$", ylabel="$V_n(u)$", xlim=(-0.015, 1.015), ylim=(-0.5, 18),
      title="(a) 变窄、变高的尖峰")
a.set_xticks([0, 0.25, 0.5, 0.75, 1])
a.legend(loc="upper right")
n = np.arange(2, 101)
b.plot(n, 1 / n, color=BLUE, label=r"$\mathbb{P}(V_n>1)$")
b.plot(n, np.ones_like(n), color=RED, linestyle="--", label=r"$\mathbb{E}V_n$")
b.set(xlabel="$n$", ylabel="概率或期望", xlim=(2, 100), ylim=(0, 1.12),
      title="(b) 概率变小，期望不变")
b.legend(loc="center right")
save(fig, "probability-vanishing-spikes", "04-random-variables-distributions-and-causality/01-random-variables.tex",
     "Almost sure/probability convergence need not control expectation without uniform integrability.",
     "U~Uniform(0,1); V_n(U)=n*I(U<=1/n); E[V_n]=1; P(V_n>1)=1/n for n>=2.",
     {"left_n": [4, 16], "right_n": [2, 100], "uniform_support": [0, 1]},
     {"n": n.tolist(), "tail_probability_at_1": (1 / n).tolist(),
      "expectation": np.ones_like(n).tolist(), "spike_areas": [1, 1]},
     "Two aligned panels distinguish sample-path value from averaged quantities; blue solid/red dashed comparisons with explicit legends. No line crosses either jump.")


# Exact mean and variance of the mean-root update, rather than one random run.
fig, (a, b) = canvas(2, 169, 65)
t = np.arange(0, 41)
ta = np.arange(1, 41)
mean_fixed = 1 - 0.8 ** t
var_fixed = (1 - 0.8 ** (2 * t)) / 9
for ax, fixed, average in ((a, mean_fixed, np.ones_like(ta)),
                           (b, var_fixed, 1 / ta)):
    ax.plot(t, fixed, color=BLUE, label=r"$\alpha=0.2$")
    ax.plot(ta, average, color=RED, linestyle="--", label=r"$\alpha_t=1/(t+1)$")
    ax.set(xlabel="更新次数 $t$", xlim=(0, 40), ylim=(0, 1.1))
    ax.legend(loc="upper right" if ax is b else "lower right")
a.set(title="(a) 重复实验的均值", ylabel=r"$\mathbb{E}\theta^{(t)}$")
b.axhline(1 / 9, color=GRAY, linewidth=0.6, linestyle=":")
b.text(26, 1 / 9 + 0.045, "$1/9$", fontsize=8)
b.set(title="(b) 重复实验的方差", ylabel=r"$\mathrm{Var}(\theta^{(t)})$")
save(fig, "stochastic-stepsize-bias-variance", "05-dynamical-systems-control-decision-and-games/01-action-and-state.tex",
     "A vanishing bias does not imply that fixed-step noise variance vanishes.",
     "theta_(t+1)=(1-alpha_t)*theta_t+alpha_t*Y_(t+1); fixed mean=1-.8^t; fixed variance=(1-.8^(2t))/9; sample mean has expectation 1 and variance 1/t for t>=1.",
     {"initial_theta": 0, "observation_mean": 1, "observation_variance": 1,
      "observations": "iid with finite variance", "fixed_alpha": 0.2,
      "decreasing_alpha_t": "1/(t+1), t starts at 0"},
     {"t": t.tolist(), "fixed_mean": mean_fixed.tolist(), "fixed_variance": var_fixed.tolist(),
      "sample_mean_t": ta.tolist(), "sample_mean_expectation": np.ones_like(ta).tolist(),
      "sample_mean_variance": (1 / ta).tolist()},
     "Same update-count scale and color/line encoding across two panels; mean and variance are separate quantities, not confidence bands or simulated paths.")


# The worked example uses three observations and explicit teaching weights.
x_data = np.array([0., 1., 3.])
y_data = np.array([9., 11., 13.])
weights = np.array([1., 0.75, 0.25])
design = np.column_stack([np.ones(3), x_data])
coeff = np.linalg.solve(design.T @ (weights[:, None] * design),
                        design.T @ (weights * y_data))
constant = np.average(y_data, weights=weights)
assert np.allclose(coeff, [9.2, 1.4]) and np.isclose(constant, 10.25)
x = np.linspace(-0.2, 3.2, 321)
fig, (a,) = canvas(1, 112, 68)
a.plot(x, np.full_like(x, constant), color=BLUE, label="局部常数")
a.plot(x, coeff[0] + coeff[1] * x, color=RED, linestyle="--", label="局部线性")
a.scatter(x_data, y_data, color=GRAY, s=24, zorder=4, label="三个观测")
a.scatter([0, 0], [constant, coeff[0]], marker="s", s=32,
          facecolors="white", edgecolors=[BLUE, RED], linewidths=1.0, zorder=5)
a.text(0.14, 10.39, "$10.25$", fontsize=8.5)
a.text(0.14, 8.82, "$9.2$", fontsize=8.5,
       bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.3})
a.axvline(0, color=GRAY, linestyle=":", linewidth=0.6)
a.set(xlabel="输入 $x$", ylabel="响应或拟合值", xlim=(-0.3, 3.3), ylim=(8.45, 14.2))
a.legend(loc="lower left", bbox_to_anchor=(0, 1.02), ncol=3,
         handlelength=1.6, columnspacing=1)
save(fig, "statistics-local-boundary-fit", "04-random-variables-distributions-and-causality/01-random-variables.tex",
     "Local linear fitting returns the fitted intercept to the boundary instead of averaging one-sided responses.",
     "Weighted least squares on design [1,x]; constant=sum(w*y)/sum(w)=10.25; linear fit=9.2+1.4*x.",
     {"target_x": 0, "weights_are": "fixed teaching construction, not kernel values inferred from a bandwidth"},
     {"observation_x": x_data.tolist(), "observation_y": y_data.tolist(), "weights": weights.tolist(),
      "constant_prediction": float(constant), "linear_coefficients": coeff.tolist(),
      "curve_x": x.tolist(), "linear_curve_y": (coeff[0] + coeff[1] * x).tolist()},
     "Neutral observations and colored fitted functions; open squares mark the two boundary predictions. Unknown true conditional mean is deliberately not drawn.")


epsilon = np.linspace(0, 0.5, 501)
hb = np.zeros_like(epsilon)
positive = epsilon > 0
hb[positive] = -epsilon[positive] * np.log(epsilon[positive])
hb -= (1 - epsilon) * np.log1p(-epsilon)
mutual = np.log(2) - hb
fig, (a,) = canvas(1, 112, 66)
a.plot(epsilon, hb, color=BLUE, label=r"$H(X\mid Y)$")
a.plot(epsilon, mutual, color=RED, linestyle="--", label="$I(X;Y)$")
a.axhline(np.log(2), color=GRAY, linewidth=0.6, linestyle=":")
a.text(0.29, np.log(2) + 0.018, r"$H(X)=\log 2$", fontsize=8.5)
a.set(xlabel=r"翻转概率 $\varepsilon$", ylabel="信息量（nat）",
      xlim=(0, 0.5), ylim=(0, 0.79))
a.legend(loc="center right")
assert np.allclose(hb + mutual, np.log(2))
save(fig, "information-binary-channel-information", "04-random-variables-distributions-and-causality/02-information-theory-and-statistical-geometry.tex",
     "Noise divides a fixed input entropy into revealed information and remaining uncertainty.",
     "X~Bernoulli(.5); N~Bernoulli(epsilon) independent; Y=X xor N; H(X|Y)=Hb(epsilon); I(X;Y)=log(2)-Hb(epsilon). Natural logarithms; 0*log(0)=0.",
     {"input_probability": 0.5, "epsilon_domain": [0, 0.5], "samples": 501, "unit": "nat"},
     {"epsilon": epsilon.tolist(), "conditional_entropy": hb.tolist(), "mutual_information": mutual.tolist()},
     "One shared axis shows two complementary information quantities; input entropy is a neutral reference. Blue solid and red dashed curves remain distinguishable in grayscale.")


# Cross-world joint distributions are constructions, not observed trial data.
joints = [np.array([[0.5, 0.], [0., 0.5]]), np.array([[0., 0.5], [0.5, 0.]])]
fig, axs = canvas(2, 112, 65)
cmap = LinearSegmentedColormap.from_list("teaching_mass", ["white", YELLOW])
for ax, joint, title in zip(axs, joints, ["(a) 模型甲", "(b) 模型乙"]):
    ax.grid(False)
    for i in range(2):
        for j in range(2):
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1,
                                   facecolor=cmap(joint[i, j] / 0.5),
                                   edgecolor=GRAY, linewidth=0.6))
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(1.5, -0.5)
    ax.set_aspect("equal")
    ax.set(xticks=[0, 1], yticks=[0, 1], xlabel="$Y(1)$", ylabel="$Y(0)$", title=title)
    ax.set_xticks([-0.5, 0.5, 1.5], minor=True)
    ax.set_yticks([-0.5, 0.5, 1.5], minor=True)
    ax.grid(which="minor", color=GRID, linewidth=0.5)
    ax.tick_params(which="minor", length=0)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{joint[i,j]:g}", ha="center", va="center", fontsize=9)
    for spine in ax.spines.values():
        spine.set_visible(False)
    assert np.allclose(joint.sum(axis=0), [0.5, 0.5])
    assert np.allclose(joint.sum(axis=1), [0.5, 0.5])
save(fig, "causal-cross-world-couplings", "04-random-variables-distributions-and-causality/03-causal-response-and-structure.tex",
     "Identical intervention marginals and zero ATE do not determine individual effects or conditional counterfactuals.",
     "Joint matrices for (Y(0),Y(1)): A=[[.5,0],[0,.5]], B=[[0,.5],[.5,0]]. Both marginals Bernoulli(.5); ATE=0. Individual effects are 0 under A, and +1/-1 with probabilities .5/.5 under B.",
     {"rows": "Y(0)=0,1", "columns": "Y(1)=0,1", "shared_color_range": [0, 0.5]},
     {"model_A_joint": joints[0].tolist(), "model_B_joint": joints[1].tolist(),
      "row_marginals": [0.5, 0.5], "column_marginals": [0.5, 0.5], "ATE": [0, 0]},
     "Aligned 2x2 probability heatmaps use a shared white-to-yellow scale and explicit cell values; equal margins are verified numerically. No colorbar is needed for the two directly printed values.")

(asset_path(HERE, "sources.json")).write_text(json.dumps({
    "schema": "analytic-teaching-figures-v1", "generator": "plots.py",
    "fonts": ["fonts/LXGWWenKai-Regular.ttf", "fonts/SourceSans3-Regular.otf", "STIX mathtext"],
    "font_representation": "PDF Type 3 subset vector glyphs; SVG glyph outlines; labels remain editable in plots.py",
    "palette": {"blue": BLUE, "red": RED, "yellow": YELLOW, "neutral": GRAY},
    "style": style_record(),
    "figures": RECORDS,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
