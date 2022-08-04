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