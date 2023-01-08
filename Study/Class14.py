class Cat:
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


    def __str__(self):
        return f'Cat {self.name}'

    def __repr__(self):
        return f'Cat {self.name}'

# print(Cat)
cat1 = Cat('Bob', 'Red', 3)
cat2 = Cat('Pups', 'White', 4)

