from math import pi


class Shape:
    def desc(self):
        print(f'Привет! Я {self.__class__.__name__}')


class Circle(Shape):
    def __init__(self, r):
        self.radius = r  # self - ссылка на самого себя

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    def desc(self):
        print(f'Привет! Я {self.__class__.__name__} с радиусом {self.radius}')



class Rectangle(Shape):
    def __init__(self, sideA, sideB):
        self.width = sideA
        self.heigth = sideB

    def perimetr(self):
        return (self.heigth + self.width) * 2

    def area(self):
        return self.width * self.heigth


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)



a = Circle(5)
a.desc()
