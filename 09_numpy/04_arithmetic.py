import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a*b)
print(a-b)
print(a+b)
print(a**b)

# sqaure of a list normal way
ls = [1,2,3,4]
for i in range(len(ls)):
    ls[i] = ls[i]**2
print(ls)

# square of a list using numpy
ls = [1,2,3,4]
a = np.array(ls)
print(a**2)