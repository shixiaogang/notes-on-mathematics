"""Editable geometric diagrams. Uses the project's pinned TikZ/font runtime."""
from pathlib import Path
import importlib.util
import json
import os
import fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'build/ch3-figures/mpl-cache'))
sp=importlib.util.spec_from_file_location('book_support',ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py')
s=importlib.util.module_from_spec(sp);sp.loader.exec_module(s)
OUT=Path(__file__).resolve().parent
records=[]

def save(name,body,facts,height=48):
    source=OUT/(name+'.tex')
    source.write_text('\\begin{tikzpicture}[x=1mm,y=1mm]\n'
        +'\\useasboundingbox (0,0) rectangle (110,'+str(height)+');\n'+body+'\n\\end{tikzpicture}\n')
    pdf=s.render_tikz(source)
    doc=fitz.open(pdf);r=doc[0].rect
    rec={'name':name,'method':'TikZ','source':str(source.relative_to(ROOT)),
        'width_mm':r.width/72*25.4,'height_mm':r.height/72*25.4,
        'reference_width_mm':112,'facts':facts,'data_source':'exact analytic sets and Euclidean geometry',
        'sampling':'none unless explicitly listed','random_sampling':False,**s.provenance()}
    rec.update(scale=112/rec['width_mm'], final_label_pt=8*112/rec['width_mm'], png_dpi=360, font_versions='fonts/README.md')
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(5,5),alpha=False)
    pix.set_dpi(360,360)
    pix.save(source.with_suffix('.png'))
    assert 100<rec['width_mm']<118,(name,rec['width_mm'])
    (OUT/(name+'.json')).write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    records.append(rec)

def covers():
    body=r'''
\node[anchor=west] at (3,46) {(a)};
\node[anchor=west] at (61,46) {(b)};
\draw[Stroke] (5,7)--(45,7);
\fill[Ink] (5,7) circle (.5); \fill[Ink] (45,7) circle (.5);
\node[below] at (5,6) {$0$}; \node[below] at (45,6) {$1$};
\draw[Blue,line width=1pt] (1,36)--(21,36);
\draw[Blue,line width=1pt] (15,27)--(35,27);
\draw[Blue,line width=1pt] (29,18)--(49,18);
\foreach \x/\y in {1/36,21/36,15/27,35/27,29/18,49/18}
  \draw[Blue,fill=white] (\x,\y) circle (.6);
\node[above] at (10,36) {$U_1$};
\node[above] at (25,27) {$U_2$};
\node[above] at (40,18) {$U_3$};
\draw[Stroke] (65,7)--(105,7);
\draw[Ink,fill=white] (65,7) circle (.5); \draw[Ink,fill=white] (105,7) circle (.5);
\draw[Red,line width=1.2pt] (65.6,7)--(70,7);
\node[below] at (64,6) {$0$}; \node[below] at (72,6) {$1/N$};
\node[below] at (105,6) {$1$};
\foreach \lo/\yy/\nn in {85/36/2,75/27/4,70/18/8}{
 \draw[Blue,line width=1pt] (\lo,\yy)--(105,\yy);
 \draw[Blue,fill=white] (\lo,\yy) circle (.6);
 \draw[Blue,fill=white] (105,\yy) circle (.6);
 \node[above] at (95,\yy) {$U_{\nn}$};
}
'''
    save('finite-open-cover',body,{'left':'K=[0,1], open U1=(-0.1,0.4), U2=(0.25,0.75), U3=(0.6,1.1)',
        'right':'X=(0,1), U_n=(1/n,1), n>=2; shown n=2,4,8',
        'red':'for a finite subfamily with maximal index N, (0,1/N] remains uncovered',
        'scope':'a finite covering example versus an explicitly proved failure; finite drawing alone is not compactness proof'})

def cantor():
    intervals=[(0.,1.)];parts=[]
    for n in range(5):
        y=45-9*n
        parts.append(r'\draw[Grid,line width=.5pt] (16,'+str(y)+')--(104,'+str(y)+');')
        parts.append(r'\node[anchor=east] at (13,'+str(y)+r') {$C_'+str(n)+r'$};')
        for a,b in intervals:
            parts.append(r'\draw[Blue,line width=1.4pt] ('+f'{16+88*a:.6f},{y}'+')--('+f'{16+88*b:.6f},{y}'+');')
        intervals=[q for a,b in intervals for q in [(a,a+(b-a)/3),(b-(b-a)/3,b)]]
    parts.extend([r'\node[below] at (16,6) {$0$};',r'\node[below] at (104,6) {$1$};'])
    save('cantor-deletion', '\n'.join(parts),{'construction':'delete open middle third from every remaining interval at each step',
        'levels':[0,1,2,3,4],'interval_counts':[1,2,4,8,16],'length_at_step_n':'(2/3)^n',
        'endpoints':'retained; limiting set contains 0 and 1 and has Lebesgue measure zero',
        'scope':'no finite stage is itself a zero-measure set'},height=50)

