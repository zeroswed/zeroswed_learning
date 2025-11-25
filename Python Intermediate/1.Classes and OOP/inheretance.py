import random

class Animal:
    info = 'A living organisam that feeds on organic material'

    def __init__(self, name):
        print("Animal is created")
        self.name = name

class Dog(Animal):
    info = "Dog is a mens' best friend"

    def __init__(self, name):
        super().__init__(name)
        print('A dog is created!')
        self.lucky_number = random.randint(1,10)
        self.fur = ""
        
        

    def bark(self):
        return (f"Woof! My nam is {self.name} and my number is {self.lucky_number}")

class Bulldog(Dog):
    
    def __init__(self, name):
        super().__init__(name)
        print("Bulldog is created")

dog1 = Bulldog('Fido')
