# Chelsea Rowe

class Math:
    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def Divide(self):
        try:
            if self.num2 == 0 or self.num2 < 0:
                raise ValueError("Divisor cannot be 0 or negative")
            return self.num1 / self.num2
        except ValueError as e:
            print(str(e))


class Mathmod(Math):
    # inherited from Math class
    def Modulo(self):
        return self.num1 % self.num2


if __name__ == '__main__':
    # testing Divide function first
    test_1 = Math(1, 0)
    test_1.Divide()

    # testing Modulo
    test_2 = Mathmod(5, 2)
    print(test_2.Modulo())

    # testing the rest of the Math methods
    test_3 = Math(3, 4)
    print(test_3.add(), test_3.subtract(), test_3.multiply())

