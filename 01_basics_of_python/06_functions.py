'''
    Functions are the reusable portion of code of a program, which will be executed only when called.
    we can pass data to the function and return data from the function.
    there are two types of functions in python -> in-built and user-defined
    len() is an example of in-built function
'''

from math import sqrt

def primeFactors(n):
    if(n <= 1):
        return
    for i in range(2,int(sqrt(n)) + 1):
        while(n%i == 0):
            print(i)
            n = n//i
    
    if(n > 1):
        print(n)

def fun():
    # if we dont wanna write any thing inside function and still our program needs to run then we use pass keyword
    pass

def hello_fun(greeting, name="Dev"):
    return f"{greeting}, {name}"

n = int(input("Enter any number : "))
primeFactors(n)

print(hello_fun("hey!"))
print(hello_fun("hey!",name = "python"))

# args and kwargs
def nums_sum(*args, **kwargs):
    print(args)
    print(kwargs)

nums_sum(1, 2, 3, a="a",b="b")

# unpacking
nums = {1,2,3}
nums_squares = {"1": 1,"2": 4,"3": 9}
nums_sum(nums, nums_squares)
nums_sum(*nums, **nums_squares)