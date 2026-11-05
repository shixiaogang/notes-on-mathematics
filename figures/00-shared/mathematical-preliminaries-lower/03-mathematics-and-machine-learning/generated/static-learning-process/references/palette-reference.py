"""Exact native color swatches supplied only as the v3 style reference."""
from pathlib import Path
import os
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'build/figure-proofs/matplotlib-cache'))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,ax=plt.subplots(figsize=(10,3),dpi=180)
fig.patch.set_facecolor('#FFFFFF');ax.set_facecolor('#FFFFFF')
for i,(main,fill) in enumerate([('#7188A3','#E5EAF0'),('#829C8B','#E8EEE9'),('#B4A16F','#F1ECDD'),('#A7787D','#F0E5E6'),('#9588A5','#ECE8F0')]):
 ax.add_patch(Rectangle((i*2+.1,1.1),1.6,1.0,facecolor=main,edgecolor=main))
 ax.add_patch(Rectangle((i*2+.1,.1),1.6,.7,facecolor=fill,edgecolor=main,linewidth=2))
ax.set_xlim(0,10);ax.set_ylim(0,2.3);ax.axis('off');fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180,facecolor='#FFFFFF');plt.close(fig)
