'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу
метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def total_mass(self, mass_per_meter, depth):
        self.mass = mass_per_meter
        self.depth = depth
        return int(self._length * self._width * self.mass * self.depth / 1000)


my_road = Road(20, 5000)
print(my_road.total_mass(25, 5))
