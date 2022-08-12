class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + ".company@emp.com"
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        print("Employees are : ")
        for emp in self.employees:
            print(emp.full_name())

dev_1 = Developer("Davy","Jhones", 100000, "Python")
dev_2 = Developer("Maria","Hill", 200000, "Java")
dev_3 = Developer("Client","Barton", 150000, "C")
dev_4 = Developer("James","Rhodes", 70000, "C++")

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.prog_lang)

mgr_1 = Manager("Nick","Fury",3500000, [dev_1,dev_2])
print(mgr_1.email)
mgr_1.print_emp()
mgr_1.add_emp(dev_3)
mgr_1.add_emp(dev_4)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

# check if an object is an instance of a class or not
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# check if a class is subclass of another
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))
print(issubclass(Developer,Employee))