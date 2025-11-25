import random



class Dog():
    info = "Dog is a mens' best friend"

    def __init__(self, name):
        print('A dog is created!')
        self.lucky_number = random.randint(1,10)
        self.name = name
        

    def bark(self):
        return (f"Woof! My nam is {self.name} and my number is {self.lucky_number}")

dog1 = Dog('Fido')

        


