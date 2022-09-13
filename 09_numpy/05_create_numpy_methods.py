import numpy as np

# array ones method
arr_ones = np.ones(shape=(2,3))
print(arr_ones)

# change dtype of existing array
arr_ones = arr_ones.astype(np.int32)
print(arr_ones)

# array zeros method
arr_zeros = np.zeros(shape=(3,4), dtype=np.int32)
print(arr_zeros)

# random.random method
arr_random = np.random.random(size=(2,3))
print(arr_random)