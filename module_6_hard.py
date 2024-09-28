class Figure:
    sides_count = 0

    def __init__(self, color, size):
        self.__sides = []  # Список сторон (целые числа)
        self.__color = []  # Список цветов в формате RGB
        self.filled = False
        if self.sides_count >= 0:
            self.set_sides(size)
            self.set_color(color[0], color[1], color[2])

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        valid = self.__is_valid_color(r, g, b)
        if valid == True:
            self.__color = []
            self.__color.append(r)
            self.__color.append(g)
            self.__color.append(b)
            self.filled = True
            return self.__color, self.filled
        else:
            return

    def get_sides(self):
        return self.__sides

    def __len__(self):  # Возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        count = 0
        new = list(new_sides)
        for i in new:
            count += 1
        if count == 1:
            if isinstance(new[0], int) and new[0] > 0:
                self.__sides = []
                for i in range(self.sides_count):
                    self.__sides.append(new[0])
        if count != 1:
            valid = self.__is_valid_sides(new)
            if valid == True:
                self.__sides = []
                for i in new:
                    self.__sides.append(i)
            return self.__sides

    def __is_valid_color(self, r, g, b):  # Служебный. На проверку корректности введённых цветов
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def __is_valid_sides(self, new):  # Служебный. На проверку корректности введённых сторон
        count = 0
        valid = False
        for side in new:
            if isinstance(side, int) and side > 0:
                count += 1
        if count == self.sides_count:
            valid = True
        return valid


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, size):
        super().__init__(color, size)

    def __radius(self):
        import math as m
        r = self.get_sides()[0] / 2 / m.pi
        return r

    def get_square(self):
        import math as m
        r = self.__radius()
        s = (m.pi * r) ** 2
        return s


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, size):
        super().__init__(color, size)

    def get_square(self):
        p = self.__len__() / 2  #Полупериметр треугольника
        s = ((p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, size):
        super().__init__(color, size)
        self.__sides = []
        if size > 0:
            for i in range(size):
                self.__sides.append(i)

    def get_volume(self):
        v = self.get_sides()[0]**3
        return v


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())