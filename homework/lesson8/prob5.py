'''
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
'''

class Storage:
    __stored_equipment = { }

    def __init__(self, equipment: str, quantity: int):
        self.equipment = equipment
        self.quantity = quantity

    @property
    def store_equipment(self):
        return self.__stored_equipment

    @store_equipment.setter
    def store_equipment(self, args):
        operation, quantity = args
        if operation == "+":
            self.quantity += quantity
            self.__stored_equipment.update({self.equipment: self.quantity})
        elif operation == "-":
            self.quantity -= quantity
            self.__stored_equipment.update({self.equipment: self.quantity})

class Equipment:
    def __init__(self, type, make, model, price):
        self.type = type
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
        super().__init__(*args,**kwargs)

    @property
    def network(self):
        return self.__network_attached

    @network.setter
    def network(self, networked: bool):
        self.__network_attached = networked


if __name__ == "__main__":

    a = Printer(type="printer", make="Cannon", model="MFC8500", price=4000.00, duplex=True, color=True)
    print(a.ink_level(pages_printed=500))
    print(a.make, a.price)
    print(a.type)

    b = Scanner(type="scanner", make="Sharp", model="Scan2000", price=8000.00, autofeed=True, pages_per_minute=50)
    print(b.give_parameters)

    c = Copier(type="copier", make="Brother", model="Floor", price=1200.00, network_attached=False)
    print(c.network)
    c.network = True
    print(c.network)

    d = Storage(c.type, 5)
    print(d.store_equipment)
    d.store_equipment = ("+", 5)
    print(d.store_equipment)
    d.store_equipment = ("-", 8)
    print(d.store_equipment)
    d.equipment = b.type
    d.store_equipment = ("+", 1)
    print(d.store_equipment)
