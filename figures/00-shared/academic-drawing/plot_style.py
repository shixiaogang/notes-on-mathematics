"""Academic drawing 2026-10: actual fonts, five muted colors, exact source data.
Only styles text and artists; never substitutes, samples, smooths or changes data.
"""
from pathlib import Path
import hashlib
import unicodedata
import json
import os
import re
import matplotlib as mpl
mpl.use("Agg")
from matplotlib import font_manager, _mathtext
from matplotlib.mathtext import MathTextParser
from matplotlib.text import Text
from matplotlib.lines import Line2D
from matplotlib import colors
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
FONTDIR = ROOT/'fonts'
CN_FILE=FONTDIR/'SourceHanSansSC-Normal.otf'
NOTE_FILE=FONTDIR/'LXGWWenKai-Regular.ttf'
EN_FILE=FONTDIR/'FiraMath-Regular.otf'
STIX_FILE=FONTDIR/'STIXTwoMath-Regular.otf'
# Unique aliases bind every Matplotlib family selection to the exact files.
# Installed Source Han Regular shares typographic family with Normal.
import dataclasses
CN,NOTE,EN,STIX='Academic SourceHan Normal','Academic WenKai','Academic Fira Math','Academic STIX2 Exceptions'
for p,alias in [(CN_FILE,CN),(NOTE_FILE,NOTE),(EN_FILE,EN),(STIX_FILE,STIX)]:
    font_manager.fontManager.addfont(p)
    entry=dataclasses.replace(font_manager.fontManager.ttflist[-1],name=alias)
    font_manager.fontManager.ttflist.append(entry)
font_manager.fontManager._findfont_cached.cache_clear()

# Compatibility names bind archived scientific generators to five exact hues.
BLUE,GREEN,YELLOW,RED,PURPLE = PALETTE = ['#7188A3','#829C8B','#B4A16F','#A7787D','#9588A5']
INK,STROKE,MUTED,GRID='#3B4252','#4C4D4F','#6B7280','#D8DCE2'
BLUE_FILL,GREEN_FILL,YELLOW_FILL,RED_FILL,PURPLE_FILL='#E5EAF0','#E8EEE9','#F1ECDD','#F0E5E6','#ECE8F0'
CYAN,ICE,GRASS,SAGE,PEACH,ORANGE,CORAL=BLUE,BLUE_FILL,GREEN,GREEN_FILL,YELLOW_FILL,YELLOW,RED
def is_cjk(code): return 0x2e80<=code<=0x9fff or 0xf900<=code<=0xfaff or 0xff00<=code<=0xffef
class AcademicUnicodeFonts(_mathtext.UnicodeFonts):
    """Fira math with explicitly selected Chinese face for mixed math labels.
    Matplotlib's native UnicodeFonts has no CJK fallback inside mathtext.
    """
    def __init__(self, default_font_prop, load_glyph_flags):
        super().__init__(default_font_prop, load_glyph_flags)
        self.fontmap['ex']=str(EN_FILE)
        self.academic_fira=font_manager.get_font(str(EN_FILE))
        self.academic_stix=font_manager.get_font(str(STIX_FILE))
        self.academic_cn=font_manager.get_font(str(NOTE_FILE if NOTE in default_font_prop.get_family() else CN_FILE))
    def _map_virtual_font(self,fontname,font_class,code):
        # Universal Unicode mathematical alphabets, never STIX private-use
        # positions. Fira Math has these glyphs in its actual font file.
        virtual = {'bb':'bb','cal':'scr','scr':'scr','frak':'frak'}
        if fontname in virtual:
            mapping=_mathtext.stix_virtual_fonts[virtual[fontname]]
            if isinstance(mapping,dict):mapping=mapping.get('rm',next(iter(mapping.values())))
            for lo,hi,dest,base in mapping:
                if lo<=code<=hi:return 'rm',code-lo+base
            return 'rm',code
        if fontname in ['it','bf','bfit'] and chr(code).isalpha():
            name=unicodedata.name(chr(code),'')
            if name.startswith('LATIN '):name=name.replace('LATIN ','')
            if name.startswith('GREEK '):name=name.replace('GREEK ','')
            name=name.replace(' LETTER','')
            style={'it':'ITALIC','bf':'BOLD','bfit':'BOLD ITALIC'}[fontname]
            try:code=ord(unicodedata.lookup('MATHEMATICAL '+style+' '+name))
            except KeyError:
                if fontname=='it' and code==ord('h'):code=0x210e
        return fontname,code
    def _get_glyph(self,fontname,font_class,sym):
        try: code=_mathtext.get_unicode_index(sym)
        except ValueError: return super()._get_glyph(fontname,font_class,sym)
        if is_cjk(code):
            if not self.academic_cn.get_char_index(code): raise ValueError(f'Missing CJK glyph U+{code:04X}')
            return self.academic_cn,code,False
        mapped_font,mapped_code=self._map_virtual_font(fontname,font_class,code)
        if not self.academic_fira.get_char_index(mapped_code):
            if not self.academic_stix.get_char_index(mapped_code):
                raise ValueError(f'Math glyph absent from both approved fonts: U+{mapped_code:04X} ({sym})')
            return self.academic_stix,mapped_code,mapped_font in ['it','bfit']
        font,code,slanted=super()._get_glyph(fontname,font_class,sym)
        if code==0xA4 and sym not in ['¤',r'\currency']:
            raise ValueError('Requested mathematical glyph absent from Fira Math: '+sym+'; do not silently replace notation')
        return font,code,slanted
