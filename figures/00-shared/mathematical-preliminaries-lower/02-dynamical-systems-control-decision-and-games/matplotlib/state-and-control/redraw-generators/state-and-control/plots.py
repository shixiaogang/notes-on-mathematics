"""Migrate quantitative dynamics/control figures from PGFPlots to Matplotlib.

Use the retained simulation tables byte-for-byte. No stochastic resampling.
The original render.py files remain the provenance of these tables.
"""
from pathlib import Path
import hashlib
import json
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").exists())
BASE = ROOT / "figures/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/matplotlib/redraw-generators/state-and-control/inputs"
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
from plot_style import BLUE, RED, GREEN, YELLOW, STROKE, MUTED, GRID, configure, prepare_figure, style_record, note
from plot_style import BLUE, GREEN, YELLOW, RED, PURPLE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
configure()

def save(fig, name):
    prepare_figure(fig)
    for ext in ["pdf", "svg", "png"]:
        fig.savefig(HERE / f"{name}.{ext}", dpi=300)
    plt.close(fig)

temperature = np.genfromtxt(BASE / "dynamics/temperature.tsv", delimiter="\t", names=True)
t = temperature["t"]
fig, ax = plt.subplots(figsize=(169/25.4, 78/25.4), layout="constrained")
ax.plot(t, temperature["deterministic"], color=PURPLE, ls="--", label="无噪声状态")
ax.plot(t, temperature["state"], color=BLUE, label="含过程噪声的状态")
ax.plot(t, temperature["observation"], color=GREEN, ls="none", marker="o", ms=3, label="传感器读数")
ax.set(title="同一初值与输入，三个不同对象", xlabel="时刻 $t$", ylabel="温差或读数",
       xlim=(-.25,24.5), ylim=(-.25,3.2), xticks=np.arange(0,25,4), yticks=[0,1,2,3])
ax.grid(True)
ax.legend(ncol=3, loc="upper left")
note(fig.supxlabel("$x_0=0$，$u_t=0.4$，$\mathrm{Var}(w_t)=0.04$，$\mathrm{Var}(v_t)=0.09$；读数从 $t=1$ 开始。", fontsize=8))
save(fig, "temperature-state-observation")

fig = plt.figure(figsize=(169/25.4, 97/25.4), layout="constrained")
grid = fig.add_gridspec(2, 3, height_ratios=[1,.22])
for i, (method, label, color, end) in enumerate([
    ("pred", "一步预测", BLUE, 11), ("filter", "当前滤波", GREEN, 12), ("smooth", "事后平滑", PURPLE, 24)]):
    ax = fig.add_subplot(grid[0,i])
    ax.fill_between(t, temperature[method+"_low"], temperature[method+"_high"], color={BLUE: BLUE_FILL, GREEN: GREEN_FILL, PURPLE: PURPLE_FILL}[color], label="$95\%$区间")
    ax.plot(t, temperature["state"], color=MUTED, lw=.6, label="真实状态")
    ax.plot(t, temperature["observation"], color=MUTED, ls="none", marker="o", mfc="white", ms=2.5, label="带噪读数")
    ax.plot(t, temperature[method], color=color, label="估计均值")
    ax.set(title=label, xlabel="$t$", xlim=(-.25,24.5), ylim=(-.25,3.2), xticks=[0,12,24], yticks=[0,1,2,3])
    ax.grid(True)
    if i==0:ax.legend(loc="upper left", fontsize=8, ncol=2)
    timeline = fig.add_subplot(grid[1,i])
    timeline.plot([1,24],[0,0], color=GRID, lw=2)
    timeline.plot([1,end],[0,0], color=color, lw=2)
    timeline.plot([12,12],[-.2,.2], color=STROKE, lw=.7)
    timeline.set(xlim=(0,25), ylim=(-.6,.6), xticks=[1,12,24], yticks=[], xlabel=f"可用于估计 $x_{{12}}$ 的读数：$y_1,\\ldots,y_{{{end}}}$")
    note(timeline.xaxis.label)
    for spine in timeline.spines.values():spine.set_visible(False)
    timeline.tick_params(length=0)
save(fig, "temperature-inference")

ou = np.genfromtxt(BASE / "dynamics/ou.tsv", delimiter="\t", names=True)
fig, (ax, density) = plt.subplots(1,2, figsize=(169/25.4,77/25.4), gridspec_kw={"width_ratios":[1.8,1]}, layout="constrained")
for name, ls in zip(["path2", "path3", "path4"], ["--", ":", "-."]):
    ax.plot(ou["t"], ou[name], color=BLUE, ls=ls, lw=.7)
ax.plot(ou["t"], ou["path1"], color=BLUE)
ax.plot(ou["t"], ou["mean"], color=STROKE, ls="--", lw=.9, label="理论均值 $e^{-t}$")
ax.axvline(.5, color=GREEN, ls=":", lw=.7)
ax.axvline(2, color=PURPLE, ls=":", lw=.7)
ax.set(title="轨迹：共享一个时间演化规律", xlabel="时刻 $t$", ylabel="$X_t$",
       xlim=(0,4), ylim=(-1.1,1.4), xticks=[0,.5,2,4], yticks=[-1,0,1])
ax.grid(True)
ax.legend(loc="lower left")
x = np.linspace(-1.1,1.7,120)
densities = {}
for time, color, linestyle in [(.5,GREEN,"-"),(2,PURPLE,"--")]:
    y = np.exp(-(x-np.exp(-time))**2 / (.36*(1-np.exp(-2*time)))) / np.sqrt(np.pi*.36*(1-np.exp(-2*time)))
    densities[str(time)] = y.tolist()
    density.plot(x,y,color=color,ls=linestyle,label=f"$t={time:g}$")
