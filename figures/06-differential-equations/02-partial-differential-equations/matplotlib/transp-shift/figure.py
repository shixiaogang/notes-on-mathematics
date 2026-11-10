# Target: constant-speed translation of a tent, v=1; profiles and space-time field.
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'transp-common'))
from transp_common import *
fig,(a,b)=figure(112,50,ncols=2)
x=np.linspace(-2,5,1401)
cs=shades(2)
a.plot(x,tent(x,0),color=RED,lw=1.4)
for t,c in zip([1,2],cs): a.plot(x,tent(x-t,0),color=c,lw=1.4)
for t,c in zip([0,1,2],[RED]+cs): a.text(t,1.05,f'$t={t}$',ha='center',color=c if t else RED,fontsize=7.5)
a.set_xlim(-2,4); a.set_ylim(0,1.25); tail(a,'$x$','(a)','$u$')
tt=np.linspace(0,3,301); X,T=np.meshgrid(x,tt)
heat(b,tent(X-T,0),(-2,5),(0,3))
for x0 in np.arange(-2,5,1): b.plot([x0,x0+3],[0,3],color=CHAR,lw=.8)
b.plot([-2,5],[0,0],color=RED,lw=3,clip_on=False)
b.set_xlim(-2,5); b.set_ylim(0,3); tail(b,'$x$','(b)','$t$')
save(fig,Path(__file__).resolve().parent,'figure',{'formula':'u(x,t)=u0(x-t), u0 tent centred at 0 half-width 1'})
