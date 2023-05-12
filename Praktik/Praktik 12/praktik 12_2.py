class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


math = Math(10, 5)

print("Сложение:", math.addition())
print("Умножение:", math.multiplication())
print("Деление:", math.division())
print("Вычитание:", math.subtraction())