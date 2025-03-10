# Functions

nameUser = input("Your name: ")
ageUser = int(input("Your age: "))


def greet(name, age):
    return f"Hello {name} and I see you are {age} right?"


print(greet(nameUser, ageUser))
