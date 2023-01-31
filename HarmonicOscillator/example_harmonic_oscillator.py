#%matplotlib widget
#import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
import time

#Physical constants in atomic units
hbar = 1

#Physical constants and parameters
m = 1.0
omega = 1.0

#General Options for the calculation
L = 20

#Solver Options
#grid size (how many discrete points to use in the range [-10,10])
npoints=1000

#Quantum state
#v=0
v=1
#v = int(input("\n Quantum Number (enter 0 for ground state):\n>"))
print("Please wait")

#Define self
#solver = PDE_BV(m1,omega1, L1, n)
#self.m = m
#self.omega = omega
#self.L = L
xlower = -L*0.5
xupper = L*0.5
#self.npoints = npoints
x = np.linspace(xlower,xupper,npoints)
h = x[1]-x[0]
psi = [None]*npoints
E = np.zeros(npoints)


#Potential as a function of position
def getV(x):
        return 0.5*m*omega**2*x**2

def getUii(i):
        return  -2*(h**2)*getV(x[i])

#-------------------------
# Main program
#-------------------------

#Calculation of F
F = np.zeros([npoints,npoints])
for i in range(0,npoints):
	F[i,i] = getUii(i) - 2/m
	if i > 0:
		F[i,i-1] = 1/m
		if i < npoints-1:
			F[i,i+1] = 1/m

#diagonalize
# w eigenvalues and v eigenvectors
#w,vs = np.linalg.eig(F)
eigenValues, eigenVectors = np.linalg.eig(F)

#Order results by energy value
idx = eigenValues.argsort()[::-1]   
w = eigenValues[idx]
vs = eigenVectors[:,idx]

#Energy
E = - w/2.0/h**2
#print("Eigenvalues:",w)
print("Ground and ten first Energy levels (in Hartree):")
print(E[0],E[1],E[2],E[3],E[4])

for k in range(0,len(w)):
	psi[k] = vs[:,k]
	integral = h*np.dot(psi[k],psi[k])
	psi[k] = psi[k]/integral**0.5

print("Plotting")
#print(psi[v])
plt.plot(x,psi[v],label=r'$\psi_v(x)$, k = ' + str(v))
#plt.plot(x,psi[v])
plt.title(r'$v=$'+ str(v) + r', $E_v$=' + '{:10.4f}'.format(E[v]))
plt.legend()
plt.xlabel(r'$x$(bohr)')
plt.ylabel(r'$\psi(x)$')
plt.show()
