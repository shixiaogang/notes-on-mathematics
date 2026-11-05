"""Analytical teaching figures for mathematical language and analysis.

All figures evaluate explicit formulas; no experiments, random sampling, or
LaTeX process is used. Run from any directory. Sources and evaluated arrays
are saved alongside the vector PDF/SVG and 300 dpi PNG previews.
"""
from pathlib import Path
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())

GRAY = "#747A80"

import sys
sys.path.insert(0, str(ROOT / 'figures/00-shared/mathematical-generators/matplotlib'))
from plot_style import (configure, prepare_figure, style_record, CN, EN, BLUE, RED, YELLOW, INK, MUTED, GRID, YELLOW_FILL)
configure()

records = {}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", choices=["language-minimum-infimum", "analysis-metric-convergence",
                                     "analysis-continuity-counterexamples", "analysis-derivative-orders"],
                    help="Regenerate only this figure; preserve the other image files.")
selection = parser.parse_args().only


def panels(number, width=169, height=74):
    fig, axes = plt.subplots(1, number, figsize=(width / 25.4, height / 25.4),
                             layout="constrained")
    for ax in np.atleast_1d(axes):
        ax.set_axisbelow(True)
        ax.grid(axis="y", color=GRID, lw=.5)
    return fig, np.atleast_1d(axes)


def save(fig, name, brief, formula, parameters, data, source, width, height):
    prepare_figure(fig)
    outputs = []
    for ext in ["pdf", "svg", "png"]:
        output = HERE / f"{name}.{ext}"
        if selection is None or name == selection:
            fig.savefig(output, dpi=300)
        outputs.append(output.name)
    plt.close(fig)
    records[name] = {
        "kind": "analytical teaching construction, not observed experimental data",
        "reader_question": brief, "chapter_source": source, "formula": formula,
        "parameters": parameters, "evaluated_data": data,
        "processing": "Direct evaluation; no smoothing or random sampling. Discontinuous pieces are drawn separately.",
        "width_mm": width, "height_mm": height, "png_dpi": 300,
        "outputs": outputs,
    }


# The endpoint membership changes attainment, although the infimum is fixed.
x = np.linspace(0, 1, 401)
fig, axes = panels(2, width=112, height=67)
for ax, color, closed, title in zip(axes, [BLUE, RED], [False, True],
                                    ["(a) 开区间 $X=(0,1)$", "(b) 闭区间 $X=[0,1]$"]):
    ax.plot(x, x, color=color)
    ax.plot([0, 1], [0, 1], "o", ms=6, mec=color, mew=1,
            mfc=color if closed else "white", zorder=5)
    ax.axhline(0, color=GRAY, ls=":", lw=.6)
    ax.set(title=title, xlabel="$x$", xlim=(-.12, 1.12), ylim=(-.10, 1.13))
    ax.set_xticks([0, .5, 1])
    ax.set_yticks([0, .5, 1])
    ax.text(.035, .96, "下确界 $0$\n" + ("在 $x=0$ 达到" if closed else "没有最小点"),
            transform=ax.transAxes, ha="left", va="top", fontsize=8)
axes[0].set_ylabel("函数值 $f(x)=x$")
save(fig, "language-minimum-infimum",
     "The same infimum need not be attained: endpoint membership is visible through hollow/filled markers.",
     "f(x)=x; X_open=(0,1), X_closed=[0,1]; both inf=0; closed argmin={0}, open argmin is empty.",
     {"domains": {"open": "(0,1)", "closed": "[0,1]"}, "infimum": 0,
      "endpoint_display": "Line segments depict the graph closure; hollow markers exclude the endpoints in the open-domain panel."},
     {"sampled_graph_closure_x": x.tolist(), "sampled_graph_closure_f": x.tolist()},
     "01-sets-functions-and-proofs.tex: 最小值与下确界", 112, 67)


