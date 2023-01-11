class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f'{self} is sleeping: "Zzzz"')


class Cat(Animal):

    def say_meow(self):
        print(f'{self.name} says "Meow!"')

    def __str__(self):
        return f'Cat {self.name}'


class Dog(Animal):

    def say_wohw(self):
        print(f'{self.name} says "Wohw!"')

    def sleep(self):
        print(f'{self.name} is sleeping: "Zzzz"')

    def __str__(self):
        return f'Dog {self.name}'


class Pig(Animal):

    def say_hru(self):
        print(f'{self.name} says "Hru!"')

    # def __str__(self):
    #     return f'Pig {self.name}'


cat = Cat('Bob', 4)
dog = Dog('Baks', 5)
pig = Pig('Peppy', 2)

print(cat.name)
print(dog.name)
print(pig.age)
pig.sleep()
dog.sleep()
dog.say_wohw()
pig.say_hru()