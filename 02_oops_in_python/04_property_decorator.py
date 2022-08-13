class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("Jhon","Wick")
# print(emp_1.email()) # this will give error
print(emp_1.email)
print(emp_1.full_name)