"""Analytic examples distinguishing continuity conditions; no empirical data."""
from pathlib import Path
import importlib.util
import json
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents
            if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
spec = importlib.util.spec_from_file_location('book_figure_support', ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py')
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)
OUT = Path(__file__).resolve().parent


def cantor_polygon(depth):
    # C_0(x)=x; each step copies the preceding graph into the outer thirds
    # with vertical scale 1/2 and inserts a constant middle third.
    x, y = np.array([0., 1.]), np.array([0., 1.])
    for _ in range(depth):
        x, y = np.r_[x/3, (2+x)/3], np.r_[y/2, (1+y)/2]
    return x, y


def load_data():
    unit = np.linspace(0., 1., 601)
    whole = np.linspace(-3., 3., 601)
    cx, cy = cantor_polygon(8)
    assert np.all(np.diff(cx) > 0) and np.all(np.diff(cy) >= 0)
    assert np.allclose([cy[0], cy[-1]], [0., 1.])
    return whole, unit, cx, cy


def build_figure(data):
    whole, unit, cx, cy = data
    fig, axs = s.figure(width_mm=169, height_mm=112, nrows=2, ncols=2)
    panels = [
        (whole, whole**2, '(a) 平方函数：实轴', '$x^2$',
         '局部 Lipschitz，连续\n不一致连续', (-3, 3), (0, 9.5)),
        (unit, unit**2, '(b) 平方函数：闭区间 [0, 1]', '$x^2$',
         'Lipschitz（L = 2）\n绝对连续、一致连续', (0, 1), (0, 1.05)),
        (unit, np.sqrt(unit), '(c) 平方根函数：[0, 1]', r'$\sqrt{x}$',
         '绝对连续、一致连续\n不满足 Lipschitz 条件', (0, 1), (0, 1.05)),
        (cx, cy, '(d) 康托尔函数：[0, 1]', '$C(x)$',
         '连续、一致连续\n不绝对连续', (0, 1), (0, 1.05)),
    ]
    for ax, (x, y, title, ylabel, note, xlim, ylim) in zip(axs.flat, panels):
        ax.plot(x, y, color=s.BLUE, linewidth=1.1)
        ax.set(xlim=xlim, ylim=ylim, xlabel='$x$', ylabel=ylabel, title=title)
        ax.grid(axis='y'); ax.set_axisbelow(True)
        ax.text(.04, .94, note, transform=ax.transAxes, va='top', fontsize=7.5,
                color=s.INK, bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1.5})
    # A fixed output gap while the input gap vanishes witnesses nonuniformity.
    ax=axs[0,0]
    ax.plot([2., 2.5], [4., 6.25], 'o', color=s.GREEN, markersize=3)
    ax.annotate('', (2.5,4.), (2.,4.), arrowprops={'arrowstyle':'|-|','color':s.GREEN,'linewidth':.75})
    axs[1,1].text(.98,.06,'曲线为八级折线近似',ha='right',transform=axs[1,1].transAxes,
                  fontsize=7.5,color=s.MUTED)
    return fig


def save_figure(fig):
    facts = {
        'source':'analytic definitions in the continuity subsection; no external or random data',
        'functions':['x^2 on R; window [-3,3]','x^2 on [0,1]','sqrt(x) on [0,1]','Cantor function on [0,1]; depth-8 polygon for display'],
        'sampling':'601 evenly spaced points for smooth functions; all 512 vertices of the depth-8 Cantor polygon',
        'cantor_recursion':'C_(n+1)(x)=C_n(3x)/2 on [0,1/3]; 1/2 on [1/3,2/3]; (1+C_n(3x-2))/2 on [2/3,1]; C_0(x)=x',
        'cantor_uniform_error_bound':'||C-C_8||_infty <= 2^-8; properties in annotation belong to limiting C, not C_8',
        'finite_approximation_warning':'Every finite polygon is Lipschitz and absolutely continuous; the displayed finite graph is not a proof that C is not absolutely continuous.',
        'square_markers':{'x':[2,2.5],'y':[4,6.25],'role':'one pair from x_n=n, y_n=n+1/n; proof requires the entire sequence, not this plotted pair'},
        'no_filtering':True, 'no_missing_values':True, 'no_aggregation':True,
        'interpretation':'curve height and apparent smoothness do not establish continuity type; definitions and analytic arguments in text do',
    }
    # The PDF remains vector; provide a >=300 dpi PNG companion as well.
    fig.savefig(OUT/'figure.png',dpi=360)
    fig.savefig(OUT/'figure.pdf')
    record={'name':'figure','method':'Matplotlib','width_mm':169,'height_mm':112,
            'png_dpi':360,'facts':facts,**s.provenance()}
    s.plt.close(fig)
    record.update({'reference_width_mm':169,'scale':1,'font_versions':'fonts/README.md',
                   'book_page_review':'pending: built-in document compiler cannot load repository root'})
    (OUT/'generation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')


if __name__ == '__main__':
    save_figure(build_figure(load_data()))
