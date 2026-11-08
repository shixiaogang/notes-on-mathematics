"""Exact analytic illustrations; white canvas, no background grid, 8 pt labels.
Reproduce with python3 generate.py. Sources are formulas in each metadata file.
"""
from pathlib import Path
import sys, json, os
R=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
os.environ.setdefault('MPLCONFIGDIR',str(R/'build/vol1-illustration-mpl'))
sys.path.insert(0,str(R/'figures/00-shared/academic-drawing'))
import plot_style as s
import matplotlib.pyplot as plt
import numpy as np
s.configure();D=Path(__file__).resolve().parent

def canvas(n=1,h=53):
 f,aa=plt.subplots(1,n,figsize=(112/25.4,h/25.4),layout='constrained');aa=np.atleast_1d(aa)
 for ax in aa:
  ax.grid(False);ax.tick_params(length=2.5);ax.set_xlabel('$x$')
 return f,aa

def save(f,name,facts):
 p=D/name;p.mkdir(exist_ok=True);s.prepare_figure(f)
 for ext in ['pdf','png']: f.savefig(p/('figure.'+ext),dpi=220)
 meta={'facts':facts,'method':'Matplotlib','source':'../generate.py','physical_size_mm':[112,f.get_figheight()*25.4],'reference_width_mm':112,'scale':1,'background_grid':False,'style':s.style_record(),'font_licenses':'fonts/licenses/','font_versions':'figures/00-shared/academic-drawing/font-manifest.json'}
 (p/'figure.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n');plt.close(f)

f,aa=canvas();ax=aa[0];x=np.linspace(.25,2,500);a=.6
ax.plot(x,x*x,color=s.BLUE);ax.plot(x,2*a*x-a*a,color=s.GREEN,ls='--')
for h,c in [(.95,s.MUTED),(.45,s.YELLOW)]:
 b=a+h;ax.plot([.25,2],[(a+b)*.25-a*b,(a+b)*2-a*b],color=c,lw=.75)
 ax.plot(b,b*b,'o',ms=3,color=c)
ax.plot(a,a*a,'o',ms=3.6,color=s.BLUE)
ax.text(1.7,3.1,'$f$',color=s.BLUE);ax.text(1.7,1.25,'切线',color=s.GREEN)
ax.set(xlim=(.2,2.05),ylim=(-.1,4.1),ylabel='$y$');ax.set_xticks([.6,1.05,1.55],['$a$','$a+h_2$','$a+h_1$']);ax.set_yticks([0,2,4])
save(f,'secants-to-tangent',{'f':'x^2','a':a,'h':[.95,.45],'secant_slope':'2a+h','tangent_slope':'2a'})

f,aa=canvas(2,55);x=np.linspace(-1,1,600)
for ax in aa: ax.axhline(0,color=s.MUTED,lw=.6);ax.set_xticks([-1,0,1])
aa[0].plot(x,np.exp(x),color=s.INK,label='$e^x$')
aa[0].plot(x,1+x,color=s.BLUE,ls='--',label='$T_1$');aa[0].plot(x,1+x+x*x/2,color=s.GREEN,label='$T_2$');aa[0].legend(loc='upper left',handlelength=1.3)
aa[0].set(ylabel='$y$',title='(a)');aa[0].set_yticks([0,1,2,3])
aa[1].plot(x,np.exp(x)-1-x,color=s.BLUE,ls='--',label='$R_1$');aa[1].plot(x,np.exp(x)-1-x-x*x/2,color=s.GREEN,label='$R_2$');aa[1].legend(loc='upper left',handlelength=1.3);aa[1].set(ylabel='$R$',title='(b)');aa[1].set_yticks([0,.4,.8])
save(f,'taylor-approximation',{'f':'exp(x)','center':0,'x':[-1,1],'T1':'1+x','T2':'1+x+x^2/2','Rk':'f-Tk','role':'exact errors, not proof of convergence'})

f,aa=canvas(2,55);xx=np.linspace(0,2,600);c=1;h=.45;ff=lambda x:1+x*x/3;F=lambda x:x+x**3/9
ax=aa[0];ax.plot(xx,ff(xx),color=s.BLUE);z=np.linspace(c,c+h,100);ax.fill_between(z,0,ff(z),color=s.BLUE_FILL)
ax.plot([c,c+h],[ff(c),ff(c)],color=s.GREEN,ls='--');ax.set(xlim=(0,2),ylim=(0,2.7),ylabel='$f$',title='(a)');ax.set_xticks([0,c,c+h],['$a$','$x$','$x+h$']);ax.set_yticks([])
ax=aa[1];ax.plot(xx,F(xx),color=s.BLUE);ax.plot([c,c+h],[F(c),F(c+h)],color=s.GREEN);ax.plot([c,c+h],[F(c),F(c+h)],'o',color=s.GREEN,ms=3)
ax.plot([c,c+h],[F(c),F(c)],color=s.MUTED,ls=':',lw=.6);ax.plot([c+h,c+h],[F(c),F(c+h)],color=s.GREEN,lw=1.1)
ax.set(xlim=(0,2),ylim=(0,3),ylabel='$F$',title='(b)');ax.set_xticks([0,c,c+h],['$a$','$x$','$x+h$']);ax.set_yticks([])
save(f,'accumulation-increment',{'f':'1+x^2/3','F':'x+x^3/9','a':0,'x':1,'h':.45,'shaded_area':'F(x+h)-F(x)','secant_slope':'integral_x^(x+h) f / h'})

f,aa=canvas(2,55);B=np.linspace(1,15,300);ep=np.geomspace(.025,1,300)
for p,c,ls in [(.5,s.GREEN,'-'),(1,s.MUTED,'--'),(2,s.BLUE,'-')]:
 y=np.log(B) if p==1 else (B**(1-p)-1)/(1-p)
 z=-np.log(ep) if p==1 else (1-ep**(1-p))/(1-p)
 aa[0].plot(B,y,color=c,ls=ls,label=rf'$p={p:g}$');aa[1].plot(ep,z,color=c,ls=ls,label=rf'$p={p:g}$')
aa[0].axhline(1,color=s.BLUE,lw=.6,ls=':');aa[1].axhline(2,color=s.GREEN,lw=.6,ls=':')
aa[0].set(xlabel='$b$',ylabel=r'$\int_1^b x^{-p}\,\mathrm{d}x$',ylim=(0,7),title='(a)');aa[0].set_xticks([1,8,15]);aa[0].legend(loc='upper left',handlelength=1.2)
aa[1].set(xlabel=r'$\varepsilon$',ylabel=r'$\int_\varepsilon^1 x^{-p}\,\mathrm{d}x$',xscale='log',xlim=(1,.025),ylim=(0,7),title='(b)');aa[1].set_xticks([1,.1,.025],['1','0.1','0.025']);aa[1].legend(loc='upper left',handlelength=1.2)
save(f,'improper-power-integrals',{'p':[.5,1,2],'left_b':[1,15],'right_epsilon':[1,.025],'truncated_integrals':'log at p=1, otherwise power antiderivative','right_y_clip':[0,7],'limits':'at infinity converges iff p>1; at zero iff p<1'})
