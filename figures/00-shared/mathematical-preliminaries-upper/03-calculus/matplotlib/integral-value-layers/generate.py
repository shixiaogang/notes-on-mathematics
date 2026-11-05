"""Analytic teaching figure: f(x)=4x(1-x), x in [0,1]; no observations or random data."""
from pathlib import Path
import sys,json
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
import plot_style as st
st.configure()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
OUT=Path(__file__).resolve().parent

def inputs():
 x=np.linspace(0,1,1601)
 edges=np.linspace(0,1,5); mids=(edges[1:]+edges[:-1])/2
 return x,4*x*(1-x),edges,mids,4*mids*(1-mids)

def draw():
 x,y,edges,mids,heights=inputs()
 fig=plt.figure(figsize=(169/25.4,80/25.4))
 a=fig.add_axes([.075,.27,.38,.62]); b=fig.add_axes([.59,.27,.38,.62])
 for ax in [a,b]:
  ax.set(xlim=(0,1),ylim=(0,1.12),xticks=[0,.5,1],yticks=[0,.5,1],xlabel='$x$')
  ax.set_ylabel('$f(x)$',labelpad=3)
  ax.plot(x,y,color=st.INK,zorder=4)
 for k in range(4):
  a.add_patch(Rectangle((edges[k],0),.25,heights[k],facecolor=st.BLUE_FILL,edgecolor=st.BLUE,lw=.75))
  a.plot([mids[k],mids[k]],[0,heights[k]],color=st.GREEN,lw=.6,ls='--')
 a.scatter(mids,heights,color=st.GREEN,s=12,zorder=5)
 a.set_title('区间取样',pad=10)
 b.set_title('取值分档',pad=10)
 # Four dyadic value bins plus the singleton maximum (height 1, measure 0).
 # Each positive-width bin's preimage generally has two interval components.
 for j in range(4):
  lo,hi=j/4,(j+1)/4
  leftlo=(1-np.sqrt(1-lo))/2; lefthi=(1-np.sqrt(1-hi))/2
  for start,end in [(leftlo,lefthi),(1-lefthi,1-leftlo)]:
   b.add_patch(Rectangle((start,0),end-start,lo,facecolor=st.BLUE_FILL,edgecolor=st.BLUE,lw=.6))
 # Highlight a single output bin and the two separated input ranges that produce it.
 l=(1-np.sqrt(.5))/2; h=.25
 b.axhspan(.5,.75,facecolor=st.YELLOW_FILL,zorder=0)
 for start,end in [(l,h),(1-h,1-l)]:
  b.add_patch(Rectangle((start,0),end-start,.5,facecolor=st.GREEN_FILL,edgecolor=st.GREEN,lw=1))
 b.axhline(.5,color=st.MUTED,lw=.6,ls='--');b.axhline(.75,color=st.MUTED,lw=.6,ls='--')
 b.text(.5,.63,'$[1/2,3/4)$',ha='center',va='center',fontsize=7.5)
 c=fig.add_axes([.59,.10,.38,.045]);c.set(xlim=(0,1),ylim=(-1,1));c.axis('off')
 c.plot([0,1],[0,0],color=st.GRID,lw=.6)
 # Endpoint types: [l,h) union (1-h,1-l].
 for start,end,lc,rc in [(l,h,True,False),(1-h,1-l,False,True)]:
  c.plot([start,end],[0,0],color=st.GREEN,lw=2)
  for val,closed in [(start,lc),(end,rc)]:
   c.plot(val,0,'o',ms=3.4,mec=st.GREEN,mfc=st.GREEN if closed else 'white',mew=.8)
 fig.text(.56,.11,'$E_2$',ha='right',fontsize=7.5)
 st.prepare_figure(fig)
 for ext in ['pdf','svg','png']:fig.savefig(OUT/f'figure.{ext}',dpi=300)
 (OUT/'analytic-definitions.json').write_text(json.dumps({'function':'f(x)=4x(1-x)','domain':[0,1],'curve_samples':1601,'riemann_partition':edges.tolist(),'sample_points':mids.tolist(),'sample_values':heights.tolist(),'riemann_midpoint_sum':float(sum(heights)/4),'lebesgue_bins':[j/4 for j in range(5)],'highlighted_bin':'[1/2,3/4)','highlighted_preimage':[[float(l),h],[1-h,float(1-l)]],'endpoint_inclusion':[['closed','open'],['open','closed']],'singleton_maximum':'{1/2} has measure zero; omitted from positive-width rectangles','style':st.style_record()},ensure_ascii=False,indent=2)+'\n')
 # Numeric relations are checked from the exact expressions used above.
 assert np.isclose(sum(heights)/4,11/16)
 assert 0<l<h<1-h<1-l<1
 for point in [l,1-l]:assert np.isclose(4*point*(1-point),.5)
 for point in [h,1-h]:assert np.isclose(4*point*(1-point),.75)
 plt.close(fig)
if __name__=='__main__':draw()
