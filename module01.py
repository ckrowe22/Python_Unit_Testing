import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(((self.radius ** 2) * math.pi), 2)

    def circumference(self):
        return round((self.radius * 2 * math.pi), 2)

    def volume(self):
        return round((4/3 * (self.radius ** 3) * math.pi), 2)