"""Replay text placement without modifying any model artwork pixels.
Usage: python render_labels.py [key...]. All paths resolve from this file.
"""
from pathlib import Path
import json,sys,itertools,runpy
from PIL import Image
from typeset_common import Typeset
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
B=Path(__file__).resolve().parent

def bbox(a):
 bs=a['boxes'];return [min(b[0] for b in bs),min(b[1] for b in bs),max(b[2] for b in bs),max(b[3] for b in bs)]
def intersect(a,b):return min(a[2],b[2])>max(a[0],b[0]) and min(a[3],b[3])>max(a[1],b[1])
def render(key):
 o=Path(key).resolve() if Path(key).is_absolute() else ROOT/key;s=json.loads((o/'labels-source.json').read_text())
 if s.get('quantitative_panels'):runpy.run_path(str(o/s['quantitative_panels']),run_name='__main__')
 bg=Image.open(o/s.get('canvas_source','background.png')).convert('RGBA');m=s.get('margin',[0,0,0,0]);l,t,r,b=m
 canvas=Image.new('RGBA',(bg.width+l+r,bg.height+t+b),'white');canvas.alpha_composite(bg,(l,t));canvas.save(o/'background-canvas.png')
 x=Typeset(o/'background-canvas.png',o,ROOT/'fonts')
 for a in s['labels']:
  if 'segments' in a:x.text(a['x'],a['y'],a['segments'],a.get('color','#3B4252'))
  else:x.label(a['x'],a['y'],a['text'],a['size'],a.get('kind','cn'),a.get('color','#3B4252'))
  x.labels[-1]['id']=a['id']
 x.save()
 p=o/'typography-check.json';check=json.loads(p.read_text())
 check['label_overlap_pairs']=[[a['id'],b['id']] for a,b in itertools.combinations(x.labels,2) if intersect(bbox(a),bbox(b))]
 regions=s.get('avoid_regions',[])
 check['annotated_object_or_line_collisions']=[{'label':a['id'],'region':r['id']} for a in x.labels for r in regions if intersect(bbox(a),r['bbox'])]
 check['avoid_regions']=regions
 check['scope']='Actual font glyph bboxes; explicit hand-measured icons/paths only. Final native and 1100px visual inspection is required for unannotated artwork.'
 p.write_text(json.dumps(check,ensure_ascii=False,indent=2))
 assert not check['label_overlap_pairs'] and not check['annotated_object_or_line_collisions'],check
 im=Image.open(o/'figure.png');im.resize((1100,round(im.height*1100/im.width)),Image.Resampling.LANCZOS).save(o/'preview1100.png')
 if s.get('vector_composite'):runpy.run_path(str(o/s['vector_composite']),run_name='__main__')
 print(key,len(x.labels),check['pixels'])
if __name__=='__main__':
 for k in sys.argv[1:] or [p.parent.name for p in B.glob('*/labels-source.json')]:render(k)
