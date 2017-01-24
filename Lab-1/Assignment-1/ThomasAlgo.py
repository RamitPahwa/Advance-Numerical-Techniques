import matplotlib as plt
import numpy as np


def A(x):
	return x*x

def B(x):
	return x

def C(x):
	return 0


def solveThomas(a,b,c,d):
	n = len(d)
    c1 = [0 for i in range(n)]
    d1 = [0 for i in range(n)]
    y = [0 for i in range(n)]

    c1[0] = c[0] / (1.0 * b[0])
    d1[0] = d[0] / (1.0 * b[0])
    
    for i in range(1,n):
        c1[i] = c[i]/(b[i] - a[i]*c1[i-1])
        d1[i] = (d[i] - a[i]*d1[i-1])/(b[i] - a[i]*c1[i-1])
    
    y[n-1] = d1[n-1]
    for i in range(n-2, -1, -1):
        y[i] = d1[i] - c1[i]*y[i+1]

    return y

def solveBVP(h):
	


