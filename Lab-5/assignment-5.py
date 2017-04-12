import os
import numpy as np
from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def power(number):
	return number*number	

def thomasAlgo(a,b,c,d):
	n=len(d)
	c_=np.zeros(n)
	d_=np.zeros(n)
	y=np.zeros(n)
	c_[1]=c[1]/b[1]
	d_[1]=d[1]/b[1]

	for i in range(2,n):
		c_[i]=c[i]/(b[i]-a[i]*c_[i-1])
		d_[i]=(d[i]-a[i]*d_[i-1])/(b[i]-a[i]*c_[i-1])

	y[n-1]=d_[n-1]
	for i in range(n-2,0,-1):
		y[i]=d_[i]-c_[i]*y[i+1]

	return y

def step1(C,dx,dt,dy,n,m):

	a=np.zeros(n,dtype=np.float32)
	b=np.zeros(n,dtype=np.float32)
	c=np.zeros(n,dtype=np.float32)
	d=np.zeros(n,dtype=np.float32)

	for j in range(1,m):
		print	
		a=[(-1/(2*power(dx))) for i in range(n)]
		b=[(1/(power(dx))+1/dt) for i in range(n)]
		c=[(-1/(2*power(dx))) for i in range(n)]
		for i in range(n):
			d[i]=(C[i][j]/dt + (C[i][j+1]-2*C[i][j]+C[i][j-1])/(2*(dy**2)))
		y=thomasAlgo(a,b,c,d)	
		for i in range(1,len(y),1):
			C[i][j]=y[i]
		C[0][j]=0.0
		C[n][j]=0.0
	C[0][m]=0
	C[n][m]=0

def step2(C,dx,dt,dy,n,m):
	a=np.zeros(n,dtype=np.float32)
	b=np.zeros(n,dtype=np.float32)
	c=np.zeros(n,dtype=np.float32)
	d=np.zeros(n,dtype=np.float32)

	for i in range(1,n):	
		a=[(-1/(2*power(dy))) for j in range(m)]
		b=[(1/(power(dy))+1/dt) for j in range(m)]
		c=[(-1/(2*power(dy))) for j in range(m)]
		for j in range(m):
			d[i]=(C[i][j]/dt + (C[i+1][j]-2*C[i][j]+C[i-1][j])/(2*(dx**2)))
		y=thomasAlgo(a,b,c,d)	
		for j in range(1,len(y),1):
			C[i][j]=y[j]
		C[i][0]=0.0
		C[i][m]=0.0
	C[n][m]=0
	C[n][0]=0



def main():
	dx=0.25
	dy=0.25
	dt=dx*dx/2
	a=-1.0
	b=1.0
	n=int((b-a)/dx)
	m=int((b-a)/dy)
	C=np.zeros((n+1,m+1),dtype=np.float32)
	for i in range(n+1):
		C[i][0]=0.0
		for j in range(1,m):
			C[i][j]=cos(pi*(-1+i*dx)/2)*cos(pi*(-1+j*dy)/2)
		C[i][m]=0.0
	
	step1(C,dx,dt,dy,n,m)
	step2(C,dx,dt,dy,n,m)
	x=[-1+i*dx for i in range(n+1)]
	x=np.asarray(x)
	y=[-1+j*dy for j in range(m+1)]
	y=np.asarray(y)
	X,Y=np.meshgrid(x,y)
	Z=C.reshape(X.shape)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d') 
	ax.plot_wireframe(X,Y,Z)
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.show()


main()