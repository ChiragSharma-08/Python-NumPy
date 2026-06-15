import numpy as np

# INTEGERS
rng = np.random.default_rng()
rng = np.random.default_rng(seed = 1)
# seed is like a seed in minecraft, one seed will give the same putput
# we can also generate a number without a seed

print(rng.integers(low=1,high=99))
print(rng.integers(low=1,high=99, size= (3,2)))

# FLOATING POINT NUMBER
np.random.seed(seed=1)
print(np.random.uniform(low= -1, high = 1, size = (2,3)))

# SUFFLING OF ARRAY
rng = np.random.default_rng()# we can also assign seed

array= np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

# RANDOM CHOICE
rng = np.random.default_rng()
fruits = np.array(["apple", "mango", "banana", "oranges", "pineapple"])
fruit = rng.choice(fruits)
fruit = rng.choice(fruits,size = 3)
print(fruit)