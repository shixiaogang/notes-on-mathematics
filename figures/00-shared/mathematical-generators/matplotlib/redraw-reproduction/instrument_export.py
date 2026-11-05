"""Record exact plotted values and actual visible text bounds at each export."""
from pathlib import Path
import json,hashlib
import numpy as np
from matplotlib.figure import Figure
from matplotlib.text import Text
from matplotlib.patches import Polygon,Circle,Rectangle
from plot_style import style_record
original=Figure.savefig

def plain(a):
 try:return np.asarray(a).tolist()
 except Exception:return str(a)

def save(self,file,*args,**kwargs):
 r=original(self,file,*args,**kwargs)
 p=Path(file)
 if p.suffix!='.png':return r
 self.canvas.draw();renderer=self.canvas.get_renderer();w,h=self.bbox.width,self.bbox.height
 labels=[]
 all_tick_text=set();drawn_tick_text=set()
 for ax in self.axes:
  for axis in [ax.xaxis,ax.yaxis]:
   for tick in axis.get_major_ticks()+axis.get_minor_ticks():all_tick_text.update([tick.label1,tick.label2])
   if ax.axison and axis.get_visible():
    for tick in axis._update_ticks():drawn_tick_text.update([tick.label1,tick.label2])
 for t in self.findobj(Text):
  if not t.get_visible() or not t.get_text() or (t in all_tick_text and t not in drawn_tick_text):continue
  b=Text.get_window_extent(t,renderer)  # Glyph rectangle, excluding Annotation leader/arrow.
  labels.append({'text':t.get_text(),'fontsize_pt':t.get_fontsize(),'role':getattr(t,'academic_role','main'),'bbox_norm':[b.x0/w,1-b.y1/h,b.x1/w,1-b.y0/h],'family':t.get_fontfamily(),'mathfamily':t.get_math_fontfamily()})
 outside=[x for x in labels if min(x['bbox_norm'][:2])<-.002 or max(x['bbox_norm'][2:])>1.002]
 pairs=[]
 for i,a in enumerate(labels):
  for j,b in enumerate(labels[i+1:],i+1):
   aa=a['bbox_norm'];bb=b['bbox_norm'];dx=min(aa[2],bb[2])-max(aa[0],bb[0]);dy=min(aa[3],bb[3])-max(aa[1],bb[1])
   if dx>1.0/w and dy>1.0/h:pairs.append([i,j])
 report={'page_px_at_canvas_dpi':[w,h],'canvas_dpi':self.dpi,'native_export_dpi':kwargs.get('dpi'),'labels':labels,'outside':outside,'overlap_pairs':pairs,'status':'Measured text bounds; scientific and object/line clearance require visual review','style':style_record()}
 p.with_suffix('.typography.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 axes=[]
 for ax in self.axes:
  lines=[{'label':x.get_label(),'x':plain(x.get_xdata()),'y':plain(x.get_ydata()),'style':x.get_linestyle(),'color':str(x.get_color())} for x in ax.lines]
  collections=[{'label':x.get_label(),'offsets':plain(x.get_offsets()),'array':plain(x.get_array()) if x.get_array() is not None else None,'paths':[plain(q.vertices) for q in x.get_paths()]} for x in ax.collections]
  images=[{'array':plain(x.get_array()),'extent':plain(x.get_extent()),'origin':x.origin} for x in ax.images]
  patches=[]
  for x in ax.patches:
   q={'type':type(x).__name__}
   if isinstance(x,Circle):q.update(center=plain(x.center),radius=x.radius)
   elif isinstance(x,Rectangle):q.update(xy=plain(x.get_xy()),width=x.get_width(),height=x.get_height())
   elif isinstance(x,Polygon):q.update(vertices=plain(x.get_xy()))
   else:q.update(vertices=plain(x.get_path().vertices))
   patches.append(q)
  axes.append({'xlim':plain(ax.get_xlim()),'ylim':plain(ax.get_ylim()),'xscale':ax.get_xscale(),'yscale':ax.get_yscale(),'lines':lines,'collections':collections,'images':images,'patches':patches})
 p.with_suffix('.data.json').write_text(json.dumps({'description':'Exact artist data recorded at the current actual export; analytic definitions remain in accompanying generator source','axes':axes},ensure_ascii=False,indent=2,default=lambda x:x.item() if hasattr(x,'item') else str(x))+'\n')
 return r
Figure.savefig=save
