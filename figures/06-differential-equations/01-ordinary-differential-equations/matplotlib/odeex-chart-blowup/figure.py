from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"odeex-common"))
from odeex_common import *
HERE=Path(__file__).resolve().parent

# Circle field with alpha'=2: u=tan t in the north chart, v=cot t in the south chart.
fig,axes=figure(width_mm=112,height_mm=54,ncols=2,gridspec_kw={'width_ratios':[1,1.35]})
panel(fig,.04,.975,.965,.24,.2)
ax=axes[0]; th=np.linspace(0,2*np.pi,400); ax.plot(np.cos(th),np.sin(th),color=BLUE,lw=1.5,zorder=2)
for a in np.linspace(0,2*np.pi,12,endpoint=False):
    y=np.array([np.sin(a),-np.cos(a)]); v=np.array([np.cos(a),np.sin(a)])*.5
    ax.annotate('',xy=y+v,xytext=y,arrowprops=dict(arrowstyle='-|>,head_width=.16,head_length=.28',color=PURPLE,lw=.85,shrinkA=0,shrinkB=0),zorder=3)
dot(ax,0,-1); ax.plot([0],[1],'o',ms=4.4,mfc='white',mec=STROKE,mew=1,zorder=6)
ax.text(0,-1.2,'S',ha='center',va='top',fontsize=8); ax.text(0,1.2,'N',ha='center',va='bottom',fontsize=8)
ax.set_xlim(-1.55,1.55); ax.set_ylim(-1.55,1.55); ax.set_aspect('equal'); ax.axis('off')
ax=axes[1]; t=np.linspace(-.05,1.53,400); u=np.tan(t); ax.plot(t[u<8],u[u<8],color=BLUE,lw=1.5,zorder=3)
t=np.linspace(.06,2.6,500); v=1/np.tan(t); m=(v<8)&(v>-8); t2=t.copy(); ax.plot(t[m],v[m],color=YELLOW,lw=1.5,zorder=3)
ax.axvspan(0,np.pi/2,fc=BLUE_FILL,ec='none',zorder=0); ax.axhline(0,color=MUTED,lw=.6,zorder=1)
ax.axvline(np.pi/2,color=RED,lw=.95,ls=(0,(3,2))); ax.axvline(np.pi/4,color=MUTED,lw=.85,ls=':'); dot(ax,0,0); dot(ax,np.pi/4,1,ms=3.6,color=INK)
ax.text(1.28,6.6,'u=tan t',color=BLUE,fontsize=7.5,ha='right',va='center'); ax.text(2.25,-3.0,'v=cot t',color=YELLOW,fontsize=7.5,ha='right',va='center')
ax.set_xlim(-.05,2.6); ax.set_ylim(-8,8); ax.set_xticks([0,np.pi/4,np.pi/2]); ax.set_xticklabels(['0','π/4','π/2']); ax.set_yticks([-5,0,5]); ax.set_xlabel('t',labelpad=1)
tags(fig,axes)
save(fig,HERE,'figure',{'u':'tan t','v':'cot t','switch':'t=pi/4,u=v=1'})