density.set(title="截面：固定时刻的分布", xlabel="状态 $x$", ylabel="$p_t(x)$",
            xlim=(-1.1,1.7), ylim=(0,1.3), xticks=[-1,0,1], yticks=[0,.5,1])
density.grid(True)
density.legend()
note(fig.supxlabel("四条精确网格模拟，共用同一个随机过程模型。", fontsize=8))
save(fig, "ou-paths-sections")

control = np.genfromtxt(BASE / "control/temperature.tsv", delimiter="\t", names=True)
fig, axes = plt.subplots(2,2, figsize=(169/25.4,110/25.4), layout="constrained")
for col, (suffix,title) in enumerate([("fixed","(a) 固定设定值"),("moving","(b) 运动参考")]):
    ax = axes[0,col]
    ax.plot(control["t"], control["r_"+suffix], color=PURPLE, ls="--", label="参考 $r_t$")
    ax.plot(control["t"], control["x_"+suffix], color=BLUE, marker="o", ms=2.5, markevery=2, label="状态 $x_t$")
    ax.set(title=title, xlim=(-.25,24.5), ylim=(-.04,2.7), xticks=[0,8,16,24], yticks=[0,1,2], ylabel="温差")
    ax.grid(True)
    ax.legend(loc="lower right")
    ax = axes[1,col]
    ax.plot(control["t"], control["ur_"+suffix], color=PURPLE, ls="--", label="前馈 $u_t^r$")
    ax.plot(control["t"], control["u_"+suffix], color=GREEN, marker="s", ms=2.5, markevery=2, label="输入 $u_t$")
    ax.set(xlim=(-.25,24.5), ylim=(0,1.3), xticks=[0,8,16,24], yticks=[0,.4,.8,1.2], xlabel="时刻 $t$", ylabel="归一化加热量")
    ax.grid(True)
    ax.legend(loc="upper right")
    if col==1:ax.text(2,1.18,"$u_0\\approx1.153$",fontsize=8)
note(fig.supxlabel("$x_0=0$，$e_t=-2(0.5)^t$；无噪声、无输入幅值限制。", fontsize=8))
save(fig, "temperature-regulation-tracking")

policy_data = {"t":[0,1,2], "fixed":[0,.4,.72], "feedback":[0,1,1.5],
               "feedback_cost":[5.25,1.49,6.74], "fixed_cost":[8.1984,.32,8.5184]}
fig, (ax,cost) = plt.subplots(1,2, figsize=(169/25.4,85/25.4), layout="constrained")
ax.axhline(2,color=PURPLE,ls="--",label="目标 $r=2$")
ax.plot(policy_data["t"],policy_data["fixed"],color=GREEN,ls="--",marker="s",ms=3,label="固定 $u=0.4$")
ax.plot(policy_data["t"],policy_data["feedback"],color=BLUE,marker="o",ms=3,label="反馈 $u=0.4-0.3(x-2)$")
ax.set(title="(a) 同一初态下的状态轨迹", xlabel="时刻 $t$", ylabel="温差 $x_t$", xlim=(-.05,2.05), ylim=(-.04,2.3), xticks=[0,1,2], yticks=[0,.5,1,1.5,2])
ax.text(1.88,1.56,"$1.5$",color=BLUE,ha="right",fontsize=8)
ax.text(1.88,.78,"$0.72$",color=GREEN,ha="right",fontsize=8)
ax.grid(True)
ax.legend(loc="upper left",bbox_to_anchor=(0.02,0.85),fontsize=8)
positions = np.arange(3)
for offset,color,values,label in [(-.17,BLUE,policy_data["feedback_cost"],"反馈策略"),(.17,GREEN,policy_data["fixed_cost"],"固定策略")]:
    bars=cost.bar(positions+offset,values,width=.30,color={BLUE: BLUE_FILL, GREEN: GREEN_FILL}[color],edgecolor=color,label=label)
    cost.bar_label(bars,fmt="%.2f",padding=3,fontsize=8)
cost.set(title="(b) 两步累计成本",ylabel="成本",ylim=(0,12.3),xticks=positions,xticklabels=["舒适偏差","输入平方","总成本"],yticks=[0,2,4,6,8])
cost.set_axisbelow(True)
cost.grid(axis="y")
cost.legend(loc="upper left")
note(fig.supxlabel("$x_0=0$，$H=2$；无噪声。舒适偏差含终端项，输入平方仅计两次行动。", fontsize=8))
save(fig, "temperature-policy-comparison")

tables = [BASE/"dynamics/temperature.tsv", BASE/"dynamics/ou.tsv", BASE/"control/temperature.tsv"]
provenance = {"tables":[{"file":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in tables],
              "samplers":[str((BASE/p).relative_to(ROOT)) for p in ["dynamics/render.py","control/render.py"]],
              "policy_source":str((BASE/"value-optimization/temperature-policy-comparison.tex").relative_to(ROOT)),
              "style":style_record(),"exports":["vector PDF","vector SVG","PNG 300 dpi"],"resampling":False}
(HERE / "sources.json").write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+"\n")
(HERE / "data.json").write_text(json.dumps({"policy":policy_data,"OU_density":{"x":x.tolist(),"density":densities,
    "formula":"exp(-(x-exp(-t))^2/(.36*(1-exp(-2*t))))/sqrt(pi*.36*(1-exp(-2*t)))"}},ensure_ascii=False,indent=2)+"\n")
