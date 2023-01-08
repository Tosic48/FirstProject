class A:
    a = 10
    _b = 20
    __c = 30
    def __init__(self):
        self.a1 = 11
        self._b = 21
        self.__c1 = 31


    def get_attr_a(self):
        return f'{self.a} {self._b} {self.__c}


    def get_attr_b(self):
        return self._b


obj = A()

print(obj.a)
print(obj.a1)
print(obj.__dict__)
print(obj.get_attr_a())
