"""
    Classes allows use to logically group data and functions in a way that is easy to reuse and also easy to re-build.
    Class is a blue print for creating instances.
"""

class Employee:
    pass

# employee objects or instances
emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

# creating attributes
emp_1.name = "Jhonny"
emp_1.age = 23

emp_2.name = "Depp"
emp_2.age = 25

print(emp_1.name)
print(emp_2.name)