def chain():
    save('chain-rule-types',r'''
\node[box,minimum width=24mm,minimum height=9mm] (x) at (16,30) {$x\in\mathbb R^2$};
\node[box,minimum width=24mm,minimum height=9mm] (y) at (56,30) {$y\in\mathbb R^3$};
\node[box,minimum width=24mm,minimum height=9mm] (l) at (96,30) {$L\in\mathbb R$};
\draw[flow] (x.east)--node[above] {$F$} (y.west);
\draw[flow] (y.east)--node[above] {$\ell$} (l.west);
\draw[->,Green] (l.south)--(96,17)--node[below] {$\nabla\ell(y)$} (56,17)--(y.south);
\draw[->,Green] (y.south)--(56,6)--node[below] {$J_F(x)^\top$} (16,6)--(x.south);
''',{'forward':'x in R2 ->F y in R3 ->ell L in R',
        'backward':'grad ell(y) in R3; J_F(x)^T is 2x3 and maps it to grad L(x) in R2',
        'scope':'arrows below indicate propagation of gradients, not inverse functions'},height=40)

def product():
    save('product-measure-grid',r'''
\fill[BlueFill] (25,6) rectangle (49,21.428571);
\fill[GreenFill] (49,6) rectangle (97,21.428571);
\fill[GreenFill] (25,21.428571) rectangle (49,42);
\fill[BlueFill] (49,21.428571) rectangle (97,42);
\draw[Stroke] (25,6) rectangle (97,42);
\draw[Stroke] (49,6)--(49,42);
\draw[Stroke] (25,21.428571)--(97,21.428571);
\node at (37,13.7) {$3$}; \node at (73,13.7) {$6$};
\node at (37,31.7) {$4$}; \node at (73,31.7) {$8$};
\node[above] at (37,43) {$\mu(A_1)=1$};
\node[above] at (73,43) {$\mu(A_2)=2$};
\node[anchor=east] at (23,13.7) {$\nu(B_1)=3$};
\node[anchor=east] at (23,31.7) {$\nu(B_2)=4$};
''',{'weights_X':[1,2],'weights_Y':[3,4],'cells_bottom_row':[3,6],'cells_top_row':[4,8],
        'total':21,'geometry':'column widths ratio 1:2, row heights ratio 3:4, cell areas proportional to weights',
        'scope':'finite atomic product measure, not an assumption about an arbitrary joint distribution'},height=49)

def line_work():
    save('line-density-work',r'''
\node[anchor=east] at (44,46) {(a)}; \node[anchor=east] at (101,46) {(b)};
\draw[->,Stroke] (7,7)--(44,7) node[right] {$x$};
\draw[->,Stroke] (7,7)--(7,42) node[above] {$y$};
\draw[Blue,line width=1.1pt] (7,7)--(39,39);
\foreach \t in {0.2,0.4,0.6,0.8}
  \fill[Blue] ({7+32*\t},{7+32*\t}) circle (.65);
\node[anchor=west] at (24,35) {$h=1$};
\node[below] at (39,7) {$1$}; \node[left] at (7,39) {$1$};
\draw[densely dotted,Grid] (39,39)--(39,7);
\draw[densely dotted,Grid] (39,39)--(7,39);
\draw[->,Stroke] (64,7)--(101,7) node[right] {$x$};
\draw[->,Stroke] (64,7)--(64,42) node[above] {$y$};
\draw[Blue,line width=1.1pt] (64,7)--(96,39);
\draw[->,Green,line width=1pt] (78,21)--(86,29) node[above left] {$\mathrm dr$};
\draw[->,Blue,line width=1pt] (78,21)--(97,21) node[right] {$F$};
\draw[densely dotted,Stroke] (86,29)--(86,21);
\draw[Stroke] (78,18)--(86,18);
\node[below] at (82,18) {$\mathrm dx$};
''',{'path':'gamma(t)=(t,t), 0<=t<=1','scalar_density':1,
        'scalar_integral':'sqrt(2)','field':[1,0],'work_integral':1,
        'local_relation':'ds=sqrt(2)dt, F dot dr=dx=dt',
        'diagram_arrows':'fixed illustrative displacements on same straight path; not a finite discretization proof'})

