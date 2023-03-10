import random

class Cat:
    name = 'Bob'
    color = 'White'
    __wild = False

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def say_meow(self):
        print(f'{self.name} says "Meow!"')

    def sleep(self):
        print(f'{self.name} is slipping: "Zzzz"')


    def __str__(self):
        return f'Cat {self.name}'

    def __repr__(self):
        return f'Cat {self.name}'


    def about(self):
        if self.__wild == True:
            print(f'Cat {self.name} is wild')
        else:
            print(f'Cat {self.name} is not wild')


    def get_home(self):
        self.__wild = False
        print(f'{self.name} got home')
        self.about()

# print(Cat)
cat1 = Cat('Bob', 'Red', 3)
cat2 = Cat('Pups', 'White', 4)

cololors = ('Red', "White",'Black', 'Spot' )

# cats = [Cat(f'cat{i}', random.choice(cololors), random.randint(1,10)) for i in range(1,100)]
#
# for cat in cats:
#     cat.say_meow()
#
# cats[87].sleep()
cat1.about()
cat1.get_home()
