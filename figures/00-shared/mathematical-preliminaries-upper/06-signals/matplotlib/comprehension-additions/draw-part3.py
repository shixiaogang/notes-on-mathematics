# -*- coding: utf-8 -*-
"""Exact analytic teaching figures for signal sampling and filtering."""
from pathlib import Path
import json
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/01-mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, provenance, BLUE, GREEN, YELLOW, INK, MUTED, BLUE_FILL

HERE = Path(__file__).resolve().parent
OWNER = 'tex/03-optimization-evolution-and-signals/03-signals-and-state-estimation/01-signal-representation-and-processing.tex'
MANIFEST = []

def export(fig, name, facts, difficulty):
    record = save(fig, HERE, name, facts)
    MANIFEST.append({'name': name, 'label': 'fig:vol1-add-'+name, 'chapter': 8,
        'owner': OWNER, 'asset': str((HERE/(name+'.pdf')).relative_to(ROOT)),
        'source': str(Path(__file__).relative_to(ROOT)), 'width_mm': 112,
        'height_mm': record['height_mm'], 'scientific_formula': facts,
        'difficulty': difficulty, 'purpose': difficulty, 'method': 'matplotlib', 'writer': 'figures_part3',
        'kind': 'analytic teaching construction; no experimental observations',
        **provenance()})

def replicas():
    fig, axs = figure(112, 48, ncols=2, sharex=True, sharey=True)
    omega = np.linspace(-4.25, 4.25, 3401)
    hat = lambda w: np.maximum(1-np.abs(w), 0)
    for ax, spacing in zip(axs, [3.0, 1.5]):
        copies = np.array([hat(omega-k*spacing) for k in range(-4, 5)])
        total = copies.sum(axis=0)
        for k, values in zip(range(-4, 5), copies):
            if not np.any(values):
                continue
            color = BLUE if k == 0 else GREEN
            ax.plot(omega, values, color=color, ls='-' if k == 0 else ':', lw=1.1 if k == 0 else .85)
        ax.plot(omega, total, color=INK, ls='--', lw=1.1)
        ax.set_title(r'$\Omega_s='+str(spacing).rstrip('0').rstrip('.')+'$')
        ax.set_xlabel(r'$\Omega$')
        ax.set_xlim(-4.25, 4.25); ax.set_ylim(-.04, 1.15)
        ax.set_xticks([-3, 0, 3]); ax.set_yticks([0, .5, 1])
    axs[0].set_ylabel(r'$T_sX_s(\Omega)$')
    assert np.isclose(hat(.75)+hat(.75-1.5), .5)
    export(fig, 'signal-spectral-replicas', {'F': 'max(1-|Omega|,0)',
        'Ts_times_Xs': 'sum over k in Z of F(Omega-k*Omega_s)',
        'Omega_max': 1, 'Omega_s': [3, 1.5], 'display_domain': [-4.25,4.25],
        'sampling': '3401 equally spaced points; k=-4,...,4 includes every nonzero copy on displayed domain'},
        'Why the sampling rate controls overlap of complete frequency copies, rather than merely a sparse drawing of one spectrum.')

def sinc_cardinal():
    fig, ax = figure(112, 48)
    t = np.linspace(-3.1, 3.1, 2481)
    centers = np.array([-1, 0, 1]); coefficients = np.array([.5, 1, -.5])
    terms = np.array([a*np.sinc(t-n) for n,a in zip(centers,coefficients)])
    labels = [r'$\frac{1}{2}\operatorname{sinc}(t+1)$',r'$\operatorname{sinc}(t)$',r'$-\frac{1}{2}\operatorname{sinc}(t-1)$']
    for values, color, ls, label in zip(terms,[GREEN,BLUE,YELLOW],[':', '--', '-.'],labels):
        ax.plot(t,values,color=color,ls=ls,lw=.9,label=label)
    ax.plot(t,terms.sum(axis=0),color=INK,lw=1.1,label=r'$f(t)$')
    sample_t=np.arange(-3,4)
    sample_values=sum(a*np.sinc(sample_t-n) for n,a in zip(centers,coefficients))
    assert np.allclose(sample_values,[0,0,.5,1,-.5,0,0])
    ax.scatter(sample_t,sample_values,color=INK,s=12,zorder=5)
    ax.axhline(0,color=MUTED,lw=.6)
    ax.set_xlim(-3.1,3.1);ax.set_ylim(-.75,1.32)
    ax.set_xticks(np.arange(-3,4));ax.set_yticks([-.5,0,.5,1])
    ax.set_xlabel(r'$t$');ax.set_ylabel('幅值')
    ax.legend(ncol=2,loc='upper right',handlelength=1.8,columnspacing=.8,
        labelspacing=.2,borderpad=.1,fontsize=7.5)
    export(fig,'signal-sinc-cardinal',{'f': '.5*sinc(t+1)+sinc(t)-.5*sinc(t-1)',
        'sinc': 'sin(pi*u)/(pi*u), sinc(0)=1', 'Ts':1, 'Omega_max': 'pi',
        'all_integer_samples': 'a[-1]=.5, a[0]=1, a[1]=-.5, all other samples=0',
        'display_domain':[-3.1,3.1], 'sampling':'2481 equally spaced points; exact integer samples separately asserted',
        'scope':'exact finite construction in L2 with bandwidth pi; not an arbitrary truncation of an infinite record'},
        'How each sample controls one cardinal sinc term, and why summing these terms reproduces the integer samples without pretending arbitrary finite recordings determine a continuous signal.')

def mean_response():
    fig, axs=figure(112,48,ncols=3,sharex=True,sharey=True)
    omega=np.linspace(0,np.pi,1801)
    for ax,M in zip(axs,[2,4,8]):
        H=np.mean(np.exp(-1j*omega[:,None]*np.arange(M)[None,:]),axis=1)
        magnitude=np.abs(H)
        assert np.isclose(magnitude[0],1)
        assert np.isclose(abs(np.mean(np.exp(-1j*(2*np.pi/M)*np.arange(M)))),0,atol=1e-14)
        ax.axvspan(1/M,1,facecolor=BLUE_FILL,zorder=0)
        ax.plot(omega/np.pi,magnitude,color=BLUE)
        ax.axvline(1/M,color=GREEN,ls='--',lw=.75)
        ax.text(1/M+.035,1.02,r'$\pi/M$',fontsize=7.5,va='bottom')
        ax.set_title(r'$M='+str(M)+'$')
        ax.set_xlim(0,1);ax.set_ylim(-.035,1.16)
        ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
        ax.set_xlabel(r'$\omega/\pi$')
    axs[0].set_ylabel(r'$|H(e^{\mathrm{i}\omega})|$')
    export(fig,'signal-mean-response',{'h':'1/M for n=0,...,M-1, zero otherwise',
        'H':'(1/M)*sum_(n=0)^(M-1) exp(-i*omega*n)', 'M':[2,4,8],
        'display_domain':[0,'pi'], 'sampling':'1801 equally spaced points, evaluated from finite complex sums; no division at removable singularities',
        'shaded_region':'omega>pi/M, frequencies outside the ideal support for M-fold downsampling'},
        'Why the isolated zeros of a moving-average filter do not delete an entire frequency interval before decimation.')

if __name__ == '__main__':
    replicas();sinc_cardinal();mean_response()
    (HERE/'manifest.json').write_text(json.dumps(MANIFEST,ensure_ascii=False,indent=2)+'\n')
