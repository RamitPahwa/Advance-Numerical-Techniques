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

def plotGraph(input_x,output_y,h):
    plt.ylabel("Y")
    plt.xlabel ("X")
    p=plt.plot(input_x,output_y,'r')
    plt.legend(p,["h="+str(h),],loc=4)
    plt.savefig("plot-h="+str(h)+".png")
    plt.show()


def crankNicolson():
	dx=0.05
	dt=0.005
	rx=1
	rt=0.1
	n=int(rx/dx) #for X
	m=int(rt/dt)  #for T or Y
	X=np.linspace(0,rx,n+1)
	T=np.linspace(0,rt,m)

	U=np.zeros((n+1,m),dtype=np.float64)
	U[:,0]=1.0
	for i in range(1,m):
		# print i
		A=[0]+[(1/(2*dx**2.0)) for j in range(1,n)]+[1/dx**2.0]
		# print A
		B=[-(1/(dx**2.0)+1/dt) for j in range(0,n+1)]
		# print B
		C=[1/(dx**2.0)]+[(1/(2*dx**2.0)) for j in range(1,n)]+[0]
		# print C
		D=[(U[0,i-1]*((3/(dx**2.0))-(1/dt)))-(1/(dx**2.0))*U[1,i-1]]+\
		[(U[j-1,i-1]*(-1*(1/(2*dx**2.0))))+(U[j,i-1]*(1/(dx**2.0)-1/dt))+(U[j+1,i-1]*(-1*(1/(2*dx**2.0)))) for j in range(1,n)]\
		+[(-1*U[n-1,i-1]*(1/(dx**2.0)))-(1/(dx**2.0)+1/dt)*U[m,i-1]]
		# print D
		U[:,i]=np.array(thomasAlgo(A,B,C,D))
		# print thomasAlgo(A,B,C,D)
		# print U	
	return U,X	

U,X=crankNicolson()
plotGraph(U[:,15],X,0)



