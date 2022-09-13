import numpy as np

# creating an array of datatype float
# method 1
float_arr = np.array([10,20,30], dtype=np.float16)
print(float_arr) # [10. 20. 30.]

# method 2
float_arr = np.array([10.0,20.0,30.0])
print(float_arr)
print(float_arr.dtype) #float64

arr = np.array([[1,2,3],[4,5,6]])

# iteration in 2d arrays :
print(arr[0,1])
print(arr[0][1])

print('----')
rows, cols = arr.shape
for row in range(0,rows):
    for col in range(0, cols):
        print(arr[row][col], end=" ")
    print()