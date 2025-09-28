class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"name is {name}, age is {age}")

class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)  # Ensure that super() is used correctly
        self.empid = empid

    def disempinfo(self):
        print(f"empid: {self.empid}")

name = input("name please: ")
age = int(input("age please: "))
empid = int(input("empid please: "))

emp = Employee(name, age, empid)
emp.disempinfo()
