"""
    Classes allows use to logically group data and functions in a way that is easy to reuse and also easy to re-build.
    Class is a blue print for creating instances.
"""

class Employee:
    # constructor
    # every time we create a new instance this constructor will run.
    def __init__(self):
        print("Constructor is initialized....")

# employee objects or instances
emp_1 = Employee()
emp_2 = Employee()