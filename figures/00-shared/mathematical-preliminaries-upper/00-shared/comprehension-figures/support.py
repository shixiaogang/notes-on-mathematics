"""Reproducible, book-sized drawing support for volume-one teaching additions.

Run generators from any directory; all fonts and outputs stay in this checkout.
The project specs/figures.md palette takes precedence over historical defaults.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile
import shutil
from dataclasses import replace
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
BLUE, GREEN, YELLOW, RED, PURPLE = '#7188A3', '#829C8B', '#B4A16F', '#A7787D', '#9588A5'
BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL = '#E5EAF0', '#E8EEE9', '#F1ECDD', '#F0E5E6', '#ECE8F0'
INK, MUTED, STROKE, GRID = '#3B4252', '#6B7280', '#4C4D4F', '#D8DCE2'
FONT_FILES = {'Chinese': 'SourceHanSansSC-Normal.otf', 'notes': 'LXGWWenKai-Regular.ttf', 'Latin_math': 'FiraMath-Regular.otf', 'math_fallback': 'STIXTwoMath-Regular.otf'}

def configure():
    for name in FONT_FILES.values():
        fm.fontManager.addfont(ROOT/'fonts'/name)
    # The Normal and Regular files share a preferred family name. Give this
    # registered file a private lookup alias so family fallback cannot select
    # an installed Regular face instead of the requested repository file.
    cn = 'Volume One Source Han Sans Normal'
    for index, entry in enumerate(fm.fontManager.ttflist):
        if Path(entry.fname).resolve() == (ROOT/'fonts'/FONT_FILES['Chinese']).resolve():
            fm.fontManager.ttflist[index] = replace(entry, name=cn)
    en = fm.FontProperties(fname=ROOT/'fonts'/FONT_FILES['Latin_math']).get_name()
    plt.rcParams.update({'font.family': [en, cn], 'font.size': 8,
        'font.weight': 'normal', 'axes.titlesize': 8, 'axes.labelsize': 8,
        'axes.titleweight': 'normal', 'axes.labelweight': 'normal',
        'xtick.labelsize': 7.5, 'ytick.labelsize': 7.5, 'legend.fontsize': 7.5,
        'axes.spines.top': False, 'axes.spines.right': False,
        'text.color': INK, 'axes.labelcolor': INK, 'axes.edgecolor': STROKE,
        'xtick.color': INK, 'ytick.color': INK, 'axes.linewidth': .75,
        'grid.color': GRID, 'grid.linewidth': .4, 'lines.linewidth': 1.1,
        'patch.linewidth': .75, 'legend.frameon': False,
        'figure.facecolor': 'white', 'axes.facecolor': 'white',
        # Both pinned OpenType faces contain CFF outlines. Type 3 vector
        # glyph programs survive XeLaTeX/xdvipdfmx PDF inclusion; forcing
        # TrueType embedding can retain CJK text while dropping its pixels.
        'savefig.facecolor': 'white', 'pdf.fonttype': 3, 'ps.fonttype': 3,
        'svg.fonttype': 'path', 'axes.unicode_minus': False,
        'mathtext.fontset': 'custom', 'mathtext.rm': en,
        'mathtext.it': en, 'mathtext.bf': en, 'mathtext.sf': en,
        'mathtext.cal': en, 'mathtext.tt': en, 'mathtext.fallback': None})

def figure(width_mm=112, height_mm=48, **kwargs):
    configure()
    return plt.subplots(figsize=(width_mm/25.4, height_mm/25.4), layout='constrained', **kwargs)

def provenance():
    licenses = {'Chinese': 'SourceHanSans-OFL.txt', 'notes': 'LXGWWenKai-OFL.txt', 'Latin_math': 'FiraMath-font-license.txt', 'math_fallback': 'STIX-OFL.txt'}
    return {'font_roles': {k: {'file': 'fonts/'+v,
        'sha256': hashlib.sha256((ROOT/'fonts'/v).read_bytes()).hexdigest(),
        'license': 'fonts/licenses/'+licenses[k]} for k,v in FONT_FILES.items()},
        'palette_source': 'specs/figures.md', 'palette': [BLUE,GREEN,YELLOW,RED,PURPLE],
        'label_size_pt': 8, 'auxiliary_size_pt': 7.5, 'synthetic_bold': False,
        'matplotlib_pdf_embedding': 'vector Type 3 glyph programs from the pinned CFF font files'}

def save(fig, directory, name, facts):
    directory = Path(directory); directory.mkdir(parents=True, exist_ok=True)
    for ext in ('pdf','png'):
        fig.savefig(directory/(name+'.'+ext), dpi=180)
    record = {'name': name, 'method': 'Matplotlib', 'width_mm': fig.get_figwidth()*25.4,
        'height_mm': fig.get_figheight()*25.4, 'facts': facts, **provenance()}
    (directory/(name+'.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    plt.close(fig)
    return record

TIKZ_PREAMBLE = r'''\documentclass[border=1mm]{standalone}
\usepackage{fontspec,xeCJK,unicode-math,tikz}
\usetikzlibrary{arrows.meta,calc,patterns,positioning,fit,decorations.pathreplacing}
\setmainfont{FiraMath-Regular.otf}[Path=FONTDIR/]
\setsansfont{FiraMath-Regular.otf}[Path=FONTDIR/]
\setCJKmainfont{SourceHanSansSC-Normal.otf}[Path=FONTDIR/]
\setCJKsansfont{SourceHanSansSC-Normal.otf}[Path=FONTDIR/]
\setmathfont{FiraMath-Regular.otf}[Path=FONTDIR/]
\setmathfont{STIXTwoMath-Regular.otf}[Path=FONTDIR/,range={\star,\top}]
\definecolor{Blue}{HTML}{7188A3}\definecolor{Green}{HTML}{829C8B}
\definecolor{Yellow}{HTML}{B4A16F}\definecolor{Red}{HTML}{A7787D}
\definecolor{Purple}{HTML}{9588A5}\definecolor{Ink}{HTML}{3B4252}
\definecolor{Muted}{HTML}{6B7280}\definecolor{Stroke}{HTML}{4C4D4F}
\definecolor{Grid}{HTML}{D8DCE2}
\definecolor{BlueFill}{HTML}{E5EAF0}\definecolor{GreenFill}{HTML}{E8EEE9}
\definecolor{YellowFill}{HTML}{F1ECDD}\definecolor{RedFill}{HTML}{F0E5E6}
\definecolor{PurpleFill}{HTML}{ECE8F0}
\tikzset{every picture/.style={font=\fontsize{8}{10}\selectfont,text=Ink,line width=.75pt,>=Stealth},
  box/.style={draw=Blue,fill=BlueFill,rounded corners=1.8pt,inner sep=4pt},
  flow/.style={->,draw=Stroke,line width=.75pt},
  note/.style={font=\fontsize{7.5}{9}\selectfont,text=Muted}}
\begin{document}
\input{SOURCE}
\end{document}
'''

def render_tikz(source):
    """Compile one editable TikZ fragment. Caller serializes invocations."""
    source = Path(source).resolve()
    with tempfile.TemporaryDirectory(prefix='vol1-figure-',dir=ROOT/'build') as tmp:
        tmp = Path(tmp)
        (tmp/'figure.tex').write_text(TIKZ_PREAMBLE.replace('FONTDIR',(ROOT/'fonts').as_posix()).replace('SOURCE',source.as_posix()))
        result = subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-no-shell-escape','figure.tex'],cwd=tmp,capture_output=True,text=True)
        if result.returncode or 'Missing character' in result.stdout:
            raise RuntimeError(source.name+'\n'+result.stdout[-7000:])
        shutil.copyfile(tmp/'figure.pdf',source.with_suffix('.pdf'))
        subprocess.run(['pdftoppm','-png','-singlefile','-r','180',str(source.with_suffix('.pdf')),str(source.with_suffix(''))],check=True,capture_output=True)
    return source.with_suffix('.pdf')
