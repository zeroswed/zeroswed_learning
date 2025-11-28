import random



class Dog():
    info = "Dog is a mens' best friend"

    def __init__(self, name='Rex', age=2, breed='Labrador'):
        print('I am alive!')
        print(random.randint(54, 68))
        self.name = name
        

    def bark(self):
        return (f"Woof! My nam is {self.name} and my number is {self.lucky_number}")

dog1 = Dog('Fido')

        


#Dog1 = Dog('Brent', 4)
Dog2 = Dog('Ken', 9)

#print(Dog)
#print(Dog1.name,'and he is', Dog1.age)

print(Dog2.name,'and he is', Dog2.age)
