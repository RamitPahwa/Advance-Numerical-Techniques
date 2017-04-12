import os
import matplotlib.pyplot as plt
# ut+ux=0

# Forward Time Backward Space,since c is positive 

def FTBS():
	dx=0.25
	v=0.5
	dt=v*dx
	n=int(1.0/dx)
	U=[[0 for i in range(n+1) ] for j in range(100)]
	# intial contidions
	for i in range(n+1):
		x=i*dx
		U[0][i]=x*x
	for i in range(99):
		for j in range(1,n+1):
			U[i+1][j]=U[i][j]-v*(U[i][j]-U[i][j-1])

	X=[]
	for i in range(n+1):
		X.append(i*dx)
	
	plt.ylabel("U")
	plt.xlabel ("X")
	p=plt.plot(X,U[1],'r')
	plt.legend(p,["v="+str(v)],loc=4)
	plt.savefig("I-TimeFTBS Step v="+str(v)+".png")
	plt.show()
	f=open("ResultsFTBS.txt",'w+')
	f.write("	Time 			Values\n\n")
	for i in range(99):
		f.write("	"+str(i)+" 		"+str(U[i])+"\n")


def LAX():
	dx=0.25
	v=0.5
	dt=v*dx
	n=int(1.0/dx)
	U=[[0 for i in range(n+3) ] for j in range(100)]
	# intial contidions
	for i in range(n+1):
		x=i*dx
		U[0][i]=x*x
	for i in range(99):
		for j in range(1,n+2):
			U[i+1][j]=0.5*((U[i][j-1]+U[i][j+1])+v*(U[i][j+1]-U[i][j-1]))

	X=[]
	for i in range(n+3):
		X.append(i*dx)
	
	plt.ylabel("U")
	plt.xlabel ("X")
	p=plt.plot(X,U[1],'r')
	plt.legend(p,["v="+str(v)],loc=4)
	plt.savefig("I-TimeLAX Step v="+str(v)+".png")
	plt.show()
	f=open("ResultsLAX.txt",'w+')
	f.write("	Time 			Values\n\n")
	for i in range(99):
		f.write("	"+str(i)+" 		"+str(U[i])+"\n")

def LW():
	# single step method
	dx=0.25
	v=0.5
	dt=v*dx
	n=int(1.0/dx)
	U=[[0 for i in range(n+3) ] for j in range(100)]
	# intial contidions
	for i in range(n+1):
		x=i*dx
		U[0][i]=x*x
	for i in range(99):
		for j in range(1,n+2):
			U[i+1][j]=U[i][j]-v*0.5*(U[i][j+1]-U[i][j-1])+v*v*0.5*(U[i][j+1]+U[i][j-1]-2*U[i][j])

	X=[]
	for i in range(n+3):
		X.append(i*dx)
	
	plt.ylabel("U")
	plt.xlabel ("X")
	p=plt.plot(X,U[1],'r')
	plt.legend(p,["v="+str(v)],loc=4)
	plt.savefig("I-TimeLW Step v="+str(v)+".png")
	plt.show()
	f=open("ResultsLW.txt",'w+')
	f.write("	Time 			Values\n\n")
	for i in range(99):
		f.write("	"+str(i)+" 		"+str(U[i])+"\n")

def MacCormack():
	dx=0.25
	v=0.5
	dt=v*dx
	n=int(1.0/dx)
	U=[[0 for i in range(n+3) ] for j in range(100)]
	# intial contidions
	for i in range(n+1):
		x=i*dx
		U[0][i]=x*x
	for i in range(99):
		# Predictor Step
		for j in range(1,n+2):
			U[i+1][j]=U[i][j]-v*(U[i][j+1]-U[i][j])
		# Corrector Step
		for j in range(1,n+2):
			U[i+1][j]=U[i][j]-(v*0.5*(U[i][j+1]-U[i][j]))-(v*0.5*(U[i+1][j]-U[i+1][j-1]))


	X=[]
	for i in range(n+3):
		X.append(i*dx)
	
	plt.ylabel("U")
	plt.xlabel ("X")
	p=plt.plot(X,U[1],'r')
	plt.legend(p,["v="+str(v)],loc=4)
	plt.savefig("I-TimeMC Step v="+str(v)+".png")
	plt.show()
	f=open("ResultsMC.txt",'w+')
	f.write("	Time 			Values\n\n")
	for i in range(99):
		f.write("	"+str(i)+" 		"+str(U[i])+"\n")

FTBS()
LAX()
LW()
MacCormack()