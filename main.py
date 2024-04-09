# Create an incremental ID in a Class in Python

import itertools


class Employee():
    id_obj = itertools.count()

    def __init__(self, name, salary):
        self.id = next(Employee.id_obj)
        self.name = name
        self.salary = salary


alice = Employee('Alice', 100)
bob = Employee('Bobbyhadz', 100)
carl = Employee('Carl', 100)

print(alice.id)  # 👉️ 0
print(bob.id)  # 👉️ 1
print(carl.id)  # 👉️ 2