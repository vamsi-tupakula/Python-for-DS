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

# random.randint method
arr_randint = np.random.randint(0,10,size=(2,4)) # 0 is inclusive and 10 is exclusive
print(arr_randint)

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
new_arr = arr.reshape(3,2)
print(new_arr)