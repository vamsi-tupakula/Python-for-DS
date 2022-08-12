"""
    Classes allows use to logically group data and functions in a way that is easy to reuse and also easy to re-build.
    Class is a blue print for creating instances.
"""

class Employee:
    # class variables
    email_suffix = "@company.com"
    employee_count = 0

    # constructor
    # every time we create a new instance this constructor will run.
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + "." + last + self.email_suffix
        Employee.employee_count += 1
    
    def full_name(self):
        return f"{self.first} {self.last}"

    # every function inside a class always takes instance as first argument to change this behavior and to send class as first argument we use class methods
    @classmethod
    def set_suffix(cls, new_suffix):
        cls.email_suffix = new_suffix
    
    @classmethod
    def from_string(cls, emp_str):
        first,last,age = emp_str.split('-')
        return cls(first,last,age)

    # static methods does not pass either class or instance they behave like normal functions except we include in class because we have some logical connection
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# employee count
print(Employee.employee_count) # 0

# employee objects or instances
emp_1 = Employee("Jhonny","Depp", 22)
emp_2 = Employee("Robert","Downey", 25)

print(Employee.employee_count) # 2

print(emp_1.email)

# get full name
print(emp_2.full_name()) # emp_2.full_name() is similar to Employee.full_name(emp_2)

# gives complete emp_1 object as dictionary
print(emp_1.__dict__)

Employee.set_suffix(".company@emp.com")
print(emp_1.email_suffix)

# creating objects using class methods
emp_str_1 = "jack-sparrow-29"
emp_str_2 = "steve-rogers-35"

emp_1_str = Employee.from_string(emp_str_1)
emp_2_str = Employee.from_string(emp_str_2)

print(emp_1_str.email)

# working with staticmethods
import datetime
my_date = datetime.date(2022,8,13)

print(Employee.is_workday(my_date))