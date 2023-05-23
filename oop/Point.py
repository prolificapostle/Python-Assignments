
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print(f"Drawing from point {self.a} to {self.b}")

    def __str__(self):
        return f"({self.a}, {self.b})"

    @classmethod
    def pre_config(cls):
        return cls(1, 1)


pen = Point(2, 3)
pen2 = Point(9, 43)
print(pen2)
print(pen.draw())

print(pen)

print(pen.pre_config())