# The values 1/n are unchanged; only the distance function changes.
n = np.arange(1, 25)
usual = 1 / n
discrete = np.ones_like(usual)
fig, (a, b) = panels(2, height=75)
a.plot(n, usual, color=BLUE, marker="o", ms=3, label="通常距离 $d_u(x,0)=|x|$")
a.plot(n, discrete, color=RED, ls="--", marker="s", ms=3,
       label=r"离散距离 $d_d(x,0)=\mathbb{I}\{x\ne0\}$")
a.axhline(0, color=GRAY, ls=":", lw=.6)
a.set(title=r"(a) 同一数列 $x_n=1/n$", xlabel="索引 $n$", ylabel="到候选极限 $0$ 的距离",
      xlim=(.5, 24.5), ylim=(-.06, 1.45))
a.set_xticks([1, 4, 8, 16, 24])
a.legend(loc="upper right")
a.text(9, .36, r"$d_u(x_n,0)\to0$", fontsize=8)
a.text(12, .83, "$d_d(x_n,0)=1$", fontsize=8)
h = np.linspace(0, .5, 301)
b.plot(h, np.ones_like(h), color=RED, lw=1.1)
b.plot([0], [1], "o", mfc="white", mec=RED, ms=6, mew=1, zorder=5)
b.plot([0], [0], "o", mfc=RED, mec=RED, ms=5, zorder=5)
b.axhspan(0, .5, color=GRAY, alpha=.10)
b.axhline(.5, color=GRAY, ls=":", lw=.6)
b.text(.29, .54, r"$\varepsilon=1/2$", fontsize=8)
b.text(.245, 1.23, "任意小的 $h>0$\n输出距离仍为 $1$", ha="center", va="center", fontsize=8)
b.set(title=r"(b) $\mathrm{id}:(\mathbb{R},d_u)\to(\mathbb{R},d_d)$",
      xlabel="输入的通常距离 $|h|$", ylabel=r"输出距离 $d_d(h,0)$",
      xlim=(-.028, .52), ylim=(-.06, 1.45))
save(fig, "analysis-metric-convergence",
     "Changing the metric can change convergence and continuity without changing the sequence values or the identity formula.",
     "x_n=1/n; d_u(x,y)=abs(x-y); d_d(x,y)=I{x!=y}. id:(R,d_u)->(R,d_d) is discontinuous at 0 since d_d(h,0)=1 for all h!=0.",
     {"n_range": [1, 24], "identity_metric_direction": "usual domain -> discrete codomain",
      "epsilon": .5, "identity_slice": "h>=0; output distance at h=0 is 0, elsewhere it is 1"},
     {"n": n.tolist(), "x_n": usual.tolist(), "usual_distance": usual.tolist(),
      "discrete_distance": discrete.tolist(), "positive_h_plot_grid": h.tolist()},
     "03-mathematical-analysis.tex: 度量空间与收敛、连续性与Lipschitz条件", 169, 75)


# Input/output neighbourhoods, a true jump, and a continuous corner.
x = np.linspace(-1, 1, 601)
fig, (a, b, c) = panels(3, height=75)
for ax in [a, b, c]:
    ax.set(xlim=(-1.08, 1.08), ylim=(-.09, 1.28), xlabel="$x$")
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([0, .5, 1])
a.plot(x, x * x, color=YELLOW)
a.axvspan(-.5, .5, color=GRAY, alpha=.08)
a.axhspan(0, .25, color=GRAY, alpha=.12)
a.axhline(.25, color=GRAY, ls=":", lw=.6)
a.vlines([-.5, .5], 0, .25, color=GRAY, ls="--", lw=.6)
a.plot([-.5, .5], [.25, .25], "o", mfc="white", mec=YELLOW, ms=4, zorder=5)
a.plot([0], [0], "o", color=GRAY, ms=3, zorder=5)
a.text(-.99, .09, r"$\varepsilon=1/4$", fontsize=8)
a.text(0, .62, r"$\delta=1/2$", ha="center", fontsize=8)
a.text(-.99, 1.11, "$f(x)=x^2$", fontsize=8)
a.set(title="(a) 连续与邻域控制", ylabel="函数值")
b.plot([-1, 0], [0, 0], color=YELLOW)
b.plot([0, 1], [1, 1], color=YELLOW)
b.plot([0], [0], "o", mfc="white", mec=YELLOW, ms=6, mew=1, zorder=5)
b.plot([0], [1], "o", color=YELLOW, ms=6, zorder=5)
b.text(-.95, .72, r"$x\uparrow0$" + " 时\n函数值仍为 $0$", fontsize=8)
b.annotate("$j(0)=1$", (0, 1), xytext=(.17, .47), fontsize=8,
           arrowprops={"arrowstyle":"-", "color":GRAY, "lw":.6})
