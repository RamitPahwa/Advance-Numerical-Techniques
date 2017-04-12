from numpy import *
from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

deltax=.05
mu=.8
c=1;
deltat=mu*deltax/c
n=int(25/deltax)
m=int(17/deltat)

x=[i*deltax for i in range(n+1)]
x=asarray(x)

t=[i*deltat for i in range(m+1)]
t=asarray(t)

u=[]
for i in range(n+1):
	u.append([exp(-20*(i*deltax-2)**2)+exp(-(i*deltax-5)**2)])
# print u
for i in range(m):
	u[0].append(u[0][i])
	for j in range(1,n+1):
		u[j].append((1-mu)*u[j][i]+mu*u[j-1][i])
u=asarray(u)
print shape(u)
# print u[:][m]
c=[]
for i in range(n+1):
	c.append(u[i][m-2])
c=asarray(c)
# plt.plot(x,c)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 

X, T = meshgrid(x, t)
Z = u.reshape(X.shape)
ax.plot_wireframe(X,T,Z)
	# ax.contour(X,Y,Z)
ax.set_xlabel('Time')
ax.set_ylabel('X')
ax.set_zlabel('u')
# plt.show()
plt.savefig("fig-1.png")
plt.show()
