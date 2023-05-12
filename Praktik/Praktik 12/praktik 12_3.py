class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def setYear(self, year):
        self.year = year

    def setType(self, car_type):
        self.car_type = car_type

    def setColor(self, color):
        self.color = color


car = Car("черный", "седан", 2021)

car.start()
car.stop()
print("Год выпуска:", car.year)
car.setYear(2022)
print("Год выпуска:", car.year)

print("Тип автомобиля:", car.car_type)
car.setType("кроссовер")
print("Тип автомобиля:", car.car_type)

print("Цвет автомобиля:", car.color)
car.setColor("белый")
print("Цвет автомобиля:", car.color)