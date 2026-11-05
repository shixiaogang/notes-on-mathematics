"""Analytic concept comparisons for mathematical preparation, chapters 3–5.

All values come from the displayed formulas. No random observations, fitting,
data filtering, downsampling, or post-export image editing is used.
"""
from pathlib import Path
import sys
import json
import hashlib
import platform
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path

sys.path.insert(0, str(ROOT / 'figures/00-shared/mathematical-generators/matplotlib'))
from plot_style import (configure, prepare_figure, style_record, CN, EN, BLUE, RED, YELLOW, INK, MUTED, GRID, YELLOW_FILL)
configure()
AUX = MUTED

RECORDS = []

def axes(n=1, height=67):
    width = 112 if n == 1 else 169
    fig, axs = plt.subplots(1, n, figsize=(width / 25.4, height / 25.4),
        layout="constrained", squeeze=False)
    for ax in axs.ravel():
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(width=.7, length=3, labelsize=8)
    return fig, axs.ravel()

def save(fig, name, facts):
    # Mathtext 3.11 uses the first text family for characters outside $...$.
    # A CJK primary family is needed for mixed Chinese/math labels; pure Latin
    # text and tick labels keep Source Sans 3 as the primary family.
    prepare_figure(fig)
    files = []
    for suffix in ("pdf", "svg", "png"):
        p = asset_path(OUT, f"{name}.{suffix}")
        fig.savefig(p, dpi=360)
        files.append({"path": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    RECORDS.append({"name": name, "teaching_construction": True,
        "width_mm": float(fig.get_size_inches()[0] * 25.4),
        "height_mm": float(fig.get_size_inches()[1] * 25.4),
        "exports": files, **facts})
    plt.close(fig)

def weighted_projection():
    x = np.linspace(-1, 1, 801)
    fig, (ax,) = axes()
    ax.plot(x, x*x, color="#4C4D4F", label=r"目标 $x^2$")
    ax.axhline(1/3, color=BLUE, ls="--", label=r"均匀权重：$1/3$")
    ax.axhline(.5, color=RED, ls="-.", label=r"Chebyshev 权重：$1/2$")
    ax.set(xlabel=r"输入 $x$", ylabel="函数值", xlim=(-1,1), ylim=(0,1.08),
        xticks=[-1,-.5,0,.5,1], yticks=[0,1/3,.5,1],
        yticklabels=["0", "1/3", "1/2", "1"])
    ax.legend(frameon=False, fontsize=8, loc="upper center")
    save(fig, "weighted-projection", {
        "question": "How can the same candidate space yield different nearest functions?",
        "formula": "target x^2 on [-1,1]; best affine projection constants 1/3 under w=1 and 1/2 under w=(1-x^2)^(-1/2)",
        "sampling": "801 uniformly spaced analytic evaluations, including endpoints; the singular weight itself is not plotted.",
        "design": "One shared coordinate panel; target neutral, first weight blue dashed, second weight red dash-dot. Same target and candidate space."})

def simple_integral():
    x = np.linspace(0, 1, 801)
    fig, axs = axes(2, 64)
    for ax, n in zip(axs, (2, 4)):
        bins = 2**n
        edges = np.sqrt(np.arange(bins + 1) / bins)
        heights = np.arange(bins + 1) / bins
        ax.fill_between(edges, heights, step="post", color=YELLOW_FILL)
        for k in range(bins):
            ax.plot(edges[k:k+2], [heights[k], heights[k]], color=YELLOW,
                    label=rf"简单函数 $s_{n}$" if k == 0 else None)
        ax.scatter([1], [1], s=12, color=YELLOW, zorder=4)
        ax.plot(x, x*x, color="#4C4D4F", ls="--", label=r"$f(x)=x^2$")
        ax.set(title=rf"$n={n}$：取值间距 $2^{{-{n}}}$", xlabel=r"输入 $x$",
               ylabel="函数值", xlim=(0, 1), ylim=(0, 1.08),
               xticks=[0, .5, 1], yticks=[0, .5, 1])
        ax.legend(frameon=False, fontsize=8, loc="upper left")
    save(fig, "simple-integral", {
        "question": "How does measuring value groups turn a function into a finite weighted sum?",
        "formula": "f(x)=x^2 on [0,1]; s_n(x)=2^(-n)*floor(2^n*f(x)), n=2,4; value-bin preimages have endpoints sqrt(k/2^n). The chapter's height cutoff n is inactive here.",
        "sampling": "801 exact evaluations of f; all exact bin edges and heights for the simple functions. Horizontal segments are separated at jumps; shaded rectangle boundaries are not interpolated function values. The singleton value at x=1 is marked, and endpoint choices do not affect the area.",
        "design": "Two aligned panels with identical x/y ranges; warm-yellow shaded rectangles show value times preimage length, dashed neutral curve shows the same target. Widths differ because the bins divide values, not input positions."})

def weak_derivative():
    x = np.linspace(-1,1,801)
    fig, (a,b) = axes(2,62)
    a.plot(x, np.abs(x), color=BLUE)
    a.scatter([0],[0], s=25, color=BLUE, zorder=5)
    a.set(title=r"(a) $f(x)=|x|$", xlabel=r"$x$", ylabel="函数值",
        xlim=(-1,1), ylim=(-.08,1.1), xticks=[-1,0,1], yticks=[0,.5,1])
    b.plot([-1,0],[-1,-1], color=RED)
    b.plot([0,1],[1,1], color=RED)
    b.scatter([0,0],[-1,1], s=28, facecolor="white", edgecolor=RED, zorder=5)
    b.set(title=r"(b) $g(x)=\mathrm{sign}(x)$", xlabel=r"$x$", ylabel="弱导数代表",
        xlim=(-1,1), ylim=(-1.3,1.3), xticks=[-1,0,1], yticks=[-1,0,1])
    save(fig, "weak-derivative", {
        "question": "Does a continuous corner prevent existence of a weak derivative?",
        "formula": "f(x)=abs(x), weak derivative g(x)=sign(x) almost everywhere on (-1,1)",
        "sampling": "801 uniform evaluations for f; two exact horizontal segments for g, separated at zero. Open endpoints denote missing classical derivative, not a particular weak representative value.",
        "design": "Aligned function and derivative panels, common x scale; no line bridging the discontinuity."})

def covering_centers():
    fig, (ax,) = axes(height=78)
    centers = np.array([(a,b) for a in (-2/3,0,2/3) for b in (-2/3,0,2/3)])
    radius = np.sqrt(2)/3
    for a,b in centers:
        ax.add_patch(Circle((a,b), radius, facecolor="none", edgecolor=YELLOW, lw=1.1))
    ax.add_patch(Rectangle((-1,-1),2,2,facecolor="none",edgecolor="#4C4D4F",lw=1))
    for q in (-1/3,1/3):
        ax.plot([q,q],[-1,1],color=AUX,ls=":",lw=.6)
        ax.plot([-1,1],[q,q],color=AUX,ls=":",lw=.6)
    ax.scatter(centers[:,0],centers[:,1],s=24,color=YELLOW,zorder=4)
    ax.set(aspect="equal",xlim=(-1.23,1.23),ylim=(-1.23,1.23),
        xlabel=r"系数 $a$",ylabel=r"系数 $b$",xticks=[-1,0,1],yticks=[-1,0,1])
    save(fig, "covering-centers", {
        "question": "How do finite representatives cover an uncountable function class?",
        "formula": "f_(a,b)(x)=a+b*x, (a,b) in [-1,1]^2; S=(-1,1); d_S equals Euclidean coefficient distance; nine centers at {-2/3,0,2/3}^2, radius sqrt(2)/3",
        "sampling": "All nine exact centers. Matplotlib Circle represents geometric closed balls; no claim of a minimal covering.",
        "design": "Equal aspect ratio preserves distance balls; candidate boundary neutral, balls warm yellow, grid auxiliary dotted. Center markers disambiguate intersecting circles."})

def budget_active_set():
    tau = np.linspace(0,4,801)
    w1 = np.where(tau<1,tau,np.where(tau<3,(tau+1)/2,2))
    w2 = np.where(tau<1,0,np.where(tau<3,(tau-1)/2,1))
    price = np.where(tau<1,2-tau,np.where(tau<3,(3-tau)/2,0))
    nonneg_price = np.maximum(1-tau,0)
    fig, (a,b) = axes(2,66)
    a.plot(tau,w1,color=BLUE,label=r"$w_1^\star$")
    a.plot(tau,w2,color=RED,ls="--",label=r"$w_2^\star$")
    b.plot(tau,price,color=BLUE,label=r"预算 $\alpha_{\mathrm{bud}}^\star$")
    b.plot(tau,nonneg_price,color=RED,ls="--",label=r"非负约束 $\alpha_2^\star$")
    for ax in (a,b):
        for q in (1,3): ax.axvline(q,color=AUX,ls=":",lw=.6)
        ax.set(xlim=(0,4),ylim=(-.08,2.16),xticks=[0,1,2,3,4],yticks=[0,1,2],xlabel=r"预算 $\tau$")
    a.legend(frameon=False,fontsize=8,loc="upper left")
    b.legend(frameon=True,framealpha=1,facecolor="white",edgecolor="none",fontsize=8,loc="upper right")
    a.set(title="(a) 最优分配",ylabel="解坐标")
    b.set(title="(b) 约束乘子",ylabel="乘子值")
    save(fig, "budget-active-set", {
        "question": "How do active constraints differ from positive shadow prices?",
        "formula": "min 0.5*||w-(2,1)||^2, w>=0, w1+w2<=tau; exact piecewise coordinate and multiplier formulas from ex:opt-kkt-budget",
        "sampling": "801 uniform points on [0,4], including both switches; tau=0 shown only as the right-limit extension, chapter example assumes tau>0.",
        "design": "Two aligned panels share budget x axis and y range; coordinate/multiplier roles explicit in titles; dotted references are switch locations."})

def hull_relaxation():
    fig, axs = axes(2,71)
    vertices = [[(0,0),(1,0),(0,1)],[(0,0),(1,0),(1,.5),(.5,1),(0,1)]]
    edges = [[(1,0),(0,1)],[(1,.5),(.5,1)]]
    for i, (ax,vs,edge) in enumerate(zip(axs,vertices,edges)):
        ax.add_patch(Polygon(vs,facecolor="#EDF2F5",edgecolor="#4C4D4F",lw=1))
        ax.plot(*np.array(edge).T,color=RED,lw=1.1)
        ax.scatter([0,1,0],[0,0,1],s=27,color=BLUE,zorder=4)
        ax.set(aspect="equal",xlim=(-.08,1.12),ylim=(-.08,1.12),xticks=[0,.5,1],yticks=[0,.5,1],
            xlabel=r"$x_1$",ylabel=r"$x_2$",title="(a) 精确凸包" if i==0 else "(b) 局部约束松弛")
    axs[0].text(.35,.22,r"最优值 $1$",fontsize=8)
    axs[1].scatter([.75],[.75],s=30,color=RED,marker="s",zorder=5)
    axs[1].text(.15,.19,r"最优值 $3/2$",fontsize=8)
    save(fig, "hull-relaxation", {
        "question": "Why can a relaxation yield a strictly better objective while the exact hull does not?",
        "formula": "integer points S={(0,0),(1,0),(0,1)}; left conv(S); right P=[0,1]^2 intersect {x1+x2<=1.5}; maximize x1+x2",
        "sampling": "Exact polygon vertices and three integer points. Right highlighted fractional maximizer=(.75,.75).",
        "design": "Identical axis limits and equal aspect; optimal faces coral; feasible polygons same shallow fill. Fractional square marker contrasts integer circles."})

def proximal_comparison():
    z = np.linspace(-3,3,1201)
    soft = np.sign(z)*np.maximum(np.abs(z)-1,0)
    projection = np.clip(z,-1,1)
    fig,(ax,) = axes(height=70)
    ax.plot(z,projection,color=BLUE,label=r"区间投影 $\Pi_{[-1,1]}$")
    ax.plot(z,soft,color=RED,ls="--",label=r"软阈值，$\eta\lambda=1$")
    ax.plot(z,z/2,color=YELLOW,ls="-.",label=r"二次收缩 $z/2$")
    ax.set(xlim=(-3,3),ylim=(-2.2,2.2),xlabel=r"输入 $z$",ylabel="输出",xticks=[-3,-1,0,1,3],yticks=[-2,-1,0,1,2])
    ax.legend(frameon=False,fontsize=8,loc="upper left")
    save(fig,"proximal-comparison",{
        "question": "How do feasibility projection, sparsity thresholding and quadratic shrinkage differ?",
        "formula": "clip(z,-1,1); sign(z)*max(abs(z)-1,0); z/2",
        "sampling": "1201 uniform points on [-3,3], includes -1,0,1; all maps continuous. No smoothing/interpolation of discontinuous maps.",
        "design": "Shared input/output panel, solid/dashed/dash-dot lines redundant with colors, direct legend names the operation rather than the color."})

def main():
    simple_integral()
    weighted_projection()
    weak_derivative()
    covering_centers()
    budget_active_set()
    hull_relaxation()
    proximal_comparison()
    (asset_path(OUT, "sources.json")).write_text(json.dumps({"python":platform.python_version(),
        "style":style_record(),"numpy":np.__version__,"matplotlib":matplotlib.__version__,"figures":RECORDS},ensure_ascii=False,indent=2)+"\n")

if __name__ == "__main__":
    main()
