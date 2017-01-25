import os
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


# solve eequation x^2*y''+x*y'=1
# given y(1)=0 & y(1.4)=0.0566

# values of function to be returned

def A(x):
    return (1.0 / x)


def B(x):
    return 0.0


def C(x):
    return (1 / x **2)


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
    a_intial,
    b_intial,
    h,
    y_a,
    y_b,
    ):
    n = int((b_intial - a_intial) / h)+1
    a = [0 for i in range(1, n)]
    b = [0 for i in range(1, n)]
    c = [0 for i in range(1, n)]
    d = [0 for i in range(1, n)]
    for i in range(1, n):
        x = a_intial + i * h
        a[i-1] = (1.0 / (h ** 2))- (A(x) / (2.0 * h))
        b[i-1] = (-2.0 / (h ** 2)) + B(x)
        c[i-1] = (1.0 / (h ** 2)) + (A(x) / (2.0 * h))
        if i == 1:
            d[i-1] = C(x) - a[i-1] * y_a
        elif i == n - 1:
            d[i-1] = C(x) - c[i-1] * y_b
        else:
            d[i-1] = C(x)

    return [y_a] + thomasAlgo(a, b, c, d) + [y_b]


def main():
    a_intial = 1
    b_intial = 1.4
    stepsize = [0.1, 0.05, 0.01]
    y_a = 0
    y_b = 0.0566
    n1 =int( (b_intial- a_intial) / stepsize[0])+1
    n2=int((b_intial - a_intial) / stepsize[1])+1
    n3=int((b_intial - a_intial) / stepsize[2])+1
    y_1 = [0 for i in range(n1 + 1)]
    y_2 = [0 for i in range(n2 + 1)]
    y_3 = [0 for i in range(n3 + 1)]
    x_1= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / stepsize[0]+1) + 1)
    x_2= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / stepsize[1]+1) + 1)
    x_3= np.linspace(a_intial, b_intial, int((b_intial - a_intial) / stepsize[2]+1) + 1)
    y_1 = solveBVP(a_intial, b_intial, stepsize[0], y_a, y_b)
    y_2 = solveBVP(a_intial, b_intial, stepsize[1], y_a, y_b)
    y_3 = solveBVP(a_intial, b_intial, stepsize[2], y_a, y_b)
    cwd=os.getcwd()    
    f=open(str(cwd)+"/Result-h="+str(stepsize[0])+".txt",'w+')
    f.write("\t\tResult\n\n")
    f.write("\tValue of X\t\tValue of Y\n\n")
    for i in range(len(x_1)):
        f.write("\t"+str(x_1[i])+"\t\t"+str(y_1[i])+"\n")
    f=open(str(cwd)+"/Result-h="+str(stepsize[1])+".txt",'w+')
    f.write("\t\tResult\n\n")
    f.write("\tValue of X\t\tValue of Y\n\n")
    for i in range(len(x_2)):
        f.write("\t"+str(x_2[i])+"\t\t"+str(y_2[i])+"\n")
    f=open(str(cwd)+"/Result-h="+str(stepsize[2])+".txt",'w+')
    f.write("\t\tResult\n\n")
    f.write("\tValue of X\t\tValue of Y\n\n")
    for i in range(len(x_3)):
        f.write("\t"+str(x_3[i])+"\t\t"+str(y_3[i])+"\n")

    plt.ylabel("Y")
    plt.xlabel ("X")
    p1,p2,p3=plt.plot(x_3,np.interp(x_3,x_1,y_1),'r--',x_3,np.interp(x_3,x_2,y_2),'gs',x_3,y_3,'b')
    plt.legend([p1, p2, p3], ["h = 0.1", "h =0.05", "h = 0.01"], loc =4)
    plt.show()

main()

			