import math


class Areas:
    def areaCirc(self, radius):
        return round(((radius ** 2) * math.pi))

    def areaSquare(self, side):
        return side * side

    def areaRect(self, side1, side2):
        return side1 * side2

    def areaTri(self, base, height):
        return round(.5 * base * height)

    def areaParall(self, base, height):
        return base * height

    def areaEllipse(self, rad_a, rad_b):
        return round(math.pi * rad_a * rad_b)