b.text(-.98, 1.11, r"$j(x)=\mathbb{I}\{x\geq0\}$", fontsize=8)
b.set(title="(b) 跳跃处不连续")
c.plot(x, np.abs(x), color=YELLOW)
c.plot([0], [0], "o", color=YELLOW, ms=4, zorder=5)
c.text(-.99, .10, "$f'_-(0)=-1$", fontsize=8)
c.text(.27, .10, "$f'_+(0)=1$", fontsize=8)
c.text(-.98, 1.11, "$f(x)=|x|$", fontsize=8)
c.set(title="(c) 连续却不可导")
save(fig, "analysis-continuity-counterexamples",
     "Continuity preserves nearby outputs, a jump breaks this property, and continuity does not guarantee a common two-sided slope.",
     "f1(x)=x^2: at x0=0, epsilon=1/4 and delta=1/2 imply |x|<delta -> |f1(x)|<epsilon. j(x)=0 for x<0, 1 for x>=0. f3(x)=|x|: continuous at 0; left/right derivatives=-1/+1.",
     {"domain": [-1, 1], "sample_count": 601, "x0": 0,
      "continuous_panel": {"epsilon": .25, "delta": .5},
      "jump_panel": {"left_limit": 0, "value_at_zero": 1, "right_limit": 1},
      "corner_panel": {"left_derivative": -1, "right_derivative": 1}},
     {"x": x.tolist(), "square": (x*x).tolist(), "absolute_value": np.abs(x).tolist(),
      "jump_segments": [[[-1, 0], [0, 0]], [[0, 1], [1, 1]]]},
     "03-mathematical-analysis.tex: 度量空间与收敛、连续性与Lipschitz条件、一元导数与局部变化率", 169, 75)


# Common function, point and signed steps for both derivative orders.
x0 = .5
f0 = x0**3 - 3*x0
fp = 3*x0*x0 - 3
fpp = 6*x0
x = np.linspace(.15, .85, 601)
h_local = x - x0
exact = x**3 - 3*x
t1 = f0 + fp*h_local
t2 = t1 + .5*fpp*h_local*h_local
h = np.linspace(-.2, .2, 601)
remainder1 = 1.5*h*h + h**3
remainder2 = h**3
fig, (a, b) = panels(2, height=81)
a.plot(x, exact, color=BLUE, lw=1.1, label="$f(x)$")
a.plot(x, t1, color=RED, ls="--", lw=1.1, label="一阶近似 $T_1(h)$")
a.plot(x, t2, color=YELLOW, ls=":", lw=1.1, label="二阶近似 $T_2(h)$")
a.plot([x0], [f0], "o", color=GRAY, ms=4, zorder=5)
for xpoint in [.4, .6]:
    a.plot([xpoint], [xpoint**3-3*xpoint], "o", mfc="white", mec=BLUE, ms=4, zorder=5)
    a.axvline(xpoint, color=GRAY, ls=":", lw=.6)
a.text(.19, -2.04, r"$x_0=1/2$", fontsize=8)
a.set(title="(a) 共同函数与两阶近似", xlabel="$x$", ylabel="函数值",
      xlim=(.15, .85), ylim=(-2.25, -.35))
