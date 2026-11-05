"""Reproduce the rank-error and nonnormal transient-growth examples.

The rank errors retain the numerical precision shown in the original source;
the transient sequence is evaluated from its original closed-form recurrence.
"""
from pathlib import Path
import hashlib
import json
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").exists())
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
sys.path.insert(0, str(ROOT / "figures/00-shared"))
from resource_paths import asset_path
from plot_style import BLUE, RED, STROKE, configure, prepare_figure, style_record
from plot_style import BLUE, GREEN, YELLOW, RED, PURPLE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
configure()

def export(fig, name):
    prepare_figure(fig)
    for suffix in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{name}.{suffix}", dpi=300)
    plt.close(fig)

rank = np.arange(5)
spectral = np.array([8, 3, 1, .2, 0])
frobenius = np.array([8.604650, 3.168596, 1.019804, .2, 0])
fig, (ax, detail) = plt.subplots(1, 2, figsize=(112/25.4, 68/25.4),
                                gridspec_kw={"width_ratios": [3, 1]}, layout="constrained")
ax.plot(rank, spectral, color=BLUE, marker="o", markersize=3, label="谱误差")
ax.plot(rank, frobenius, color=GREEN, linestyle="--", marker="o", markerfacecolor="white", markersize=4, label="Frobenius误差")
ax.axhline(1, color=STROKE, lw=.6, ls="--")
ax.set(xlabel="$k$", ylabel="误差", xticks=rank, yticks=[1, 4, 8], ylim=(-.15, 9.2))
ax.legend(loc="upper right", fontsize=8)
detail.scatter([0], [spectral[2]], color=BLUE, s=18)
detail.scatter([0], [frobenius[2]], facecolor="white", edgecolor=GREEN, s=26)
detail.axhline(1, color=STROKE, lw=.6, ls="--")
detail.set(title="$k=2$ 局部放大", ylim=(.98, 1.04), xlim=(-.5, 1), xticks=[], yticks=[1, 1.02])
detail.annotate("$1$", (0, 1), (.3, .991), fontsize=8, arrowprops={"arrowstyle":"-", "color":BLUE,"lw":.5})
detail.annotate("$1.0198$", (0, 1.019804), (.15, 1.032), fontsize=8, arrowprops={"arrowstyle":"-", "color":GREEN,"lw":.5})
export(fig, "error-rank-curves")

k = np.arange(21)
x1 = 40/3 * (.8**k - .5**k)
x2 = .5**k
norm = np.hypot(x1, x2)
fig, (ax, axnorm) = plt.subplots(1, 2, figsize=(169/25.4, 77/25.4), layout="constrained")
ax.plot(x1, x2, color=BLUE)
for i in [0, 1]:
    ax.annotate("", (x1[i+1], x2[i+1]), (x1[i], x2[i]),
                arrowprops={"arrowstyle":"->", "color":BLUE, "lw":1.1})
for i in [0, 1, 2, 3, 6, 12]:
    ax.plot(x1[i], x2[i], "o", color=BLUE, ms=3)
    if i != 3:
        ax.annotate("$k=0$" if i == 0 else f"${i}$", (x1[i], x2[i]), xytext=(5, 4), textcoords="offset points", fontsize=8)
ax.set(title="同一初值的二维轨迹", xlabel="$x_1$", ylabel="$x_2$", xlim=(-.3, 6), ylim=(-.12, 1.18), xticks=[0, 2, 4], yticks=[0, .5, 1])
axnorm.plot(k[:17], norm[:17], color=RED)
axnorm.plot(k[[0,1,2,3,6,12,16]], norm[[0,1,2,3,6,12,16]], "o", color=RED, ms=3)
axnorm.axhline(1, color=STROKE, ls="--", lw=.6)
axnorm.annotate("$k=2$", (2, norm[2]), (3, 5.6), fontsize=8)
axnorm.set(title="长度先增大，再衰减", xlabel="$k$", ylabel="$\|\mathbf{x}^{(k)}\|_2$", xlim=(-.5, 17), ylim=(-.3, 6), xticks=[0,4,8,12,16], yticks=[0,1,5])
fig.supxlabel("矩阵元素（按行）：0.8，4；0，0.5；初态 $(0,1)$；谱半径 $0.8$。", fontsize=8)
export(fig, "transient-growth")

data = {"rank_error": {"k":rank.tolist(), "spectral":spectral.tolist(), "frobenius":frobenius.tolist()},
        "transient_growth": {"A":[[.8,4],[0,.5]], "initial":[0,1], "k":k.tolist(), "x1":x1.tolist(), "x2":x2.tolist(), "norm":norm.tolist(),
                             "formula":"x1(k)=40/3*(0.8^k-0.5^k); x2(k)=0.5^k"}}
data_path = asset_path(HERE, "data.json")
data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n")
sources = [f"figures/01-mathematical-preliminaries-upper/00-shared/tikz/linear-space/{name}.tex" for name in ["error-rank-curves", "transient-growth"]]
(asset_path(HERE, "sources.json")).write_text(json.dumps({"sources":sources, "data_sha256":hashlib.sha256(data_path.read_bytes()).hexdigest(), "style":style_record(), "exports":["pdf", "svg", "png300dpi"]}, ensure_ascii=False, indent=2)+"\n")
