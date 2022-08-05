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

n = int(input("Enter any number : "))
primeFactors(n)