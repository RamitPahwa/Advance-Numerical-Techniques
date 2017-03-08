import os
import numpy as np
import matplotlib.pyplot as plt
import math

# Crank Nicolson

def thomasAlgo(
    a,
    b,
    c,
    d,
    ):
    n = len(d)
    c1 = [0 for i in range(0, n)]
    d1 = [0 for i in range(0, n)]
    y = [0 for i in range(0, n)]

    c1[0] = c[0] / b[0]
    d1[0] = d[0] / b[0]

    for i in range(1, n, 1):
        c1[i] = c[i] / (b[i] - a[i] * c1[i - 1])
        d1[i] = (d[i] - a[i] * d1[i - 1]) / (b[i] - a[i] * c1[i - 1])

    y[n - 1] = d1[n - 1]
    for i in range(n - 2, -1, -1):
        y[i] = d1[i] - c1[i] * y[i + 1]

    return y

def crankNicolson():
	dx=0.05
	dt=0.005
	rx=1
	rt=0.1
	n=int(rx/dx) #for X
	m=int(rt/dt)  #for T or Y
	X=np.linspace(0,rx,n)
	T=np.linspace(0,rt,m)
	print len(X)
	print len(T)

	U=np.zeros((n,m),dtype=np.float64)
	print len(U)

crankNicolson()


