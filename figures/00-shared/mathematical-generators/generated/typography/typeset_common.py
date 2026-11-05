"""Font-accurate text overlays only; do not alter or trace the model artwork."""
from pathlib import Path
import json, re, hashlib, unicodedata
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

INK='#3B4252'; MUTED='#6B7280'; SCALE=3
FONT_FILES={'cn':'SourceHanSansSC-Normal.otf','note':'LXGWWenKai-Regular.ttf','en':'FiraMath-Regular.otf','math':'FiraMath-Regular.otf','mi':'FiraMath-Regular.otf'}
def run(text,font='cn',size=28,dy=0):return dict(text=text,font=font,size=size,dy=dy)
def mathvar(text,sub=None,sup=None,size=29):
 text=''.join(chr(0x1D44E+ord(c)-ord('a')) if 'a'<=c<='z' and c!='h' else ('ℎ' if c=='h' else c) for c in text)
 a=[run(text,'mi',size)]
 if sub is not None:a.append(run(str(sub),'math',size*.65,size*.18))
 if sup is not None:a.append(run(str(sup),'math',size*.65,-size*.45))
 return a

class Typeset:
 def __init__(self,background,out,fonts):
  self.out=Path(out);self.out.mkdir(parents=True,exist_ok=True);self.fonts=Path(fonts)
  self.base=Image.open(background).convert('RGBA')
  self.layer=Image.new('RGBA',(self.base.width*SCALE,self.base.height*SCALE),(0,0,0,0))
  self.draw=ImageDraw.Draw(self.layer);self.cache={};self.labels=[]
 def font(self,kind,size):
  key=(kind,size)
  if key not in self.cache:self.cache[key]=ImageFont.truetype(str(self.fonts/FONT_FILES[kind]),round(size*SCALE))
  return self.cache[key]
 def text(self,x,y,segments,color=INK):
  widths=[self.draw.textlength(r['text'],font=self.font(r['font'],r['size'])) for r in segments]
  left=x*SCALE-sum(widths)/2;boxes=[]
  for r,w in zip(segments,widths):
   f=self.font(r['font'],r['size']);base=(y+r['dy'])*SCALE
   self.draw.text((left,base),r['text'],font=f,fill=color,anchor='ls')
   boxes.append([round(v/SCALE,2) for v in self.draw.textbbox((left,base),r['text'],font=f,anchor='ls')]);left+=w
  self.labels.append(dict(center_x=x,baseline_y=y,segments=segments,color=color,boxes=boxes))
 def label(self,x,y,text,size=28,kind='cn',color=INK):
  segments=[]
  for c in text:
   if unicodedata.category(c)=='Sm':c=unicodedata.normalize('NFKC',c)
   mathchar=(ord(c)<128 or 0x0370<=ord(c)<=0x03ff or 0x1f00<=ord(c)<=0x1fff or 0x2190<=ord(c)<=0x22ff or 0x27c0<=ord(c)<=0x2aff or 0x1d400<=ord(c)<=0x1d7ff or unicodedata.category(c)=='Sm')
   k='math' if kind in ['cn','note'] and mathchar else kind
   if segments and segments[-1]['font']==k:segments[-1]['text']+=c
   else:segments.append(run(c,k,size))
  self.text(x,y,segments,color)
 def paired_heading(self,icon,segments,color=INK,gap=9):
  widths=[self.draw.textlength(r['text'],font=self.font(r['font'],r['size']))/SCALE for r in segments]
  b=[self.draw.textbbox((0,r['dy']*SCALE),r['text'],font=self.font(r['font'],r['size']),anchor='ls') for r in segments]
  top=min(a[1] for a in b)/SCALE;bottom=max(a[3] for a in b)/SCALE
  self.text(icon[2]+gap+sum(widths)/2,(icon[1]+icon[3]-top-bottom)/2,segments,color)
 def save(self):
  layer=self.layer.resize(self.base.size,Image.Resampling.LANCZOS)
  layer.save(self.out/'text-layer.png')
  # Genuine transparent model canvas can be composited on pure white; no texture cleanup.
  flat=Image.alpha_composite(Image.new('RGBA',self.base.size,'white'),self.base)
  Image.alpha_composite(flat,layer).convert('RGB').save(self.out/'figure.png',dpi=(300,300))
  (self.out/'labels.json').write_text(json.dumps(self.labels,ensure_ascii=False,indent=2))
  cmaps={k:TTFont(self.fonts/v).getBestCmap() for k,v in FONT_FILES.items()}
  missing=[(s['font'],c) for a in self.labels for s in a['segments'] for c in s['text'] if not c.isspace() and ord(c) not in cmaps[s['font']]]
  outside=[b for a in self.labels for b in a['boxes'] if not(0<=b[0] and b[2]<=self.base.width and 0<=b[1] and b[3]<=self.base.height)]
  (self.out/'typography-check.json').write_text(json.dumps(dict(missing_glyphs=missing,outside_canvas=outside,pixels=self.base.size),ensure_ascii=False,indent=2))
  assert not missing and not outside,(missing,outside)
