"""New exact data panels for paths and mixed TikZ/Matplotlib figures."""
from pathlib import Path
import sys,json,math
import numpy as np
import matplotlib.pyplot as plt
import pymupdf as fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
REGISTRY=json.loads((OUT/'registry.json').read_text())
def figure_dir(key):
 p=Path(REGISTRY['figures']['v1-'+key]['folder'])
 return Path(__import__('os').environ['ACADEMIC_PROOF_DIR'])/p.relative_to('figures') if __import__('os').environ.get('ACADEMIC_PROOF_DIR') else ROOT/p
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,RED,GREEN,MUTED,note
from plot_style import BLUE, GREEN, YELLOW, RED, PURPLE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
configure()
sys.path.insert(0,str(OUT));import instrument_export

def export(fig,key,name='figure'):
 d=figure_dir(key);d.mkdir(parents=True,exist_ok=True)
 prepare_figure(fig)
 for ext in ['pdf','svg','png']:fig.savefig(d/f'{name}.{ext}',dpi=360)
 plt.close(fig)

def paths():
 t=np.arange(0,100,10);values=np.array([[14,16,12,23,20,26,23,31,27,34],[14,10,15,10,14,8,11,7,13,9],[14,20,24,19,27,32,30,24,34,37]])
 fig,ax=plt.subplots(figsize=(112/25.4,69/25.4),layout='constrained')
 for i,(y,c,m) in enumerate(zip(values,[BLUE,GREEN,PURPLE],['o','s','^']),1):ax.plot(t,y,color=c,marker=m,ms=3,ls=['-','--',':'][i-1],label=rf'$\omega_{i}$')
 ax.axvline(50,color=MUTED,ls=':',lw=.65)
 ax.set(xlabel=r'时间 $t$',ylabel=r'过程取值 $X_t(\omega)$',xlim=(-2,92),ylim=(0,41),xticks=[0,25,50,75,90],yticks=[0,10,20,30,40])
 ax.legend(loc='upper left',ncols=3)
 note(ax.text(52,39,r'固定 $t_0=50$，沿竖线取随机变量',fontsize=8,va='top'))
 export(fig,'rv-paths')
 (figure_dir('rv-paths')/'data.json').write_text(json.dumps({'kind':'Exact teaching coordinates copied from active TikZ source, not simulated observations','time':t.tolist(),'paths':values.tolist(),'fixed_time':50,'section_values':[26,8,32]},ensure_ascii=False,indent=2)+'\n')

def mixed(key,which):
 if which=='transient':
  k=np.arange(21);x1=40/3*(.8**k-.5**k);x2=.5**k;y=np.hypot(x1,x2)
  assert y[1]>y[0] and y[-1]<.2
  fig,ax=plt.subplots(figsize=(82/25.4,65/25.4),layout='constrained')
  ax.plot(k,y,color=BLUE,marker='o',ms=2.6)
  ax.axhline(1,color=MUTED,ls=':',lw=.6)
  ax.set(xlabel=r'迭代步 $k$',ylabel=r'$\Vert A^k x_0\Vert_2$',xlim=(-.4,20.4),ylim=(0,5.7),xticks=[0,5,10,15,20],yticks=[0,1,3,5])
  definition={'matrix':[[.8,4],[0,.5]],'x0':[0,1],'steps':k.tolist(),'trajectory':np.c_[x1,x2].tolist(),'norm2':y.tolist(),'formula':'x1[k]=(40/3)(0.8^k-0.5^k), x2[k]=0.5^k'}
 else:
  theta=np.linspace(0,np.pi,601);arc=theta;chord=2*np.sin(theta/2)
  fig,ax=plt.subplots(figsize=(82/25.4,65/25.4),layout='constrained')
  ax.plot(theta,arc,color=BLUE,label='短弧长度')
  ax.plot(theta,chord,color=GREEN,ls='--',label='弦长')
  ax.set(xlabel=r'圆心角 $\theta$',ylabel='距离',xlim=(0,np.pi),ylim=(0,3.4),xticks=[0,np.pi/2,np.pi],xticklabels=['0',r'$\pi/2$',r'$\pi$'],yticks=[0,1,2,3])
  ax.legend(loc='upper left')
  definition={'circle_radius':1,'theta':theta.tolist(),'arc':arc.tolist(),'chord':chord.tolist(),'formulas':['d_intrinsic=theta, 0<=theta<=pi','d_extrinsic=2*sin(theta/2)']}
 export(fig,key,'data-panel')
 d=figure_dir(key);(d/'data-panel-definitions.json').write_text(json.dumps(definition,ensure_ascii=False,indent=2)+'\n')
 left=fitz.open(d/'source.pdf');right=fitz.open(d/'data-panel.pdf');doc=fitz.open();page=doc.new_page(width=169/25.4*72,height=65/25.4*72)
 page.show_pdf_page(fitz.Rect(0,0,82/25.4*72,page.rect.height),left,0)
 page.show_pdf_page(fitz.Rect(87/25.4*72,0,page.rect.width,page.rect.height),right,0)
 doc.save(d/'figure.pdf');page.get_pixmap(dpi=360).save(d/'figure.png');(d/'figure.svg').write_text(page.get_svg_image(text_as_path=True))
 (d/'composition.json').write_text(json.dumps({'route':'TikZ geometry + Matplotlib quantitative panel, vector PDF composition with PyMuPDF at native 82mm panel widths','left':'source.pdf','right':'data-panel.pdf','page_mm':[169,65],'definitions':'data-panel-definitions.json','style':style_record()},ensure_ascii=False,indent=2)+'\n')
 left.close();right.close();doc.close()
paths();mixed('ch06-transient-growth','transient');mixed('geometry-circle-distances','circle')
