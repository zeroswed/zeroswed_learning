import random

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"
    
my_dog = Dog("Buddy", 3, "Golden Retriever")
print(my_dog.bark())
print(my_dog.fetch("ball"))     