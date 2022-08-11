"""
    Classes allows use to logically group data and functions in a way that is easy to reuse and also easy to re-build.
    Class is a blue print for creating instances.
"""

class Employee:
    # constructor
    # every time we create a new instance this constructor will run.
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + "." + last + "@company.com"
    
    def full_name(self):
        return f"{self.first} {self.last}"

# employee objects or instances
emp_1 = Employee("Jhonny","Depp", 22)
emp_2 = Employee("Robert","Downey", 25)

print(emp_1.email)

# get full name
print(emp_2.full_name()) # emp_2.full_name() is similar to Employee.full_name(emp_2)