"""教学图：二次型水平集的三种情形——正定、半正定、不定。

解析式固定构造：
(a) 正定 f=x^2+2y^2：椭圆同心，唯一无约束极小在原点；
(b) 半正定 f=x^2：水平集退化为两条平行线（槽），极小值集合是整条 y 轴；
(c) 不定 f=x^2-y^2：双曲线，原点是鞍点。
无随机数，不调用 LaTeX。从任意目录运行：python3 plots.py [--only ...]
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW, RED = "#7188A3", "#829C8B", "#B4A16F", "#A7787D"
INK, MUTED, GRID, STROKE = "#3B4252", "#6B7280", "#D8DCE2", "#4C4D4F"
BLUE_FILL, RED_FILL, GREEN_FILL, YELLOW_FILL = "#E5EAF0", "#F0E5E6", "#E8EEE9", "#F1ECDD"
CN_MAIN, CN_AUX, EN = "Source Han Sans SC", "LXGW WenKai", "Fira Math"

matplotlib.rcParams.update({
    "font.family": [EN, CN_MAIN], "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": EN, "mathtext.it": EN,
    "mathtext.bf": EN, "mathtext.sf": EN,
    "axes.unicode_minus": False, "text.color": INK, "axes.labelcolor": INK,
    "axes.edgecolor": STROKE, "axes.linewidth": .75,
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": STROKE, "ytick.color": STROKE,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "grid.color": GRID, "grid.linewidth": .4,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 3, "svg.fonttype": "path",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, (a, b, c) = plt.subplots(1, 3, figsize=(169 / 25.4, 58 / 25.4))

# ---- (a) 正定：椭圆 ----
th = np.linspace(0, 2 * np.pi, 120)
for k, col in zip((0.5, 1.0, 2.0, 3.5), (BLUE, BLUE, BLUE, BLUE)):
    a.plot(np.sqrt(k) * np.cos(th), np.sqrt(k / 2) * np.sin(th),
           color=col, lw=.9)
a.plot(0, 0, "o", ms=5, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
a.text(0.12, -0.35, "无约束极小", fontsize=7.5, color=YELLOW)
a.set_title("(a) 正定 $f=x^2+2y^2$：椭圆", fontsize=8)
a.set(xlim=(-2.2, 2.2), ylim=(-1.8, 1.8), xticks=range(-2, 3), yticks=range(-1, 2))
a.set_aspect("equal")
a.grid(True)

# ---- (b) 半正定：平行直线槽 ----
for k in (0.5, 1.0, 1.5):
    x = np.sqrt(k)
    b.plot([x, x], [-1.6, 1.6], color=BLUE, lw=.9)
    b.plot([-x, -x], [-1.6, 1.6], color=BLUE, lw=.9)
b.axhline(0, color=GREEN, lw=1.0)
b.plot(0, 0, "o", ms=5, mfc=YELLOW, mec=INK, mew=.5, zorder=5)
b.text(0.12, -1.35, "极小值集合：整条 $y$ 轴", fontsize=7.5, color=GREEN)
b.set_title("(b) 半正定 $f=x^2$：平行线槽", fontsize=8)
b.set(xlim=(-2.2, 2.2), ylim=(-1.8, 1.8), xticks=range(-2, 3), yticks=range(-1, 2))
b.set_aspect("equal")
b.grid(True)

# ---- (c) 不定：双曲线 ----
xs = np.linspace(-2.4, 2.4, 200)
for k, col in ((1.0, BLUE), (2.0, BLUE)):
    xr = np.sqrt(k)
    branch = np.linspace(xr, 2.5, 80)
    c.plot(branch, np.sqrt(branch**2 - k), color=col, lw=.9)
    c.plot(branch, -np.sqrt(branch**2 - k), color=col, lw=.9)
    c.plot(-branch, np.sqrt(branch**2 - k), color=col, lw=.9)
    c.plot(-branch, -np.sqrt(branch**2 - k), color=col, lw=.9)
c.plot(0, 0, "o", ms=5, mfc=RED, mec=INK, mew=.5, zorder=5)
c.text(0.12, 0.35, "鞍点", fontsize=7.5, color=RED)
c.text(-2.35, -1.55, "沿 $x$ 方向升高，沿 $y$ 方向下降", fontsize=7.5, color=MUTED)
c.set_title("(c) 不定 $f=x^2-y^2$：双曲线", fontsize=8)
c.set(xlim=(-2.6, 2.6), ylim=(-1.9, 1.9), xticks=range(-2, 3), yticks=range(-1, 2))
c.set_aspect("equal")
c.grid(True)

finalize(fig)
fig.tight_layout()
if selection == NAME:
    for ext in ("pdf", "svg", "png"):
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "二次型的水平集形状怎样编码正定、半正定与不定？",
    "formula": "(a) f=x^2+2y^2>0 (x!=0)，唯一极小在原点；"
               "(b) f=x^2>=0，极小值 0 取遍整条 y 轴；"
               "(c) f=x^2-y^2，原点沿 x 是谷、沿 y 是脊，为鞍点。",
    "parameters": {
        "positive_definite": "f=x^2+2y^2，椭圆水平集 k in {0.5,1,2,3.5}",
        "semidefinite": "f=x^2，竖直线 x=±sqrt(k)，k in {0.5,1,1.5}",
        "indefinite": "f=x^2-y^2，双曲线 x^2-y^2=k，k in {1,2}",
    },
    "evaluated_data": {
        "PD_minimum": "(0,0)", "PSD_min_set": "{(0,y): y in R}",
        "indefinite_saddle": "(0,0)",
    },
    "processing": "解析曲线直接求值；无随机采样。",
    "width_mm": 169, "height_mm": 58, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
