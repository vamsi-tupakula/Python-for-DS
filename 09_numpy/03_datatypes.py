import numpy as np

# creating an array of datatype float
# method 1
float_arr = np.array([10,20,30], dtype=np.float16)
print(float_arr) # [10. 20. 30.]

# method 2
float_arr = np.array([10.0,20.0,30.0])
print(float_arr)
print(float_arr.dtype) #float64