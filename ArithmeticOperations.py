import numpy as np

# Scaler Arithmatic

array = np.array([1.5, 2.6, 3.4])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 5)
print(array ** 2)
print("----------------------------------")

# Vectorize math function

print(np.sqrt(array))

print(np.round(array))
print(np.floor(array))
print(np.ceil(array))

print(np.pi)
print("------------------------------------------")

# Element-wise arithmatic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)
print("----------------------------------------")

# comparison operators
scores = np.array([26, 32, 53, 38, 100, 89, 39])
print(scores == 100)
print(scores < 36)
print(scores > 36)

scores[scores<36] = 0
print(scores)