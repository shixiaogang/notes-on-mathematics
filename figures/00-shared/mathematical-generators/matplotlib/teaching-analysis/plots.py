"""Analytic teaching figures for the first mathematical part.

Run with Python, NumPy and Matplotlib. No TeX or book build is invoked.
All functions, finite patterns and parameters are recorded in sources.json.
"""
from pathlib import Path
import itertools
import json
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared/mathematical-generators/matplotlib'))
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
from plot_style import configure, prepare_figure, style_record
from plot_style import BLUE, RED, YELLOW, INK, STROKE, MUTED, GRID, YELLOW_FILL

configure()
RECORDS = []
MM = 1 / 25.4


def new_figure(width, height, **kwargs):
    return plt.subplots(figsize=(width * MM, height * MM), **kwargs)


def save(fig, name, formulas, parameters, data, purpose):
    prepare_figure(fig)
    for ext in ('pdf', 'svg', 'png'):
        fig.savefig(asset_path(HERE, f'{name}.{ext}'), dpi=300)
    RECORDS.append({
        'name': name, 'source': 'Analytic teaching construction; no empirical data',
        'reader_task': purpose, 'formulas': formulas, 'parameters': parameters,
        'evaluated_data': data, 'size_mm': [round(v / MM, 3) for v in fig.get_size_inches()],
        'outputs': [f'{name}.{ext}' for ext in ('pdf', 'svg', 'png')],
        'generator': 'plots.py', 'style': style_record(),
    })
    plt.close(fig)


def mobius():
    subsets = [(), (1,), (3,), (1, 3)]
    g = [2 * len(s) + 3 * int({1, 3}.issubset(s)) for s in subsets]
    h = [sum((-1) ** (len(s) - len(t)) * g[i] for i, t in enumerate(subsets)
             if set(t).issubset(s)) for s in subsets]
    assert g == [0, 2, 2, 7] and h == [0, 2, 2, 3]
    fig, ax = new_figure(112, 64)
    x = np.arange(4)
    for offset, values, color, label in [(-.18, g, BLUE, '累计 $g$'), (.18, h, RED, '局部 $h$')]:
        ax.bar(x + offset, values, width=.32, color=color, edgecolor=STROKE, linewidth=.6, label=label)
        for xx, yy in zip(x + offset, values):
            ax.text(xx, yy + .18, str(yy), ha='center', va='bottom')
    ax.set_xticks(x, [r'$\varnothing$', r'$\{1\}$', r'$\{3\}$', r'$\{1,3\}$'])
    ax.set_ylim(0, 8.6); ax.set_yticks([0, 2, 4, 6, 8]); ax.set_ylabel('贡献值')
    ax.legend(loc='upper left', ncols=2)
    fig.subplots_adjust(left=.14, right=.98, bottom=.2, top=.96)
    save(fig, 'combinatorics-mobius-cumulative-local', ['g(S)=2|S|+3 I({1,3} subset S)',
         'h(S)=sum_{T subset S} (-1)^{|S|-|T|} g(T)'], {'subsets': subsets},
         {'g': g, 'h': h}, 'Distinguish accumulated subset values from newly contributed interaction.')


def fat_square():
    fig, axes = new_figure(169, 70, ncols=2)
    points = {}
    for ax, gamma in zip(axes, [.5, 1.2]):
        for sx, sy in itertools.product([-1, 1], repeat=2):
            lo_x, hi_x = (gamma, 1.42) if sx > 0 else (-1.42, -gamma)
            lo_y, hi_y = (gamma, 1.42) if sy > 0 else (-1.42, -gamma)
            ax.add_patch(Rectangle((lo_x, lo_y), hi_x-lo_x, hi_y-lo_y,
                                  facecolor=YELLOW_FILL, edgecolor='none'))
            ax.plot(sx * gamma, sy * gamma, 'o', color=YELLOW, ms=4.5,
                    mfc=YELLOW if gamma <= 1 else 'white', mew=.9)
        ax.add_patch(Rectangle((-1, -1), 2, 2, fill=False, edgecolor=STROKE, linewidth=1))
        ax.axvline(0, lw=.6, color=MUTED); ax.axhline(0, lw=.6, color=MUTED)
        ax.set(xlim=(-1.42, 1.42), ylim=(-1.42, 1.42), aspect='equal',
               xticks=[-1, 0, 1], yticks=[-1, 0, 1], xlabel=r'$f(x_1)$', ylabel=r'$f(x_2)$')
        ax.set_title(r'$B=1,\ \gamma=' + str(gamma) + '$')
        points[str(gamma)] = [[sx*gamma, sy*gamma] for sx, sy in itertools.product([-1, 1], repeat=2)]
    fig.subplots_adjust(left=.065, right=.98, bottom=.2, top=.85, wspace=.3)
    save(fig, 'combinatorics-fat-margin-output-square',
         ['allowed outputs: [-B,B]^2', 'thresholds r1=r2=0', 'signed output >= gamma'],
         {'B': 1, 'gamma': [.5, 1.2], 'thresholds': [0, 0]}, {'required_boundary_points': points},
         'Distinguish output-class amplitude bounds from the separation margin required for all signs.')


