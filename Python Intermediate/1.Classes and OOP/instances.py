import random



class Dog():
    info = "Dog is a mens' best friend"

<<<<<<< HEAD
    def __init__(self, name='Rex', age=2, breed='Labrador'):
        print('I am alive!')
        print(random.randint(54, 68))
=======
    def __init__(self, name):
        print('A dog is created!')
        self.lucky_number = random.randint(1,10)
>>>>>>> 5d5700a157ff82b39316367d0d3dc99e44f3b408
        self.name = name
        

    def bark(self):
        return (f"Woof! My nam is {self.name} and my number is {self.lucky_number}")

dog1 = Dog('Fido')

        


<<<<<<< HEAD
#Dog1 = Dog('Brent', 4)
Dog2 = Dog('Ken', 9)

#print(Dog)
#print(Dog1.name,'and he is', Dog1.age)

print(Dog2.name,'and he is', Dog2.age)
=======
>>>>>>> 5d5700a157ff82b39316367d0d3dc99e44f3b408
