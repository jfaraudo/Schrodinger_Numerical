#Example Diagonalisation of a Matrix

#Import libraries
import numpy as np
#import numpy.linalg as linalg

#generate a matrix randomly
#A = np.random.random((3,3))
#provide a Matrix
A = np.array([[0.16,0.8,0.077], [0.5,0.04,0.1],[0.66,0.85,0.69]])


print("Matrix:")
print(A)

#Diagonalisation
eigenValues, eigenVectors = np.linalg.eig(A)

print("\nResult from direct diagonalisation")

for k in range(0,len(eigenValues)):

   print("EigenState",k)
   print("Eigenvalue:", eigenValues[k])
   print("Eigenvector:",eigenVectors[:,k],"\n")

#Sorting of the Eigenvalues and Eigenvectors
id = np.argsort(eigenValues)

Val = eigenValues[id]
Vect = eigenVectors[:,id]

print("\n Ordered EigenValues and EigenVectors\n")

for k in range(0,len(Val)):

   print("EigenState",k)
   print("Eigenvalue:", Val[k])
   print("Eigenvector:",Vect[:,k],"\n")
   


