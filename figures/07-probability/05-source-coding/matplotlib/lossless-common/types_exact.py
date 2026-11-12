"""Exact type-class enumeration for i.i.d. blocks from the running source p = (0.4,0.3,0.2,0.1)."""
import math
import numpy as np
P = np.array([.4, .3, .2, .1])


def types(n):
    "all compositions (k1..k4) of n, log2 of the class size, and -log2 p of one block in the class"
    k1, k2, k3 = np.meshgrid(np.arange(n+1), np.arange(n+1), np.arange(n+1), indexing='ij')
    k1, k2, k3 = k1.ravel(), k2.ravel(), k3.ravel(); k4 = n-k1-k2-k3; m = k4 >= 0
    K = np.stack([k1[m], k2[m], k3[m], k4[m]], 1)
    lg = np.array([math.lgamma(i+1) for i in range(n+1)])
    logcount = (lg[n] - lg[K].sum(1))/math.log(2)
    selfinfo = -(K*np.log2(P)).sum(1)
    return K, logcount, selfinfo


def class_prob(logcount, selfinfo):
    return np.exp2(logcount - selfinfo)
