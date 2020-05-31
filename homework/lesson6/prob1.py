'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
 и завершать скрипт.
'''

class TrafficLight:
    __colors = [ "красный", "желтый", "зеленый" ]
    __timing = [ 7, 2, 8 ]
    _color = "красный"

    def running(self, color):
        self.index_of_existing = self.__colors.index(self._color)
        try:
            self.index_of_request = self.__colors.index(color)
        except ValueError:
            print(f'Нет такого цвета у светофора: {color}.')
            exit(1)
        if(self.index_of_existing == self.index_of_request):
            print(f"Цвета светофора должны переключаться. Текущий цвет уже {self._color}.")
        elif((self.index_of_existing == self.__colors.index(self.__colors[-1])) and (self.index_of_request == 0) or
                (self.index_of_request - self.index_of_existing == 1)):
            self._color = self.__colors[self.index_of_request]
            print(f"Цвет переключается на {self._color}, и продолжительность составит {self.__timing[self.index_of_request]} секунд(ы).")
        else:
            print(f"Цвета должны быть последовательны. Вы пропустили {self.__colors[self.index_of_request-1]}.")

colors = ["красный", "зеленый", "желтый", "зеленый", "красный", "синий"]

mylight = TrafficLight()
for color in colors:
    mylight.running(color)


