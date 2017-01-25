import os
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


# solve eequation x^2*y''+x*y'=1
# given y(1)=0 & y(1.4)=0.0566

# values of function to be returned

def A(x):
    return (-2.0*x)


def B(x):
    return (-2.0)


def C(x):
    return (-4.0*x)


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


def solveBVP(
    alpha,
    beta,
    gamma,
    h,
    a_intial,
    b_intial
    ):
    n = int((b_intial - a_intial) / (1.0*h))
    a = [0 for i in range(1, n)]
    b = [0 for i in range(1, n)]
    c = [0 for i in range(1, n)]
    d = [0 for i in range(1, n)]
    for i in range(1, n):
        x = a_intial + i * h
        a[i-1] = (1.0 / (h ** 2))- (A(x) / (2.0 * h))
        b[i-1] = (-2.0 / (h ** 2)) + B(x)
        c[i-1] = (1.0 / (h ** 2)) + (A(x) / (2.0 * h))
        d[i-1] = C(x)
        if i == 1:
            denom0 = alpha[0] - (1.5 * beta[0] / h);
            b[i-1] += a[i-1] * (-2 * beta[0] / h) / denom0;
            c[i-1] += a[i-1] * (0.5 * beta[0] /h) / denom0;
            d[i-1] -= a[i-1] * (gamma[0] / denom0);


    denom1 = alpha[1] + (1.5 * beta[1] / h);
    b[i-1] += c[i-1] * (2 * beta[1] / h) / denom1;
    a[i-1] += c[i-1] * (-0.5 * beta[1] /h) / denom1;
    d[i-1] -= c[i-1] * (gamma[1]/ denom1);
    y=thomasAlgo(a, b, c, d)
    y_a=((-2 * beta[0]/ h)*y[0] + (0.5 * beta[0] /h)*y[1] +gamma[0])/denom0;
    y_b= ((2 * beta[1] / h)*y[-1] +(-0.5 * beta[1] /h)*y[-2] + gamma[1])/denom1;

    return [y_a] + y + [y_b]

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
    plt.show()


def main():
    a_intial = 0
    b_intial = 1
    stepsize = [0.1, 0.05, 0.005]
    alpha= [1.0,2.0]
    beta=[-1.0,-1.0]
    gamma=[0.0,1.0]
    n1 =int( (b_intial- a_intial) / stepsize[0])+1
    n2=int((b_intial - a_intial) / stepsize[1])+1
    n3=int((b_intial - a_intial) / stepsize[2])+1
    y_1 = [0 for i in range(n1 + 1)]
    y_2 = [0 for i in range(n2 + 1)]
    y_3 = [0 for i in range(n3 + 1)]
    x_1= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / (1.0*stepsize[0])+1))
    x_2= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / (1.0*stepsize[1])+1))
    x_3= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / (1.0*stepsize[2])+1))
    y_1 = solveBVP(alpha, beta  ,gamma, stepsize[0], a_intial, b_intial)
    y_2 = solveBVP(alpha, beta,gamma, stepsize[1], a_intial, b_intial)
    y_3 = solveBVP(alpha, beta,gamma, stepsize[2], a_intial, b_intial)
    createFile(x_1,y_1,stepsize[0])
    createFile(x_2,y_2,stepsize[1])
    createFile(x_3,y_3,stepsize[2])

    
    p1,p2,p3=plt.plot(x_3,np.interp(x_3,x_1,y_1),'r',x_3,np.interp(x_3,x_2,y_2),'g',x_3,y_3,'b')
    plt.legend([p1, p2, p3], ["h = 0.25", "h =0.1", "h = 0.001"], loc =4)
    plt.show()

main()