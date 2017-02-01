import os
import numpy as np
import matplotlib.pyplot as plt

def blockAlgo(a, b, c, d):
    n = len(d)
    
    b_ = np.zeros(a.shape)
    c_ = np.zeros(a.shape)
    d_ = np.zeros((n,2,1))
    w = np.zeros((n,2,1))

    c_[0] = np.linalg.inv(b[0]).dot(c[0]) 
    d_[0] = np.linalg.inv(b[0]).dot(d[0]) 
    
    for i in range(1,n):
        b_[i] = b[i] - a[i].dot(c_[i-1])
        c_[i] = np.linalg.inv(b_[i]).dot(c[i])
        d_[i] = np.linalg.inv(b_[i]).dot((d[i] - a[i].dot(d_[i-1])))
    
    w[n-1] = np.copy(d_[n-1])
    for i in range(n-2, -1, -1):
        w[i] = d_[i] - c_[i].dot(w[i+1])

    return w
def solveBVP(a_intial, b_intial, c1, c2, c3, h):
    n = int ((b_intial-	a_intial) / (1.0*h))
    a = np.zeros((n-1,2,2))
    b = np.zeros((n-1,2,2))
    c = np.zeros((n-1,2,2))
    d = np.zeros((n-1,2,1))

    for i in range(n-1):
        # As i starts from 0, we define x = l + (i+1)*h
        x = a_intial+(i+1)*h             
        a[i] = np.array(([[((1.0 / (h**2))-(2.0/h)), 0],[1, 2.0/h ]]))
        b[i] = np.array(([[1.0-(2.0 / (h**2)), -6.0],[1, -2.0 / h]]))
        c[i] = np.array(([[((1.0 / (h**2))+(2.0/h)), 0],[0, 0]]))
        d[i] = np.array(([[1],[0]]))
        if i == 0:
            d[i] =  d[i] - a[i].dot(np.array(([[c1], [c2]])))

    d[n-2] = d[n-2] -  c[n-2].dot(np.array(([[c3], [0]])))
    w = blockAlgo(a, b, c, d)
    w = np.vstack(([np.array(([[c1], [c2]]))], w))
    return np.vstack((w, [np.array(([[c3], [0]]))]))

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
	b_intial=1
	c1=0
	c2=0
	c3=1
	step_sizes=[0.1,0.5,0.002]
	n1=int((b_intial - a_intial) / (1.0*step_sizes[0])+1)
	n2=int((b_intial - a_intial) / (1.0*step_sizes[1])+1)
	n3=int((b_intial - a_intial) / (1.0*step_sizes[2])+1)
	x_1= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / (1.0*step_sizes[0])+1))
	x_2= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / (1.0*step_sizes[1])+1))
	x_3= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / (1.0*step_sizes[2])+1))
	w_1=solveBVP(a_intial,b_intial,c1,c2,c3,step_sizes[0])
	w_2=solveBVP(a_intial,b_intial,c1,c2,c3,step_sizes[1])
	w_3=solveBVP(a_intial,b_intial,c1,c2,c3,step_sizes[2])
	y_1 = w_1[[range(w_1.shape[0])],[1],[0]]
	y_2 = w_2[[range(w_2.shape[0])],[1],[0]]
	y_3 = w_3[[range(w_3.shape[0])],[1],[0]]
	y_1=y_1[0]
	y_2=y_2[0]
	y_3=y_3[0]
	z_1 = w_1[[range(w_1.shape[0])],[0],[0]]
	z_2 = w_2[[range(w_2.shape[0])],[0],[0]]
	z_3 = w_3[[range(w_3.shape[0])],[0],[0]]
	z_1=z_1[0]
	z_2=z_2[0]
	z_3=z_3[0]
	y_1[n1-1]=(step_sizes[0]/2.0)*(y_1[n1-2]*(2.0/step_sizes[0])+z_1[n1-1]+z_1[n1-1])
	y_2[n2-1]=(step_sizes[1]/2.0)*(y_2[n2-2]*(2.0/step_sizes[1])+z_2[n2-1]+z_2[n2-1])
	y_3[n3-1]=(step_sizes[2]/2.0)*(y_3[n3-2]*(2.0/step_sizes[2])+z_3[n3-1]+z_3[n3-1])
	createFile(x_1,y_1,step_sizes[0])
	createFile(x_2,y_2,step_sizes[1])
	createFile(x_3,y_3,step_sizes[2])
	plotGraph(x_1,y_1,step_sizes[0])
	plotGraph(x_2,y_2,step_sizes[1])
	plotGraph(x_3,y_3,step_sizes[2])
	p1,p2,p3=plt.plot(x_3,np.interp(x_3,x_1,y_1),'r.',x_3,np.interp(x_3,x_2,y_2),'g--',x_3,y_3,'b')
	plt.legend([p1, p2, p3], ["h = 0.1", "h =0.5", "h = 0.002"], loc =4)
	plt.savefig("allTogether.png")
	plt.show()
	
main()