'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
'''

class Car:
    is_police = False
    speed = 0

    def __init__(self, name, color, *args, **kwargs):
        self.name = name
        self.color = color
        for key, value in kwargs.items():
            self.key = value

    def go(self, destination):
        self.destination = destination
        print(f'{self.name} is driving to: {self.destination}.')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} is turning {self.direction}.')

    def show_speed(self, **kwargs):
        try:
            self.speed = kwargs["speed"]
        except KeyError:
            self.speed = self.speed
        print(f"{self.name}'s speed is {self.speed}mph.")


class TownCar(Car):
    # Miles per gallon efficiency
    mpg = 0
    speed_maximum = 60

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == "mpg" or key == "speed_maximum":
                self.key = value
        super().__init__(*args,**kwargs)

    def show_speed(self, **kwargs):
        try:
            self.speed = kwargs["speed"]
        except KeyError:
            self.speed = self.speed

        if(self.speed > self.speed_maximum):
            print(f'Slow down there, buddy. Your speed of {self.speed}mph is too high.')
        else:
            print(f"{self.name}'s speed is {self.speed}mph.")


class WorkCar(TownCar):
    '''
    towing_capacity and cargo_room are mandatory parameters for this class, which extends TownCar
    '''
    def __init__(self, towing_capacity, cargo_room, *args, **kwargs):
        self.towing_capacity = towing_capacity
        self.cargo_room = cargo_room
        super().__init__(*args, **kwargs)
        self.speed_maximum = 10
        self.mpg = 12

class PoliceCar(Car):
    # sirens = True
    # equipment = [ ]

    def __init__(self, sirens, equipment, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sirens = sirens
        self.equipment = equipment

    def get_equipment(self):
        return ', '.join(self.equipment)

my_car = TownCar("Eclipse","Grey",mpg=25)
my_car.go("Home")
print(my_car.color)
print(my_car.speed_maximum)
print(my_car.mpg)
my_car.turn("left")
my_car.show_speed(speed=50)

print("-------------------")

mywork_car = WorkCar(name="Tow Truck", color="White", towing_capacity=6000, cargo_room=5000)
print(mywork_car.name)
print(mywork_car.speed_maximum)
print(mywork_car.mpg)
print(f'Your work car towing capacity is {mywork_car.towing_capacity} lbs.')
mywork_car.show_speed(speed=15)

print("-------------------")
mypolice_car = PoliceCar(name="Ford", color="Black", sirens=True, equipment=["camera", "sport tires", "loud speaker"])
print(f'Your police vehicle is equipped with: {mypolice_car.get_equipment()}.')
mypolice_car.turn("right")
mypolice_car.go("work")
