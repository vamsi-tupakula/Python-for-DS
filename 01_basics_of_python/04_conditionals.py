'''
    Conditional statements controls the flow of execution in a program based on boolean expression
    • if statement
    • if-else statement
    • if-elif-else statement
'''

# program to check whether the user is an adult or not
age = int(input("Enter your age : "))

if(age <= 0):
    print("Invalid! age")
elif(age >= 18):
    print("Adult!..")
else:
    print("Not an adult... try after " + str(18 - age) + " years :-)")