a.set_xticks([.2, .4, .5, .6, .8])
a.legend(loc="upper right")
b.plot(h, remainder1, color=RED, ls="--", label="$f(x_0+h)-T_1(h)$")
b.plot(h, remainder2, color=YELLOW, ls=":", lw=1.1, label="$f(x_0+h)-T_2(h)$")
b.axhline(0, color=GRAY, lw=.6)
b.axvline(0, color=GRAY, lw=.6)
for step in [-.1, .1]:
    r1 = 1.5*step*step+step**3
    r2 = step**3
    b.plot([step], [r1], "o", mfc=RED, mec="#4C4D4F", mew=.5, ms=4, zorder=5)
    b.plot([step], [r2], "s", mfc=YELLOW, mec="#4C4D4F", mew=.5, ms=4, zorder=5)
    b.annotate(f"{r1:.3f}", (step, r1), xytext=(step, .039),
               ha="center", fontsize=8, arrowprops={"arrowstyle":"-", "color":GRAY,"lw":.6})
    b.annotate(f"{r2:.3f}", (step, r2), xytext=(step, -.015),
               ha="center", fontsize=8, arrowprops={"arrowstyle":"-", "color":GRAY,"lw":.6})
b.set(title="(b) 扣除近似后的误差", xlabel="带符号步长 $h$", ylabel="剩余函数值",
      xlim=(-.21, .21), ylim=(-.026, .087))
b.set_xticks([-.2, -.1, 0, .1, .2])
b.legend(loc="upper center", fontsize=7.8)
steps = [-.1, .1]
step_data = [{"h": step, "x": x0+step, "f": (x0+step)**3-3*(x0+step),
              "T1": f0+fp*step, "T2": f0+fp*step+.5*fpp*step*step,
              "first_order_remainder": 1.5*step*step+step**3,
              "second_order_remainder": step**3} for step in steps]
save(fig, "analysis-derivative-orders",
     "The first derivative determines the tangent term; the second derivative corrects its quadratic error on the same function, point and signed steps.",
     "f(x)=x^3-3x; x0=1/2; h=x-x0; f0=-11/8; f'(x0)=-9/4; f''(x0)=3. T1(h)=f0+f'(x0)h; T2(h)=T1(h)+f''(x0)h^2/2. f(x0+h)-T1(h)=3h^2/2+h^3; f(x0+h)-T2(h)=h^3.",
     {"x0": x0, "f0": f0, "first_derivative": fp, "second_derivative": fpp,
      "local_x_domain": [.15,.85], "remainder_h_domain": [-.2,.2], "highlighted_steps": steps,
      "color_roles": "Blue exact function, red first-order approximant/remainder, yellow second-order approximant/remainder; colors remain consistent across panels."},
     {"local_x": x.tolist(), "local_h": h_local.tolist(), "exact_f": exact.tolist(), "T1": t1.tolist(), "T2": t2.tolist(),
      "h": h.tolist(), "first_order_remainder": remainder1.tolist(),
      "second_order_remainder": remainder2.tolist(), "highlighted_evaluations": step_data},
     "03-mathematical-analysis.tex: 一元导数与局部变化率、二阶导数与曲率; common example requested by the author", 169, 81)

manifest = {
    "style": style_record(),
    "description": "Four analytical teaching figures for the opening mathematics chapters.",
    "fonts": {"Chinese": "fonts/LXGWWenKai-Regular.ttf", "Latin": "fonts/SourceSans3-Regular.otf", "math": "Matplotlib STIX"},
    "palette": {"blue": BLUE, "red": RED, "yellow": YELLOW, "auxiliary_gray": GRAY},
    "vector_outputs": "PDF embeds fonts; SVG uses vector glyph paths. Editable labels and all plotted geometry remain in plots.py.",
    "latex_execution": False,
    "figures": records,
}
(HERE / "sources.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n")
