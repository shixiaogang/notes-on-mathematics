from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
L=ineq_sqp([.5,1.7],[1.,0,0],T=6)
fig,ax=figure(width_mm=96,height_mm=33); panels(fig,.12,.99,.97,.3,0)
for t,l in enumerate(L[:-1]):
    for i in range(3):
        v=l['g'][i]; inW=(i+1) in l['S']
        ax.add_patch(plt_rect:=__import__('matplotlib.patches',fromlist=['Rectangle']).Rectangle((t-.47,2-i-.42),.94,.84,facecolor=GREEN_FILL if inW else 'white',edgecolor=GREEN if inW else GRID,lw=.9 if inW else .6))
        ax.text(t,2-i,'%.2f'%v if abs(v)>=.005 else ('0' if abs(v)<5e-7 else '%.0e'%v),ha='center',va='center',fontsize=7.5,color=RED if v>5e-3 else INK)
ax.set_xlim(-.55,5.55); ax.set_ylim(-.55,2.55); ax.set_xticks(range(6)); ax.set_yticks([0,1,2]); ax.set_yticklabels(['$g_3$','$g_2$','$g_1$']); ax.set_xlabel('$t$',labelpad=1)
ax.spines['left'].set_visible(False); ax.spines['bottom'].set_visible(False); ax.tick_params(length=0)
save(fig,HERE,'figure',{'g':[l['g'].tolist() for l in L[:-1]],'W':[l['S'] for l in L[:-1]]})
