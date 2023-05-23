from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.pi = pi

    def area_of_circle(self):
        area = pi * self.radius ** 2
        return area

    def circumference_of_circle(self):
        circumference = 2 * pi * self.radius
        return circumference

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be a Negative Value")
        self.__radius = value


circle1 = Circle(1)
print(circle1.area_of_circle())
print(circle1.circumference_of_circle())
