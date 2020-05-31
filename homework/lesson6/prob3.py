'''
 Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
 income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
 например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
 реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
 атрибутов, вызвать методы экземпляров).
'''

class Worker:
    wage = 0
    bonus = 0
    income_dict = {"wage": wage, "bonus": bonus}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.income_dict

class Position(Worker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_full_name(self):
        print(self.name,self.surname)

    def get_total_inome(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self.income_dict["wage"] = self.wage
        self.income_dict["bonus"] = self.bonus
        print(self._income["wage"] + self._income["bonus"])

my_position = Position("Sergey", "Motorny", "Engineer")
my_position.get_full_name()
my_position.get_total_inome(1000,2003)
