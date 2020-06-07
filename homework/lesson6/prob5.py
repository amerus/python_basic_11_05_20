'''
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.
'''

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f"Запуск отрисовки книги {self.title}.")

class Pen(Stationary):
    brand = "Parker"
    def __init__(self, *args, **kwargs):
        self.brand = self.brand
        super().__init__(*args, **kwargs)
    def draw(self):
        print(f"{self.title} вырисовывается ручкой {self.brand}.")


class Pencil(Stationary):
    softness = "3M"
    def __init__(self, *args, **kwargs):
        self.softness = self.softness
        super().__init__(*args, **kwargs)
    def draw(self):
        print(f"{self.title} вырисовывается карандашем с мягкостью {self.softness}.")

class Handle(Stationary):
    color = "красный"
    def __init__(self, *args, **kwargs):
        self.color = self.color
        super().__init__(*args, **kwargs)
    def draw(self):
        print(f"{self.title} вырисовывается маркером с цветом {self.color}.")

stationary = Stationary("Остров сокровищ")
stationary.draw()

pen = Pen("Остров сокровищ")
pen.draw()

pencil = Pencil("Остров сокровищ")
pencil.draw()

marker = Handle("Остров сокровищ")
marker.draw()
