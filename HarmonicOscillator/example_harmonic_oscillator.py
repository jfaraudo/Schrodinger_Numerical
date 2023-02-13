#%matplotlib widget
#import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
import time

#Potential as a function of position
def getV(x):
        potvalue = (1.0/2.0)*x**2 
        return potvalue

#Solver Options
L = 20 # Interval for calculating the wave function [-L/2,L/2]
npoints=1000 #grid size (how many discrete points to use in the range [-L/2,L/2])

#Domain at which the solution will be calculated
xlower = -L/2.0
xupper = L/2.0
x = np.linspace(xlower,xupper,npoints)
h = x[1]-x[0]  #discretization in space

#Init Energy and Wavefunction
psi = [None]*npoints
E = np.zeros(npoints)

print("Please wait")

#-------------------------
# Main program
#-------------------------

#Calculation of F
print("Calculating matrix...")
F = np.zeros([npoints,npoints])
for i in range(0,npoints):
	F[i,i] = -2*(h**2)*getV(x[i]) - 2
	if i > 0:
		F[i,i-1] = 1
		if i < npoints-1:
			F[i,i+1] = 1

#diagonalize the matrix F
print("Diagonalizing...")
eigenValues, eigenVectors = np.linalg.eig(F)

#Order results by eigenvalue
# w ordered eigenvalues and vs ordered eigenvectors
idx = eigenValues.argsort()[::-1]   
w = eigenValues[idx]
vs = eigenVectors[:,idx]

#Energy Level
E = - w/(2.0*h**2)

#Print Energy Values
print("RESULTS:")
for k in range(0,9):
	print("State ",k," Energy = %.2f" %E[k])

#Calculation of normalised Wave Functions
for k in range(0,len(w)):
	psi[k] = vs[:,k]
	integral = h*np.dot(psi[k],psi[k])
	psi[k] = psi[k]/integral**0.5

#Plot Wave functions
print("Plotting")

#v = int(input("\n Quantum Number (enter 0 for ground state):\n>"))
for v in range(0,9):
	plt.plot(x,psi[v],label=r'$\psi_v(x)$, k = ' + str(v))
	#plt.plot(x,psi[v])
	plt.title(r'$n=$'+ str(v) + r', $E_n$=' + '{:.2f}'.format(E[v]))
	plt.legend()
	plt.xlabel(r'$x$(dimensionless)')
	plt.ylabel(r'$\psi(x)$')
	plt.show()

print("Bye")
