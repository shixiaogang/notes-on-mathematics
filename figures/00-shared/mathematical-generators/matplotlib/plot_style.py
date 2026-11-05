"""Shared scientific plot style for the book.

Native TeX diagrams use the global tex/styles/figure-style.tex.
These settings give the existing Matplotlib generators the same font families,
regular-weight labels, muted palette and visual hierarchy. Plot geometry,
analytic evaluations and final physical sizes belong to each generator.
"""
from pathlib import Path

import matplotlib as mpl
from matplotlib import font_manager
from matplotlib.text import Text

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
BLUE, RED, YELLOW = "#7998AD", "#D57B70", "#D6B35D"
INK, STROKE, MUTED, GRID = "#222222", "#4C4D4F", "#747A80", "#C8CDCF"
BLUE_FILL, RED_FILL, YELLOW_FILL = "#EDF2F5", "#F8E8E5", "#FFF1CF"
CN_FILE = ROOT / "fonts/LXGWWenKai-Regular.ttf"
EN_FILE = ROOT / "fonts/SourceSans3-Regular.otf"
CN = font_manager.FontProperties(fname=CN_FILE).get_name()
EN = font_manager.FontProperties(fname=EN_FILE).get_name()


def configure():
    """Set defaults before constructing any axes, without touching plot data."""
    for filename in (CN_FILE, EN_FILE, ROOT / "fonts/STIXTwoText-Regular.otf"):
        font_manager.fontManager.addfont(filename)
    mpl.rcParams.update({
        "font.family": [EN, CN], "font.size": 8.5, "font.weight": "normal",
        "axes.labelsize": 8.5, "axes.titlesize": 9,
        "axes.labelweight": "normal", "axes.titleweight": "normal",
        "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 8,
        "mathtext.fontset": "stix", "axes.unicode_minus": False,
        "text.usetex": False, "pdf.fonttype": 3, "ps.fonttype": 3,
        "svg.fonttype": "path", "text.color": INK,
        "axes.labelcolor": INK, "axes.edgecolor": STROKE,
        "axes.linewidth": .9, "axes.spines.top": False,
        "axes.spines.right": False, "xtick.color": STROKE,
        "ytick.color": STROKE, "xtick.major.width": .6,
        "ytick.major.width": .6, "xtick.minor.width": .6,
        "ytick.minor.width": .6, "grid.color": GRID,
        "grid.linewidth": .5, "grid.alpha": 1,
        "lines.linewidth": 1.1, "patch.linewidth": 1,
        "legend.frameon": False, "figure.facecolor": "white",
        "axes.facecolor": "white", "savefig.facecolor": "white",
    })


def prepare_figure(fig):
    """Resolve CJK/math fallback and shared details before every export.

    Matplotlib mathtext uses its first text family for text outside $...$;
    Chinese/math labels therefore need WenKai first, while purely Latin text
    and numerical ticks use Source Sans 3 first. The PDF uses vector Type 3
    glyph programs because Source Sans 3 has CFF outlines.
    """
    for ax in fig.axes:
        for spine in ax.spines.values():
            spine.set_color(STROKE)
            spine.set_linewidth(.9)
        ax.tick_params(which="both", width=.6, colors=STROKE, labelsize=8)
        for line in ax.get_xgridlines() + ax.get_ygridlines():
            line.set_color(GRID)
            line.set_linewidth(.5)
            line.set_alpha(1)
    for text in fig.findobj(Text):
        content = text.get_text()
        has_cjk = any("\u2e80" <= ch <= "\u9fff" or
                      "\ufeff" <= ch <= "\uffef" for ch in content)
        # Ordinary Text uses per-glyph fallback, so English stays Source Sans.
        # Mathtext requires the CJK face first for Chinese/full-width text
        # outside the mathematical spans (including e.g. a full-width colon).
        text.set_fontfamily([CN, EN] if has_cjk and "$" in content else [EN, CN])
        text.set_fontweight("normal")
        text.set_fontsize(min(9, max(8, text.get_fontsize())))


def style_record():
    return {
        "scope": "全书",
        "native_style": "tex/styles/figure-style.tex",
        "plot_reference": "figures/06-foundations/02-learning-theory/matplotlib/volume1-risk-and-shift.py",
        "shared_generator_style": "figures/00-shared/mathematical-generators/matplotlib/plot_style.py",
        "fonts": {"Chinese": "fonts/LXGWWenKai-Regular.ttf",
                  "Latin_and_numbers": "fonts/SourceSans3-Regular.otf",
                  "math": "STIX mathtext (shared book font family)"},
        "label_weight": "Regular", "label_size_pt": [8, 9],
        "palette": {"blue": BLUE, "red": RED, "yellow": YELLOW,
                    "ink": INK, "stroke": STROKE, "muted": MUTED,
                    "grid": GRID, "blue_fill": BLUE_FILL,
                    "red_fill": RED_FILL, "yellow_fill": YELLOW_FILL},
        "series_colors": {"one": [YELLOW], "two": [BLUE, RED],
                          "three": [BLUE, RED, YELLOW]},
        "line_width_pt": {"main": 1.1, "axes": .9, "grid": .5,
                          "auxiliary": .6},
        "pdf_fonttype": 3, "svg_fonttype": "path",
        "background": "white",
    }