MathTextParser._font_type_mapping['custom']=AcademicUnicodeFonts

def configure():
    mpl.rcParams.update({'font.family':[EN,STIX,CN],'font.size':8,'font.weight':'normal',
      'axes.labelsize':8,'axes.titlesize':8,'axes.labelweight':'normal','axes.titleweight':'normal',
      'xtick.labelsize':8,'ytick.labelsize':8,'legend.fontsize':8,
      'mathtext.fontset':'custom','mathtext.default':'it','mathtext.fallback':None,
      'mathtext.rm':EN,'mathtext.it':EN,'mathtext.bf':EN,'mathtext.bfit':EN,'mathtext.cal':EN,
      'mathtext.sf':EN,'mathtext.tt':EN,'axes.unicode_minus':False,'text.usetex':False,
      'pdf.fonttype':3,'ps.fonttype':3,'svg.fonttype':'path',
      'text.color':INK,'axes.labelcolor':INK,'axes.edgecolor':STROKE,'axes.linewidth':.95,
      'axes.spines.top':False,'axes.spines.right':False,'xtick.color':STROKE,'ytick.color':STROKE,
      'xtick.major.width':.6,'ytick.major.width':.6,'xtick.minor.width':.5,'ytick.minor.width':.5,
      'grid.color':GRID,'grid.linewidth':.4,'grid.alpha':1,'lines.linewidth':1.4,
      'patch.linewidth':.8,'legend.frameon':False,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

def prepare_figure(fig):
    for ax in fig.axes:
        for spine in ax.spines.values(): spine.set_color(STROKE); spine.set_linewidth(.95)
        ax.tick_params(which='both',width=.8,colors=STROKE)
        for line in ax.get_xgridlines()+ax.get_ygridlines():
            line.set_color(GRID);line.set_linewidth(.4);line.set_alpha(1)
    if not getattr(fig, '_academic_strokes_applied', False):
        for ax in fig.axes:
            # Axes3D treats extra keyword arguments as a request to enable its grid.
            if getattr(ax, 'name', '') == '3d':
                ax.grid(False)
            else:
                ax.grid(False, which='both')
            for line in ax.lines:
                if line.get_linewidth() > 0:
                    line.set_linewidth(max(.85, line.get_linewidth()*1.3))
            for patch in ax.patches:
                if patch.get_linewidth() > 0:
                    patch.set_linewidth(max(.85, patch.get_linewidth()*1.3))
        fig._academic_strokes_applied = True
    for text in fig.findobj(Text):
        # English first gives actual Fira glyphs; CJK falls back only to the
        # explicitly loaded Normal face. Notes opt into WenKai by role.
        note=getattr(text,'academic_role','')=='note'
        if note: text.set_fontsize(7.5)
        text.set_fontfamily([EN,STIX,NOTE if note else CN]);text.set_fontweight('normal')
        text.set_math_fontfamily('custom')
    if fig.get_layout_engine() is not None:
        for _ in range(3):fig.canvas.draw()
        fig.set_layout_engine(None)
    # Finalize after generators' last tight_layout/subplots_adjust call, at export.
    # The same physical layout is reused for PDF, SVG and PNG.
    if not getattr(fig, '_academic_export_wrapped', False):
        original_savefig = fig.savefig
        def publication_savefig(filename, *args, **kwargs):
            finalize_panel_markers(fig)
            result = original_savefig(filename, *args, **kwargs)
            audit = os.environ.get('ACADEMIC_PANEL_AUDIT')
            if audit and isinstance(filename, (str, Path)) and str(filename).endswith('.pdf'):
                record = dict(asset=str(Path(filename).relative_to(ROOT)),
                              **getattr(fig, '_academic_panel_record', {'panels': []}))
                with Path(audit).open('a') as stream:
                    stream.write(json.dumps(record, ensure_ascii=False)+'\n')
            return result
        fig.savefig = publication_savefig
        fig._academic_export_wrapped = True

def finalize_panel_markers(fig):
    """Place panel letters below real content, with a shared baseline per row.

    Preserve axes, glyph and curve sizes. Reuse the space left by old titles;
    extend the canvas only when the measured labels need more room. Unlabelled
    axes below a labelled axis belong to that panel (e.g. an error subplot).
    """
    if getattr(fig, '_academic_panels_applied', False):
        return
    fig._academic_panels_applied = True
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    panels = []
    for text in fig.findobj(Text):
        match = re.fullmatch(r'\(([a-z])\)(?:\s+.*)?', text.get_text().strip())
        if not match or not text.get_visible():
            continue
        bbox = text.get_window_extent(renderer)
        ax = text.axes
        x = (bbox.x0+bbox.x1)/2/fig.bbox.width
        if ax is None:
            ax = min(fig.axes, key=lambda a: abs((a.get_position().x0+a.get_position().x1)/2-x))
        pos = ax.get_position()
        panels.append(dict(letter=match[1], ax=ax, x=(pos.x0+pos.x1)/2,
                           row=(pos.y0+pos.y1)/2))
        # Explanatory suffixes are already stated in the caption.
        text.set_text('')
        text.set_visible(False)
    if not panels:
        return
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    width, height = fig.get_size_inches()*72
    rows = []
    for panel in sorted(panels, key=lambda p: -p['row']):
        row = next((r for r in rows if abs(r[0]['row']-panel['row']) < .16), None)
        if row is None:
            rows.append([panel])
        else:
            row.append(panel)
    def content_box(ax):
        return ax.get_tightbbox(renderer).transformed(fig.transFigure.inverted())
    boxes = {ax: content_box(ax) for ax in fig.axes}
    gap_pt = 3*72/25.4
    # A centred 8 pt parenthesized letter is 8 pt high on this renderer.
    for row in rows:
        bottoms = []
        for panel in row:
            pos = panel['ax'].get_position()
            members = [panel['ax']]
            for ax in fig.axes:
                other = ax.get_position()
                overlap = min(pos.x1, other.x1)-max(pos.x0, other.x0)
                if (ax not in [p['ax'] for p in panels] and other.y1 <= pos.y1+.01
                        and overlap > .6*min(pos.width, other.width)):
                    members.append(ax)
            bottoms.extend(boxes[a].y0*height for a in members)
        # A shared legend is part of the bottom row's content.
        if row is rows[-1]:
            bottoms.extend(legend.get_window_extent(renderer).y0/fig.bbox.height*height
                           for legend in fig.legends if legend.get_visible())
        baseline = min(bottoms)-gap_pt-6.5
        for panel in row:
            panel['baseline_pt'] = baseline
    lowest = min(p['baseline_pt'] for p in panels)-2
    need = max(0, 3-lowest)
    content_top = max(box.y1*height for box in boxes.values())
    visible_texts = [t for t in fig.texts if t.get_visible() and t.get_text()]
    if visible_texts:
        content_top = max(content_top, *(t.get_window_extent(renderer).y1/fig.bbox.height*height for t in visible_texts))
    shift = min(need, max(0, height-content_top-3))
    growth = need-shift
    positions = {ax: ax.get_position().frozen() for ax in fig.axes}
    text_positions = {text: text.get_position() for text in fig.texts}
    legend_boxes = {legend: legend.get_bbox_to_anchor().transformed(fig.transFigure.inverted()).frozen()
                    for legend in fig.legends}
    new_height = height+growth
    fig.set_size_inches(width/72, new_height/72, forward=False)
    lift = shift+growth
    for ax, pos in positions.items():
        ax.set_position([pos.x0, (pos.y0*height+lift)/new_height,
                         pos.width, pos.height*height/new_height])
    for text, (x,y) in text_positions.items():
        text.set_position((x, (y*height+lift)/new_height))
    for legend, box in legend_boxes.items():
        legend.set_bbox_to_anchor((box.x0, (box.y0*height+lift)/new_height,
                                  box.width, box.height*height/new_height), transform=fig.transFigure)
    record = []
    for panel in panels:
        y = (panel['baseline_pt']+lift)/new_height
        fig.text(panel['x'], y, '('+panel['letter']+')', ha='center', va='baseline',
                 fontsize=8, fontfamily=[EN,STIX,CN], color=INK)
        record.append(dict(letter=panel['letter'], x_pt=panel['x']*width,
                           baseline_pt=y*new_height, gap_mm=3))
    fig._academic_panel_record = dict(panels=record, width_mm=width*25.4/72,
                                     height_mm=new_height*25.4/72,
                                     canvas_growth_mm=growth*25.4/72)

def note(text):
    text.academic_role='note';text.set_fontfamily([EN,STIX,NOTE]);return text

def style_record():
    return {'palette_name':'Book muted five-color 2026-10-11','palette':PALETTE,'fonts':{
      'Chinese_body':str(CN_FILE.relative_to(ROOT)),'Chinese_note':str(NOTE_FILE.relative_to(ROOT)),
      'Latin_digits_math':str(EN_FILE.relative_to(ROOT)),'only_missing_math_glyphs':str(STIX_FILE.relative_to(ROOT))},'font_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [CN_FILE,NOTE_FILE,EN_FILE,STIX_FILE]},
      'mathtext':'custom Fira Math; CJK-specific fallback to explicitly loaded Normal/WenKai; general math fallback disabled; actual STIX2 only for Fira-absent glyphs per user authorization',
      'label_size_pt':{'main':8,'note':7.5},'fixed_pale_fills':{'blue':BLUE_FILL,'green':GREEN_FILL,'yellow':YELLOW_FILL,'red':RED_FILL,'purple':PURPLE_FILL},'line_width_pt':{'main':1.4,'axes':.95,'auxiliary':.85,'grid':.65},'background':'white','panel_markers':{'position':'below content','gap_mm':3,'font_size_pt':8,'alignment':'shared baseline per visual row; plot size preserved'},
      'fine_yellow_curve':'No automatic color substitution; semantic colors are chosen explicitly in scientific sources',
      'export':'PDF vector Type3 outlines; SVG glyph paths; PNG genuine export dpi'}
