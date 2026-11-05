# -*- coding: utf-8 -*-
"""Refresh figure facts; standalone TikZ rendering is serialized by the caller."""
from pathlib import Path
import json
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0,str(ROOT/'figures/01-mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import provenance

HERE = Path(__file__).resolve().parent
OWNER_PREFIX='tex/01-mathematical-preliminaries-upper/05-graphs-and-signals/'
SPECS=[
 ('signal-correlation-direction',8,'01-signal-representation-and-processing.tex',
  {'x':[1,2,1], 'h':[1,2], 'extension':'zero', 'correlation_n0':'x[0]*h[0]+x[1]*h[1]=5',
   'convolution_n1':'x[0]*h[1]+x[1]*h[0]=4', 'scope':'real sequences; correlation convention sum_r x[n+r]*conj(h[r])'},
  'The same signal window uses the original-order template in correlation and reversed weights in convolution; output indices must also be stated.'),
 ('graph-adjacency-orientation',9,'02-graph-structure-and-computation.tex',
  {'arcs':[[1,2],[1,3]],'weights':[1,1],'adjacency_convention':'row source, column target',
   'A':[[0,1,1],[0,0,0],[0,0,0]],'f':[1,2,3],'A_times_f':[5,0,0],'A_transpose_times_f':[0,1,1]},
  'Reading out-neighbour values and sending values along outgoing arcs require opposite matrix actions under the fixed storage convention.'),
 ('graph-negative-cycle-reach',9,'02-graph-structure-and-computation.tex',
  {'vertices':['s','a','b','t','u','c','d'],
   'arcs':[ ['s','a',1],['s','u',4],['a','b',-2],['b','a',1],['b','t',2],['c','d',-2],['d','c',1] ],
   'walk_infimum':{'s':0,'u':4,'a':'-infinity','b':'-infinity','t':'-infinity','c':'+infinity','d':'+infinity'},
   'negative_cycles':['a->b->a total -1, reachable from s','c->d->c total -1, unreachable from s'],
   'scope':'finite directed graph; repeated vertices/arcs allowed in the walk objective'},
  'A negative cycle affects exactly the vertices reachable from a source-reachable negative cycle; a finite side branch and an unreachable negative cycle need distinct query outcomes.'),
 ('graph-max-sum-choice',9,'02-graph-structure-and-computation.tex',
  {'h':[[4,0],[0,4]],'x':[0,1],'y':[0,1], 'max_x_sum_y':4,'sum_y_max_x':8,
   'left_highlight':'common x=0 for every y; x=1 ties with value4',
   'right_highlight':'x=0 for y=0 and x=1 for y=1', 'scope':'finite real-valued table'},
  'Exchanging a sum and a maximum changes whether one shared decision is required or a separate decision is allowed for each retained configuration.')
]

records=[]
for name,chapter,owner,facts,difficulty in SPECS:
    records.append({'name':name,'label':'fig:vol1-add-'+name,'chapter':chapter,
        'owner':OWNER_PREFIX+owner,'asset':str((HERE/(name+'.pdf')).relative_to(ROOT)),
        'source':str((HERE/(name+'.tex')).relative_to(ROOT)), 'width_mm':112,
        'nominal_content_width_mm':110,'border_mm':1,'label_pt':8,'auxiliary_pt':7.5,
        'scientific_formula':facts,'difficulty':difficulty,'purpose':difficulty,
        'method':'tikz','writer':'figures_part3',
        'replay':'Serialize calls to support.render_tikz(source); this metadata script does not compile assets.',
        **provenance()})
(HERE/'manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
