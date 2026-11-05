"""Analytic teaching constructions for the reader audit of chapters 6--13.

No experimental observations or external datasets are used.  Run from any
directory with Matplotlib and NumPy; fonts and plot style come from the repo.
"""
from pathlib import Path
import hashlib
import json
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
sys.path.insert(0, str(ROOT / 'figures/00-shared/mathematical-generators/matplotlib'))
from plot_style import (BLUE, RED, YELLOW, INK, MUTED, BLUE_FILL,
                        configure, prepare_figure, style_record)

configure()
RECORDS = []


def save(fig, name, size_mm, facts, source):
    fig.set_size_inches(np.array(size_mm) / 25.4)
    prepare_figure(fig)
    exports = {}
    for suffix in ('pdf', 'svg', 'png'):
        path = asset_path(OUT, f'{name}.{suffix}')
        fig.savefig(path, dpi=220)
        exports[suffix] = {'path': str(path.relative_to(ROOT)),
                           'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    RECORDS.append({'name': name, 'size_mm': size_mm,
                    'construction': '解析教学构造；无实验数据',
                    'facts': facts, 'chapter_source': source,
                    'exports': exports})
    plt.close(fig)


def cech_rips():
    side = .9
    h = np.sqrt(3)*side/2
    vertices = np.array([[-side/2, 0], [side/2, 0], [0, h]])
    center = np.array([0, h/3])
    fig, ax = plt.subplots()
    fig.subplots_adjust(left=.04, right=.96, bottom=.06, top=.91)
    for p in vertices:
        ax.add_patch(Circle(p, .5, facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1, alpha=.72))
    ax.add_patch(Polygon(vertices, fill=False, edgecolor=RED, lw=1.1))
    ax.scatter(vertices[:, 0], vertices[:, 1], c=INK, s=18, zorder=4)
    for text, p, offset in zip(['$v_1$', '$v_2$', '$v_3$'], vertices,
                               [(-.15, -.11), (.06, -.11), (.05, .04)]):
        ax.text(*(p + offset), text)
    ax.plot([0, 0], [center[1], h], color=MUTED, ls='--', lw=.6)
    ax.scatter(*center, c=INK, s=17, marker='x', linewidth=.6, zorder=5)
    ax.annotate(r'$0.9/\sqrt{3}>0.5$', xy=center, xytext=(.52, .93),
                arrowprops={'arrowstyle': '-', 'color': MUTED, 'lw': .6},
                ha='left', color=INK)
    fig.text(.5, .035, '三对球分别相交，三球没有共同交点', ha='center', color=INK)
    ax.set_title('两两相交与共同相交')
    ax.set(xlim=(-1.0, 1.05), ylim=(-.55, 1.31))
    ax.set_aspect('equal'); ax.axis('off')
    save(fig, 'geometry-cech-rips-intersection', [112, 81],
         {'epsilon': 1., 'equilateral_side': .9, 'ball_radius': .5,
          'vertices': vertices.tolist(), 'circumcenter': center.tolist(),
          'minimum_enclosing_radius': float(side/np.sqrt(3)),
          'cech_has_edges': True, 'cech_has_2_simplex': False,
          'rips_has_2_simplex': True, 'balls': 'open; boundary excluded'},
         'tex/01-mathematical-preliminaries-upper/02-linear-algebra-and-geometry/02-differential-geometry-and-symmetry.tex')


def kernel_distinguishability():
    fig, axes = plt.subplots(1, 2)
    fig.subplots_adjust(left=.07, right=.985, bottom=.23, top=.84, wspace=.32)
    ax = axes[0]
    ax.vlines([0], 0, [1], color=BLUE, lw=1.1)
    ax.scatter([0], [1], color=BLUE, s=20, zorder=3, label=r'$P=\delta_0$')
    ax.vlines([-1, 1], 0, [.5, .5], color=RED, lw=1.1, ls='--')
    ax.scatter([-1, 1], [.5, .5], color=RED, marker='s', s=20, zorder=3,
               label=r'$Q=(\delta_{-1}+\delta_1)/2$')
    ax.set(xlim=(-1.4, 1.4), ylim=(0, 1.55), xlabel='$x$', ylabel='概率质量')
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, .5, 1])
    ax.set_title('支持不同，两者均值均为零')
    ax.legend(loc='upper center', frameon=False, handlelength=1.4)
    ax = axes[1]
    mmd_squared = 1.5 + .5*np.exp(-2) - 2*np.exp(-.5)
    ax.bar([0, 1], [0, np.sqrt(mmd_squared)], color=YELLOW, width=.48)
    ax.scatter([0], [0], color=YELLOW, s=20, zorder=3)
    ax.text(0, .035, '$0$', ha='center')
    ax.text(1, np.sqrt(mmd_squared)+.025, f'{np.sqrt(mmd_squared):.3f}', ha='center')
    ax.set(ylim=(0, .75), ylabel='总体MMD')
    ax.set_xticks([0, 1], ['线性核\n$xy$', '高斯核\n$e^{-(x-y)^2/2}$'])
    ax.set_yticks([0, .2, .4, .6])
    ax.set_title('可辨别哪些差异取决于核')
    save(fig, 'information-kernel-distinguishability', [169, 68],
         {'P_support': [0], 'P_mass': [1], 'Q_support': [-1, 1],
          'Q_mass': [.5, .5], 'means': [0, 0],
          'linear_kernel': 'x*y', 'linear_mmd': 0,
          'gaussian_kernel': 'exp(-(x-y)**2/2)',
          'gaussian_mmd_squared': '1.5 + 0.5*exp(-2) - 2*exp(-0.5)',
          'gaussian_mmd': float(np.sqrt(mmd_squared)),
          'estimation': 'exact population expectations; no sample estimator'},
         'tex/04-manifolds-distributions-and-inference/02-probability-distributions/02-information-theory-and-statistical-geometry.tex')


if __name__ == '__main__':
    cech_rips()
    kernel_distinguishability()
    record = {'style': style_record(), 'figures': RECORDS,
              'generator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'shared_style_sha256': hashlib.sha256((ROOT / 'figures/00-shared/mathematical-generators/matplotlib/plot_style.py').read_bytes()).hexdigest()}
    (asset_path(OUT, 'sources.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
