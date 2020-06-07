'''
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.
'''
class Storage:
    __stored_equipment = {"сканер": 0, "принтер": 0, "ксерокс": 0}

    def __init__(self, equipment: str):
        self.equipment = equipment

    @property
    def store_equipment(self):
        return self.__stored_equipment

    @store_equipment.setter
    def store_equipment(self, args):
        operation, quantity = args
        if operation == "+":
            self.quantity = self.__stored_equipment[self.equipment] + quantity
            self.__stored_equipment.update({self.equipment: self.quantity})
        elif operation == "-":
            if(quantity <= self.__stored_equipment[self.equipment]):
                self.quantity = self.__stored_equipment[self.equipment] - quantity
                self.__stored_equipment.update({self.equipment: self.quantity})
            else:
                print("Cannot subtract more thank stored. Draining all inventory instead.")
                self.__stored_equipment.update({self.equipment: 0})

class Equipment:
    def __init__(self, type, make, model, price):
        self.type = type
        self.make = make
        self.model = model
        self.price = price

class Printer(Equipment):
    def __init__(self, duplex = True, color = True, *args, **kwargs):
        self.duplex = duplex
        self.color = color
        super().__init__(*args, **kwargs)

    def ink_level(self, pages_printed: int):
        if self.duplex == True:
            return pages_printed * 100 / 5000
        else:
            return pages_printed * 100 / 10000

class Scanner(Equipment):
    def __init__(self, autofeed = True, pages_per_minute = 500, *args, **kwargs):
        self.__autofeed = autofeed
        self.__pages_per_minute = pages_per_minute
        super().__init__(*args, **kwargs)

    @property
    def give_parameters(self):
        return "Autofeed {} and pages per minute {}".format(self.__autofeed, self.__pages_per_minute)


class Copier(Equipment):
    def __init__(self, network_attached = False, *args, **kwargs):
        self.__network_attached = network_attached
        super().__init__(*args,**kwargs)

    @property
    def network(self):
        return self.__network_attached

    @network.setter
    def network(self, networked: bool):
        self.__network_attached = networked


class ValidateInput:

    __existing_items = ["принтер", "сканер", "ксерокс"]
    __matching_classes = [Printer, Scanner, Copier]

    def __init__(self, item_name, item_count):
        self.item_name = item_name
        self.item_count = item_count

    def validate_name(self):
        if(self.item_name in self.__existing_items):
            return dict(zip(self.__existing_items,self.__matching_classes))[self.item_name]
        else:
            return False

    def validate_count(self):
        return self.item_count.isdigit()

if __name__ == "__main__":

    while True:
        item_name = input("Введите наименование товара. Например, сканер, принтер или ксерокс (stop для остановки): \t")
        if item_name == "stop":
            break
        item_count = input("Введите количество: \t")
        item_operation = input("Добавить или вычесть (+ или -)?: ")
        a = ValidateInput(item_name, item_count)
        try:
            if(a.validate_name() and a.validate_count()):
                my_object = a.validate_name()
                b = my_object(type=item_name, make="", model="", price=0)
                c = Storage(b.type)
                c.store_equipment = (item_operation, int(item_count))
                print(c.store_equipment)
            else:
                raise ValueError("Enter a valid item with a valid count number.")
        except ValueError as e:
            print(e)
