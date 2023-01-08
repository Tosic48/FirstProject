import abc


class AbstractAnimal(abc.ABC):

    @abc.abstractmethod
    def say_meow(self):
        pass

    @abc.abstractmethod
    def sleep(self):
        pass


class Cat(AbstractAnimal):
    name = 'Bob'
    color = 'White'
    wild = False

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def say_meow(self):
        print(f'{self.name} says "Meow!"')

    def sleep(self):
        print(f'{self.name} is slipping: "Zzzz"')

    def play(self):
        print(f'{self.name} is playing..')

    def __str__(self):
        return f'Cat {self.name}'


class Dog(AbstractAnimal):

    def __init__(self, name):
        self.name = name

    def say_wohw(self):
        print(f'{self.name} say "Wohw"')


cat = Cat('Bob', 'white', 3)

# cat.say_meow()

dog = Dog('Baks')

dog.sleep()
