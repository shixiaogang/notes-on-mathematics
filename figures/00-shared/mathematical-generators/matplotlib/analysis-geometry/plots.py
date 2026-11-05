"""Deterministic teaching figures for the first seven mathematics chapters.

Run with a Python environment containing NumPy and Matplotlib. No TeX is used.
Analytic expressions, domains, discretization and software versions are saved
in manifest.json alongside the PDF/SVG/PNG outputs.
"""
from pathlib import Path
import sys
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path

sys.path.insert(0, str(ROOT / 'figures/00-shared/mathematical-generators/matplotlib'))
from plot_style import (configure, prepare_figure, style_record, CN, EN, BLUE, RED, YELLOW, INK, MUTED, GRID, YELLOW_FILL)
configure()
LINE = MUTED

RECORDS = []

def axes(n=1, height=66, width=None):
    width = width or (112 if n == 1 else 169)
    fig, axs = plt.subplots(1, n, figsize=(width / 25.4, height / 25.4),
                            layout="constrained", squeeze=False)
    for ax in axs.ravel():
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(width=.7, length=3)
    return fig, axs.ravel()

def save(fig, name, facts):
    prepare_figure(fig)
    for suffix in ["pdf", "svg", "png"]:
        fig.savefig(asset_path(OUT, f"{name}.{suffix}"), dpi=360)
    RECORDS.append({"name": name, "teaching_construction": True,
        "source": "Analytic expressions and exact finite-dimensional examples in the associated mathematics chapter.",
        "width_mm": round(fig.get_size_inches()[0] * 25.4, 3),
        "height_mm": round(fig.get_size_inches()[1] * 25.4, 3), **facts})
    plt.close(fig)

def recurrence():
    t = np.arange(21)
    constant, decaying = [1.], [1.]
    for k in t[:-1]:
        constant.append(.5 * constant[-1] + .1)
        decaying.append(.5 * decaying[-1] + .1 / (k + 1))
    fig, (ax,) = axes()
    ax.plot(t, constant, color=BLUE, marker="o", ms=3, label=r"$\delta_t=0.1$")
    ax.plot(t, decaying, color=RED, marker="s", ms=3, label=r"$\delta_t=0.1/(t+1)$")
    ax.axhline(.2, color=LINE, ls="--", lw=.6)
    ax.text(12, .25, r"$0.1/(1-0.5)=0.2$", fontsize=8)
    ax.set(xlabel="迭代步 t", ylabel="递推值 e(t)", ylim=(0, 1.06), xticks=[0,5,10,15,20])
    ax.legend(frameon=False, fontsize=8)
    save(fig, "language-perturbed-recurrence", {"formula": "e[t+1]=0.5*e[t]+delta[t], e[0]=1",
        "parameters": {"rho": .5, "constant_delta": .1}, "sampling": "All integer steps 0,...,20; no sampling or randomness."})

def convergence():
    fig, axs = axes(2, 79)
    for n, color, ls in [(4,BLUE,"-"),(8,RED,"--"),(16,YELLOW,":")]:
        axs[0].plot([0,1/n], [n,n], color=color, ls=ls)
        axs[0].plot([1/n,1/n],[0,n],color=color,ls=":",lw=.6)
        axs[0].plot([1/n,1],[0,0],color=color,ls=ls,label=f"$n={n}$")
        axs[0].scatter([0,1/n],[n,n],s=17,facecolor="white",edgecolor=color,zorder=4)
    axs[0].scatter([0],[0],s=15,color=LINE,zorder=5)
    axs[0].set(title="(a) 逐点消失，积分保持为 1",xlabel="$x$",ylabel="$f_n(x)$",xlim=(-.025,1),ylim=(-.5,17))
    axs[0].legend(frameon=False,fontsize=8)
    n=20
    x=np.linspace(0,2*np.pi,2401)
    axs[1].plot(x,np.sin(n*x)/n,color=BLUE,label=r"$f_n(x)=\sin(nx)/n$")
    axs[1].plot(x,np.cos(n*x),color=RED,ls="--",label=r"$f_n'(x)=\cos(nx)$")
    axs[1].set(title="(b) 函数误差小，导数仍振荡",xlabel="$x$",ylabel="函数值 / 导数值",ylim=(-1.12,1.12),xticks=[0,np.pi,2*np.pi],xticklabels=["0",r"$\pi$",r"$2\pi$"])
    axs[1].legend(frameon=False,fontsize=8,loc="upper center",
                  bbox_to_anchor=(.5,-.25))
    save(fig,"analysis-convergence-obstacles",{"formulas":["f_n(x)=n*1_(0,1/n)(x) on [0,1]; endpoints zero","f_n(x)=sin(n*x)/n; derivative cos(n*x)"],
        "parameters":{"spikes_n":[4,8,16],"oscillation_n":20},"sampling":"Spike segments drawn separately; 2401 uniform samples on [0,2*pi] for oscillations. Vertical dashed drop indicates a jump, not a continuous segment."})

