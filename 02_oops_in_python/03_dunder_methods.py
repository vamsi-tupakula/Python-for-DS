class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + ".company@emp.com"
    
    def __repr__(self):
        return f"Employee({self.first} {self.last}, {self.pay})"

emp_1 = Employee("John","Wick",1200000)
print(emp_1)
# run above line uncommenting repr function observe the difference