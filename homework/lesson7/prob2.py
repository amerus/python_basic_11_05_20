'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Fabric(ABC):

    @abstractmethod
    def fabric_calculator(self, main_dimension: float) -> float:
        pass

class FabricCalc(Fabric):

    def __init__(self, garment_name):
        self.__garment_name = garment_name

    def fabric_calculator(self, main_dimension) -> float:
        self.main_dimension = main_dimension
        if self.__garment_name == 'пальто':
            return float(2 * self.main_dimension + 0.3)
        elif self.__garment_name == 'костюм':
            return float(self.main_dimension / 6.5 + 0.5)

    @property
    def your_garment(self):
        return self.__garment_name

a = FabricCalc('пальто')
print(a.your_garment, a.fabric_calculator(12))
a = FabricCalc('костюм')
print(a.your_garment, a.fabric_calculator(23))
