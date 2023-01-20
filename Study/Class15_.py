class Person:

    TOTAL = 0

    def __init__(self, age):
        self.age = age

    def is_adult(self):
        if age > 18:
            return True
        else:
            return False

    @staticmethod
    def is_adult(selfage):
        if age > 18:
            return True
        else:
            return False


p = Person(30)
p2 = Person(17)
print(p.is_adult())
print(p2.is_adult())
