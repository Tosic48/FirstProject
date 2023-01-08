class Animal():

    def
    self.name = name
    self.color = color
    self.age = age


class Cat(Animal):

    def say_meow(self):
        print(f'{self.name} says "Meow!"')

    def sleep(self):
        print(f'{self.name} is slipping: "Zzzz"')

    def __str__(self):
        return f'Cat {self.name}'

class Pig(Animal):

    def say_hry(self):
        print(f'{self.name} says "Meow!"')

    def sleep(self):
        print(f'{self.name} is slipping: "Zzzz"')

    def __str__(self):
        return f'Pig {self.name}'

class Dog(Animal):

    def say_whow(self):
        print(f'{self.name} says "Meow!"')

    def sleep(self):
        print(f'{self.name} is slipping: "Zzzz"')

    def __str__(self):
        return f'Dog {self.name}'


cat = Cat('Bob', 4)
dog = Dog('Baks', 5)
pig = Pig('Peppy',2)

print(cat.name)
