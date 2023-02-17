
#Example: order array
import numpy as np

# Original array
array = np.array([10, 52, 62, 16, 16, 54, 453])
print("array:",array)

# Indices of the sorted elements of a
# given array
indices = np.argsort(array)
print("Ordered indices:",indices)

#create ordered array
array2=array[indices]
print("Ordered array:",array2)
