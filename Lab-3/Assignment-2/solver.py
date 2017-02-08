import os
import numpy as np
import matplotlib.pyplot as plt
import math

def intialGuess(x):
	return x*(math.pi-x)+0.5

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


def solver(a_intial,b_intial,y_a,y_b,h,k,y,n):
	A=np.array([1.0/h**2 -((1.0/4*h**2)*(2*y[i-1]-2*y[i+1])) for i in range(1,n)],dtype=np.float64)
	B=np.array([-2.0/h**2 -2.0*(y[i]) + 1 for i in range(1,n)],dtype=np.float64)
	C=np.array([1.0/h**2 -((1.0/4*h**2)*(2*y[i+1]-2*y[i-1])) for i in range(1,n)],dtype=np.float64)
	D=np.array([-1.0 - y[i]+y[i]**2 +((y[i+1]-y[i-1])/2*h)**2 -((1.0/h**2)*(y[i+1]-2*y[i]+y[i-1])) for i in range(1,n)],dtype=np.float64)
	dy=np.array([0]+thomasAlgo(A,B,C,D)+[0],dtype=np.float64)
	return dy

def createFile(input_x,output_y,h):
    cwd=os.getcwd()    
    f=open(str(cwd)+"/Result-h="+str(h)+".txt",'w+')
    f.write("\t\tResult for h="+str(h)+"\n\n")
    f.write("\tValue of X\t\tValue of Y\n\n")
    for i in range(len(input_x)):
        f.write("\t"+str(input_x[i])+"\t\t"+str(output_y[i])+"\n")

def plotGraph(input_x,output_y,h):
    plt.ylabel("Y")
    plt.xlabel ("X")
    p=plt.plot(input_x,output_y,'r')
    plt.legend(p,["h="+str(h),],loc=4)
    plt.savefig("plot-h="+str(h)+".png")
    plt.show()

def main():
	a_intial=0
	b_intial=math.pi
	y_a=0.5
	y_b=0.5
	error=0.01
	n=100
	h=math.pi/n
	y=np.zeros(n+1)
	y_temp=np.zeros(n+1)
	# dy here may not be required
	dy=np.zeros(n+1)
	for i in range(n+1):
		y[i]=intialGuess(a_intial+i*h)
	# print y
	# for k th iteration
	k=1
	flag=0
	while(flag==0):
		# print k 
		dy=solver(a_intial,b_intial,y_a,y_b,h,k,y,n)
		y_temp=np.add(y,dy)
		if np.amax(np.absolute(np.subtract(y_temp,y)))<=error :
			y=y_temp
			flag=1
		else:
			y=y_temp
			flag=0
			k=k+1
	x=np.linspace(0,1,n+1)
	createFile(x,y,h)
	plotGraph(x,y,h)

main()