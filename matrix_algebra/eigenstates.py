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

   


