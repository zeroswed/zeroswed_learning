import random

class Dog:
    info = "Dog is a mens' best friend"

    def __init__(self, name='Rex', age=2):
#        print('I am alive!')
#        print(random.randint(54, 68))
        self.name = name
        self.age = age
        


Dog1 = Dog('Brent', 4)
print(Dog1.name,'and he is', Dog1.age)