def power_convergence():
    x = np.linspace(0, 1, 501); n = np.arange(1, 101)
    fig, axes = new_figure(169, 67, ncols=2)
    for k, color, ls in zip([2, 8, 32], [BLUE, RED, YELLOW], ['-', '--', '-.']):
        axes[0].plot(x, x**k, color=color, ls=ls, label=f'$n={k}$')
    axes[0].plot([0, 1], [0, 0], color=MUTED, lw=.6)
    axes[0].plot(1, 0, 'o', color=MUTED, mfc='white', ms=4, mew=.6)
    axes[0].plot(1, 1, 'o', color=MUTED, ms=4)
    axes[0].set(xlim=(-.02, 1.04), ylim=(-.04, 1.08), xticks=[0, .5, 1],
                yticks=[0, .5, 1], xlabel='$x$', ylabel='函数值')
    axes[0].legend(loc='upper left', handlelength=1.7)
    axes[1].plot(n, (2*n+1)**-.5, color=YELLOW, label=r'$L^2$误差')
    axes[1].axhline(1, color=MUTED, lw=.6, ls='--', label='上确界误差')
    axes[1].set(xlim=(1, 100), ylim=(0, 1.08), xticks=[1, 25, 50, 100],
                yticks=[0, .5, 1], xlabel='$n$', ylabel='误差')
    axes[1].legend(loc='center right')
    fig.subplots_adjust(left=.07, right=.98, bottom=.2, top=.97, wspace=.34)
    save(fig, 'analysis-power-convergence-scales',
         ['f_n(x)=x^n on [0,1]', 'limit=0 for x<1; limit(1)=1',
          'sup|f_n-limit|=1 (not attained)', 'L2 error=(2n+1)^(-1/2)'],
         {'curve_n': [2, 8, 32], 'right_n': [1, 100], 'left_sampling': 501},
         {'x': x.tolist(), 'curves': {str(k): (x**k).tolist() for k in [2, 8, 32]},
          'n': n.tolist(), 'l2_error': ((2*n+1)**-.5).tolist()},
         'Locate moving worst inputs despite vanishing integrated error.')


def clarke():
    x = np.linspace(-1.2, 1.2, 501)
    fig, axes = new_figure(169, 67, ncols=2)
    for ax, sign in zip(axes, [1, -1]):
        ax.plot(x, sign*np.abs(x), color=BLUE)
        ax.axhline(0, color=RED, ls='--', lw=1.1)
        ax.plot(0, 0, 'o', color=BLUE, ms=4)
        ax.set(xlim=(-1.2, 1.2), ylim=(-1.25, 1.25), xticks=[-1, 0, 1],
               yticks=[-1, 0, 1], xlabel='$x$', ylabel='$f(x)$')
        ax.set_title('$|x|$' if sign > 0 else '$-|x|$')
    fig.subplots_adjust(left=.065, right=.98, bottom=.2, top=.86, wspace=.33)
    save(fig, 'analysis-clarke-stationarity-boundary',
         ['f_plus(x)=|x|', 'f_minus(x)=-|x|', 'Clarke subdifferentials at 0=[-1,1]',
          'g=0 is a global affine lower bound only for f_plus'], {},
         {'x': x.tolist(), 'absolute_value': np.abs(x).tolist()},
         'Separate a local generalized stationary condition from convex global minimization.')


def chord():
    x = np.linspace(-1.3, 2.3, 501)
    fig, ax = new_figure(112, 75)
    ax.plot(x, x*x/2, color=BLUE, label='$f$')
    xx = np.linspace(-1, 2, 301)
    ax.plot(xx, .5*xx+1, color=RED, label='弦')
    ax.plot(x, .5*x-.125, color=YELLOW, ls='--', label='切线')
    ax.plot([-1, 2], [.5, 2], 'o', ms=4, color=RED)
    ax.plot(.5, .125, 'o', ms=4, color=YELLOW)
    ax.set(xlim=(-1.3, 2.3), ylim=(-.85, 2.85), xlabel='$x$', ylabel='函数值',
           xticks=[-1, 0, .5, 2], yticks=[0, 1, 2])
    ax.legend(loc='upper left')
    fig.subplots_adjust(left=.14, right=.98, bottom=.18, top=.98)
    save(fig, 'optimization-convex-chord-tangent',
         ['f(x)=x^2/2', 'chord(x)=x/2+1 for -1<=x<=2',
          'tangent at .5: x/2-1/8'], {'u': -1, 'v': 2, 'x0': .5},
         {'x': x.tolist(), 'f': (x*x/2).tolist()},
         'Distinguish the finite chord upper bound from the global first-order affine lower bound.')


