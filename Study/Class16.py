class Student:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        self.name = new_name

    @name.deleter
    def name(self):
        del self._name

s = Student('Igor')
print(s.name)
# print(s.get_name)
print(s.name)
# s.name = 'Inga'
# print(s.name)
#
#
# del s.name
# print(s.name)

