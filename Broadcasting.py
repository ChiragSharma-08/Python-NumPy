import numpy as np

# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape

# The dimensions have the same size.
# OR
# One of the dimensions has a size of 1

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])
array3 = np.array([[1,2,3,4],[5,6,7,8]])
print(array1.shape)
print(array2.shape)
print(array3.shape)

print(array1 * array2)
print(array1 * array3)
# print(array2 * array3) # Cause an error