def majorizer():
    x = np.linspace(-.6, 2.1, 501)
    F = x*x/2; Q = .5+(x-1)+(x-1)**2; tangent = x-.5
    assert np.all(Q-F >= -1e-14)
    fig, ax = new_figure(112, 75)
    ax.plot(x, F, color=BLUE, label='$F$')
    ax.plot(x, Q, color=RED, label='$Q$')
    ax.plot(x, tangent, color=YELLOW, ls='--', label='切线')
    ax.plot(1, .5, 'o', ms=4, color=STROKE)
    ax.plot(.5, .25, 'o', ms=4, color=RED)
    ax.plot(.5, .125, 'o', ms=4, color=BLUE)
    ax.plot([.5, .5], [.125, .25], color=MUTED, lw=.6)
    ax.set(xlim=(-.6, 2.1), ylim=(-1.12, 2.95), xlabel='$x$', ylabel='函数值',
           xticks=[0, .5, 1, 2], yticks=[-1, 0, 1, 2])
    ax.legend(loc='upper left')
    fig.subplots_adjust(left=.14, right=.98, bottom=.18, top=.98)
    save(fig, 'optimization-majorizer-versus-tangent',
         ['F(x)=x^2/2', 'Q(x|1)=1/2+(x-1)+(x-1)^2', 'Q-F=(x-1)^2/2',
          'tangent=x-1/2', 'F(.5)=1/8 <= Q(.5|1)=1/4 <= F(1)=1/2'],
         {'current': 1, 'surrogate_minimizer': .5},
         {'x': x.tolist(), 'F': F.tolist(), 'Q': Q.tolist(), 'tangent': tangent.tolist()},
         'Show why matching value and slope cannot replace a majorizing upper bound.')


def point_readout():
    fig, ax = new_figure(112, 79)
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor=STROKE, linewidth=1))
    xs = np.linspace(-1.25, 1.4, 401)
    for value in [-1, 0, 1, 1.25]:
        ax.plot(xs, (value-xs)/.75, color=GRID, lw=.6)
    ax.annotate('', xy=(1, .75), xytext=(0, 0),
                arrowprops={'arrowstyle': '->', 'lw': 1.1, 'color': YELLOW})
    ax.plot(.8, .6, 'o', color=YELLOW, ms=4.5)
    ax.text(.8, 1.1, r'$(4/5,3/5)$', ha='center')
    ax.text(1.04, .67, r'$K_{3/4}$', ha='left', va='top')
    ax.axhline(0, color=MUTED, lw=.6); ax.axvline(0, color=MUTED, lw=.6)
    ax.set(xlim=(-1.3, 1.5), ylim=(-1.25, 1.25), aspect='equal',
           xlabel='$a$', ylabel='$b$', xticks=[-1, 0, 1], yticks=[-1, 0, 1])
    fig.subplots_adjust(left=.15, right=.98, bottom=.16, top=.97)
    save(fig, 'functional-affine-point-readout',
         ['f(x)=a+bx, RKHS norm^2=a^2+b^2', 'point value at z=.75: a+.75b',
          'K_z has coefficients (1,.75), norm=1.25', 'max on unit disk at (.8,.6), value=1.25'],
         {'z': .75, 'radius': 1, 'level_lines': [-1, 0, 1, 1.25]},
         {'kernel_coefficients': [1, .75], 'maximizing_coefficients': [.8, .6]},
         'Interpret a point evaluation as an inner-product direction in the function coefficient plane.')


def locality():
    x = np.linspace(0, 1, 501)
    bernstein = 6*x*x*(1-x)**2
    hat = np.maximum(1-np.abs(x-.5)/.25, 0)
    gaussian = np.exp(-((x-.5)**2)/(2*.12**2))
    fig, ax = new_figure(112, 75)
    ax.plot(x, bernstein, color=BLUE, label='Bernstein')
    ax.plot(x, hat, color=RED, ls='--', label='样条帽')
    ax.plot(x, gaussian, color=YELLOW, ls='-.', label='高斯基')
    ax.set(xlim=(0, 1), ylim=(-.02, 1.08), xlabel='$x$', ylabel='单位系数的函数增量',
           xticks=[0, .25, .5, .75, 1], yticks=[0, .5, 1])
    ax.legend(loc='upper left', handlelength=1.7)
    fig.subplots_adjust(left=.14, right=.98, bottom=.18, top=.98)
    save(fig, 'functional-basis-locality',
         ['B_{4,2}(x)=6x^2(1-x)^2', 'hat(x)=max(1-|x-.5|/.25,0)',
          'gaussian(x)=exp(-(x-.5)^2/(2*.12^2))'],
         {'domain': [0, 1], 'center': .5, 'hat_halfwidth': .25, 'gaussian_sigma': .12,
          'coefficient_increment': 1, 'normalization': 'none'},
         {'x': x.tolist(), 'bernstein': bernstein.tolist(), 'hat': hat.tolist(), 'gaussian': gaussian.tolist()},
         'Distinguish compact support, globally supported polynomials, and rapid Gaussian decay.')


def main():
    for function in [mobius, fat_square, power_convergence, clarke,
                     chord, majorizer, point_readout, locality]:
        function()
    record = {'purpose': 'Reader revision, first five mathematical chapters',
              'libraries': {'matplotlib': matplotlib.__version__, 'numpy': np.__version__},
              'figures': RECORDS}
    (HERE / 'sources.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(f'Exported {len(RECORDS)} analytic figures (PDF/SVG/PNG).')


if __name__ == '__main__':
    main()
