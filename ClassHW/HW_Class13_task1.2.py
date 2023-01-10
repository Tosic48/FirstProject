# class MediaPlayer:
##     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
# media1.open('filemedia1')
# media2.open('filemedia2')
# media1.play()
# media2.play()
# ---------------------------------------------------------------------------
# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         print(" ".join(map(str, filter(lambda x: Graph.LIMIT_Y[0]<= x <=Graph.LIMIT_Y[1], self.data))))
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()
# -----------------------------------------------------------
# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         for i ,key in enumerate(fields):
#             setattr(self, key,lst_values[i])
# -------------------------------------------------------
# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def select(self, a, b):
#         return self.lst_data[a: b+1]
#
#     def insert(self, data):
#         for x in data:
#             self.lst_data.append(dict(zip(self.FIELDS, x.split())))
#
# data = DataBase()
# data.insert(lst_in)
# print(data.lst_data)
# --------------------------------------------------------------------
class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        if eng in self.tr:
            del self.tr[eng]
        else:
            print(False)

    def translate(self, eng):
        if eng in self.tr:
            return self.tr[eng]
        else:
            None

tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car' , 'автомобиль')
tr.add('leaf' , 'лист')
tr.add('river' , 'река')
tr.add('go' , 'идти')
tr.add('go' , 'ехать')
tr.add('go', 'ходить')
tr.add('milk' , 'молоко')
tr.remove('car')
print(*tr.translate('go'))