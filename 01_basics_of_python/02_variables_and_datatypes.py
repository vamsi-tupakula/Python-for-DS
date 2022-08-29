'''
    what are variables?
    -> variables are the user defined memory locations used to store some data. or variable is a name to which a value can be assigned
    -> we store some information in the variable and later we can access that information using the name of the variable
'''

name = "python"
birth_year = "1991" # python was created in 1991

print(name)
print(birth_year)

'''
    Naming rules for variables:
        there are some rules and conventions that need to be kept in mind for naming variables.
        1. Name can start with upper-case or lower-case alphabet
        2. Name can contain numbers but not in the beginning
        3. _ can appear anywhere in the name
        4. spaces are not allowed
        Note : use some meaning full names instead of random characters
'''

'''
    Datatype of a variables :
        datatype of a variable defines the number and range of the value that the variable can have.
        there are three main data types in python :
        1.Number
            Integer
            Floating
            Complex
        2.String
        3.Boolean
'''

a = 12 # integer
b = 12.33 # float

print(a)
print(b)

course = "Data Science with Python"
print(len(course)) # to print the length of the string

# accessing the string elements using indexing
print(course[0]) # print char at index 0
print(course[5]) # print char at index 5

# boolean
play = True
study = False

print(play)
print(study)

# More about Numbers and floats
print(abs(-123)) # 123
print(round(3.745)) # 4
print(round(3.224)) # 3
print(round(3.5)) # 4
print(round(3.755,1)) # 3.8

# add num_1 and num_2 to get output as 300
num_1 = '100'
num_2 = '200'
print(num_1 + num_2) # 100200
print(int(num_1) + int(num_2)) # 300


# Scoping
# LEGB - Local, Enclosing, Global Built-in
x = 'global x'

def test():
    global x
    x = 'local x'

test()
print(x)

def outer():
    x = 'outer x'
    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()