def optimization():
    fig,axs=axes(2,72)
    grid=np.linspace(-2.3,2.3,401); xx,yy=np.meshgrid(grid,grid)
    objective=.5*(xx**2+16*yy**2)
    for ax in axs:
        ax.contour(xx,yy,objective,levels=[.1,.4,1,2,4,8,16,32],colors=LINE,linewidths=.6)
        ax.set(xlabel="$w_1$",ylabel="$w_2$",xlim=(-.2,2.25),ylim=(-1.45,2.25))
    paths=[]
    for matrix,eta in [(np.diag([1.,16.]),.1),(np.eye(2),.5)]:
        path=[np.array([2.,2.])]
        for _ in range(18): path.append(path[-1]-eta*matrix@path[-1])
        paths.append(np.array(path))
    for ax,path,color,title in zip(axs,paths,[BLUE,RED],["(a) 固定步长的梯度下降","(b) 按曲率缩放的更新"]):
        ax.plot(path[:,0],path[:,1],"o-",color=color,ms=2.5)
        ax.scatter([0],[0],marker="*",color=YELLOW,s=45,zorder=5)
        ax.set_title(title)
    save(fig,"optimization-preconditioned-paths",{"formula":"f(w)=0.5*(w1^2+16*w2^2)",
        "parameters":{"initial":[2,2],"gradient_eta":.1,"preconditioner":[[1,0],[0,.0625]],"preconditioned_eta":.5,"steps":18},
        "sampling":"401-by-401 grid for exact quadratic contours; every iterate shown."})

def functional_tents():
    x=np.linspace(0,1,2001);fig,(ax,)=axes()
    for n,c,ls in [(5,BLUE,"-"),(25,RED,"--")]:
        ax.plot(x,np.maximum(1-n*x,0),color=c,ls=ls,label=f"$n={n}$")
    ax.scatter([0],[1],color=INK,s=18,zorder=5)
    ax.text(.31,.70,r"$f_n(0)=1$",fontsize=10)
    ax.text(.31,.48,r"$\|f_n\|_2=1/\sqrt{3n}\to0$",fontsize=10)
    ax.set(xlabel="$x$",ylabel="$f_n(x)$",xlim=(-.02,1),ylim=(-.03,1.10))
    ax.legend(frameon=False,fontsize=8)
    save(fig,"functional-point-evaluation",{"formula":"f_n(x)=max(1-n*x,0), x in [0,1]; integral f_n^2=1/(3*n)","parameters":{"n":[5,25]},"sampling":"2001 uniform samples including both breakpoints exactly."})

def spectral_shrinkage():
    j=np.arange(1,26);mu=1./j**2;fig,(ax,)=axes()
    for lam,c,mark in [(.01,BLUE,"o"),(.1,RED,"s")]:
        ax.plot(j,mu/(mu+lam),color=c,marker=mark,ms=2.8,label=rf"$\lambda={lam}$")
    ax.set(xlabel="谱方向 j",ylabel="保留比例",ylim=(0,1.05),xticks=[1,5,10,15,20,25])
    ax.legend(frameon=False,fontsize=8)
    save(fig,"functional-spectral-shrinkage",{"formula":"mu_j=j^(-2); retention=mu_j/(mu_j+lambda)","parameters":{"lambda":[.01,.1],"directions":25},"sampling":"All first 25 integer spectral directions. This figure does not truncate the definition of the infinite-dimensional effective dimension."})


def circle_distances():
    fig,axs=axes(2,72);theta=np.linspace(0,2*np.pi,721)
    axs[0].plot(np.cos(theta),np.sin(theta),color=LINE,lw=.6)
    arc=np.linspace(0,np.pi/2,181)
    axs[0].plot(np.cos(arc),np.sin(arc),color=BLUE,lw=1.1)
    axs[0].plot([1,0],[0,1],color=RED,ls="--",lw=1.1)
    axs[0].scatter([1,0],[0,1],color=INK,s=19,zorder=4)
    axs[0].set(title="(a) 圆上允许的路径与环境弦",aspect="equal",xlim=(-1.2,1.2),ylim=(-1.2,1.2),xlabel="第一坐标",ylabel="第二坐标")
    angle=np.linspace(0,np.pi,401)
    axs[1].plot(angle,angle,color=BLUE,label="短弧长度")
    axs[1].plot(angle,2*np.sin(angle/2),color=RED,ls="--",label="弦长")
    axs[1].set(title="(b) 同一对端点的两种距离",xlabel="夹角 θ",ylabel="单位圆上的长度",xticks=[0,np.pi/2,np.pi],xticklabels=["0",r"$\pi/2$",r"$\pi$"])
    axs[1].legend(frameon=False,fontsize=8)
    save(fig,"geometry-circle-distances",{"formula":"Unit circle; geodesic d=theta, chord d=2*sin(theta/2), theta in [0,pi]", "parameters":{"example_angle":"pi/2","radius":1},"sampling":"721 circle points,181 short-arc points,401 angles for length comparison."})

if __name__ == "__main__":
    for build in [recurrence, convergence, optimization, functional_tents,
                  spectral_shrinkage,
                  circle_distances]:
        build()
    (asset_path(OUT, "manifest.json")).write_text(json.dumps({"purpose":"Teaching constructions; no experimental data.",
        "style":style_record(),"numpy":np.__version__,"matplotlib":matplotlib.__version__,"fonts":{"Chinese":CN,"Latin":EN,"math":"Matplotlib STIX"},
        "export_settings":{"formats":["pdf","svg","png"],"png_dpi":360,"font_size_pt":8.5,
            "pdf_fonttype":3,"svg_fonttype":"path","background":"white","tex_rendering":False},
        "palette":{"blue":BLUE,"red":RED,"yellow":YELLOW},"figures":RECORDS},ensure_ascii=False,indent=2)+"\n")
