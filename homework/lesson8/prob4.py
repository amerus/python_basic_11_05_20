'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
'''

class Storage:
    __stored_equipment = [ ]

    def __init__(self, address, size):
        self.address = address
        self.size = size

    @property
    def stored_equipment(self):
        return self.__stored_equipment

    @stored_equipment.setter
    def stored_equipment(self, additional_equipment):
        self.__stored_equipment.extend(additional_equipment)

class Equipment:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

class Printer(Equipment):
    def __init__(self, duplex: bool, color: bool, *args, **kwargs):
        self.duplex = duplex
        self.color = color
        super().__init__(*args, **kwargs)

    def ink_level(self, pages_printed: int):
        if self.duplex == True:
            return pages_printed * 100 / 5000
        else:
            return pages_printed * 100 / 10000

class Scanner(Equipment):
    def __init__(self, autofeed: bool, pages_per_minute: int, *args, **kwargs):
        self.__autofeed = autofeed
        self.__pages_per_minute = pages_per_minute
        super().__init__(*args, **kwargs)

    @property
    def give_parameters(self):
        return "Autofeed {} and pages per minute {}".format(self.__autofeed, self.__pages_per_minute)


class Copier(Equipment):
    def __init__(self, network_attached: bool, *args, **kwargs):
        self.__network_attached = network_attached
        super().__init__(*args, **kwargs)

    @property
    def network(self):
        return self.__network_attached

    @network.setter
    def network(self, networked: bool):
        self.__network_attached = networked


if __name__ == "__main__":

    a = Printer(make="Cannon", model="MFC8500", price=4000.00, duplex=True, color=True)
    print(a.ink_level(pages_printed=500))
    print(a.make, a.price)

    b = Scanner(make="Sharp", model="Scan2000", price=8000.00, autofeed=True, pages_per_minute=50)
    print(b.give_parameters)

    c = Copier(make="Brother", model="Floor", price=1200.00, network_attached=False)
    print(c.network)
    c.network = True
    print(c.network)

    d = Storage("Moscow", 1000)
    d.stored_equipment = ["Scanner", "Printer", "Copier"]
    print(d.stored_equipment)


