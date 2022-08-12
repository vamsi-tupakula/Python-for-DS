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

dev_1 = Developer("Davy","Jhones", 100000, "Python")
dev_2 = Developer("Maria","Hill", 200000, "Java")

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.prog_lang)