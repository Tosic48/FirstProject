from math import pi, tau

class Figure:
    def __init__(self, n):
        self.n = n


class Square(Figure):
    def perimeter(self):
        return self.n * 4

    def area(self):
        return self.n**2


class Circle(Figure):
    def perimeter(self):
        return round(self.n * tau, 2)

    def area(self):
        return round(self.n**2 * pi, 2)


n = int(input())

square = Square(n)
circle = Circle(n)

print(f"Синий круг: периметр = {circle.perimeter()}, площадь = {circle.area()},")
print(f"Красный квадрат: периметр = {square.perimeter()}, площадь = {square.area()}")