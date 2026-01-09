#Day 8 – OOP CONCEPTS

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old")


p1 = Person("ashu", 32)
p2 = Person("ravi", 28)


print(p1.name, p1.age)
p1.greet()
print(p2.name, p2.age)
p2.greet()

print("\n****************\n")

#MINI TASK


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def DO(self):
        print(f"Name: {self.name} | Salary: {self.salary}")
    def yearly_sal(self):
        return self.salary *12
    

e1 = Employee("Ashu", 80000)
e2 = Employee("Ravi", 45000)
e3 = Employee("Neha", 100000)

ys= e1.yearly_sal()
print(f"Yearly Salary:{ys}")

e1.DO()
ys= e1.yearly_sal()
print(f"Yearly Salary:{ys}")
e2.DO()
ys= e2.yearly_sal()
print(f"Yearly Salary:{ys}")
e3.DO()
ys= e3.yearly_sal()
print(f"Yearly Salary:{ys}")

print("\n****************\n")

employees = [
    Employee("Ashu", 80000),
    Employee("Ravi", 45000),
    Employee("Neha", 100000)
]

for emp in employees:
    emp.DO()
    print("Yearly Salary: ", emp.yearly_sal() )