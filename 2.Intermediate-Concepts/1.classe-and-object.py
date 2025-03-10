class Person:
    def __init__(self, name, age):  # Contructor
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello my name is {self.name} and I am {self.age}"


# Creating an object
p1 = Person("Youssouf", 27)

print(p1.greet())


# Inheritance

class Employee (Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_salary(self):
        return f"My salary is {self.salary}"


e1 = Employee("Youssouf", 27, 60000)

print(e1.greet())
print(e1.show_salary())
