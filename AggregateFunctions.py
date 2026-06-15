import numpy as np

# Aggrigate functions = summarize data and typically 
#                       return a single value

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))
print(np.argmax(array))

# Sum of all the columns
print(np.sum(array, axis = 0))

# Sum of all the rows
print(np.sum(array, axis = 1))