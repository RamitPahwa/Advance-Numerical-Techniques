from numpy import *
from math import *
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

deltax=[0.1,0.05,0.01]
deltay=[0.1,0.05,0.01]
for l in range(3):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d') 

	n=int(4/deltax[l])
	m=int(4/deltay[l])

	x=[-1+i*deltax[l] for i in range(n+1)]
	x=asarray(x)
	y=[-1+j*deltay[l] for j in range(m+1)]
	y=asarray(y)

	U=[]
	for i in range(n+1):
		U.append([((i*deltax[l])**2)/2])
		if(i==n):
			for j in range(1,m+1):
				U[i].append((8+2*j*deltay[l]))
		else:
			for j in range(1,m):
				U[i].append(0)
			U[i].append((i*deltax[l])**2)
	# print U
	U=asarray(U)
	for k in range(50):
		for i in range(1,n):
			for j in range(1,m):
				U[i][j]=1/(2*((1/deltax[l]**2)+ 1/deltay[l]**2))*((U[i+1][j]+U[i-1][j])/(deltax[l]**2)+(U[i][j+1]+U[i][j-1])/(deltay[l]**2))

	X, Y = meshgrid(x, y)
	Z = U.reshape(X.shape)
	ax.plot_wireframe(X,Y,Z)
		# ax.contour(X,Y,Z)
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.savefig("dx=dy="+str(deltax[l])+".png")
	plt.show()