def flux():
    save('normal-projection',r'''
\draw[Stroke] (20,{-5.207})--(103,{42.713});
\fill[Ink] (55,15) circle (.6);
\draw[->,Blue,line width=1.1pt] (55,15)--(55,41) node[above] {$F$};
\draw[->,Green,line width=1pt] (55,15)--(43.741670,34.5);
\node[anchor=east] at (42.5,34.5) {$F_\perp$};
\draw[->,Muted,line width=.85pt] (55,15)--(66.258330,21.5);
\node[below right] at (66.3,21.5) {$F_\parallel$};
\draw[densely dashed,Grid] (43.741670,34.5)--(55,41)--(66.258330,21.5);
\draw[->,Stroke] (80.980762,30)--(73.480762,42.990381);
\node[above] at (73.480762,42.990381) {$n$};
''',{'tangent_unit':[0.8660254037844386,.5],'normal_unit':[-.5,.8660254037844386],
        'field':[0,1],'normal_projection':[-0.4330127018922193,.75],
        'tangential_projection':[.4330127018922193,.25],
        'drawing_scale':'26 mm per field vector unit, 15 mm per normal vector unit',
        'scope':'a two-dimensional normal section through a surface; local decomposition only, not a two-dimensional replacement for surface flux'},height=48)

def boundary():
    save('boundary-orientation-cancellation',r'''
\node[anchor=west] at (3,46) {(a)}; \node[anchor=west] at (61,46) {(b)};
\draw[Blue,line width=1pt] (7,7) rectangle (43,43);
\draw[Grid] (25,7)--(25,43); \draw[Grid] (7,25)--(43,25);
\draw[->,Blue] (16,7)--(22,7); \draw[->,Blue] (43,16)--(43,22);
\draw[->,Blue] (34,43)--(28,43); \draw[->,Blue] (7,34)--(7,28);
\foreach \yy in {16,34}{
 \draw[->,Muted] (24.3,{\yy-3})--(24.3,{\yy+3});
 \draw[->,Muted] (25.7,{\yy+3})--(25.7,{\yy-3});
}
\foreach \xx in {16,34}{
 \draw[->,Muted] ({\xx+3},24.3)--({\xx-3},24.3);
 \draw[->,Muted] ({\xx-3},25.7)--({\xx+3},25.7);
}
\draw[Blue,line width=1pt] (83,25) circle (18);
\draw[Green,line width=1pt] (83,25) circle (8);
\draw[->,Blue] (101,25) arc (0:80:18);
\draw[->,Green] (91,25) arc (0:-85:8);
\node at (83,38) {$\Omega$};
''',{'left':'four squares each with counterclockwise boundary; every internal edge traversed twice with opposite directions',
        'right':'annulus, outer boundary CCW, inner boundary CW, region always on left',
        'internal_arrow_offsets_mm':.7,'interpretation':'small offsets separate opposite arrows visually; the mathematical shared edges coincide',
        'application':'Green formula and compatible patch cancellation in Stokes theorem'})

def gauss():
    save('gauss-shared-face',r'''
\fill[GreenFill] (50,6)--(60,13)--(60,38)--(50,31)--cycle;
\foreach \xx in {14,50}{
 \draw[Blue] (\xx,6)--({\xx+36},6)--({\xx+36},31)--(\xx,31)--cycle;
 \draw[Blue] (\xx,6)--({\xx+10},13)--({\xx+46},13);
 \draw[Blue] (\xx,31)--({\xx+10},38)--({\xx+46},38)--({\xx+36},31);
 \draw[Blue] ({\xx+46},13)--({\xx+46},38);
 \draw[Blue] ({\xx+10},13)--({\xx+10},38);
}
\draw[->,Stroke,line width=1pt] (55,23)--(69,23) node[above] {$n_1$};
\draw[->,Stroke,line width=1pt] (55,23)--(41,23) node[below] {$n_2$};
\draw[->,Blue] (24,15)--(36,15) node[above] {$F$};
\draw[->,Blue] (72,15)--(84,15) node[above] {$F$};
''',{'objects':'two adjacent unit cubes sharing one square face',
        'field':[1,0,0],'normals_on_shared_face':[[1,0,0],[-1,0,0]],
        'shared_fluxes':[1,-1],'external_net_flux':0,'divergence':0,
        'projection':'oblique drawing of three-dimensional cubes; affine display axes not physical metric scales',
        'role':'shared interface cancels when summing subregion fluxes; not proof of general divergence theorem'})

if __name__=='__main__':
    for fn in [covers,cantor,chain,product,line_work,flux,boundary,gauss]:
        fn()
    (OUT/'generation-manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    print('Generated',len(records),'editable geometric figures.')
